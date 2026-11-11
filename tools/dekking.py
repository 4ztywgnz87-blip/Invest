"""Dekkingslijst: welke bronnen moeten voor een analyse zeker nagekeken zijn?

Gebruik:
  python3 tools/dekking.py lijst --type aandeel --regio BE [--snel]   # tabel om in het werkdossier te plakken
  python3 tools/dekking.py controleer rapporten/<TICKER>/<datum>/werkdossier.md

Status per rij in het werkdossier:
  ✅ nagekeken (noteer wat/waar)      ➖ niets gevonden of niet van toepassing (reden verplicht)
  ❌ geblokkeerd (alternatief verplicht)   ⬜ nog te doen
Een rapport is pas af als er geen ⬜ meer staat en elke ➖/❌ een notitie heeft.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TOEZICHT = {
    "BE": ("FSMA (transparantieverklaringen)", "FSMA (transacties leidinggevenden)", "Euronext + Belgisch Staatsblad"),
    "NL": ("AFM (register substantiële deelnemingen)", "AFM (MAR-meldingen)", "Euronext"),
    "FR": ("AMF (déclarations de franchissement)", "AMF (transactions des dirigeants)", "Euronext"),
    "DE": ("BaFin / Unternehmensregister (Stimmrechte)", "BaFin (Directors' Dealings)", "Börse Frankfurt / Bundesanzeiger"),
    "UK": ("FCA NSM (TR-1)", "FCA NSM (PDMR)", "LSE RNS"),
    "US": ("SEC EDGAR (SC 13D/13G, DEF 14A)", "SEC EDGAR (Form 4)", "SEC EDGAR (8-K)"),
    "JP": ("EDINET (grote aandeelhouders)", "EDINET / TDnet", "TDnet"),
}
ANDERS = ("nationale toezichthouder (aandeelhouders)", "nationale toezichthouder (insiders)", "beurs / officieel publicatieblad")

# (naam, waarvoor, ook bij snelle update?)
AANDEEL = [
    ("Laatste jaarverslag + kerncijfers 4 jaar ervoor", "cijfers, trend", False),
    ("Laatste halfjaar-/kwartaalverslag + persbericht", "recentste cijfers", True),
    ("Investeerderspresentatie", "strategie, vooruitzichten", False),
    ("Earnings call (transcript of verslag)", "toon management", False),
    ("Verslag van de commissaris (oordeel, kernpunten, wissel revisor)", "betrouwbaarheid cijfers", False),
    ("Remuneratieverslag", "R2, R3", False),
    ("{aandeelhouders}", "R1", True),
    ("{insiders}", "R5", True),
    ("Corporate actions: {beurs} + persberichten bedrijf", "R6", True),
    ("Rechtszaken: jaarverslag + zoekronde nieuws (NL/EN/FR/lokaal) + mededingingsautoriteit/EC", "R4", False),
    ("Kredietbeoordeling (S&P, Moody's, Fitch: persbericht)", "schuld", False),
    ("Persberichten van het bedrijf (laatste 12 maanden; snelle update: sinds vorig rapport)", "actualiteit", True),
    ("Basisnieuws: De Tijd / L'Echo", "actualiteit", True),
    ("Basisnieuws: Reuters (originele URL)", "actualiteit", True),
    ("Internationale kwaliteitspers (FT, Bloomberg, WSJ, AP)", "actualiteit", False),
    ("Vakpers van de sector", "sector, keten", False),
    ("Macro rechtstreeks bij de bron (ECB, Fed, Eurostat, Statbel)", "rente, inflatie, valuta", True),
    ("Verslagen van de 3–5 dichtste concurrenten", "vergelijking", False),
    ("Keten: verslagen/IR-site van de niveau-1-partijen", "keten", False),
    ("Short-seller-onderzoek (enkel aanwijzing, nooit bron)", "R2, R4", False),
    ("Sancties en sectorregelgeving (EU-sanctielijst, sectorregulator)", "risico", False),
    ("Fiscaliteit België (FOD Financiën)", "netto rendement", False),
    ("Koersdata (tools/koers.py)", "techniek, waardering", True),
]
ETF = [
    ("Factsheet + KID", "kosten, samenstelling", True),
    ("Prospectus + jaarverslag van het fonds", "replicatie, uitlening, risico", False),
    ("Holdings-bestand van de uitgever", "samenstelling", True),
    ("Indexmethodologie (indexaanbieder)", "index", False),
    ("Tracking difference (justETF / trackingdifferences.com, enkel data)", "kosten", False),
    ("Alternatieven op dezelfde index (2–4 factsheets)", "vergelijking", False),
    ("Uitgever: rechtszaken/sancties, fondsgrootte en sluitingsrisico", "risico", False),
    ("Basisnieuws: De Tijd / L'Echo", "actualiteit", True),
    ("Basisnieuws: Reuters (originele URL)", "actualiteit", True),
    ("Internationale kwaliteitspers (FT, Bloomberg, WSJ, AP)", "actualiteit", False),
    ("Macro rechtstreeks bij de bron (ECB, Fed, Eurostat, Statbel)", "rente, inflatie, valuta", True),
    ("Fiscaliteit België (FOD Financiën: beurstaks, Reynders-taks, meerwaardebelasting)", "netto rendement", False),
    ("Koersdata (tools/koers.py)", "techniek", True),
]
STATUSSEN = ("✅", "➖", "❌", "⬜")


def rijen(type_: str, regio: str, snel: bool):
    a, i, b = TOEZICHT.get(regio.upper(), ANDERS)
    basis = ETF if type_ in ("etf", "fonds") else AANDEEL
    for naam, waarvoor, bij_snel in basis:
        if snel and not bij_snel:
            continue
        yield naam.format(aandeelhouders=f"Aandeelhouders: {a}", insiders=f"Insiders: {i}", beurs=b), waarvoor


def lijst(type_: str, regio: str, snel: bool) -> str:
    uit = ["## Dekkingslijst", "",
           "> ✅ nagekeken · ➖ niets gevonden / n.v.t. (reden) · ❌ geblokkeerd (alternatief) · ⬜ te doen. Geen ⬜ meer = klaar.", "",
           "| Bron | Waarvoor | Status | Wat gevonden / waarom niet (zoektermen, talen, datum) |", "|---|---|---|---|"]
    uit += [f"| {n} | {w} | ⬜ | |" for n, w in rijen(type_, regio, snel)]
    return "\n".join(uit)


def controleer(tekst: str) -> tuple[list[str], list[str]]:
    """Geeft (fouten, info). Lege lijst fouten = dekkingslijst volledig."""
    m = re.search(r"^## Dekkingslijst\s*$(.*?)(?=^## |\Z)", tekst, re.M | re.S)
    if not m:
        return ["geen '## Dekkingslijst' in het werkdossier (maak ze met tools/dekking.py lijst)"], []
    fouten, tel = [], {s: 0 for s in STATUSSEN}
    for regel in m.group(1).splitlines():
        cel = [c.strip() for c in regel.strip().strip("|").split("|")]
        if len(cel) < 4 or cel[0] in ("Bron", "") or set(cel[0]) <= set("-: "):
            continue
        naam, status, notitie = cel[0], cel[2], cel[3]
        s = next((x for x in STATUSSEN if x in status), None)
        if s is None:
            fouten.append(f"dekkingslijst '{naam}': onbekende status '{status}'")
            continue
        tel[s] += 1
        if s == "⬜":
            fouten.append(f"dekkingslijst '{naam}': nog niet nagekeken")
        elif not notitie:
            fouten.append(f"dekkingslijst '{naam}': {s} zonder notitie (wat gevonden / waarom niet / welk alternatief)")
    if not sum(tel.values()):
        fouten.append("dekkingslijst is leeg")
    return fouten, [f"dekkingslijst: {tel['✅']} nagekeken, {tel['➖']} niets/n.v.t., {tel['❌']} geblokkeerd, {tel['⬜']} open"]


def main(argv=None):
    ap = argparse.ArgumentParser()
    s = ap.add_subparsers(dest="cmd", required=True)
    l = s.add_parser("lijst")
    l.add_argument("--type", default="aandeel", choices=["aandeel", "ipo", "etf", "fonds"])
    l.add_argument("--regio", default="BE", help="BE NL FR DE UK US JP (anders: algemene benaming)")
    l.add_argument("--snel", action="store_true", help="enkel de rijen voor een snelle update")
    c = s.add_parser("controleer")
    c.add_argument("werkdossier")
    a = ap.parse_args(argv)
    if a.cmd == "lijst":
        print(lijst(a.type, a.regio, a.snel))
        return
    fouten, info = controleer(Path(a.werkdossier).read_text(encoding="utf-8"))
    for i in info:
        print(i)
    for f in fouten:
        print(f"❌ {f}")
    if fouten:
        sys.exit(1)
    print("✅ Dekkingslijst volledig.")


if __name__ == "__main__":
    main()
