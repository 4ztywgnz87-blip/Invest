# Bronnen: waar vind je wat?

## Toegang vanuit deze omgeving (getest 2026-11-08)
| Bron | Status | Hoe |
|------|--------|-----|
| Yahoo Finance (koersen, ticker zoeken) | ✅ | `tools/koers.py` |
| SEC EDGAR API (`data.sec.gov`, `efts.sec.gov`) | ✅ met beschrijvende User-Agent | `common.SEC_UA`; `www.sec.gov` website gaf 403 → gebruik de API-endpoints |
| De Tijd (tijd.be) | ✅ (betaalmuur op artikels) | WebSearch voor de kern, WebFetch voor vrije delen |
| Reuters | ❌ direct (401) | WebSearch-resultaten + andere bronnen; web-fetch agent proberen |
| sofina.be | ❌ direct (certificaatprobleem op de site) | web-fetch agent, of het verslag bij een andere bron (FSMA, Euronext, NBB) |
| sofinagroup.com (nieuwe Sofina-site) | ✅ direct (getest 2026-11-08) | `tools/pdf.py download` met `https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/...`; PDF-links staan in de HTML van /en/investors/reports-and-publications |
| FSMA transacties leidinggevenden | ✅ direct | `https://www.fsma.be/en/manager-transaction/<bedrijf>-<nr>` (nummer ophogen) |
| Investing.com transcripts | ✅ via web-fetch agent | titel kan foutief jaar tonen: controleer de inhoud |
| EDINET (Japan) | ❌ direct (403) | SoftBank IR-site (group.softbank ✅), TDnet-persberichten, WebSearch |
| FSMA, NBB Balanscentrale, Euronext | ✅ | direct |

**Algemene volgorde als iets geblokkeerd is**: (1) directe download met `tools/pdf.py`/`curl`, (2) de `web-fetch` agent, (3) dezelfde info bij een andere (officiële) bron, (4) WebSearch-snippets enkel als laatste redmiddel en altijd met de originele bron-URL. Noteer blokkades in het werkdossier en vul deze tabel aan.

## Primaire bronnen per regio
**België**
- Jaarverslagen/persberichten: investor-relationssite van het bedrijf.
- **FSMA** (fsma.be): transparantieverklaringen (aandeelhouders > 5%, …), transacties van leidinggevenden (insiders, MAR), prospectussen (IPO's, uitgiftes).
- **NBB Balanscentrale** (consult.cbso.nbb.be): neergelegde jaarrekeningen (ook van niet-genoteerde dochters/holdings → handig voor R1-structuren).
- **Belgisch Staatsblad**: statutenwijzigingen, kapitaalverhogingen, benoemingen.
- Euronext (live.euronext.com): corporate actions, notering.

**Rest van Europa**
- Nationale toezichthouders/OAM's: AMF (FR), AFM (NL, register substantiële deelnemingen + MAR-meldingen), BaFin (DE), CONSOB (IT), CNMV (ES), FCA NSM (UK), Finansinspektionen (SE), Finanstilsynet (DK/NO).
- ESMA-registers.

**Verenigde Staten** (SEC EDGAR)
- 10-K (jaar), 10-Q (kwartaal), 8-K (belangrijke gebeurtenissen), DEF 14A (vergoedingen, R2/R3), Form 4 (insiders, R5), SC 13D/13G (aandeelhouders > 5%, R1), 20-F/6-K (buitenlandse bedrijven).
- API: `https://data.sec.gov/submissions/CIK##########.json`, `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (gestructureerde cijfers!).

**Japan** — EDINET (yuho = jaarverslag), TDnet (persberichten), IR-site (vaak Engelse vertalingen).

## Koers & markt
- Yahoo Finance via `tools/koers.py` (vermeld als bron "Yahoo Finance koersdata").
- Indexen/ETF's: factsheets van de uitgever (iShares, Vanguard, Amundi, Xtrackers), KID/KIID, jaarverslag van het fonds.

## Macro & grondstoffen
ECB, Federal Reserve/FRED, Eurostat, Statbel, NBB, IMF, Wereldbank, OESO, IEA, EIA (olie/gas), OPEC-rapporten, LME (metalen), USDA/FAO (landbouw), Drewry/Freightos (vrachttarieven), SIA/SEMI (chips).

## Nieuws (zo breed mogelijk)
Basis: **De Tijd, Reuters**. Verder: L'Echo, Trends, VRT/Standaard (economie), FT, Bloomberg, WSJ, AP, CNBC, The Economist, Handelsblatt, Les Echos, FD (NL), Nikkei Asia, sector-vakpers (bv. Fierce Pharma, Utility Dive, Offshore Energy, DigiTimes, Lloyd's List), persberichten van overheden en toezichthouders.

## Rechtszaken (R4)
Jaarverslag (geschillen/voorzieningen/contingent liabilities), 10-K "Legal Proceedings", CourtListener (VS), Europese Commissie (mededinging), nationale mededingingsautoriteiten, nieuws (zoek "<bedrijf> rechtszaak / lawsuit / class action / procès / investigation").

## Geen bron van feiten
Reddit, X/Twitter, StockTwits, beursforums (Beursduivel, IEX-forum, …), reacties onder artikels, AI-gegenereerde samenvattingssites zonder bronnen. Mag hooguit een aanwijzing zijn om verder te zoeken.
