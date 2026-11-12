# Werkdossier — Sofina (SOF.BR) — 2026-11-11

> Aantekeningen tijdens de analyse. Elke bevinding met bron (document + pagina of URL).
> Na elke fase: bijwerken + commit + push. Bij hervatten: hier verdergaan.

## Status
| Fase | Status | Opmerking |
|------|--------|-----------|
| 0 Identificatie & voorbereiding | ✅ | koers, dekkingslijst, app-feedback (geen) |
| 1 Koers & techniek | ✅ | koers.py 11-11 |
| 2 Verslagen | ✅ | HJ26, JV25, JV21–24, presentaties |
| 3 Bestuur & rode vlaggen | ✅ | R1 geraakt; R2 middel |
| 4 Keten (2 niveaus) | ✅ |  |
| 5 Sector & concurrenten | ✅ | GBL, Brederode, Exor, Investor AB |
| 6 Actualiteit | ✅ |  |
| 7 Earnings call | ✅ | HJ26-transcript |
| 8 Waardering & advies | ✅ | Afwachten 5/10 |
| 9 Kritische expertblik | ✅ |  |
| 10 Fact-check | ✅ | feitenlog A–E, controle ok |
| 11 Teamreview ronde 1 | ✅ | FA niet goedgekeurd, AS ok met opm., KB niet goedgekeurd; 44 opmerkingen verwerkt/verworpen (review.md) |

| 11 Teamreview ronde 2 (+3) | ✅ | alle drie goedgekeurd met opmerkingen; 20 opmerkingen; geen ronde 3 |
| 12 Rapport bouwen | ⬜ | |
| 13 Afronding & feedback | ⬜ | |

(⬜ te doen · 🔄 bezig · ✅ klaar)

