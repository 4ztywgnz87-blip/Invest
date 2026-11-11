"""Rangorde van bronnen: hoe betrouwbaar is een bron?

  A  primair      bedrijf zelf, toezichthouder, overheid, centrale bank, statistiekbureau, beurs
  B  kwaliteit    persagentschappen en kwaliteitspers, erkende vakpers
  C  overig       andere media, brokers/banken (analyse), dataportalen
  D  zwak         doorgeefsites, wiki's, samenvattingssites: enkel als aanwijzing, zoek het origineel

Gebruik:  python3 tools/bronrang.py <url> [uitgever]
"""
from __future__ import annotations

import re
import sys

A_DOMEINEN = (
    "fsma.be", "nbb.be", "ejustice.just.fgov.be", "fgov.be", "belgium.be", "statbel.fgov.be", "euronext.com",
    "europa.eu", "ecb.europa.eu", "esma.europa.eu", "sec.gov", "federalreserve.gov", "stlouisfed.org", "treasury.gov",
    "bls.gov", "bea.gov", "eia.gov", "iea.org", "imf.org", "worldbank.org", "oecd.org", "bis.org", "opec.org",
    "afm.nl", "amf-france.org", "bafin.de", "consob.it", "cnmv.es", "fca.org.uk", "fi.se", "finanstilsynet.dk",
    "finanstilsynet.no", "edinet-fsa.go.jp", "jpx.co.jp", "courtlistener.com", "spglobal.com", "moodys.com", "fitchratings.com",
)
BASIS_DOMEINEN = ("tijd.be", "lecho.be", "reuters.com")          # afgesproken basis voor nieuws
B_DOMEINEN = BASIS_DOMEINEN + (
    "ft.com", "bloomberg.com", "wsj.com", "apnews.com", "afp.com", "belga.be", "economist.com", "nytimes.com", "bbc.com",
    "bbc.co.uk", "npr.org", "cnbc.com", "handelsblatt.com", "faz.net", "lesechos.fr", "lemonde.fr", "fd.nl", "nikkei.com",
    "scmp.com", "aljazeera.com", "theguardian.com", "trends.knack.be", "knack.be", "vrt.be", "standaard.be", "rtbf.be",
    "techcrunch.com", "theinformation.com", "fiercepharma.com", "utilitydive.com", "offshore-energy.biz", "digitimes.com",
    "lloydslist.com", "spglobal.com",
    "belganewsagency.eu", "businessam.be", "lalibre.be", "levif.be", "washingtonpost.com", "fortune.com", "axios.com", "semafor.com",
    "euronews.com", "sifted.eu", "tech.eu", "abcnews.go.com", "abcnews.com", "nbcnews.com", "cbsnews.com",
)
D_DOMEINEN = (
    "wikipedia.org", "devdiscourse.com", "rttnews.com", "investinglive.com", "tradingeconomics.com", "tastytrade.com",
    "msn.com", "benzinga.com", "fool.com", "zerohedge.com", "seekingalpha.com", "marketbeat.com", "simplywall.st",
    "stocktwits.com", "reddit.com", "x.com", "twitter.com", "medium.com", "substack.com", "investopedia.com",
)
# "Devdiscourse / Reuters", "AP (via Spectrum News 13)": het artikel is van iemand anders overgenomen.
DOORGEEF = re.compile(r"\bvia\b|/", re.I)


def domein(url: str | None) -> str:
    m = re.match(r"https?://([^/]+)", url or "")
    return re.sub(r"^(www|m|en|nl|fr)(-cdn)?\.", "", m.group(1).lower()) if m else ""


def _in(d: str, lijst) -> bool:
    return any(d == x or d.endswith("." + x) for x in lijst)


def rang(bron: dict) -> tuple[str, str]:
    """Geeft (rang, reden) voor een bron uit rapport.json of bronnen.json."""
    d = domein(bron.get("url"))
    uitgever = bron.get("uitgever") or ""
    if _in(d, D_DOMEINEN):
        return "D", f"{d} is een doorgeef- of samenvattingssite"
    if bron.get("type") == "primair" or _in(d, A_DOMEINEN):
        return "A", "primaire bron"
    if _in(d, B_DOMEINEN):
        return "B", "kwaliteitspers"
    if bron.get("type") == "nieuws" and DOORGEEF.search(uitgever):
        return "C", f"'{uitgever}': overgenomen artikel — liever de site van de oorspronkelijke uitgever"
    return "C", "overige bron"


def is_basis(bron: dict) -> bool:
    """De Tijd/L'Echo/Reuters zelf, of een persagentschap (Reuters, AP, Belga) dat een andere uitgever volledig overnam."""
    return _in(domein(bron.get("url")), BASIS_DOMEINEN) or bool(re.search(r"\b(reuters|associated press|ap|belga)\b", bron.get("uitgever") or "", re.I))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    r, reden = rang({"url": sys.argv[1], "uitgever": sys.argv[2] if len(sys.argv) > 2 else "", "type": "nieuws"})
    print(f"{r} — {reden}")
