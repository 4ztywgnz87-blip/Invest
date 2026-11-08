"""Jaar- en kwartaalverslagen (PDF) downloaden en doorzoeken.

Gebruik:
  python3 tools/pdf.py download SOF.BR <url> [--naam jaarverslag-2025]
  python3 tools/pdf.py inhoud  <pdf>                 # aantal pagina's + inhoudstafel-achtige koppen
  python3 tools/pdf.py zoek    <pdf> "term1" "term2" # op welke pagina's staan de termen (met fragment)
  python3 tools/pdf.py pagina  <pdf> 12-15           # tekst van pagina's (1-gebaseerd)

PDF's komen in data/<TICKER>/docs/. Ze worden NIET in git bewaard (te groot), wel de
tekstextractie (.txt per pagina-blok) zodat een volgende sessie niet opnieuw moet downloaden.
Verwijs in het rapport altijd naar document + paginanummer.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pdfplumber

from common import session, ticker_dir


def download(ticker: str, url: str, naam: str | None) -> Path:
    docs = ticker_dir(ticker) / "docs"
    docs.mkdir(exist_ok=True)
    naam = naam or re.sub(r"[^A-Za-z0-9._-]", "_", url.rsplit("/", 1)[-1].split("?")[0]) or "document"
    pad = docs / (naam if naam.lower().endswith(".pdf") else naam + ".pdf")
    r = session().get(url, timeout=120)
    if r.status_code != 200:
        sys.exit(f"Download mislukt ({r.status_code}) voor {url}. Probeer een andere bron/spiegel of WebFetch.")
    if not r.content[:5].startswith(b"%PDF"):
        sys.exit(f"Geen PDF ontvangen van {url} (content-type: {r.headers.get('content-type')}).")
    pad.write_bytes(r.content)
    tekst_cache(pad)
    print(f"Opgeslagen: {pad} ({len(r.content)//1024} kB)")
    return pad


def tekst_cache(pad: Path) -> list[str]:
    """Tekst per pagina, gecachet in <pdf>.txt (pagina's gescheiden door form feed)."""
    cache = pad.with_suffix(".txt")
    if cache.exists() and cache.stat().st_mtime >= pad.stat().st_mtime:
        return cache.read_text(encoding="utf-8").split("\f")
    paginas = []
    with pdfplumber.open(pad) as pdf:
        for p in pdf.pages:
            t = p.extract_text(x_tolerance=1.5) or ""
            if t and t.count(" ") < len(t) / 30:  # woorden aan elkaar geplakt -> andere instelling
                t = p.extract_text(x_tolerance=1) or t
            paginas.append(t)
    cache.write_text("\f".join(paginas), encoding="utf-8")
    return paginas


def laad(pad_str: str) -> list[str]:
    pad = Path(pad_str)
    if pad.suffix == ".txt":
        return pad.read_text(encoding="utf-8").split("\f")
    return tekst_cache(pad)


def inhoud(pad: str) -> None:
    paginas = laad(pad)
    print(f"{len(paginas)} pagina's")
    for i, t in enumerate(paginas, 1):
        regels = [r.strip() for r in t.splitlines() if r.strip()]
        kop = next((r for r in regels[:4] if 4 < len(r) < 90 and not r.replace(" ", "").isdigit()), "")
        print(f"p{i:>4}  {kop}")


def zoek(pad: str, termen: list[str], ctx: int = 90) -> None:
    paginas = laad(pad)
    for term in termen:
        rx = re.compile(re.escape(term), re.I)
        treffers = [(i, m) for i, t in enumerate(paginas, 1) for m in rx.finditer(t)]
        print(f"\n## '{term}': {len(treffers)} treffers op pagina's {sorted({i for i, _ in treffers})}")
        for i, m in treffers[:25]:
            t = paginas[i - 1]
            frag = t[max(0, m.start() - ctx): m.end() + ctx].replace("\n", " ")
            print(f"  p{i}: …{frag}…")


def pagina(pad: str, bereik: str) -> None:
    paginas = laad(pad)
    a, _, b = bereik.partition("-")
    a, b = int(a), int(b or a)
    for i in range(a, min(b, len(paginas)) + 1):
        print(f"\n===== pagina {i} =====\n{paginas[i - 1]}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    s = ap.add_subparsers(dest="cmd", required=True)
    d = s.add_parser("download"); d.add_argument("ticker"); d.add_argument("url"); d.add_argument("--naam")
    i = s.add_parser("inhoud"); i.add_argument("pdf")
    z = s.add_parser("zoek"); z.add_argument("pdf"); z.add_argument("termen", nargs="+")
    p = s.add_parser("pagina"); p.add_argument("pdf"); p.add_argument("bereik")
    a = ap.parse_args(argv)
    if a.cmd == "download":
        download(a.ticker, a.url, a.naam)
    elif a.cmd == "inhoud":
        inhoud(a.pdf)
    elif a.cmd == "zoek":
        zoek(a.pdf, a.termen)
    else:
        pagina(a.pdf, a.bereik)


if __name__ == "__main__":
    main()
