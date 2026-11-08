# Werkdossier — Sofina (SOF.BR) — 2026-11-08

> Aantekeningen tijdens de analyse. Elke bevinding met bron (document + pagina of URL).
> Na elke fase: bijwerken + commit + push. Bij hervatten: hier verdergaan.

## Status
| Fase | Status | Opmerking |
|------|--------|-----------|
| 0 Identificatie & voorbereiding | ✅ | |
| 1 Koers & techniek | ✅ | koers.json opgehaald 08-11-2026 |
| 2 Verslagen | ✅ | JV2021–2025, HJ2026, presentaties FY25 + HY26 |
| 3 Bestuur & rode vlaggen | ✅ | R1 GERAAKT (54,6%); R5 FSMA; R6 claimemissie |
| 4 Keten (2 niveaus) | ✅ | |
| 5 Sector & concurrenten | ✅ | |
| 6 Actualiteit | ✅ | |
| 7 Earnings call | ✅ | |
| 8 Waardering & advies | ✅ | |
| 9 Kritische expertblik | ✅ | |
| 10 Fact-check | ✅ | |
| 11 Teamreview ronde 1 | ✅ | 1 niet goedgekeurd (FA), 2 met opmerkingen; alles verwerkt | |
| 11 Teamreview ronde 2 (+3) | ⬜ | |
| 12 Rapport bouwen | ⬜ | |
| 13 Afronding & feedback | ⬜ | |

## Identificatie
- Ticker / beurs / ISIN / valuta: SOF.BR / Euronext Brussel / BE0003717312 / EUR (JV2025 p.56)
- Type: aandeel (beursgenoteerde investeringsholding; "Investment Entity" onder IFRS 10)
- Sector / defensief: investeringsholding (private equity / durfkapitaal / groeikapitaal) — NIET defensief
- Vorig rapport: geen
- Indexen: BEL20, BEL ESG, STOXX Europe 600, MSCI Europe (JV2025 p.56)

## Gelezen documenten
| Document | Pagina's gelezen | Waar opgeslagen |
|----------|------------------|-----------------|
| Halfjaarverslag 2026 (02-09-2026) | 3,5,10–17,30–41 | data/SOF.BR/docs/hj2026.pdf |
| Presentatie HY2026 | 3–16 | data/SOF.BR/docs/pres_hj2026.pdf |
| Jaarverslag 2025 (26-03-2026) | 5–8,37,56–75 (gov+remuneratie),107,129–138 | data/SOF.BR/docs/jv2025.pdf |
| Presentatie FY2025 | 1–11 | data/SOF.BR/docs/pres_jv2025.pdf |
| Jaarverslagen 2021–2024 | kerncijfertabellen, aandeelhouders | data/SOF.BR/docs/jv202x.pdf |
| Transparantiemelding 28-09-2026 (BlackRock >3%) | 1–2 | data/SOF.BR/docs/transp_2026-09-28.pdf |
| Website aandeelhoudersstructuur (melding 19-08-2026) | — | sofinagroup.com/en/investors/shareholder-centre/shareholding-structure |

Blokkade: sofina.be geeft certificaatfout, maar **sofinagroup.com werkt direct** (curl/pdf.py). Bronnen.md bijwerken.

## Bevindingen per fase
### Koers (fase 1) — Yahoo, 06-11-2026
- Koers €267,6; 52w 207,8–285; SMA50 255,4; SMA200 236,6 → stijgende trend
- Rendement 1j +11,1%, 3j +38,7%, 5j −29,4%; max daling 5j −60,3% (top eind 2021 ~€432)
- Volatiliteit 21,3%/j; steun 238,8 (2-9-2026), 212,0 (11-6-2026), 203,6 (30-3-2026)
- Stop-loss −20% = 214,1; technisch 234,0 (onder steun 238,8)
- Slot per jaar: 2019 192,6; 2020 277; 2021 432; 2022 205,6; 2023 225,4; 2024 218,4; 2025 247,0 (Yahoo, mogelijk aangepast voor claimrecht)

