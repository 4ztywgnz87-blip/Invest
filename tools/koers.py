"""Koersdata en technische analyse.

Gebruik:
  python3 tools/koers.py zoek "sofina"          # ticker opzoeken (beurs, naam, type)
  python3 tools/koers.py analyse SOF.BR          # koershistoriek + technische kerncijfers
  python3 tools/koers.py analyse SOF.BR --aankoop 250   # stop-loss t.o.v. aankoopkoers
  python3 tools/koers.py analyse ORSTED.CO --tot 2021-02-15   # terugkijktest: enkel data tot de peildatum

Schrijft data/<TICKER>/koers.json (incl. kant-en-klare grafiekblokken voor het rapport).
Bron: Yahoo Finance (onofficiële publieke endpoints). Vermeld als bron in het rapport.
"""
from __future__ import annotations

import argparse
import datetime as dt
import statistics
import sys

from common import session, ticker_dir, write_json

YQ = "https://query1.finance.yahoo.com"
YQ2 = "https://query2.finance.yahoo.com"


def zoek(q: str) -> list[dict]:
    r = session().get(f"{YQ2}/v1/finance/search", params={"q": q, "quotesCount": 10, "newsCount": 0}, timeout=20)
    r.raise_for_status()
    out = []
    for x in r.json().get("quotes", []):
        out.append({
            "symbool": x.get("symbol"),
            "beurs": x.get("exchDisp") or x.get("exchange"),
            "naam": x.get("longname") or x.get("shortname"),
            "type": x.get("quoteType"),
            "sector": x.get("sectorDisp") or x.get("sector"),
        })
    return out


def historiek(symbool: str, bereik: str = "10y", interval: str = "1d", tot: str | None = None) -> dict:
    """tot (JJJJ-MM-DD): enkel data tot en met die datum (terugkijktest), met 10 jaar historiek ervoor."""
    params = {"interval": interval, "events": "div,splits"}
    if tot:
        eind = dt.datetime.fromisoformat(tot).replace(tzinfo=dt.UTC) + dt.timedelta(days=1)
        params.update(period1=int((eind - dt.timedelta(days=3653)).timestamp()), period2=int(eind.timestamp()))
    else:
        params["range"] = bereik
    r = session().get(f"{YQ}/v8/finance/chart/{symbool}", params=params, timeout=30)
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
    rijen = []
    for i, ts in enumerate(res.get("timestamp") or []):
        c = q["close"][i]
        if c is None:
            continue
        rijen.append({
            "datum": dt.datetime.fromtimestamp(ts, dt.UTC).date().isoformat(),
            "slot": round(c, 4),
            "hoog": q["high"][i], "laag": q["low"][i], "volume": q["volume"][i],
            "slot_aangepast": round(adj[i], 4) if adj and adj[i] is not None else None,
        })
    if tot:
        rijen = [x for x in rijen if x["datum"] <= tot]
    ev = res.get("events", {})
    dividenden = sorted(
        ({"datum": dt.datetime.fromtimestamp(int(k), dt.UTC).date().isoformat(), "bedrag": v["amount"]} for k, v in ev.get("dividends", {}).items()),
        key=lambda d: d["datum"])
    splits = sorted(
        ({"datum": dt.datetime.fromtimestamp(int(k), dt.UTC).date().isoformat(), "verhouding": f'{v["numerator"]}:{v["denominator"]}'} for k, v in ev.get("splits", {}).items()),
        key=lambda d: d["datum"])
    if tot:
        dividenden = [d for d in dividenden if d["datum"] <= tot]
        splits = [d for d in splits if d["datum"] <= tot]
    return {"meta": res["meta"], "rijen": rijen, "dividenden": dividenden, "splits": splits}


def sma(waarden: list[float], n: int) -> float | None:
    return round(sum(waarden[-n:]) / n, 4) if len(waarden) >= n else None


def steunniveaus(rijen: list[dict], venster: int = 10, aantal: int = 4) -> list[dict]:
    """Lokale dieptepunten (swing lows) van het laatste jaar, laagste eerst gegroepeerd."""
    laatste = rijen[-260:]
    lows = []
    for i in range(venster, len(laatste) - venster):
        p = laatste[i]["laag"] or laatste[i]["slot"]
        omgeving = [(r["laag"] or r["slot"]) for r in laatste[i - venster:i + venster + 1]]
        if p == min(omgeving):
            lows.append({"datum": laatste[i]["datum"], "niveau": round(p, 2)})
    nu = laatste[-1]["slot"]
    onder = sorted([l for l in lows if l["niveau"] < nu], key=lambda l: -l["niveau"])
    gekozen = []
    for l in onder:  # samenvoegen als binnen 2% van elkaar
        if all(abs(l["niveau"] - g["niveau"]) / g["niveau"] > 0.02 for g in gekozen):
            gekozen.append(l)
        if len(gekozen) == aantal:
            break
    return gekozen


def max_daling(slot: list[float]) -> float:
    piek, md = slot[0], 0.0
    for c in slot:
        piek = max(piek, c)
        md = min(md, c / piek - 1)
    return round(md * 100, 1)


