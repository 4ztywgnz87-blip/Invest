"""Bronnengeheugen per bedrijf: welke artikels/verslagen zijn al gelezen?

Doel: bij een nieuw rapport geen bronnen opnieuw analyseren, tenzij ze gewijzigd zijn.

Gebruik:
  python3 tools/bronnen.py check  SOF.BR <url>             # nieuw / gekend / gewijzigd?
  python3 tools/bronnen.py voegtoe SOF.BR <url> --titel "..." --uitgever "De Tijd" \
        --datum 2026-03-05 --type nieuws --samenvatting "1-3 zinnen: wat staat erin, welke cijfers" \
        [--inhoud-bestand pad/naar/tekst.txt]
  python3 tools/bronnen.py lijst  SOF.BR [--type nieuws]
  python3 tools/bronnen.py zoek   SOF.BR "hormuz"            # in titels + samenvattingen

Types: primair (verslag, persbericht bedrijf, toezichthouder), nieuws, data, analyse, overig.
De samenvatting is wat een volgende analyse hergebruikt i.p.v. de bron opnieuw te lezen.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys

from common import read_json, session, ticker_dir, write_json

TYPES = ("primair", "nieuws", "data", "analyse", "overig")


def norm_url(url: str) -> str:
    url = url.strip()
    url = re.sub(r"[?&](utm_[^=&]+|fbclid|gclid)=[^&]*", "", url)
    return url.rstrip("/")


def pad(ticker):
    return ticker_dir(ticker) / "bronnen.json"


def laad(ticker) -> list[dict]:
    return read_json(pad(ticker), [])


def inhoud_hash(tekst: str) -> str:
    tekst = re.sub(r"\s+", " ", tekst).strip().lower()
    return hashlib.sha256(tekst.encode()).hexdigest()[:16]


def haal_hash(url: str) -> str | None:
    try:
        r = session().get(url, timeout=30)
        if r.status_code != 200:
            return None
        if r.content[:5].startswith(b"%PDF"):
            return hashlib.sha256(r.content).hexdigest()[:16]
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "lxml")
        for t in soup(["script", "style", "nav", "header", "footer", "aside"]):
            t.decompose()
        return inhoud_hash(soup.get_text(" "))
    except Exception:
        return None


def check(ticker, url, online=True):
    u = norm_url(url)
    for b in laad(ticker):
        if b["url"] == u:
            if online and b.get("hash"):
                h = haal_hash(u)
                if h and h != b["hash"]:
                    return "GEWIJZIGD", b
            return "GEKEND", b
    return "NIEUW", None


def voegtoe(ticker, url, titel, uitgever, datum, type_, samenvatting, inhoud_bestand=None):
    if type_ not in TYPES:
        sys.exit(f"type moet een van {TYPES} zijn")
    lijst = laad(ticker)
    u = norm_url(url)
    h = None
    if inhoud_bestand:
        h = inhoud_hash(open(inhoud_bestand, encoding="utf-8").read())
    else:
        h = haal_hash(u)
    nu = dt.date.today().isoformat()
    bestaand = next((b for b in lijst if b["url"] == u), None)
    item = {"url": u, "titel": titel, "uitgever": uitgever, "datum": datum, "type": type_,
            "samenvatting": samenvatting, "hash": h, "gelezen_op": nu}
    if bestaand:
        bestaand.update({k: v for k, v in item.items() if v})
        bestaand.setdefault("historiek", []).append(nu)
    else:
        lijst.append(item)
    lijst.sort(key=lambda b: (b.get("datum") or ""), reverse=True)
    write_json(pad(ticker), lijst)
    print(("Bijgewerkt" if bestaand else "Toegevoegd") + f": {titel} ({u})")


def main(argv=None):
    ap = argparse.ArgumentParser()
    s = ap.add_subparsers(dest="cmd", required=True)
    c = s.add_parser("check"); c.add_argument("ticker"); c.add_argument("url"); c.add_argument("--offline", action="store_true")
    v = s.add_parser("voegtoe"); v.add_argument("ticker"); v.add_argument("url")
    v.add_argument("--titel", required=True); v.add_argument("--uitgever", required=True)
    v.add_argument("--datum", required=True); v.add_argument("--type", required=True, choices=TYPES)
    v.add_argument("--samenvatting", required=True); v.add_argument("--inhoud-bestand")
    l = s.add_parser("lijst"); l.add_argument("ticker"); l.add_argument("--type", choices=TYPES)
    z = s.add_parser("zoek"); z.add_argument("ticker"); z.add_argument("q")
    a = ap.parse_args(argv)
    if a.cmd == "check":
        status, b = check(a.ticker, a.url, online=not a.offline)
        print(status)
        if b:
            print(f'  gelezen op {b["gelezen_op"]}: {b["titel"]} — {b["samenvatting"]}')
    elif a.cmd == "voegtoe":
        voegtoe(a.ticker, a.url, a.titel, a.uitgever, a.datum, a.type, a.samenvatting, a.inhoud_bestand)
    else:
        q = getattr(a, "q", "").lower()
        for b in laad(a.ticker):
            if getattr(a, "type", None) and b["type"] != a.type:
                continue
            if q and q not in (b["titel"] + " " + b["samenvatting"]).lower():
                continue
            print(f'{b.get("datum") or "?":<10} [{b["type"]}] {b["uitgever"]}: {b["titel"]}\n    {b["samenvatting"]}\n    {b["url"]}')


if __name__ == "__main__":
    main()
