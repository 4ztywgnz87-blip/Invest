"""Rapport bouwen: rapport.json -> controle -> rapport.html (+ rapport.pdf).

Gebruik:
  python3 tools/rapport.py controleer rapporten/SOF.BR/2026-11-08/rapport.json
  python3 tools/rapport.py bouw       rapporten/SOF.BR/2026-11-08/rapport.json [--pdf]

De structuur van rapport.json staat in .claude/skills/analyseer/rapport-formaat.md.
'bouw' weigert te bouwen zolang er FOUTEN zijn (waarschuwingen mogen).
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import grafiek
from common import ROOT

LABELS = {"feit": "Feit", "berekening": "Berekening", "inschatting": "Inschatting", "mening": "Mening"}
OORDELEN = ("Kopen", "Houden", "Verkopen", "Afwachten", "Onvoldoende info")
ERNST = ("nogo", "hoog", "middel", "info")
TYPES = ("aandeel", "etf", "fonds", "ipo")
VERPLICHT = {
    "aandeel": ["bestuur", "cijfers", "investeringen", "keten", "sector", "actualiteit", "earnings_call",
                "waardering", "techniek", "expert", "profiel"],
    "ipo": ["bestuur", "cijfers", "investeringen", "keten", "sector", "actualiteit", "waardering", "expert", "profiel"],
    "etf": ["samenstelling", "kosten", "index", "risico", "actualiteit", "techniek", "fiscaliteit", "expert", "profiel"],
    "fonds": ["samenstelling", "kosten", "beheer", "risico", "actualiteit", "fiscaliteit", "expert", "profiel"],
}
BLOKTYPES = ("tekst", "lijst", "tabel", "grafiek", "kader", "kerncijfers")


# ---------------------------------------------------------------- controle
class Controle:
    def __init__(self):
        self.fouten, self.waarsch = [], []

    def fout(self, m):
        self.fouten.append(m)

    def let_op(self, m):
        self.waarsch.append(m)


def _blokken(r: dict):
    """Alle blokken met hun locatie."""
    for i, b in enumerate(r.get("samenvatting", [])):
        yield f"samenvatting[{i}]", b
    for i, b in enumerate(r.get("wijzigingen", [])):
        yield f"wijzigingen[{i}]", b
    for v in r.get("rode_vlaggen", []):
        for i, b in enumerate(v.get("uitleg", [])):
            yield f"rode_vlag '{v.get('titel')}'[{i}]", b
    for s in r.get("secties", []):
        for i, b in enumerate(s.get("inhoud", [])):
            yield f"sectie {s.get('id')}[{i}]", b


def _items(b: dict):
    """Elementen met label/bronnen binnen een blok."""
    t = b.get("type")
    if t == "tekst":
        yield b
    elif t in ("lijst", "kerncijfers"):
        yield from b.get("items", [])


def controleer(r: dict) -> Controle:
    c = Controle()
    meta = r.get("meta", {})
    for k in ("ticker", "naam", "type", "datum"):
        if not meta.get(k):
            c.fout(f"meta.{k} ontbreekt")
    typ = meta.get("type")
    if typ and typ not in TYPES:
        c.fout(f"meta.type moet een van {TYPES} zijn")

    adv = r.get("advies", {})
    if adv.get("oordeel") not in OORDELEN:
        c.fout(f"advies.oordeel moet een van {OORDELEN} zijn")
    if adv.get("oordeel") != "Onvoldoende info":
        s = adv.get("score")
        if not isinstance(s, (int, float)) or not 1 <= s <= 10:
            c.fout("advies.score moet 1–10 zijn")
        sc = adv.get("scenarios", [])
        if [x.get("naam") for x in sc] != ["Slecht", "Normaal", "Goed"]:
            c.fout("advies.scenarios moet precies Slecht, Normaal, Goed bevatten (in die volgorde)")
        for k in ("koopzone", "koersdoel"):
            if adv.get(k) is None:
                c.let_op(f"advies.{k} ontbreekt")
    if not adv.get("reden"):
        c.fout("advies.reden ontbreekt")

    # Bronnen
    bron_ids = {b.get("id") for b in r.get("bronnen", [])}
    for b in r.get("bronnen", []):
        for k in ("id", "titel", "uitgever"):
            if not b.get(k):
                c.fout(f"bron {b.get('id')}: veld '{k}' ontbreekt")
        if not b.get("url") and not b.get("document"):
            c.fout(f"bron {b.get('id')}: url of document (bv. 'Jaarverslag 2025 p.34') verplicht")
        if b.get("type") == "forum":
            c.fout(f"bron {b.get('id')}: forums zijn nooit een bron van feiten")
    gebruikt = set()

    def check_bronnen(waar, ids, verplicht):
        ids = ids or []
        if verplicht and not ids:
            c.fout(f"{waar}: feit zonder bron")
        for i in ids:
            if i not in bron_ids:
                c.fout(f"{waar}: bron {i} bestaat niet")
            gebruikt.add(i)

    for waar, b in _blokken(r):
        t = b.get("type")
        if t not in BLOKTYPES:
            c.fout(f"{waar}: onbekend bloktype '{t}'")
            continue
        for it in _items(b):
            lab = it.get("label")
            if lab not in LABELS:
                c.fout(f"{waar}: label '{lab}' ongeldig (feit/berekening/inschatting/mening)")
            check_bronnen(waar, it.get("bronnen"), lab == "feit")
            if lab == "inschatting" and not it.get("tekst", "").strip():
                c.fout(f"{waar}: lege inschatting")
        if t in ("tabel", "grafiek"):
            check_bronnen(waar, b.get("bronnen"), not b.get("bron_tekst"))
            if t == "grafiek":
                n = len(b.get("x", []))
                for rs in b.get("reeksen", []):
                    if len(rs.get("waarden", [])) != n:
                        c.fout(f"{waar}: reeks '{rs.get('naam')}' heeft {len(rs.get('waarden', []))} waarden, x heeft {n}")
                if len(b.get("reeksen", [])) > grafiek.MAX_REEKSEN:
                    c.fout(f"{waar}: max {grafiek.MAX_REEKSEN} reeksen per grafiek (splits op)")
            if t == "tabel":
                nk = len(b.get("kolommen", []))
                for j, rij in enumerate(b.get("rijen", [])):
                    if len(rij) != nk:
                        c.fout(f"{waar}: tabelrij {j} heeft {len(rij)} cellen, verwacht {nk}")
    for v in r.get("rode_vlaggen", []):
        if v.get("ernst") not in ERNST:
            c.fout(f"rode vlag '{v.get('titel')}': ernst moet een van {ERNST} zijn")
    ongebruikt = bron_ids - gebruikt
    if ongebruikt:
        c.let_op(f"bronnen nooit geciteerd: {sorted(ongebruikt)}")

    # Secties
    ids = [s.get("id") for s in r.get("secties", [])]
    for s in VERPLICHT.get(typ, []):
        if s not in ids:
            c.fout(f"verplichte sectie '{s}' ontbreekt (of zet ze erin met de reden waarom er niets is)")

    # Regel R1: aandeelhouders > 49 %
    if typ in ("aandeel", "ipo"):
        ah = r.get("aandeelhouders")
        if not ah or not ah.get("verdeling"):
            c.fout("aandeelhouders.verdeling ontbreekt (verplicht voor regel R1)")
        else:
            check_bronnen("aandeelhouders", ah.get("bronnen"), True)
            pct = sorted((x.get("pct") or 0 for x in ah["verdeling"] if not x.get("vrij_verhandelbaar") and not x.get("eigen_aandelen")), reverse=True)
            grootste, top3 = (pct[0] if pct else 0), sum(pct[:3])
            stem = sorted((x.get("stemrecht_pct") or x.get("pct") or 0 for x in ah["verdeling"] if not x.get("vrij_verhandelbaar") and not x.get("eigen_aandelen")), reverse=True)
            top3_stem = sum(stem[:3])
            r["_r1"] = {"grootste": grootste, "top3": round(top3, 2), "top3_stem": round(top3_stem, 2),
                        "geraakt": grootste > 49 or top3 > 49 or top3_stem > 49}
            if r["_r1"]["geraakt"] and not any(v.get("regel") == "R1" for v in r.get("rode_vlaggen", [])):
                c.fout(f"Regel R1 geraakt (grootste {grootste}%, top 3 samen {top3:.1f}%, stemrecht top 3 {top3_stem:.1f}%) "
                       "maar er is geen rode vlag met regel 'R1'")
    # Onvoldoende info vereist 3 zoekrondes
    for o in r.get("onvoldoende_info", []):
        if len(o.get("zoekrondes", [])) < 3:
            c.fout(f"onvoldoende_info '{o.get('onderwerp')}': minstens 3 gedocumenteerde zoekrondes nodig")
    if not r.get("bronnen"):
        c.fout("geen bronnen")
    return c


# ---------------------------------------------------------------- weergave
def inline(tekst: str, bron_nr: dict) -> str:
    """Beperkte opmaak: **vet**, [[term|uitleg]], [n] bronverwijzing."""
    t = html.escape(tekst or "")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[\[(.+?)\|(.+?)\]\]", r'<span class="term">\1</span> <span class="uitleg">(\2)</span>', t)
    return t


def bron_refs(ids, bron_nr):
    if not ids:
        return ""
    return "".join(f'<a class="ref" href="#bron-{i}">{bron_nr.get(i, "?")}</a>' for i in ids)


def bouw_html(r: dict) -> str:
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]))
    bron_nr = {b["id"]: n for n, b in enumerate(r.get("bronnen", []), 1)}
    from markupsafe import Markup

    env.filters["inline"] = lambda t: Markup(inline(t, bron_nr))
    env.filters["refs"] = lambda ids: Markup(bron_refs(ids, bron_nr))
    env.filters["svg"] = lambda b: Markup(grafiek.svg(b))
    env.filters["getal"] = lambda v, e="": grafiek.fmt(v, e) if isinstance(v, (int, float)) else (v if v is not None else "–")
    css = (ROOT / "templates" / "rapport.css").read_text(encoding="utf-8")
    tpl = env.get_template("rapport.html.j2")
    return tpl.render(r=r, labels=LABELS, bron_nr=bron_nr, css=Markup(css),
                      gebouwd=dt.datetime.now().strftime("%d-%m-%Y %H:%M"))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["controleer", "bouw"])
    ap.add_argument("json")
    ap.add_argument("--pdf", action="store_true")
    a = ap.parse_args(argv)
    pad = Path(a.json)
    r = json.loads(pad.read_text(encoding="utf-8"))
    c = controleer(r)
    for w in c.waarsch:
        print(f"⚠️  {w}")
    for f in c.fouten:
        print(f"❌ {f}")
    if c.fouten:
        sys.exit(f"\n{len(c.fouten)} fout(en) — los op voor je bouwt.")
    print(f"✅ Controle ok ({len(c.waarsch)} waarschuwing(en)).")
    if a.cmd == "bouw":
        uit = pad.with_name("rapport.html")
        uit.write_text(bouw_html(r), encoding="utf-8")
        print(f"HTML: {uit}")
        if a.pdf:
            pdf = pad.with_name("rapport.pdf")
            subprocess.run(["node", str(ROOT / "tools" / "pdf_export.js"), str(uit), str(pdf)], check=True)
            print(f"PDF:  {pdf}")


if __name__ == "__main__":
    main()