def rendement(rijen: list[dict], dagen: int) -> float | None:
    if len(rijen) <= dagen:
        return None
    a = rijen[-dagen - 1]["slot_aangepast"] or rijen[-dagen - 1]["slot"]
    b = rijen[-1]["slot_aangepast"] or rijen[-1]["slot"]
    return round((b / a - 1) * 100, 1)


def analyse(symbool: str, aankoop: float | None = None, tot: str | None = None) -> dict:
    h = historiek(symbool, tot=tot)
    rijen = h["rijen"]
    slot = [r["slot"] for r in rijen]
    nu = slot[-1]
    jaar = slot[-252:]
    dag_rend = [slot[i] / slot[i - 1] - 1 for i in range(max(1, len(slot) - 252), len(slot))]
    vol = round(statistics.pstdev(dag_rend) * (252 ** 0.5) * 100, 1) if len(dag_rend) > 20 else None
    s50, s200 = sma(slot, 50), sma(slot, 200)
    if s50 and s200:
        trend = "stijgend" if nu > s50 > s200 else "dalend" if nu < s50 < s200 else "zijwaarts/gemengd"
    else:
        trend = "onbekend (te weinig data)"
    steun = steunniveaus(rijen)
    basis = aankoop or nu
    stop20 = round(basis * 0.8, 2)
    # Technische stop: net onder het dichtstbijzijnde steunniveau dat lager ligt dan -5% en hoger dan -25%.
    tech = next((s for s in steun if basis * 0.75 <= s["niveau"] <= basis * 0.95), None)

    # Jaarlijkse slotkoersen (cycliciteit zichtbaar maken).
    per_jaar = {}
    for r in rijen:
        per_jaar[r["datum"][:4]] = r["slot"]

    # Wekelijkse punten van 5 jaar voor de grafiek (licht houden).
    vijfj = rijen[-1260:]
    stap = max(1, len(vijfj) // 260)
    punten = vijfj[::stap]
    if punten[-1] is not vijfj[-1]:
        punten.append(vijfj[-1])

    m = h["meta"]
    bron = f"Yahoo Finance koersdata {symbool}, opgehaald {dt.date.today().isoformat()}"
    if tot:
        bron += f", afgekapt op peildatum {tot}"
    resultaat = {
        "symbool": symbool,
        "naam": m.get("longName") or m.get("shortName"),
        "beurs": m.get("fullExchangeName") or m.get("exchangeName"),
        "valuta": m.get("currency"),
        "type": m.get("instrumentType"),
        "opgehaald": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "bron": bron,
        "laatste_datum": rijen[-1]["datum"],
        "peildatum": tot,
        "koers": nu,
        "hoog_52w": round(max(jaar), 2), "laag_52w": round(min(jaar), 2),
        "sma50": s50, "sma200": s200, "trend": trend,
        "rendement_pct": {"1m": rendement(rijen, 21), "6m": rendement(rijen, 126), "1j": rendement(rijen, 252),
                           "3j": rendement(rijen, 756), "5j": rendement(rijen, 1260)},
        "volatiliteit_jaar_pct": vol,
        "max_daling_5j_pct": max_daling(slot[-1260:]),
        "steunniveaus": steun,
        "stop_loss": {"basis": basis, "basis_is_aankoop": aankoop is not None, "min20": stop20,
                       "technisch": round(tech["niveau"] * 0.98, 2) if tech else None,
                       "technisch_steun": tech},
        "slot_per_jaar": per_jaar,
        "dividenden": h["dividenden"][-20:],
        "splits": h["splits"],
        "grafiek_blok": {
            "type": "grafiek", "soort": "lijn", "titel": f"Koers {symbool} – laatste 5 jaar", "eenheid": m.get("currency"),
            "x": [p["datum"] for p in punten],
            "reeksen": [{"naam": "Slotkoers", "waarden": [p["slot"] for p in punten]}],
            "lijnen": [l for l in [
                {"naam": "Stop-loss −20%", "waarde": stop20},
                {"naam": "Gemiddelde 200 dagen", "waarde": s200} if s200 else None] if l],
            "bron_tekst": bron,
        },
    }
    return resultaat


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    z = sub.add_parser("zoek"); z.add_argument("q")
    a = sub.add_parser("analyse"); a.add_argument("symbool"); a.add_argument("--aankoop", type=float)
    a.add_argument("--tot", help="peildatum JJJJ-MM-DD (terugkijktest): geen data van daarna")
    args = ap.parse_args(argv)
    import json
    if args.cmd == "zoek":
        for x in zoek(args.q):
            print(f'{x["symbool"]:<12} {str(x["beurs"]):<12} {str(x["type"]):<10} {x["naam"]}')
        return
    res = analyse(args.symbool, args.aankoop, args.tot)
    pad = ticker_dir(args.symbool) / (f"koers_{args.tot}.json" if args.tot else "koers.json")
    write_json(pad, res)
    kort = {k: v for k, v in res.items() if k not in ("grafiek_blok", "slot_per_jaar", "dividenden")}
    print(json.dumps(kort, ensure_ascii=False, indent=1))
    print(f"\nOpgeslagen: {pad}", file=sys.stderr)


if __name__ == "__main__":
    main()
