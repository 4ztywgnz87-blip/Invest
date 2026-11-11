"""Rapport bouwen: rapport.json -> controle -> rapport.html (+ rapport.pdf).

Gebruik:
  python3 tools/rapport.py controleer rapporten/SOF.BR/2026-11-08/rapport.json
  python3 tools/rapport.py bouw       rapporten/SOF.BR/2026-11-08/rapport.json [--pdf]

De structuur van rapport.json staat in .claude/skills/analyseer/rapport-formaat.md.
'bouw' weigert te bouwen zolang er FOUTEN zijn (waarschuwingen mogen).
Zonder afgeronde teamreview (>= 2 rondes, 3 reviewers) kan enkel met --concept gebouwd worden.
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

import bronrang
import dekking
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
BLOKTYPES = ("kop", "uitleg", "tekst", "lijst", "tabel", "grafiek", "kader", "kerncijfers")
REVIEWERS = ("financieel-analist", "actua-specialist", "kritische-belegger")
REVIEW_OORDELEN = ("goedgekeurd", "goedgekeurd met opmerkingen", "niet goedgekeurd")


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


def controleer_review(r: dict, c: "Controle", definitief: bool) -> None:
    rv = r.get("review")
    meld = c.fout if definitief else c.let_op
    if not rv:
        meld("review ontbreekt: het analyseteam heeft dit rapport nog niet gereviewd (fase 11)")
        return
    rondes = rv.get("rondes", [])
    for rd in rondes:
        for naam, oordeel in rd.get("oordelen", {}).items():
            if naam not in REVIEWERS:
                c.fout(f"review ronde {rd.get('nr')}: onbekende reviewer '{naam}'")
            if oordeel not in REVIEW_OORDELEN:
                c.fout(f"review ronde {rd.get('nr')}: oordeel '{oordeel}' ongeldig")
    if rv.get("status") != "afgerond":
        meld("review is nog niet afgerond (status ≠ 'afgerond')")
        return
    snel = r.get("meta", {}).get("soort") == "snelle_update"
    if not rondes or (len(rondes) < 2 and not snel):
        c.fout("review: minstens 2 rondes nodig (onafhankelijk + samen opnieuw bekijken); 1 ronde mag enkel bij een snelle update")
        return
    laatste = rondes[-1].get("oordelen", {})
    ontbrekend = [n for n in REVIEWERS if n not in laatste]
    if snel:
        if not laatste:
            c.fout("review: een snelle update heeft minstens één reviewer nodig")
    elif ontbrekend:
        c.fout(f"review: in de laatste ronde ontbreken {ontbrekend}")
    if "niet goedgekeurd" in laatste.values() and not rv.get("open_punten"):
        c.fout("review: een reviewer keurt niet goed, maar er staan geen open punten in het rapport")
    if not rv.get("feiten_gecontroleerd"):
        c.fout("review: feiten_gecontroleerd ontbreekt (financieel analist moet bronnen naast het rapport leggen)")


def bereken_score(so: dict) -> dict:
    """Gewogen gemiddelde van de onderdelen + correcties, afgerond (half naar boven), begrensd op 1–10."""
    onderdelen = so.get("onderdelen", [])
    basis = sum((o.get("gewicht") or 0) * (o.get("punten") or 0) for o in onderdelen) / 100
    corr = sum(x.get("punten") or 0 for x in so.get("correcties", []))
    totaal = basis + corr
    return {"basis": round(basis, 2), "correcties": round(corr, 2), "totaal": round(totaal, 2),
            "score": max(1, min(10, int(totaal + 0.5)))}


def controleer_scoreopbouw(r: dict, c: "Controle", definitief: bool) -> None:
    adv = r.get("advies", {})
    if adv.get("oordeel") == "Onvoldoende info":
        return
    so = adv.get("score_opbouw")
    if not so:
        (c.fout if definitief else c.let_op)("advies.score_opbouw ontbreekt: toon per onderdeel hoe de score tot stand komt")
        return
    onderdelen = so.get("onderdelen", [])
    if not onderdelen:
        c.fout("advies.score_opbouw.onderdelen is leeg")
        return
    som = sum(o.get("gewicht") or 0 for o in onderdelen)
    if abs(som - 100) > 0.01:
        c.fout(f"advies.score_opbouw: gewichten tellen op tot {som}%, moet 100% zijn")
    for o in onderdelen:
        p = o.get("punten")
        if not isinstance(p, (int, float)) or not 0 <= p <= 10:
            c.fout(f"score_opbouw '{o.get('naam')}': punten moeten 0–10 zijn")
        if not o.get("uitleg"):
            c.fout(f"score_opbouw '{o.get('naam')}': uitleg ontbreekt (waarom deze punten?)")
    for x in so.get("correcties", []):
        if not isinstance(x.get("punten"), (int, float)) or not x.get("uitleg"):
            c.fout(f"score_opbouw correctie '{x.get('naam')}': punten en uitleg verplicht")
    uit = bereken_score(so)
    so["_berekend"] = uit
    if adv.get("score") != uit["score"]:
        c.fout(f"advies.score ({adv.get('score')}) ≠ berekende score uit score_opbouw ({uit['score']}; "
               f"basis {uit['basis']} + correcties {uit['correcties']})")
    if r.get("_r1", {}).get("geraakt") and not any("R1" in (x.get("naam") or "") for x in so.get("correcties", [])):
        c.fout("R1 geraakt maar score_opbouw heeft geen correctie met 'R1' in de naam")


def controleer_bronrang(r: dict, c: "Controle") -> None:
    """Waarschuwt voor zwakke bronnen en voor nieuws zonder de afgesproken basis (De Tijd/L'Echo, Reuters)."""
    bronnen = r.get("bronnen", [])
    rangen = {b.get("id"): bronrang.rang(b) for b in bronnen}
    for b in bronnen:
        b["_rang"] = rangen[b.get("id")][0]
    zwak = [b for b in bronnen if b["_rang"] == "D"]
    for b in zwak:
        c.let_op(f"zwakke bron [{b.get('id')}] {b.get('uitgever')}: {rangen[b.get('id')][1]} — zoek het origineel of een primaire bron")
    enkel_zwak = []
    for waar, b in _blokken(r):
        for it in _items(b):
            ids = it.get("bronnen") or []
            if it.get("label") == "feit" and ids and all(rangen.get(i, ("C",))[0] == "D" for i in ids):
                enkel_zwak.append(waar)
    if enkel_zwak:
        c.let_op(f"{len(enkel_zwak)} feit(en) steunen enkel op een zwakke bron: {', '.join(enkel_zwak[:6])}{' …' if len(enkel_zwak) > 6 else ''}")
    nieuws = [b for b in bronnen if b.get("type") == "nieuws"]
    if nieuws and not any(bronrang.is_basis(b) for b in bronnen):
        c.let_op("geen enkele bron van De Tijd, L'Echo of Reuters (de afgesproken basis voor nieuws)")


def controleer_soort(r: dict, c: "Controle") -> None:
    m = r.get("meta", {})
    soort = m.get("soort")
    if soort not in (None, "volledig", "snelle_update"):
        c.fout(f"meta.soort '{soort}' ongeldig (volledig | snelle_update)")
    if soort != "snelle_update":
        return
    if not m.get("vorig_rapport"):
        c.fout("snelle update zonder meta.vorig_rapport")
    else:
        try:
            dagen = (dt.date.fromisoformat(m["datum"]) - dt.date.fromisoformat(m.get("basis_rapport") or m["vorig_rapport"])).days
            if dagen > 90:
                c.fout(f"snelle update: het laatste volledige rapport is {dagen} dagen oud (max 90) — maak een volledige update")
        except (ValueError, KeyError):
            c.fout("snelle update: meta.datum / meta.vorig_rapport / meta.basis_rapport moeten JJJJ-MM-DD zijn")
    if not r.get("wijzigingen"):
        c.fout("snelle update zonder 'wijzigingen' (wat is er veranderd?)")


def controleer_dekking(map_: Path | None, c: "Controle", definitief: bool) -> None:
    wd = map_ / "werkdossier.md" if map_ else None
    if not wd or not wd.exists():
        return
    fouten, info = dekking.controleer(wd.read_text(encoding="utf-8"))
    if fouten and "geen '## Dekkingslijst'" in fouten[0]:
        c.let_op(fouten[0])
        return
    for f in fouten:
        (c.fout if definitief else c.let_op)(f)


def controleer(r: dict, definitief: bool = True, map_: Path | None = None) -> Controle:
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
    controleer_scoreopbouw(r, c, definitief)
    # Onvoldoende info vereist 3 zoekrondes
    for o in r.get("onvoldoende_info", []):
        if len(o.get("zoekrondes", [])) < 3:
            c.fout(f"onvoldoende_info '{o.get('onderwerp')}': minstens 3 gedocumenteerde zoekrondes nodig")
    ks = r.get("keten_schema")
    if ks is not None:
        if not ks.get("centrum") or not ks.get("takken"):
            c.fout("keten_schema: 'centrum' en 'takken' zijn verplicht")
        for t in ks.get("takken", []):
            if not t.get("naam"):
                c.fout("keten_schema: elke tak heeft een 'naam' nodig")
            if len(t.get("onder", [])) > 5:
                c.fout(f"keten_schema '{t.get('naam')}': maximaal 5 punten op niveau 2")
    elif r.get("meta", {}).get("type") in ("aandeel", "ipo"):
        c.let_op("geen keten_schema (schema van de keten bovenaan het hoofdstuk 'keten')")
    zonder_wat = 0
    for _, b in _blokken(r):
        if b.get("type") != "kerncijfers":
            continue
        for it in b.get("items", []):
            if it.get("beoordeling") not in (None, "goed", "normaal", "zwak"):
                c.fout(f"kerncijfer '{it.get('naam')}': beoordeling moet goed, normaal of zwak zijn")
            if it.get("beoordeling") and not it.get("beoordeling_uitleg"):
                c.fout(f"kerncijfer '{it.get('naam')}': beoordeling zonder beoordeling_uitleg")
            if not it.get("wat"):
                zonder_wat += 1
    if zonder_wat:
        c.let_op(f"{zonder_wat} kerncijfer(s) zonder 'wat' (uitleg onder de knop: wat is dit cijfer?)")
    if not r.get("bronnen"):
        c.fout("geen bronnen")
    controleer_bronrang(r, c)
    controleer_soort(r, c)
    controleer_dekking(map_, c, definitief)
    controleer_review(r, c, definitief)
    return c


# ---------------------------------------------------------------- weergave
def inline(tekst: str, bron_nr: dict) -> str:
    """Beperkte opmaak: **vet**, *cursief*, [[term|uitleg]] (term = knop, uitleg klapt open)."""
    t = html.escape(tekst or "")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", t)
    t = re.sub(r"\[\[(.+?)\|(.+?)\]\]",
               r'<span class="term" tabindex="0" role="button" aria-expanded="false">\1</span><span class="uitleg">\2</span>', t)
    return t.replace("\n", "<br>")


def bron_refs(ids, bron_nr):
    if not ids:
        return ""
    return "".join(f'<a class="ref" href="#bron-{i}">{bron_nr.get(i, "?")}</a>' for i in ids)


def _pct(v, nu):
    if not nu or v is None:
        return ""
    d = (v / nu - 1) * 100
    if abs(d) < 0.5:
        return ""
    return f"{'+' if d > 0 else '−'}{abs(d):.0f}%"


def prijsbalk(r: dict):
    """Alle prijzen van het advies op één schaal (posities in % van de balk)."""
    a = r.get("advies", {})
    nu = a.get("koers_nu")
    punten = []  # (soort, naam, waarde)
    if a.get("stop_loss"):
        punten.append(("stop", "Stop-loss", a["stop_loss"].get("waarde")))
    if a.get("koersdoel") is not None:
        punten.append(("doel", "Koersdoel", a["koersdoel"]))
    if a.get("intrinsieke_waarde"):
        punten.append(("iw", "Intrinsieke waarde", a["intrinsieke_waarde"]))
    for sc in a.get("scenarios", []):
        punten.append(("sc " + sc["naam"], sc["naam"], sc.get("koers")))
    kz = a.get("koopzone") or {}
    waarden = [w for _, _, w in punten if isinstance(w, (int, float))]
    waarden += [w for w in (nu, kz.get("van"), kz.get("tot")) if isinstance(w, (int, float))]
    if nu is None or len(waarden) < 3:
        return None
    lo, hi = min(waarden), max(waarden)
    marge = (hi - lo) * 0.06 or 1
    lo, hi = lo - marge, hi + marge
    pos = lambda w: round((w - lo) / (hi - lo) * 100, 1)
    return {
        "min": min(waarden), "max": max(waarden), "nu": pos(nu),
        "zone": {"links": pos(kz["van"]), "breedte": round(pos(kz["tot"]) - pos(kz["van"]), 1)} if kz.get("van") and kz.get("tot") else None,
        "punten": [{"soort": s, "naam": n, "pos": pos(w)} for s, n, w in punten if isinstance(w, (int, float))],
    }


def structureer(r: dict) -> None:
    """Weergavestructuur: hoofdstukken in uitklapbare delen, vlaggen met details apart, prijsbalk."""
    for s in r.get("secties", []):
        intro, delen = [], []
        for b in s.get("inhoud", []):
            if b.get("type") == "kop":
                delen.append({"titel": b.get("tekst", ""), "blokken": []})
            elif delen:
                delen[-1]["blokken"].append(b)
            else:
                intro.append(b)
        s["_intro"], s["_delen"] = intro, delen
    for v in r.get("rode_vlaggen", []):
        u = v.get("uitleg", [])
        k = next((i for i, b in enumerate(u) if (b.get("tekst") or "").lstrip("*").lower().startswith("de details")), None)
        if k is None:
            k = 3 if len(u) > 3 else len(u)
        v["_kern"], v["_details"] = u[:k], u[k:]
    # Aandeelhouders als één gestapelde balk: de drie grootste (R1) gekleurd, met de 49%-grens.
    ah = (r.get("aandeelhouders") or {}).get("verdeling") or []
    echte = sorted((x for x in ah if not x.get("eigen_aandelen") and not x.get("vrij_verhandelbaar")), key=lambda x: -(x.get("pct") or 0))
    top3 = {id(x) for x in echte[:3]}
    volg = echte + [x for x in ah if x.get("eigen_aandelen")] + [x for x in ah if x.get("vrij_verhandelbaar")]
    r["_ah_balk"] = [{"naam": x.get("naam"), "pct": x.get("pct") or 0,
                      "soort": "top" if id(x) in top3 else "eigen" if x.get("eigen_aandelen") else "vrij" if x.get("vrij_verhandelbaar") else "ander"}
                     for x in volg if (x.get("pct") or 0) > 0]
    r["_vlaggen"] = [v for v in r.get("rode_vlaggen", []) if v.get("ernst") != "info"]
    r["_vlaggen_info"] = [v for v in r.get("rode_vlaggen", []) if v.get("ernst") == "info"]
    a = r.get("advies", {})
    nu = a.get("koers_nu")
    r["_prijsbalk"] = prijsbalk(r)
    r["_pct"] = {
        "koopzone": " tot ".join(x for x in (_pct((a.get("koopzone") or {}).get("van"), nu), _pct((a.get("koopzone") or {}).get("tot"), nu)) if x),
        "koersdoel": _pct(a.get("koersdoel"), nu),
        "iw": _pct(a.get("intrinsieke_waarde"), nu),
        "scenarios": [_pct(sc.get("koers"), nu) for sc in a.get("scenarios", [])],
    }


def bouw_html(r: dict) -> str:
    structureer(r)
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]))
    bron_nr = {b["id"]: n for n, b in enumerate(r.get("bronnen", []), 1)}
    from markupsafe import Markup

    env.filters["inline"] = lambda t: Markup(inline(t, bron_nr))
    env.filters["refs"] = lambda ids: Markup(bron_refs(ids, bron_nr))
    env.filters["svg"] = lambda b: Markup(grafiek.svg(b))
    env.filters["getal"] = lambda v, e="": grafiek.fmt(v, e) if isinstance(v, (int, float)) else (v if v is not None else "–")
    # Woordenlijst: alle [[term|uitleg]] uit het rapport, alfabetisch.
    # Enkel binnen tekstwaarden zoeken: op de hele JSON zou "[[" van geneste
    # lijsten (tabelrijen) als term gelezen worden.
    def teksten(o):
        if isinstance(o, str):
            yield o
        elif isinstance(o, dict):
            for v in o.values():
                yield from teksten(v)
        elif isinstance(o, list):
            for v in o:
                yield from teksten(v)

    woorden = {}
    for s in teksten(r):
        for term, uitleg in re.findall(r"\[\[([^\[\]|]+)\|([^\[\]]+)\]\]", s):
            woorden.setdefault(term.strip(), uitleg.strip())
    r["_woordenlijst"] = sorted(woorden.items(), key=lambda kv: kv[0].lower())
    css = (ROOT / "templates" / "rapport.css").read_text(encoding="utf-8")
    tpl = env.get_template("rapport.html.j2")
    return tpl.render(r=r, labels=LABELS, bron_nr=bron_nr, css=Markup(css),
                      gebouwd=dt.datetime.now().strftime("%d-%m-%Y %H:%M"))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["controleer", "bouw"])
    ap.add_argument("json")
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--concept", action="store_true", help="bouwen zonder afgeronde teamreview (met CONCEPT-markering)")
    a = ap.parse_args(argv)
    pad = Path(a.json)
    r = json.loads(pad.read_text(encoding="utf-8"))
    c = controleer(r, definitief=not a.concept, map_=pad.parent)
    r["_concept"] = a.concept
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
