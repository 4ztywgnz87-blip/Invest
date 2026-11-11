# Bronnen: waar vind je wat?

## Toegang vanuit deze omgeving (getest 2026-11-08)
| Bron | Status | Hoe |
|------|--------|-----|
| Yahoo Finance (koersen, ticker zoeken) | ✅ | `tools/koers.py` |
| SEC EDGAR API (`data.sec.gov`, `efts.sec.gov`) | ✅ met beschrijvende User-Agent | `common.SEC_UA`; `www.sec.gov` website gaf 403 → gebruik de API-endpoints |
| De Tijd (tijd.be) | ✅ (betaalmuur op artikels) | WebSearch voor de kern, WebFetch voor vrije delen |
| Reuters, AP, FT, WSJ, De Tijd, L'Echo, MarketWatch, Barron's | ❌ **laten Claude niet toe** (getest 2026-11-11: niet doorzoekbaar en niet op te halen; dit is een keuze van die sites, niet omzeilen) | Zoek hetzelfde bericht bij een uitgever die het persagentschap **volledig overneemt met naamsvermelding** (bv. een regionale krant met "By Reuters", CNBC, Yahoo Finance) en vermeld de uitgever als "Reuters (overgenomen door …)". Voor Belgisch nieuws: persberichten van het bedrijf, Belga, VRT NWS, Trends/Knack, Business AM, La Libre, RTBF, MarketScreener (NL), Bolero/KBC, Test-Aankoop, VFB. Zet in de dekkingslijst ❌ met het gebruikte alternatief. De gebruiker heeft een abonnement op De Tijd: vraagt hij om een artikel mee te nemen, dan kan hij de tekst zelf plakken. |
| CNBC, Bloomberg (koppen), Yahoo Finance, nasdaq.com | ✅ WebSearch; pagina via web-fetch agent | CNBC is de bruikbaarste B-bron voor Amerikaans marktnieuws |
| Ook geblokkeerd (getest 2026-11-11) | ❌ | De Standaard, De Morgen, HLN, Nieuwsblad, Le Soir, NRC, Le Monde, Les Echos, FAZ, BBC, The Guardian, The Economist, NYT, Politico, DW, Business Insider |
| **Wel toegankelijk** (getest 2026-11-11, WebSearch met `allowed_domains`) | ✅ | België: VRT NWS, Trends/Knack, Trends-Tendances, Business AM, La Libre, RTBF, Belga (belganewsagency.eu), De Aandeelhouder, Bolero/KBC, VFB, Test-Aankoop. Nederland/Duitsland: FD, IEX, Handelsblatt. Internationaal: Bloomberg, CNBC, Washington Post, Fortune, Forbes, Axios, Semafor, Nikkei Asia, Euronews, SCMP, Al Jazeera, NPR, ABC/NBC/CBS News. Tech/durfkapitaal: TechCrunch, The Information, Sifted, Tech.eu. Bedrijfsnieuws en persberichten: MarketScreener (ook NL-talig, neemt persberichten en agentschapsnieuws over), Zonebourse, Boursorama, GlobeNewswire, Business Wire, Morningstar |
| Artikels die de gebruiker zelf aanlevert (De Tijd-abonnement) | ✅ | Geplakte tekst of PDF in de chat, of een mail die hij zichzelf doorstuurt (Gmail-koppeling, enkel lezen op zijn vraag). Bron vermelden als "De Tijd, <titel>, <datum> (aangeleverd door de gebruiker)" |
| Eurostat, ECB (persberichten, `eurofxref-hist-90d.xml` voor dagkoersen), news.belgium.be, gbl.com, brederode.eu, exor.com, ir.spacex.com | ✅ | WebSearch met `allowed_domains`, daarna web-fetch agent of `curl` |
| sofina.be | ❌ direct (certificaatprobleem op de site) | web-fetch agent, of het verslag bij een andere bron (FSMA, Euronext, NBB) |
| sofinagroup.com (nieuwe Sofina-site) | ✅ direct (getest 2026-11-08) | `tools/pdf.py download` met `https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/...`; PDF-links staan in de HTML van /en/investors/reports-and-publications |
| FSMA transacties leidinggevenden | ✅ direct | `https://www.fsma.be/en/manager-transaction/<bedrijf>-<nr>` (nummer ophogen) |
| Investing.com transcripts | ✅ via web-fetch agent | titel kan foutief jaar tonen: controleer de inhoud |
| EDINET (Japan) | ❌ direct (403) | SoftBank IR-site (group.softbank ✅), TDnet-persberichten, WebSearch |
| FSMA, NBB Balanscentrale, Euronext | ✅ | direct |

**Algemene volgorde als iets geblokkeerd is**: (1) directe download met `tools/pdf.py`/`curl`, (2) de `web-fetch` agent, (3) dezelfde info bij een andere (officiële) bron, (4) WebSearch-snippets enkel als laatste redmiddel en altijd met de originele bron-URL. Noteer blokkades in het werkdossier en vul deze tabel aan.

