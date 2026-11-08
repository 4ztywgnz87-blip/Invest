"""Gedeelde hulpfuncties voor de Invest-tools."""
from __future__ import annotations

import json
import re
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAPPORTEN = ROOT / "rapporten"

# Generieke browser-UA: sommige sites weigeren requests zonder UA.
BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
# SEC vraagt een beschrijvende UA voor geautomatiseerde clients.
SEC_UA = "Invest-research-tool (personal, non-commercial)"


def session(ua: str = BROWSER_UA) -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": ua, "Accept-Language": "nl,en;q=0.8"})
    return s


def slug(ticker: str) -> str:
    """Mapnaam voor een ticker: SOF.BR -> SOF.BR (alleen veilige tekens)."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", ticker.upper())


def ticker_dir(ticker: str) -> Path:
    d = DATA / slug(ticker)
    d.mkdir(parents=True, exist_ok=True)
    return d


def read_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