### Verslagen
**Kerncijfers (look-through / "in transparantie", mln EUR, 31/12)**
| | 2021 | 2022 | 2023 | 2024 | 2025 | HJ2026 (30/6) |
|---|---|---|---|---|---|---|
| NAV (intrinsieke waarde) | 11.354 | 9.313 | 9.083 | 10.305 | 10.843 | 11.534 |
| NAV/aandeel (€) | 337,86 | 279,41 | 273,62 | 311,77 | 305,77 | 326,48 |
| Nettoresultaat | 2.593 | −1.872 | −104 | 1.360 | 113 | 857 (H1) |
| Investeringen | 1.284 | 1.013 | 517 | 951 | 1.139 | 733 (H1) |
| Desinvesteringen | 1.161 | 1.174 | 590 | 1.211 | 845 | 237 (H1) |
| Bruto kas | 1.049 | 929 | 893 | 1.031 | 1.723 | 1.080 |
| Financiële schulden | 730 | 696 | 696 | 697 | 1.293 | 1.299 |
| Netto kas (+)/schuld (−) | +319 | +233 | +197 | +334 | +430 | −219 |
| Jaarrendement NAV (incl. dividend) | 29,0% | −16,5% | −0,9% | 15,2% | −0,8% | — |
Bronnen: JV2022 p.? (kerncijfers 2021/22, jv2022.txt r.263–291), JV2023 kerncijfers, JV2024 p.? (r.824–846), JV2025 p.37, HJ2026 p.10; rendementen JV2025 p.74 (remuneratieverslag tabel "Average annual return"). Nettoresultaat 2021: JV2021 (FR) "Résultat net 2.593".
- 10-jaars gemiddeld jaarrendement NAV: 8,4% (JV2025 p.5 highlights). 4-jaars: −1,4%/j, 9,9% onder MSCI ACWI (JV2025 p.66).
- Waardecreatie 2025: +1,9%; zonder valuta +10,1% (pres FY25 p.10). HJ2026: +8,1%; zonder valuta +6,0% (pres HY26 p.10). Direct HJ26 +0,9% (ex-FX −0,2%); Private Funds +16,1% (ex-FX +13,0%) (pres HY26 p.11).
- Portefeuille 30/6/2026 €11.831m: Sofina Direct 5.862 (LT-minderheid 2.901, Growth 2.961), Private Funds 5.969 (HJ2026 p.10).
- 92% niet-beursgenoteerd, 8% beursgenoteerd (HJ2026 p.12). Level 3 (moeilijk te waarderen) = 11.569 van 11.831 (HJ2026 p.37).
- Regio: Noord-Amerika 42%, Europa 35%, Azië 23% (HJ2026 p.12). USD-activa €7.632m; EUR +10% → −€694m (HJ2026 p.40).
- Top 10 Direct = 27% van portefeuille: ByteDance, Cambridge Associates, Proeduca, Nuxe, Drylock, Cognita, Mérieux NutriSciences, Vinted, Salto (verkocht na 30/6), Cleo AI. ByteDance enige >5% (HJ2026 p.11). ByteDance gewaardeerd met multiples + illiquiditeitskorting (p.11 vn 3).
- Top 10 GP's = 24%: Sequoia, Lightspeed, HongShan, Thrive, a16z, Founders Fund, Peak XV, Battery, Iconiq, Insight (p.11).
- Top 10 onderliggend Private Funds ≈10%: SpaceX, ByteDance, Stripe, Anthropic, OpenAI, Databricks, Anduril, DoorDash, Ramp, Prometheus (HJ2026 p.11) — op basis van GP-rapporten 31/12/25 of 31/3/26.
- Afgeleide producten om sommige beursgenoteerde posities in Private Funds af te dekken (beperkt opwaarts) (HJ2026 p.37).
- Openstaande verplichtingen (uncalled commitments) €1.456m (HJ2026 p.40); nieuwe toezeggingen H1 €475m.
- Obligaties: €700m 1,000% (2021, vervalt 2028); €600m 3,707% (nov 2025, vervalt 2033) (JV2025 p.58; pres HY26 p.6). Niet-opgenomen kredietlijnen €1.375m (pres HY26 p.6).
- LTV 1,9% (30/6/2026) vs −4,1% (31/12/2025) (HJ2026 p.10).
- Dividenden ontvangen: 2025 €49m; H1 2026 €31m.
- Kosten ("other expenses"): 2025 €69,5m; 2024 €63,5m (JV2025 p.107) → ~0,64% van NAV (berekening). Bovenop: beheerkosten + carried interest in de fondsen (niet zichtbaar; exposures "net of carried interest").
- Dividend per aandeel (bruto, betaald in jaar): 2022 3,13; 2023 3,24; 2024 3,35; 2025 3,50 (JV2025 p.72); over 2025: 3,66 (+4,6%) betaald mei 2026 (pres FY25 p.3; JV2025 p.130).
- Kapitaalverhoging (claimemissie) 7-10-2025: 2.446.428 nieuwe aandelen à €223 = €545,6m (JV2025 p.57, p.130). Emissie onder koers én onder NAV → mechanische verwatering NAV/aandeel (JV2025 p.72). Transactiekosten €7,5m.
- Aandelen: 36.696.428 totaal; eigen aandelen 1.412.381 (3,85%) op 14-08-2026 (website). Uitstaand 35.328.731 op 30-6-2026.
- Inkoop eigen aandelen 2025: 189.068 gekocht, 236.640 afgestoten (opties + liquiditeitscontract Kepler Cheuvreux) (JV2025 p.57).

