"""Terugkijktest: wat gebeurde er echt na de peildatum van een terugkijkrapport?

Gebruik:
  python3 tools/terugkijk.py uitkomst terugkijk/ORSTED.CO/2021-02-15/rapport.json \
      [--index ^OMXC25] [--factor 2025-10-07:0.62]

Leest het rapport (peildatum, koers, koopzone, koersdoel, stop-loss, scenario's, verkoopsignalen),
haalt de koersen NA de peildatum op en schrijft `uitkomst.json` naast het rapport:
  - koers na 6 maanden, 1 jaar, 2 jaar en vandaag; laagste en hoogste koers in de 2 jaar
  - is de stop-loss geraakt (wanneer)? Is het koersdoel gehaald (wanneer)? Werd de koopzone bereikt?
  - welk scenario lag het dichtst bij de koers na 2 jaar?
  - rendement incl. dividend t.o.v. een vergelijkingsindex

--factor DATUM:FACTOR corrigeert voor een kapitaalverhoging of andere actie die Yahoo niet (volledig)
verwerkt (bv. claimemissie): koersen vanaf DATUM worden ÷ FACTOR gerekend, zodat alles in de eenheid van
het rapport staat (dezelfde schaal als koers, koopzone, stop-loss en scenario's op de peildatum).
DATUM = de eerste dag die Yahoo wél aangepast/na de actie toont. De factor moet uit een officiële bron
komen (theoretische koers ex-claim / laatste koers met claim) en in de evaluatie staan.
Dit script gebruikt NA de peildatum gegevens: het hoort enkel bij de evaluatie, nooit bij het rapport zelf.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from common import session

YQ = "https://query1.finance.yahoo.com"


def reeks(symbool: str, van: str) -> list[dict]:
    begin = dt.datetime.fromisoformat(van).replace(tzinfo=dt.UTC) - dt.timedelta(days=10)
    r = session().get(f"{YQ}/v8/finance/chart/{symbool}", timeout=30, params={
        "interval": "1d", "events": "div,splits", "period1": int(begin.timestamp()),
        "period2": int(dt.datetime.now(dt.UTC).timestamp())})
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
    rij = []
    for i, ts in enumerate(res.get("timestamp") or []):
        if q["close"][i] is None:
            continue
        rij.append({"datum": dt.datetime.fromtimestamp(ts, dt.UTC).date().isoformat(), "slot": q["close"][i],
                    "laag": q["low"][i] or q["close"][i], "hoog": q["high"][i] or q["close"][i],
                    "adj": adj[i] if adj and adj[i] is not None else q["close"][i]})
    return rij


def corrigeer(rij: list[dict], factoren: list[tuple[str, float]]) -> None:
    for datum, f in factoren:
        for r in rij:
            if r["datum"] >= datum:
                for k in ("slot", "laag", "hoog", "adj"):
                    r[k] /= f


def op(rij: list[dict], datum: str) -> dict | None:
    """Laatste rij op of vóór datum."""
    kand = [r for r in rij if r["datum"] <= datum]
    return kand[-1] if kand else None


def plus(datum: str, maanden: int) -> str:
    d = dt.date.fromisoformat(datum)
    j, m = divmod(d.month - 1 + maanden, 12)
    return dt.date(d.year + j, m + 1, min(d.day, 28)).isoformat()


def eerste(rij, voorwaarde):
    return next((r["datum"] for r in rij if voorwaarde(r)), None)


def uitkomst(rapport: Path, index: str | None, factoren: list[tuple[str, float]]) -> dict:
    r = json.loads(rapport.read_text(encoding="utf-8"))
    m, adv = r["meta"], r["advies"]
    peil = m.get("peildatum")
    if not peil:
        sys.exit("rapport heeft geen meta.peildatum: geen terugkijkrapport")
    rij = reeks(m["ticker"], peil)
    corrigeer(rij, factoren)
    start = op(rij, peil)
    na = [x for x in rij if x["datum"] > peil]
    vandaag = rij[-1]["datum"]
    twee = [x for x in na if x["datum"] <= plus(peil, 24)]
    p0 = start["slot"]

    def punt(d):
        x = op(rij, d) if d <= vandaag else None
        if not x or x["datum"] <= peil:
            return None
        return {"datum": x["datum"], "koers": round(x["slot"], 2), "verschil_pct": round((x["slot"] / p0 - 1) * 100, 1),
                "rendement_incl_dividend_pct": round((x["adj"] / start["adj"] - 1) * 100, 1)}

    stop = (adv.get("stop_loss") or {}).get("waarde")
    doel = adv.get("koersdoel")
    kz = adv.get("koopzone") or {}
    uit = {
        "ticker": m["ticker"], "peildatum": peil, "koers_peildatum": round(p0, 2), "berekend_op": vandaag,
        "correcties": [{"voor": d, "factor": f} for d, f in factoren],
        "rapport": {"oordeel": adv.get("oordeel"), "score": adv.get("score"), "koopzone": kz, "koersdoel": doel,
                    "stop_loss": stop, "scenarios": adv.get("scenarios")},
        "koers": {"6m": punt(plus(peil, 6)), "1j": punt(plus(peil, 12)), "2j": punt(plus(peil, 24)), "vandaag": punt(vandaag)},
        "binnen_2j": {
            "laagste": min(({"datum": x["datum"], "koers": round(x["laag"], 2)} for x in twee), key=lambda z: z["koers"], default=None),
            "hoogste": max(({"datum": x["datum"], "koers": round(x["hoog"], 2)} for x in twee), key=lambda z: z["koers"], default=None),
            "stop_loss_geraakt": eerste(twee, lambda x: stop is not None and x["slot"] <= stop),
            "koersdoel_gehaald": eerste(twee, lambda x: doel is not None and (x["slot"] >= doel if doel >= p0 else x["slot"] <= doel)),
            "koopzone_bereikt": eerste(twee, lambda x: kz.get("tot") is not None and kz.get("van") is not None and kz["van"] <= x["slot"] <= kz["tot"]),
        },
    }
    k2 = uit["koers"]["2j"]
    if k2 and adv.get("scenarios"):
        best = min(adv["scenarios"], key=lambda s: abs((s.get("koers") or 0) - k2["koers"]))
        uit["dichtste_scenario_2j"] = {"naam": best["naam"], "koers_scenario": best.get("koers"), "kans_volgens_rapport": best.get("kans")}
    if index:
        ir = reeks(index, peil)
        i0 = op(ir, peil)
        uit["index"] = {"symbool": index}
        for k, d in (("1j", plus(peil, 12)), ("2j", plus(peil, 24)), ("vandaag", ir[-1]["datum"])):
            x = op(ir, d)
            uit["index"][k] = round((x["adj"] / i0["adj"] - 1) * 100, 1) if x and x["datum"] > peil else None
    uit["bron"] = f"Yahoo Finance koersdata {m['ticker']}{' en ' + index if index else ''}, opgehaald {dt.date.today().isoformat()}"
    return uit


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("uitkomst")
    u.add_argument("rapport", type=Path)
    u.add_argument("--index", help="vergelijkingsindex of ETF, bv. ^OMXC25, ^BFX, IWDA.AS")
    u.add_argument("--factor", action="append", default=[], help="DATUM:FACTOR (koersen vanaf DATUM ÷ FACTOR, naar de eenheid van het rapport)")
    a = ap.parse_args(argv)
    factoren = [(x.split(":")[0], float(x.split(":")[1])) for x in a.factor]
    res = uitkomst(a.rapport, a.index, factoren)
    pad = a.rapport.parent / "uitkomst.json"
    pad.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    print(f"\nOpgeslagen: {pad}", file=sys.stderr)


if __name__ == "__main__":
    main()