## Identificatie
- Ticker / beurs / ISIN / valuta: SOF.BR / Euronext Brussel (primaire notering; ook OTC SFNXF, Frankfurt 8FS) / BE0003717312 / EUR
- Type / soort: aandeel · **volledig rapport van nul** op vraag van de gebruiker (11-11-2026): vorige rapporten (8-11 en eerste versie 11-11) niet als basis gebruikt; geen snelle update. Bronnen opnieuw zelf gelezen (gedownloade PDF's hergebruikt als originelen).
- Sector / defensief: investeringsholding (durfkapitaal/groeikapitaal, niet-genoteerd) / niet defensief
- Vorig rapport: bewust genegeerd (start van 0). De eerste versie van 11-11 is vervangen (staat in git-geschiedenis).
- App: geen open feedback of vragen (query 11-11); opvolging SOF-BR-2026-11-11: geen signalen aangevinkt.

## Dekkingslijst
| Bron | Waarvoor | Status | Wat gevonden / waarom niet (zoektermen, talen, datum) |
|---|---|---|---|
| Laatste jaarverslag + kerncijfers 4 jaar ervoor | cijfers, trend | ✅ | JV2025 volledig doorgenomen (kerncijfers, governance, remuneratie, risico's, audit); kerncijfers JV2021–2024 (JV22 p.9, JV23 p.27, JV24 p.19). |
| Laatste halfjaar-/kwartaalverslag + persbericht | recentste cijfers | ✅ | Halfjaarverslag 2026 p.3–53 + persbericht NL 2-9-2026. Sofina publiceert geen kwartaalcijfers. |
| Investeerderspresentatie | strategie, vooruitzichten | ✅ | Presentatie HJ2026 (2-9-2026) en JV2025 (26-3-2026). |
| Earnings call (transcript of verslag) | toon management | ✅ | Transcript HJ2026-call (Investing.com, 3-9-2026, rang C) via web-fetch; transcript JV2025-call niet gevonden (investing.com lijst, sofinagroup.com) → enkel presentatie. |
| Verslag van de commissaris (oordeel, kernpunten, wissel revisor) | betrouwbaarheid cijfers | ✅ | EY, zonder voorbehoud, 6 jaar, kernpunt waardering niet-genoteerd (JV25 p.143–147); beperkt nazicht HJ26 zonder opmerkingen (p.53). Geen wissel. |
| Remuneratieverslag | R2, R3 | ✅ | JV25 p.66–75. |
| Aandeelhouders: FSMA (transparantieverklaringen) | R1 | ✅ | JV25 p.56–57 (consortium 54,60%); art.15-persbericht 7-10-2025; transparantiemelding 28-9-2026 (vermogensbeheerder 3,01%, niet in rapport: profiel §6). |
| Insiders: FSMA (transacties leidinggevenden) | R5 | ✅ | fsma.be/en/manager-transaction/sofina-1 t.e.m. 130 doorlopen (11-11-2026). |
| Corporate actions: Euronext + Belgisch Staatsblad + persberichten bedrijf | R6 | ✅ | Claimemissie 2025, obligatie 2025, inkoopprogramma's (okt. 2025, 3-4-2026), verkoop Salto/Kopi Kenangan. Euronext/Staatsblad: niet apart nodig, kapitaalverhoging bevestigd via art.15-persbericht en JV25 p.57. Persbericht 3-4-2026 zelf: 404 op sofinagroup.com → MarketScreener-overname. |
| Rechtszaken: jaarverslag + zoekronde nieuws (NL/EN/FR/lokaal) + mededingingsautoriteit/EC | R4 | ✅ | JV25/HJ26: geen geschillen. Ronde 1 EN/NL/FR 'Sofina lawsuit/rechtszaak/procès/investigation', ronde 2 'actionnaires plainte/litige/tribunal/FSMA sanction', ronde 3 shortseller + Zilingo (2022–2023 vereffening deelneming). Niets tegen Sofina zelf. EC/BMA: niets gevonden (holding zonder marktpositie). |
| Kredietbeoordeling (S&P, Moody's, Fitch: persbericht) | schuld | ✅ | S&P A− stabiel (24-9-2025, bevestigd 5-6-2026) via JV25 p.36 en HJ26 p.46; persbericht S&P zelf niet opgehaald (S&P-site vraagt login) → bedrijfsverslag. |
| Persberichten van het bedrijf (laatste 12 maanden; snelle update: sinds vorig rapport) | actualiteit | ✅ | PB HJ26, PB voorzitter 26-3-2026, art.15, transparantie 28-9-2026; lijst op sofinagroup.com via JS (niet leesbaar) → zoekrondes + MarketScreener. |
| Basisnieuws: De Tijd / L'Echo | actualiteit | ❌ | tijd.be en lecho.be weigeren Claude (getest 11-11-2026). Alternatief: La Libre, MandA.be, Bolero/Test-Aankoop (enkel voor feiten), persberichten Sofina. |
| Basisnieuws: Reuters (originele URL) | actualiteit | ❌ | reuters.com geblokkeerd. Reuters-bericht ByteDance $550 mld via SCMP (overname met vermelding). |
| Internationale kwaliteitspers (FT, Bloomberg, WSJ, AP) | actualiteit | ✅ | Bloomberg (Zilingo, koppen TikTok), CNBC (Anthropic, SpaceX, Nasdaq, olie, TikTok JV), Fortune, Axios. FT/WSJ/AP geblokkeerd. |
| Vakpers van de sector | sector, keten | ✅ | TechCrunch, MandA.be (Cognita), Vinted-persberichten; GBL/Brederode/Exor-verslagen. |
| Macro rechtstreeks bij de bron (ECB, Fed, Eurostat, Statbel) | rente, inflatie, valuta | ✅ | ECB 29-10-2026 + referentiekoersen, Fed 28-10-2026, Eurostat flash okt. 2026 (incl. België 5,2%). |
| Verslagen van de 3–5 dichtste concurrenten | vergelijking | ✅ | GBL Q3 2026, Brederode HJ2026, Exor HJ2026 (eigen PDF's), Investor AB Q3 2026 (rapportpagina). |
| Keten: verslagen/IR-site van de niveau-1-partijen | keten | ✅ | Vinted (persberichten), SpaceX/Anthropic (CNBC), ByteDance (geen IR: Reuters/CNBC), Cognita (MandA, call). Drylock: geen 2026-cijfers gevonden (NBB niet geraadpleegd) → enkel HJ26-vermelding. Nuxe, Proeduca, Cambridge Associates: geen publieke cijfers gezocht buiten HJ26. |
| Short-seller-onderzoek (enkel aanwijzing, nooit bron) | R2, R4 | ✅ | Enkel shortpositie Fraser Perring 2022 (Bolero/KBC-notitie); geen nieuw rapport 2025–2026. Niet in rapport (profiel §6). |
| Sancties en sectorregelgeving (EU-sanctielijst, sectorregulator) | risico | ✅ | HJ26 p.41: niet geraakt door EU-sancties, <3% blootstelling Oekraïne/Rusland/Wit-Rusland. Geen sectorregulator (geen bank/verzekeraar). |
| Fiscaliteit België (FOD Financiën) | netto rendement | ❌ | fin.belgium.be toont CAPTCHA (web-fetch 11-11-2026). Alternatief: roerende voorheffing uit JV25 p.149; meerwaardebelasting via Bolero-FAQ (C). |
| Koersdata (tools/koers.py) | techniek, waardering | ✅ | koers.py analyse SOF.BR 11-11-2026 (laatste slot 10-11); peers via Yahoo. |


## Gelezen documenten
| Document | Pagina's gelezen | Waar opgeslagen |
|----------|------------------|-----------------|

## Bevindingen per fase
### Verslagen

### Bestuur & rode vlaggen (R1–R6)

### Keten
- Niveau 1:
- Niveau 2:

### Sector & concurrenten

### Blootstellingskaart (fase 6)
| Blootstelling | Waarom relevant | Gezocht (zoektermen, talen) | Gevonden |
|---------------|-----------------|-----------------------------|----------|
| AI-/techwaarderingen (fondsen, ByteDance) | ±15–20% van portefeuille | Nasdaq sell-off, Anthropic IPO, SpaceX Q3, ByteDance valuation (EN) | Nasdaq −5,5% 5-11; Anthropic vork $70–78, S-1 H1 omzet $16,3 mld, verlies $80,7 mld (grotendeels niet-cash); SpaceX Q3 winst |
| VS-politiek: AI/datacenters/chips | AI-belangen, Anthropic, ByteDance/China | midterms 2026 AI data center regulation chips China (EN) | Democraten winnen Huis + Senaat (CNBC 4-11); oproep moratorium datacenters (CNBC 5-11); chipexport: geen concreet beleid bevestigd |
| Dollar (65% portefeuille) | ±10% = −694/+848 mln | ECB-referentiekoersen | EUR/USD 1,1394 (30-6) → 1,1127 (11-11) |
| Rente en inflatie EU/VS | waarderingen, exits, rentekost | ECB/Fed/Eurostat persberichten | ECB +25 bp juni en sept. (2,50%), houdt 29-10; Fed 3,75–4,00%; inflatie eurozone 4,0% okt. |
| Olie/Golfoorlog VS–Iran | inflatie, consumptiebedrijven, Cognita Midden-Oosten | oil Brent Iran Hormuz (EN) | Brent ≈$117 eind okt. → $91,49 op 10-11 (vredeshoop); onzeker |
| China (ByteDance, Hypershell, Ji Xiang Ju, Petkit) | Azië 23% | ByteDance valuation, TikTok JV (EN) | $550 mld feb. 2026; TikTok VS-JV jan. 2026. Trump–Xi/chipexport: niet bevestigd via A/B |
| UK onderwijs (Cognita) | top 10 Direct | Cognita 2026 (EN) | verkoopproces Jacobs vastgelopen 2025; btw op schoolgelden UK (secundair, niet in rapport als feit) |
| India/Indonesië (INR €347 mln) | Lenskart, Pine Labs, FirstClub, Kopi Kenangan | — | niet apart onderzocht; klein |
| Exits/verkopen | cash | Salto Inflexion, Kopi Kenangan (EN/ES) | Salto: Inflexion + Baskische families 33%, onder voorwaarden (Inflexion juli 2026); Kopi: enkel HJ26 |
| Belgische fiscaliteit | netto rendement | meerwaardebelasting, TOB (NL) | FOD CAPTCHA; Bolero/KPMG (C) |

### Actualiteit

### Earnings call

### Waardering (aannames)

## Feitenlog (vul aan tijdens het lezen; basis voor de fact-check)
| Feit (zoals in het rapport) | Letterlijk citaat / tabelregel | Bron + pagina of URL + datum | Rang | 2e bron | Status |
|------|------|------|------|------|------|

## Open vragen / blokkades

### Feitenlog A — Halfjaarverslag 2026 (HJ26, sofinagroup.com, 2-9-2026, rang A; zelf gelezen 11-11)
| Feit | Citaat / tabelregel | Bron | Status |
|---|---|---|---|
| NAV €11,534 mld, €326,48/aandeel (30-6-26) vs €10,843 mld / €305,77 (31-12-25) | "Net Asset Value (in million €) 11,534 10,843 ; Net Asset Value per share (in €) 326.48 305.77" | HJ26 p.10 | ✅ |
| Aandelen uitstaand 35.328.731 (30-6) / 35.461.125 (31-12) | voetnoot 3 p.10 | HJ26 p.10 | ✅ |
| Nettowinst H1 €857 mln (€24,20/aandeel) vs −€394 mln H1-25 | "Net result (share of the group) 857 -394" | HJ26 p.10, p.20 | ✅ |
| Netto schuld €219 mln, LTV 1,9% (eind 2025: netto kas €430 mln, −4,1%) | "Net debt (+) / Net cash (-) 219 -430; Loan-to-value 1.9% -4.1%" | HJ26 p.10 | ✅ |
| Portefeuille €11,831 mld: Direct 5,862 (LTMI 2,901; Growth 2,961), Private Funds 5,969 | tabel p.10 | HJ26 p.10 | ✅ |
| Bruto kas €1,080 mld, schulden €1,299 mld, overige −78 | tabel p.10 | HJ26 p.10 | ✅ |
| Investeringen H1 €733 mln, desinvesteringen €237 mln (H1-25: 650/384) | "Investments in portfolio -733 -650; Divestments 237 384" | HJ26 p.10 | ✅ |
| Dividenden ontvangen €31 mln (H1-25 €18 mln) look-through | tabel p.10 | HJ26 p.10 | ✅ |
| Top 10 Direct = 27% portefeuille: ByteDance, Cambridge Associates, Proeduca, Nuxe, Drylock, Cognita, Mérieux NutriSciences, Vinted, Salto, Cleo AI | lijst p.11 | HJ26 p.11, p.40 | ✅ |
| ByteDance enige positie >5% van portefeuille (incl. via fondsen) | "ByteDance ... is the sole holding representing more than 5%" | HJ26 p.11, p.41 | ✅ |
| Top 5 Direct 15–20%, top 7 >20% | p.11/p.41 | HJ26 | ✅ |
| Top 10 onderliggende in fondsen ≈10% portefeuille: SpaceX, ByteDance, Stripe, Anthropic, OpenAI, Databricks, Anduril, DoorDash, Ramp, Prometheus; GP-rapporten meestal per 31-12-25 of 31-3-26 | p.11 | HJ26 p.11 | ✅ |
| Top 10 GP's = 24%: Sequoia, Lightspeed, HongShan, Thrive, a16z, Founders Fund, Peak XV, Battery, Iconiq, Insight | p.11 | HJ26 p.11 | ✅ |
| 92% niet-genoteerd, 8% genoteerd; regio NA 42% / Europa 35% / Azië 23% | p.12, p.42 (4.929/4.134/2.768) | HJ26 | ✅ |
| Direct per sector: digitale transformatie 36%, consumptie 27%, onderwijs 12%, zorg 12%, duurzame toeleveringsketens 4%, overig 9% | p.42 | HJ26 p.42 | ✅ |
| Private Funds: durfkapitaal 75%, groeikapitaal 22%, LBO 3%; NA 70% | p.42 | HJ26 p.42 | ✅ |
| Waardecreatie H1: Direct 1% (61 mln), Private Funds 16% (690 mln), totaal 8%; FX-effect +226 mln | brugtabel p.25 | HJ26 p.25 | ✅ |
| Beheerskosten H1 €43,3 mln (kasstroom), €27,4 mln 'other expenses' in resultaat | p.25, p.20 | HJ26 | ✅ |
| Waardering niveau 3: €11,569 mld van €11,831 mld; €5,978 mld op basis van GP-rapporten (±10% = ±597 mln) | p.37–38 | HJ26 p.38 | ✅ |
| Genoteerde activa via fondsen €688 mln (eind 2025 €447 mln); Sofina gebruikt soms derivaten om genoteerde posities in te dekken | p.37 | HJ26 p.37 | ✅ |
| USD-blootstelling €7,632 mld; −10% EUR/USD = +848 mln, +10% = −694 mln; GBP 727, INR 347 | p.40 | HJ26 p.40 | ✅ |
| Niet-opgevraagde verbintenissen fondsen €1,449 mld (+7 Direct = 1,456) | p.40 | HJ26 p.40 | ✅ |
| Obligaties: €700 mln 1,000% 23-9-2028; €600 mln 3,707% 13-11-2033 (rating A−); reële waarde €1,257 mld | p.46 | HJ26 p.46 | ✅ |
| S&P A− (stabiel) 24-9-2025, bevestigd 5-6-2026 | p.46 | HJ26 p.46 | ✅ |
| Kredietlijnen €1,375 mld, €5 mln gebruikt | p.48 | HJ26 p.48 | ✅ |
| Eigen aandelen 1.367.697 op 30-6 (31-12: 1.235.303); H1: 243.753 gekocht, 111.359 verkocht; totaal 36.696.428 aandelen | p.45 | HJ26 p.45 | ✅ |
| Dividend 2025 (betaald 2026) €3,66 bruto/aandeel = €129,5 mln | p.45 | HJ26 p.45 | ✅ |
| Kapitaalverhoging 2025: aandelen 34.250.000 → 36.696.428 (+2.446.428); uitgiftepremie 4,4 → 536,8 mln | p.45, p.21 | HJ26 | ✅ |
| Rentekosten H1 €15,4 mln (H1-25 €4,1 mln) | p.20 | HJ26 p.20 | ✅ |
| Latente belasting: 0–61% van NAV dochters Private Funds kan theoretisch belastbaar worden aan 25% bij verkoop/liquidatie, niet geboekt | voetnoot 2 p.24 | HJ26 p.24 | ✅ |
| Fout in gewogen aandelental H1-25 rechtgezet (WPA 11,8728 → 11,9123), geen impact balans | voetnoot p.20 | HJ26 p.20 | ✅ |
| Na 30-6: investering Exein; meer in Scalable Capital, Twin Health; verkoop Salto en Kopi Kenangan getekend | p.17, p.48 | HJ26 | ✅ |
| H1-transacties: nieuw Cerealis (10%), XBOW, Eye Security, FirstClub, Hypershell, Primer, Creature Comforts, Ji Xiang Ju, Supabase; exit SES, Honasa; deels Lenskart; dividend-recap opseo en Nuxe | p.15 | HJ26 p.15 | ✅ |
| Niet-gerealiseerde verliezen vooral persoonlijke hygiëne (Drylock), software, digitale retail; winsten onderwijs, preventieve gezondheid, dochters | p.47 | HJ26 p.47 | ✅ |
| Commissaris EY (Boschmans, Dupuis): beperkt nazicht, geen opmerkingen | p.53 | HJ26 p.53 | ✅ |
| Voorzitter Charlotte Strömberg (sinds AV 2026, eerder vicevoorzitter, bestuur sinds 2017) | p.4 | HJ26 p.4 | ✅ |
| ByteDance gewaardeerd via HSG Co-Investment 2016-A met multiples + illiquiditeitskorting | p.11 vn 3 | HJ26 | ✅ |
| Belang ByteDance via vehikel: 41,67% van vehikel, 0,17% van ByteDance | p.32 | HJ26 p.32 | ✅ |
| Genoteerde Direct (niveau 1): bioMérieux 1,00% €81 mln; Luxempart 6,07% €94 mln; Pine Labs 1,46% €24 mln; THG 7,13% €45 mln | p.30 | HJ26 p.30 | ✅ |

### Feitenlog B — Jaarverslag 2025 (JV25, 26-3-2026, rang A) + jaarverslagen 2021–2024 (rang A)
| Feit | Citaat / tabelregel | Bron | Status |
|---|---|---|---|
| NAV/aandeel: 2021 337,86 · 2022 279,41 · 2023 273,62 · 2024 311,77 · 2025 305,77 | kerncijfertabellen | JV22 p.9 (7 in druk), JV23 p.27, JV24 p.19, JV25 p.37 | ✅ |
| NAV totaal (mld): 2021 11,354 · 2022 9,313 · 2023 9,083 · 2024 10,305 · 2025 10,843 | idem | idem | ✅ |
| Nettoresultaat (mln): 2021 2.593 · 2022 −1.872 · 2023 −104 · 2024 1.360 · 2025 113 | idem | idem | ✅ |
| Investeringen/desinvesteringen (mln): 2021 1.284/1.161 · 2022 1.013/1.174 · 2023 517/590 · 2024 951/1.211 · 2025 1.139/845 | idem | idem | ✅ |
| Ontvangen dividenden (mln): 2021 59 · 2022 53 · 2023 44 · 2024 60 · 2025 49 | idem | idem | ✅ |
| Bruto kas (mln): 2021 1.049 · 2022 929 · 2023 893 · 2024 1.031 · 2025 1.723; schulden 730/696/696/697/1.293 | idem | idem | ✅ |
| Direct / Private Funds (mld): 2021 5,811/5,252 · 2022 4,760/4,302 · 2023 4,739/4,189 · 2024 5,331/4,723 · 2025 5,616/4,893 | idem | idem | ✅ |
| Bruto dividend per boekjaar: 2021 3,128571 · 2022 3,24 · 2023 3,35 · 2024 3,50 · 2025 3,66 (+4,6%) | "gross dividend of EUR 3.66 per share, representing a net dividend of EUR 2.562" | JV22 p.9, JV23 p.27/131, JV24 p.135, JV25 p.149; pres JV25 p.3 | ✅ |
| Gemiddeld jaarrendement NAV (incl. dividend): 2021 29,0% · 2022 −16,5% · 2023 −0,9% · 2024 15,2% · 2025 −0,8% | tabel "Average annual return" | JV25 p.74 | ✅ |
| 4 jaar gemiddeld −1,4%/jaar, 9,9 procentpunt onder MSCI ACWI (EUR) | "Over the past four years, Sofina's Average annual return amounted to -1.4%, which underperformed the MSCI ACWI ... by 9.9%" | JV25 p.66 | ✅ |
| Koers 2025 +13,1%, NAV +5,2% (mede door kapitaalverhoging) | p.66 | JV25 p.66 | ✅ |
| Claimemissie €545 mln afgerond 7-10-2025: 2.446.428 nieuwe aandelen à €223 | p.57 | JV25 p.57 | ✅ |
| Obligatie €600 mln 3,707% 13-11-2025 (8 j); 7–8 jaar looptijd | p.35, p.58 | JV25 | ✅ |
| Doel-LTV 5–10%; minimale bruto kas €300 mln | "target Loan-to-value ratio between 5% and 10%"; "minimum gross cash position of EUR 300 m at all times" | JV25 p.35, p.15 | ✅ |
| S&P A− stabiel (sept. 2025): conservatief financieel beleid, lage schuld, sterke liquiditeit vs risico illiquide portefeuille | p.36 | JV25 p.36 | ✅ |
| Beurswaarde €8,8 mld eind 2025; vrij verhandelbaar 42,04% (€3,8 mld); gemiddeld 26.143 aandelen/dag | p.56 | JV25 p.56 | ✅ |
| Referentieaandeelhouder (consortium sinds 31-8-2007, MIC sinds 1-7-2013): UFB 8.225.068 (22,41%), SPI 9.092.485 (24,78%), MIC 2.717.108 (7,40%) = 20.034.661 = 54,60% van ALLE 36.696.428 aandelen (voetnoot JV zegt 'zonder eigen aandelen', maar rekenkundig is het totaal; stemrecht zonder eigen aandelen ±56,4% (okt. 2025) / 56,71% (eigen aandelen 30-6-2026)) — gecorrigeerd na review FA-1/KB-1; eigen aandelen 1.149.306 (3,13%) op 3-10-2025 | tabel p.56 | JV25 p.56, p.137 | ✅ |
| Eén stem per aandeel; geen aparte klassen of bijzondere controlerechten; geen relatieovereenkomst met referentieaandeelhouder (raad vond niet nodig); geen bekende afspraken over overdracht/stemrecht | p.56, p.58 | JV25 | ✅ |
| 2025 geen transparantiemeldingen; geen andere partij ≥3% | p.57 | JV25 p.57 | ✅ |
| Inkoop eigen aandelen 2025: 189.068 gekocht (2024: 422.655), 236.640 verkocht; doel: opties dekken + liquiditeitscontract Kepler Cheuvreux; machtiging tot 20% (AV 4-5-2023, 5 j) | p.57 | JV25 p.57 | ✅ |
| Change-of-control-clausules in beide obligaties, PSU's en kredietovereenkomsten | p.58 | JV25 p.58 | ✅ |
| Raad 13 leden, 8 onafhankelijk; CEO Harold Boël (bestuurder sinds 2004, mandaat tot AV 2028); Nicolas Boël vertrok AV 13-5-2026; Lancksweert (voorzitter) vertrok AV 2026 (leeftijdsgrens); Strömberg voorzitter, Soubie vicevoorzitter; UFB (Pascal Hubinont) en Charles Peugeot voorgesteld | p.59–60 | JV25 | ✅ |
| Vergoeding niet-uitvoerende bestuurders = 3% van netto dividenden (sinds 2011); totaal €2,54 mln 2025 (€2,26 mln 2024), +11,5% door kapitaalverhoging; voorzitter + €150.000 vast | p.66–67, p.74 | JV25 | ✅ |
| CEO totaal 2025 €2.026.540 (2024 €1.983.982): vast €494.370, STI €245.234, LTIP €565.593, opties €605.682, pensioen €111.661; 70,1% variabel | tabel p.71 | JV25 p.71 | ✅ |
| Overige Leadership Council (5) samen €8.113.785 (2024 €7.599.777) | p.71 | JV25 p.71 | ✅ |
| Ratio hoogste/laagste loon 1:20 | p.75 | JV25 p.75 | ✅ |
| LTIP 2022-2025: relatief criterium (vs MSCI ACWI) niet gehaald → 0 PSU's; transitie-PSU's: 31,2% van maximum gevest (ANAVPS +8,12%, SBTi 22,49%) | p.72 | JV25 p.72 | ✅ |
| Voor LTIP werd NAV/aandeel aangepast om verwatering kapitaalverhoging (uitgifte onder koers en NAV) en tijdelijke kas te neutraliseren; uitoefenprijs opties aangepast (Euronext-methode) | p.72, p.74 | JV25 | ✅ |
| Geen vertrekvergoeding voor CEO/Leadership Council; geen contractueel terugvorderingsrecht (clawback) variabel loon, afwijking van Principe 7.12 Code 2020 | p.70 | JV25 p.70 | ✅ |
| Remuneratiebeleid AV 8-5-2025 98,92% goedgekeurd; remuneratieverslag 2024 98,45% | p.75 | JV25 p.75 | ✅ |
| Opties 24-11-2025: CEO 22.000 aan €239,40 (uitoefenbaar vanaf 1-1-2029); CEO hield 182.000 opties eind 2025 | p.73–74 | JV25 | ✅ |
| Commissaris EY: oordeel zonder voorbehoud; 6 opeenvolgende jaren; kernpunt = waardering niet-genoteerde beleggingen (IPEV, onafhankelijke waarderingsspecialist) | p.143–144, p.147 | JV25 | ✅ |
| Geen geschillen/rechtszaken vermeld in jaarverslag (zoektermen litigation, dispute: 0 treffers) | zoekopdracht | JV25 | ✅ |
| 83 medewerkers, 4 kantoren, 33 beleggingsprofessionals | p.15 | JV25 p.15 | ✅ |

### Feitenlog C — FSMA (rang A, opgehaald 11-11-2026, fsma.be/en/manager-transaction/sofina-<nr>)
| Feit | Tabelregel | Nr | Status |
|---|---|---|---|
| CEO Harold Boël schreef in op claimemissie: 15.923 aandelen à €223 = €3.550.829 (24-9-2025, "Primary market: subscription to a capital increase") | nr 24 | 24 | ✅ |
| CEO opties uitgeoefend à €128,12 en aandelen verkocht: 2.000 verkocht à €246,60 (22-1-2026); 2.000 uitgeoefend (30-3-2026); 6.500 uitgeoefend 25-7 + verkocht 27-7-2026 à €238,77; 10.000 uitgeoefend 4-9-2026 (geen bijhorende verkoop gevonden in nrs 1–130); 5.000 uitgeoefend + verkocht à €243,20 (8-10-2026); 4.500 uitgeoefend + verkocht à €261,36 (21-10-2026). Alles "linked to remuneration package" | nrs 36, 3, 38, 39, 42, 57, 58, 64, 65 | ✅ |
| Edward Koopman (Leadership Council): 1.250 uitgeoefend à €126,76 en verkocht à €255,96 (15-10-2026) en €271,26 (27-10-2026) | nrs 59, 60, 67, 69 | ✅ |
| Bestuurders kochten op de beurs: Strömberg 450 à €210,60 (31-3-2026); Teo 100 à €209,00 (31-3-2026); Peugeot 178 à €224,66 (15-6-2026); Gatopardi (verbonden met Peugeot) 183 à €222,49 (15-6) en 118 à €251,69 (4-9-2026) | nrs 19, 30, 37, 22, 40 | ✅ |
| Lancksweert, Tombeur, Van Waeyenberge, Lagache, Koopman schreven in op claimemissie à €223 (sept. 2025) | nrs 33, 16, 27, 12, 23 | ✅ |
| 5-10-2026: UFB kocht buiten de beurs 480.653 aandelen van SPI en 201.099 van MIC à €250,51 (samen ≈ €170,8 mln); interne verschuiving binnen het consortium, totaal consortium ongewijzigd | nrs 46, 47, 50, 55 | ✅ |
| Transparantie 28-9-2026 (sofinagroup.com): een vermogensbeheerder overschreed 3% (2,24% aandelen + 0,77% instrumenten); noemer 36.696.428 → **niet in rapport** (profiel §6: geen posities van grote fondsen); wel bevestiging dat noemer ongewijzigd 36.696.428 | transp_2026-09-28 p.1 | — | ✅ |

### Feitenlog D — rendement, korting, actualiteit, keten, concurrenten
| Feit | Citaat / tabelregel | Bron (rang) | Status |
|---|---|---|---|
| Gemiddeld jaarrendement NAV (div. herbelegd) t/m 2025: 1j −0,8% · 3j 4,2% · 4j −1,4% · 5j 4,1% · 7j 7,9% · 10j 8,4%; MSCI ACWI (EUR) 7,9/16,8/8,5/12,1/13,5/10,8; Euro Stoxx 50 21,2/18,0/10,4/12,9/12,5/8,5 | grafiek "Average annual return" (visueel nagekeken) | JV25 p.38 (A) | ✅ |
| Korting/premie op jaareinde (koers vs NAV): 2021 +28% · 2022 −26% · 2023 −18% · 2024 −30% · 2025 −19% · 30-6-2026 −32% | grafiek "Sofina Price & NAV per share" | pres HJ26 p.6 (A) + eigen berekening slotkoersen Yahoo | ✅ |
| Slotkoers per jaar: 2021 432,0 · 2022 205,6 · 2023 225,4 · 2024 218,4 · 2025 247,0; 10-11-2026 270,40; 30-6-2026 222,6 | koers.json; HJ26 p.10 (222,6) | Yahoo (C) + HJ26 (A) | ✅ |
| PB HJ26: NAV +6,8% in 6 mnd; "2026 ons meest actieve jaar ooit voor Sofina Private Funds"; "macro-economische omgeving voor meer mature ondernemingen blijft uitdagend" | citaten | PB 2-9-2026 NL p.1–2 (A) | ✅ |
| Persbericht 26-3-2026: Lancksweert met pensioen (leeftijdsgrens) na AV 13-5-2026; Strömberg voorzitter; Soubie vicevoorzitter; Nicolas Boël ontslag om gezondheidsredenen | citaat | PB 26-3-2026 (A) | ✅ |
| Art. 15: 36.696.428 stemrechten (7-10-2025), geen converteerbare instrumenten | citaat | PB 7-10-2025 (A) | ✅ |
| Inkoopprogramma aangekondigd 3-4-2026 (voorwaarden niet gevonden); programma okt. 2025 max €26,1 mln om opties te dekken | MarketScreener-overnames persberichten | MarketScreener (C) — origineel sofinagroup.com 404 | ⚠️ enkel C |
| Anthropic: prijsvork $70–78, 825 mln aandelen, prijszetting 18-11, handel 19-11-2026 (Nasdaq: ANT), tot $1,4 bln volledig verwaterd | CNBC 10-11-2026 | CNBC (B), TechCrunch (C) | ✅ |
| SpaceX (genoteerd sinds juni 2026): Q3 omzet ≈$14,6 mld, nettowinst $4,4 mld, winst (vs verlies vorig jaar) | CNBC/Fortune 20-10-2026 | CNBC (B), Fortune (B) | ✅ |
| Nasdaq −5,5% op 5-11-2026 (slechtste dag in ~19 maanden), correctie; aanleiding: Democratische winst midterms, vrees voor rem op AI-datacenters | CNBC 5-11-2026 | CNBC (B), Axios (B) | ✅ |
| ByteDance: General Atlantic verkoopt deel aan $550 mld (feb. 2026, Reuters via SCMP); buyback 2025 >$330 mld; TikTok-VS-joint-venture sinds 22-1-2026 (Oracle, Silver Lake, MGX elk 15%, ByteDance 19,9%) | SCMP/CNBC | SCMP (B: Reuters overgenomen), CNBC (B) | ✅ |
| Vinted 2025: omzet €1,1 mld (+38%), nettowinst €62 mln (−19%), vrije kasstroom €137 mln; secundaire transactie 27-4-2026 aan €8 mld waardering | persberichten Vinted | company.vinted.com (A) | ✅ |
| Cognita: verkoop van belang Jacobs aan Blackstone/CVC (€6 mld) liep vast in 2025; Sofina ~13,4% belang, £270 mln geïnvesteerd in 2019 (volgens MandA) | MandA.be | MandA (C) — FT-origineel niet toegankelijk | ⚠️ C, als context |
| ECB 29-10-2026: depositorente 2,50% ongewijzigd (verhoging +25 bp sept. 2026) | persbericht ECB | ECB (A) | ✅ |
| Fed 28-10-2026: 3,75–4,00% ongewijzigd (verhoging sept.), 2 tegenstemmen voor verhoging | FOMC-statement | federalreserve.gov (A) | ✅ |
| Inflatie eurozone okt. 2026 flash 4,0% (sept. 3,8%), energie +20,8%, België 5,2% | Eurostat 4-11-2026 | Eurostat (A) | ✅ |
| EUR/USD ECB-referentie: 31-12-2024 1,0389 · 31-12-2025 1,1750 · 30-6-2026 1,1394 · 11-11-2026 1,1127 | eurofxref-hist | ECB (A) | ✅ |
| Olie: Brent tot ≈$117 eind oktober door aanvallen op schepen in Hormuz (oorlog VS–Iran) | CNBC 30-10-2026 | CNBC (B), Euronews (B) | ✅ |
| GBL 30-9-2026: NAV €99,21/aandeel, koers €71,10, korting 28,3%; LTV 4,1% | p.6/9 | gbl.com Q3 (A) | ✅ |
| Brederode 30-6-2026: eigen vermogen €154,64/aandeel (+9,2% na uitkering), koers €104,60 | p.1–2 | brederode.eu (A) | ✅ |
| Exor 30-6-2026: NAV/aandeel €157,9 (−3,9%), korting 57,6%, inkoop tot €500 mln | p.2/5 | exor.com (A) | ✅ |
| Investor AB 30-9-2026: aangepaste NAV SEK 411/aandeel, schuldgraad 1,8% | rapportpagina | investorab.com (A, via zoekfragment) | ✅ |
| Koersen 10-11-2026 (Yahoo): GBL 79,45 · Brederode 100,80 · Exor 74,30 · Investor B SEK 431,05 | Yahoo chart API | Yahoo (C) | ✅ |
| Fiscaliteit: netto dividend €2,562 op €3,66 bruto (30% roerende voorheffing) | JV25 p.149 | JV25 (A) | ✅ |
| Meerwaardebelasting 10% vanaf 1-1-2026, vrijstelling €10.000/jaar, fotomoment 31-12-2025 | FOD-pagina geblokkeerd (CAPTCHA); Bolero/Belfius FAQ | Bolero (C), Belfius (C) | ⚠️ C (FOD ❌) |

### Feitenlog E — Analistencall halfjaar 2026 (Investing.com-transcript, gepubliceerd 3-9-2026, rang C; AI-ondersteund transcript, titel toont foutief "H1 2025")
| Feit | Citaat | Status |
|---|---|---|
| Opbrengst kapitaalverhoging + obligatie uitzetten over ±3 jaar; netto schuldgraad doel 5–10%, "coherent with" S&P A− | "it should take three years" | ✅ |
| Korting: "we are still in the 20s, versus ... historical average, which is between 15% and 20%" | citaat ("348" in transcript = transcriptiefout, niet gebruikt) | ✅ |
| ByteDance "higher than 5%" maar "not higher than 10%"; "itchy fingers in high teens"; Sofina is LP in SPV, "no say and no view into the liquidity generation" | citaten | ✅ |
| Direct "flat for all practical purposes"; waardecreatie vooral uit fondsen; operationele cijfers Direct positief, multiples negatief | citaten | ✅ |
| Cognita: "doing well, but the growth is not as high as it was" (Midden-Oosten, betaalbaarheid) | citaat | ✅ |
| Software-multiples hersteld van dieptepunt maar lager dan vorig jaar | citaat | ✅ |
| Exits moeilijker door hogere rente; "we have permanent capital" | citaat | ✅ |
| Inkoop eigen aandelen, dividend, rentekosten: niet besproken | — | ✅ |
| Ontwijkend: timing schuldopbouw ("I am making no comment"), hypothetische co-investering HongShan | citaten | ✅ |
| Salto: tegenstrijdig in call ("pending closing" vs "closed in July") → in rapport: getekend, afronding volgens HJ26 onder voorwaarden | — | ⚠️ |
| Call jaarresultaten 2025 (maart 2026): geen transcript gevonden (investing.com lijst p.1, sofinagroup.com enkel presentatie) | — | ➖ |

### Feitenlog F — aanvullingen na teamreview ronde 1
| Feit | Citaat / tabelregel | Bron | Status |
|---|---|---|---|
| Familie vijf generaties actief | "Our reference family shareholder has been active in business for five generations" | HJ26 p.7 (A) | ✅ |
| Auditcomité 80%, remuneratiecomité 75% onafhankelijk | "Audit Committee 80% … Remuneration Committee 75%" | JV25 p.59/61 (A) | ✅ |
| Belangen (volledig verwaterd): Cambridge Associates 21,40%, Proeduca 17,22%, Cognita 14,06% (Lernen Midco), MNH 15,49%, Cleo AI 11,11%, Nuxe 49,00%, Drylock 25,00%, Vinted 2,88%, Cerealis 10,00% | tabellen | HJ26 p.30–32 (A) | ✅ |
| Verdeling consortium na 5-10-2026 (berekening): UFB 8.906.820, SPI 8.611.832, MIC 2.516.009; op 36.696.428 = 24,27/23,47/6,86%; op 35.328.731 stemgerechtigde = 25,21/24,38/7,12% (56,71%) | JV25 p.56 + FSMA nrs 46/47/50/55 | berekening | ✅ |
| FX-effect 2025 −€925 mln; waardecreatie +1,9% (+10,1% zonder FX) | brug "Currency Impact -925" | pres JV25 slide 10 (A) | ✅ |
| Beheerkosten cash 2025 €74,2 mln (2024 €61,2 mln) | "Management expenses 2 -74,197" | JV25 (managementkasstroom) (A) | ✅ |
| CEO-totaal 2021–2025: 4,09 / 1,27 / 1,24 / 1,98 / 2,03 mln | tabel p.74 | JV25 p.74 (A) | ✅ |
| LTIP cash 2025: CEO €565.593, LC €2.353.754; LC-pensioen 666.409 incl. eenmalige bijdrage | tabel + voetnoot 6 p.71 | JV25 p.71 (A) | ✅ |
| Bestuurders totaal incl. voorzitter €2.689.281 (+11,5%) | p.74 | JV25 p.74 (A) | ✅ |
| Inkoopprogramma 9-6 tot 31-8-2026: max €23 mln, 100.000 aandelen, KBC Securities, dekking opties | zoekfragment persbericht Sofina (link nu 404) | sofinagroup.com (A, via zoekmachine) | ⚠️ |
| AV 13-5-2026: UFB en Charles Peugeot benoemd (3 j), EY herbenoemd, dividend €3,66 | zoekfragment persbericht (link nu 404) | sofinagroup.com (A, via zoekmachine) | ⚠️ |
| Salto: Inflexion Partnership Capital III lead minderheidsinvesteerder, samen met Baskische families 33%, onder voorbehoud toezichthouders (juli 2026) | persbericht Inflexion; Dealroom | inflexion.com (A) | ✅ |
| ECB 11-6-2026: depositorente 2,00 → 2,25% | persbericht ECB | ecb.europa.eu (A) | ✅ |
| Brent $91,49 op 10-11-2026 (kort onder $90), −20% in november | CNBC 10-11-2026 | CNBC (B) | ✅ |
| Democraten winnen Huis en Senaat (3-11-2026); oproep moratorium datacenters | CNBC 4/5-11-2026 | CNBC (B) | ✅ |
| Nasdaq in correctie (>10% onder top) | CNBC 5-11-2026 | CNBC (B) | ✅ |
| Anthropic S-1: H1 2026 omzet $16,3 mld, nettoverlies $80,7 mld (± $72,4 mld niet-cash, omzetbare leningen) | Fortune 26-10-2026, CNBC | Fortune (B) | ✅ |
| Crypto: 0 treffers 'crypto', 'blockchain', 'digital asset' in JV25 en HJ26 | grep | JV25, HJ26 | ✅ |

### Waardering (aannames, na ronde 1)
- Basis: officiële NAV €326,48 (30-6-2026). Bandbreedte nu €315–335 (dollar +€5,2; techafwaardering −€4 tot −€12).
- Korting: eigen gemiddelde eind 2022–30-6-2026 = 25,0%; management 15–20% (bewering).
- Scenario's (nov. 2028): Slecht −8%/j, 32% korting → €190 (25%); Normaal +6%/j, 22% → €285 (55%); Goed +11%/j, 15% → €340 (20%). Gewogen €272. Staart −40% (€160), kans 5–10%.
- Koopzone: korting 25–31% op €326,48 = €225–245. Score 5,25 − 1 (R1) = 4,25 → 4.