### Bestuur & rode vlaggen (R1–R6)
- **R1 GERAAKT**: Referentieaandeelhouder = consortium (art. 1:19 WVV) van Union Financière Boël SA 8.225.068 (22,41%), Société de Participations Industrielles SA 9.092.485 (24,78%), Mobilière et Immobilière du Centre SA 2.717.108 (7,40%) = 20.034.661 aandelen = **54,60%** van alle aandelen; met eigen aandelen (vermoeden van onderling overleg) 58,45% (website, melding 19-08-2026; JV2025 p.56). Overleg sinds 31-08-2007 (MIC sinds 1-7-2013). Eén stem per aandeel, geen dubbel stemrecht, eigen aandelen zonder stemrecht (JV2025 p.56). Stemrecht berekend: 20.034.661 / (36.696.428 − 1.412.381) = 56,8%.
- Historiek: 54,60% (2022, 2023), 54,93% (2024: UFB kocht 114.679 aandelen bij), 54,60% na claimemissie (consortium tekende in voor 1.220.965 nieuwe aandelen, net iets minder dan pro rata) (JV2022–JV2025).
- Vrij verhandelbaar 42,04% eind 2025 (JV2025 p.56).
- Geen "relationship agreement" met referentieaandeelhouder (raad vond niet nodig) (JV2025 p.58).
- Raad: 13 leden, 8 onafhankelijk; CEO Harold Boël (sinds 2004, mandaat tot 2028); Nicolas Boël stapt op AVA 13-5-2026; Union Financière Boël (vertegenwoordigd door Pascal Hubinont) voorgedragen als bestuurder; nieuwe voorzitter Charlotte Strömberg vanaf AVA 2026 (JV2025 p.59–60).
- **R2**: CEO-vergoeding 2025 €2,03m (2024 €1,98m); 70% variabel. Andere 5 LC-leden samen €8,1m. Ratio hoogste/laagste 1:20. Bestuurders: 3% van netto dividenden (vast sinds 2011); voorzitter +€150k. Remuneratiebeleid goedgekeurd 98,92% (AVA 2025) (JV2025 p.66–75). LTIP 2022–2025 cohort NIET gevest (onder MSCI ACWI). Bij LTIP-test werd NAV/aandeel gecorrigeerd voor de verwatering van de claimemissie (JV2025 p.72) → mening: begrijpelijk maar management-vriendelijk.
- Verbonden partijen: enkel leningen/deposito's met eigen dochters; "significant off-market transactions: nihil" (JV2025 p.137). → geen R2-vlag.
- **R3**: geen vertrekvergoedingen voorzien in beleid ("no severance or departure allowance") (JV2025 p.70). Geen terugvorderingsrecht (clawback) — afwijking van Code 2020 (p.70).
- R4: nog zoeken (nieuws/rechtszaken).
- R5: nog zoeken (FSMA MAR-meldingen).
- R6: claimemissie okt 2025 €545m à €223 (reden: investeringscapaciteit "to invest through cycles"); obligatie €600m nov 2025; inkoop eigen aandelen (dekking opties + liquiditeit); machtiging inkoop tot 20% (AVA 4-5-2023, 5 jaar); toegestaan kapitaal resterend €18,2m.

### Keten
- Niveau 1: ByteDance; Cambridge Associates; Proeduca; Nuxe; Drylock; Cognita; Mérieux NutriSciences; Vinted; + Private Funds (Sequoia/HongShan/…) → onderliggend SpaceX, Stripe, Anthropic, OpenAI
- Niveau 2: (todo)

### Sector & concurrenten
(todo) — kandidaten: GBL, Ackermans & van Haaren, Exor, Investor AB, HAL Trust, Gimv, Brederode, HgCapital Trust/ICG? (dichtste: GBL, Brederode, AvH, Exor, Investor)