## Rangorde van bronnen (verplicht)
`python3 tools/bronrang.py <url>` geeft de rang; `tools/bronnen.py voegtoe` en `tools/rapport.py controleer` tonen ze ook.

| Rang | Wat | Gebruik |
|---|---|---|
| **A primair** | Het bedrijf zelf (verslagen, persberichten), toezichthouders, overheden, centrale banken, statistiekbureaus, beurzen, kredietbeoordelaars | Eerste keuze voor elk cijfer en elke officiële gebeurtenis |
| **B kwaliteit** | Persagentschappen en kwaliteitspers (De Tijd, L'Echo, Reuters, AP, FT, Bloomberg, WSJ, CNBC, …) en erkende vakpers | Nieuws, context, citaten |
| **C overig** | Andere media, brokers/banken (analyse), dataportalen, overgenomen artikels | Mag, maar zoek voor kerncijfers een A- of B-bron erbij |
| **D zwak** | Wikipedia, doorgeef- en samenvattingssites (Devdiscourse, RTTNews, investingLive, Trading Economics, MSN, …) | **Enkel als aanwijzing.** Zoek het origineel. Lukt dat na 3 pogingen niet: label het als `inschatting` of laat het weg, en noteer het in de dekkingslijst |

Vuistregels:
- **Ga altijd één stap terug naar de oorsprong.** Citeert een site Reuters of AP → zoek het artikel bij Reuters/AP zelf (of bij een B-uitgever die het overnam). Citeert een artikel een persbericht of verslag → gebruik dat persbericht of verslag.
- **Macrocijfers rechtstreeks bij de bron**: rente bij ECB/Fed, inflatie bij Eurostat/Statbel/BLS, wisselkoers bij de ECB-referentiekoers. Niet via een nieuwssite of Trading Economics.
- **Basis voor nieuws = De Tijd/L'Echo en Reuters, maar die sites laten Claude niet toe** (zie de toegangstabel). Zoek daarom voor elk belangrijk nieuwsfeit een Reuters- of AP-bericht dat een andere uitgever volledig overnam, of een B-bron zoals CNBC, en gebruik voor Belgisch nieuws de persberichten van het bedrijf en Belgische alternatieven. Noteer dit telkens in de dekkingslijst (❌ + alternatief).
- De controle waarschuwt bij elke D-bron en bij feiten die enkel op een D-bron steunen. Een definitief rapport heeft er geen, of de reden staat in het werkdossier.

## Dekkingslijst (verplicht)
`python3 tools/dekking.py lijst --type <type> --regio <BE|NL|FR|DE|UK|US|JP> [--snel]` geeft de lijst met bronnen die voor dit type en land **zeker** nagekeken moeten worden. Plak ze in het werkdossier en vul per rij in: ✅ nagekeken (wat gevonden) · ➖ niets gevonden / niet van toepassing (reden, zoektermen, talen) · ❌ geblokkeerd (welk alternatief gebruikt). `python3 tools/dekking.py controleer <werkdossier.md>` en `tools/rapport.py controleer` geven een fout zolang er een ⬜ staat of een notitie ontbreekt. Voeg zelf rijen toe voor bronnen die specifiek zijn voor dit bedrijf (sectorregulator, belangrijke deelneming, …).

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

## Vaak vergeten (staan in de dekkingslijst)
- **Verslag van de commissaris** (in het jaarverslag): voorbehoud of toelichtende paragraaf, kernpunten van de controle, wissel van revisor. Een voorbehoud of onverwachte wissel is een rode vlag.
- **Kredietbeoordeling**: persberichten van S&P, Moody's, Fitch (rating, vooruitzicht, reden van wijziging).
- **Gestructureerde jaarcijfers**: Europese bedrijven leggen hun jaarverslag neer in ESEF/XBRL-formaat (via de toezichthouder of filings.xbrl.org); VS via de SEC companyfacts-API. Handig om 5-jaarcijfers te controleren.
- **Verslagen van de concurrenten zelf** voor de vergelijkingstabel (niet de cijfers van een dataportaal overnemen).
- **Short-seller-onderzoek** (Hindenburg, Muddy Waters, Viceroy, Gotham, …): nooit een bron, wel een aanwijzing voor R2/R4. Zoek "<bedrijf> short seller report"; staat er iets, controleer de beweringen in primaire bronnen en vermeld het antwoord van het bedrijf. (Short-posities zelf blijven uitgesloten.)
- **Sancties en regelgeving**: EU-sanctiekaart (sanctionsmap.eu), OFAC (VS), en de sectorregulator (CREG, EMA/FDA, ECB-bankentoezicht, …).
- **Beleggersverenigingen**: VFB (België), VEB (Nederland) voor geschillen met aandeelhouders en vragen op de algemene vergadering.

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