### Blootstellingskaart (fase 6)
| Blootstelling | Waarom relevant | Gezocht (zoektermen, talen) | Gevonden |
|---|---|---|---|
| USD (+GBP, INR, CNY) | USD €7,6 mld = 65% portefeuille | "EUR/USD november 2026" (EN/NL) | ~1,13 (TradingEconomics 4-11); 2025 FX-impact −€925m |
| ByteDance/TikTok/China | grootste positie 5–10% | "ByteDance valuation 2026", "TikTok US deal" (EN), "Sofina ByteDance" (NL) | JV 22-1-2026; GA-verkoop $550 mld (Reuters 25-2-2026) |
| AI-waarderingen (Anthropic, OpenAI, SpaceX) | top-10 fondsposities ±10% | "Anthropic IPO", "OpenAI valuation", "SpaceX IPO" (EN) | S-1 Anthropic 26-10; OpenAI $852 mld + vertrouwelijke filing; SpaceX IPO 12-6; Nasdaq −6,4% op 5-11 |
| Rente/inflatie | waardering groeibedrijven; herfinanciering 2028 | "ECB October 2026", "eurozone inflation October 2026" (EN) | depo 2,5%; inflatie okt 4,0%; ECB 17-12 |
| Golfoorlog/olie | inflatie, multiples | "Gulf war oil 2026", "Iran war oil prices" (EN) | olie >$100 (sept); stromen herstellen eind okt, prijs hoog (Al Jazeera) |
| UK-btw privéscholen | Cognita | "Cognita verkoop mislukt" (NL), EN | mislukte verkoop 2025 (Bolero 20-8-2025) |
| India-exits | Lenskart, Pine Labs, Honasa | HJ2026; AS-review | gedeeltelijke verkopen 2026 (HJ2026) |
| BE-fiscaliteit | netto rendement | "meerwaardebelasting 2026" (NL) | 10%, vrijstelling €10.000 (KPMG) |
| Rechtszaken | R4 | NL/FR/EN | niets tegen Sofina; class actions tegen TikTok |
| Klimaat/pandemie | — | niet relevant voor holding | niet gevonden |

### Actualiteit

### Earnings call

### Waardering (aannames)
- Koers 267,6 / NAV 326,48 (30-6-2026) → korting −18,0% (berekening).

## Fact-check log
| Feit | Bron 1 | Bron 2 | Status |
|------|--------|--------|--------|
| Consortium 54,60% | JV2025 p.56 | website melding 19-08-2026 (54,596%) | ✅ |
| NAV/aandeel 326,48 | HJ2026 p.10 | pres HY26 p.8 | ✅ |

## Open vragen / blokkades
- Wie controleert SPI en MIC? (families Boël / Janssen / …?) → NBB / nieuws

## Aanvulling fase 3–9 (2026-11-08)
- R5 (FSMA): UFB kocht 5-10-2026 off-exchange 480.653 (van SPI, sofina-47/55) + 201.099 (van MIC, sofina-46/50) à €250,51 → interne herschikking, totaal consortium ongewijzigd. CEO: inschrijving claimemissie 15.923 à €223 (sofina-24); optie-uitoefening à €128,12 + verkoop (sofina-36, 38/39, 42, 57/58, 64/65). Bestuurders kochten: Strömberg 450 à 210,60 (sofina-19), Teo 100 à 209 (sofina-30), Peugeot 178 à 224,66 (sofina-37), Gatopardi 183 à 222,49 (sofina-22) + 118 à 251,69 (sofina-40).
- R4: geen rechtszaken tegen Sofina gevonden (3 zoekrondes: JV, EN-nieuws, FR/NL-nieuws). Wel class actions tegen TikTok/ByteDance (NL WAMCA, VS).
- Call H1 2026 (Investing.com transcript): zie rapport sectie earnings_call.
- Actualiteit: SpaceX IPO 12-6-2026 ($135, $1,77 bn), Anthropic $965 mld (mei), S-1 26-10-2026; OpenAI $852 mld; ECB 2,5%, inflatie 3,8% (Golfoorlog VS-Iran); EUR/USD ~1,13.
- Peers: korting berekend t.o.v. NAV 30-6-2026: GBL −22%, Brederode −35%, Exor −54%; AvH NAV niet gevonden.
- Waardering: NAV 326; korting 20% → faire koers 261; scenario's 180/290/350 (25/50/25%).
- Concept rapport.json + review.md aangemaakt.
