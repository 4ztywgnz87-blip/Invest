# Werkdossier — DEME Group (DEME.BR) — TERUGKIJKTEST, peildatum 2024-11-15

> **Terugkijktest** (zie `.claude/skills/analyseer/terugkijk.md`): enkel bronnen en koersen van vóór 15-11-2024. Huidige werkwijze (zonder voorstellen W1–W4, op vraag van de gebruiker, zodat Ørsted en DEME vergelijkbaar zijn). Geschreven op 2026-11-12.

> Aantekeningen tijdens de analyse. Elke bevinding met bron (document + pagina of URL).
> Na elke fase: bijwerken + commit + push. Bij hervatten: hier verdergaan.

## Status
| Fase | Status | Opmerking |
|------|--------|-----------|
| 0 Identificatie & voorbereiding | ✅ | peildatum 15-11-2024 (dag na trading update Q3) |
| 1 Koers & techniek | ✅ | koers_2024-11-15.json |
| 2 Verslagen | ✅ | AR2023, 1H24, Q3 2024 |
| 3 Bestuur & rode vlaggen | ✅ | R1 geraakt (AvH 62,1%), R4 Sabetta |
| 4 Keten (2 niveaus) | ✅ |  |
| 5 Sector & concurrenten | ✅ | Fugro, Subsea7 |
| 6 Actualiteit | ✅ | Trump, Ørsted, orderboek |
| 7 Earnings call | ✅ | enkel persberichten |
| 8 Waardering & advies | ✅ | Afwachten 5/10; IW ±136 |
| 9 Kritische expertblik | ✅ |  |
| 10 Fact-check | ✅ | zie hieronder |
| 11 Teamreview ronde 1 | ✅ | 3× goedgekeurd met opm. |
| 11 Teamreview ronde 2 (+3) | ✅ | 3× goedgekeurd met opm.; geen ronde 3 |
| 12 Rapport bouwen | ✅ | HTML + PDF |
| 13 Afronding & feedback | ✅ | niet in de app (terugkijktest) |

(⬜ te doen · 🔄 bezig · ✅ klaar)

## Identificatie
- Ticker / beurs / ISIN / valuta: DEME.BR / Euronext Brussel / BE0974413453 / EUR (AR2023 p.78)
- Type / soort: aandeel / terugkijktest (peildatum 2024-11-15)
- Sector / defensief: maritieme aannemer (offshore-energie, baggeren, infra) — niet defensief
- Vorig rapport: geen

## Dekkingslijst
> ✅ nagekeken · ➖ niets gevonden / n.v.t. (reden) · ❌ geblokkeerd (alternatief) · ⬜ te doen. Geen ⬜ meer = klaar.

| Bron | Waarvoor | Status | Wat gevonden / waarom niet (zoektermen, talen, datum) |
|---|---|---|---|
| Laatste jaarverslag + kerncijfers 4 jaar ervoor | cijfers, trend | ✅ | Annual Report 2023 (maart 2024): kerncijfers 2021–2023; beursgang 2022, dus geen 5 jaar beursgenoteerd |
| Laatste halfjaar-/kwartaalverslag + persbericht | recentste cijfers | ✅ | persbericht halfjaar 2024 (29-8-2024) en trading update Q3 (14-11-2024) |
| Investeerderspresentatie | strategie, vooruitzichten | ❌ | investors.deme-group.com time-out, gcs-web geweigerd; alternatief: persberichten |
| Earnings call (transcript of verslag) | toon management | ❌ | niet bereikbaar (zie onvoldoende_info); alternatief: CEO-citaat persbericht |
| Verslag van de commissaris (oordeel, kernpunten, wissel revisor) | betrouwbaarheid cijfers | ➖ | niet gelezen in deze terugkijktest (pagina's commissaris niet teruggevonden in tekstextractie) |
| Remuneratieverslag | R2, R3 | ✅ | AR2023 remuneratieverslag (CEO 1.986k, ExCo 4.480k, bestuurders 785k) |
| Aandeelhouders: FSMA (transparantieverklaringen) | R1 | ✅ | AR2023 p.136 (transparantiewet, drempel 5%): AvH 62,12%, VINCI 12,11%; FSMA-databank zelf niet bevraagd |
| Insiders: FSMA (transacties leidinggevenden) | R5 | ✅ | FSMA deme-1 t/m deme-16 (april 2024): opties uit verloningsplan, prijs 0 |
| Corporate actions: Euronext + Belgisch Staatsblad + persberichten bedrijf | R6 | ✅ | AR2023: beursgang via partiële splitsing 29-6-2022; geen nieuwe aandelen |
| Rechtszaken: jaarverslag + zoekronde nieuws (NL/EN/FR/lokaal) + mededingingsautoriteit/EC | R4 | ❌ | enkel AR2023 note 25 (Sabetta, consortiumclaim); nieuwsronde niet gedaan — open punt |
| Kredietbeoordeling (S&P, Moody's, Fitch: persbericht) | schuld | ➖ | DEME heeft geen publieke kredietrating gevonden in AR2023 (bankleningen met covenants) |
| Persberichten van het bedrijf (laatste 12 maanden; snelle update: sinds vorig rapport) | actualiteit | ✅ | halfjaar 2024, trading update Q3 2024 |
| Basisnieuws: De Tijd / L'Echo | actualiteit | ❌ | sites laten Claude niet toe; alternatief VRT NWS (energie-eiland, 24-10 en 12-11-2024) |
| Basisnieuws: Reuters (originele URL) | actualiteit | ❌ | reuters.com geblokkeerd; Reuters via AJOT (6-11-2024) |
| Internationale kwaliteitspers (FT, Bloomberg, WSJ, AP) | actualiteit | ➖ | niet apart gezocht; Reuters gebruikt |
| Vakpers van de sector | sector, keten | ✅ | offshorewind.biz (AR6, 3-9-2024) |
| Macro rechtstreeks bij de bron (ECB, Fed, Eurostat, Statbel) | rente, inflatie, valuta | ✅ | ECB AAA 10j en depositorente (14-11-2024), FRED DGS10 |
| Verslagen van de 3–5 dichtste concurrenten | vergelijking | ✅ | Fugro FY2023, Subsea7 FY2023 (+ aantal aandelen okt. 2024, ECB-wisselkoers), Cadeler FY2023 (EBITDA te klein); dichtste concurrenten niet beursgenoteerd (inschatting) |
| Keten: verslagen/IR-site van de niveau-1-partijen | keten | ✅ | Ørsted-melding Ocean Wind (1-11-2023) |
| Short-seller-onderzoek (enkel aanwijzing, nooit bron) | R2, R4 | ➖ | niet gezocht |
| Sancties en sectorregelgeving (EU-sanctielijst, sectorregulator) | risico | ➖ | Russisch verleden (Mordraga) via strafzaak; geen actuele sanctieblootstelling gevonden in AR2023 |
| Fiscaliteit België (FOD Financiën) | netto rendement | ➖ | niet nagekeken in officiële bron; in rapport als mening |
| Koersdata (tools/koers.py) | techniek, waardering | ✅ | koers.py --tot 2024-11-15 voor DEME, Fugro, Subsea7, Cadeler |


## Gelezen documenten
| Document | Pagina's gelezen | Waar opgeslagen |
|----------|------------------|-----------------|
| DEME Annual Report 2023 (maart 2024) | 8 (kerncijfers), 78–79 (aandeel), 136 (aandeelhouders), remuneratie (tekstregels 3550–3640), note 25 (geschillen), note 28 (verbonden partijen), risico's | data/DEME.BR/docs/DEME_20Annual_Report_2023_ENG_0.pdf |
| Persbericht halfjaar 2024 (29-8-2024) | 1–7 | data/DEME.BR/docs/cpr01_hugin_P2024_20DEME_201H24_20results_20ENG.pdf |
| Trading update Q3 2024 (14-11-2024) | 1–5 | data/DEME.BR/docs/cpr01_hugin_P2024_20DEME_20Trading_20update_20Q3_202024_20ENG.pdf |

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
| VS-politiek (Trump) | VS ±11% omzet 1H24 | "Trump election offshore wind stocks November 2024" | Reuters 6-11-2024: groene aandelen −; DEME −5,7% |
| Wind op zee: klanten | Offshore Energy ±46% | Ørsted Ocean Wind 2023 | stopzetting 1-11-2023; DEME-koers €84 okt. 2023 |
| Orderboek / pijplijn | toekomstige omzet | trading update Q3 | €7,1 mld (−9%) |
| Rente | financiering klanten, waardering | ECB, FRED | EUR 10j 2,45%, VS 4,43%, ECB-depo 3,25% |
| Midden-Oosten | groei 1→6% omzet | 1H24 | Oxagon, Abu Dhabi |
| Projecten vaste prijs | marge | AR2023 risico's | kostenoverschrijdingen als risico |
| Russisch verleden | R4 | AR2023 note 25 | strafzaak Sabetta |
| Belgisch energiebeleid (Prinses Elisabetheiland) | lopend project + vervolgwerk | VRT 'energie-eiland kosten oktober november 2024' | raming tot €7 mld; Elia beslist 28-11-2024 |
| Europese veilingen wind op zee | vraag naar installatie | 'AR6 offshore wind September 2024' | VK AR6 5,3 GW |
| Rode Zee / Suez, Egypte | Afrika 8% omzet | (AS-review, 3 rondes) | geen DEME-specifiek effect gevonden |
| Werkkapitaal | vrije kasstroom | 1H24 | −575 mln (vooruitbetalingen) |

### Actualiteit

### Earnings call

### Waardering (aannames)

## Feitenlog (vul aan tijdens het lezen; basis voor de fact-check)
| Feit (zoals in het rapport) | Letterlijk citaat / tabelregel | Bron + pagina of URL + datum | Rang | 2e bron | Status |
|------|------|------|------|------|------|
| Omzet/EBITDA/nettowinst 2021–2023 | "Turnover 3,285.4 2.654,7 2,510.6 … EBITDA 596.5 473.9 469.3 … Net result Share of the Group 162.8 112.7 114.6" | AR2023 p.8 (pdf) | A | FA-review | ✅ |
| Vrije kasstroom / netto schuld / investeringen 2021–2023 | "Free cash flow 61.6 -80.4 130.7 / Net financial debt -512.2 -520.5 -392.7 / Investments 398.9 483.9 282.0" | AR2023 p.8 | A | | ✅ |
| AvH 62,12%, VINCI 12,11%, vrij 25,77%; 25.314.482 aandelen | "Ackermans & van Haaren NV 15,725,684 62.12%" | AR2023 p.78, p.136 | A | | ✅ |
| EPS 6,43; dividend 2,10; uitkering 33% | "Earnings per share … 6.43 … Gross dividend 2.10 … Pay-out ratio 33%" | AR2023 p.79 | A | | ✅ |
| CEO €1.986k; ExCo €4.480k; bestuurders €785k | remuneratietabellen | AR2023 remuneratieverslag | A | | ✅ |
| Strafzaak Sabetta (Gent), hoorzitting 6-12-2023 | "summoned to appear before the criminal court in Ghent" | AR2023 note 25 | A | | ✅ |
| 1H24: omzet 1.916,4 (+30%), EBITDA 344,9 (18,0%), nettowinst 141,1, EPS 5,58, FCF 277,8, netto schuld −351,8, kas 508,7 | tabellen p.2–6 | Persbericht 1H24 | A | | ✅ |
| Verwachting: omzet volgende jaren ≈ 2024, marge 16–20% | "management expects the topline to be in line with 2024 … EBITDA margin to range between 16 and 20%" | Persbericht 1H24 p.3 | A | | ✅ |
| Orderboek 1H24 7.622,5; afloop 2026 1.394,8 | tabel "Orderbook run-off" | Persbericht 1H24 p.4 | A | | ✅ |
| Amerika 11% omzet 1H24 (19% 1H23) | "America 11% 19% 4%" | Persbericht 1H24 p.5 | A | | ✅ |
| Verliezen VS en Taiwan in 1H23 | "recorded losses on projects in the US and in Taiwan" | Persbericht 1H24 (segment Offshore) | A | | ✅ |
| Q3: omzet 2.994,4 (+32%), orderboek 7.141,1 (−9%), guidance >20%, capex ±300 | tabellen p.2–3 | Trading update Q3 2024 | A | | ✅ |
| Energie-eiland: raming 2,2 → 3,6 → 7 à 8 mld; Febeliec vraagt uitstel aanbestedingen | "nu zou het dus 7 tot zelfs 8 miljard kunnen worden" | VRT 24-10-2024 | B | | ✅ |
| AR6: ±5,3 GW, Hornsea 4 2,4 GW | "approximately 5.3 GW … securing 2.4 GW for the Hornsea 4" | offshorewind.biz 3-9-2024 | B | | ✅ |
| Subsea7: 302.188.272 aandelen; koers NOK 181,5 (15-11-2024); EBITDA 2023 $714 mln; netto schuld $552 mln | Euronext 7-10-2024; koers_2024-11-15.json; Inderes 29-2-2024 | A/data | | ✅ |
| ECB: EUR/NOK 11,759; EUR/USD 1,0533; AAA 10j 2,448% (14-11-2024) | ECB data-API | A | | ✅ |
| Insiders: 16 meldingen april 2024, opties, prijs 0 | "Transaction linked to remuneration package: acceptance and exercise of options/warrants" | FSMA deme-1…16 | A | | ✅ |

## Fact-check (fase 10)
- Beurswaarde 25.314.482 × 136,2 = 3.447,8 mln; EV + 351,8 = 3.799,6; /596,5 = 6,37×; EBITDA 2024 ≈ 3.285,4 × 1,20 × 18,16% = 716 → 5,31×; K/W 136,2/6,43 = 21,2; 136,2/11,16 = 12,2; dividend 2,10/136,2 = 1,54%.
- Fugro: 254,8/2,27 = 112,2 mln aandelen × 16,13 = 1.810 + 110,5 = 1.921 / 397,3 = 4,8×.
- Waarde (ronde 1 herzien): FCF = EBITDA − 350 − 0,25×(EBITDA−380) − 20; /7,5%/25,314. EBITDA 513 → 110 → 58; 600 → 175 → 92; 711 → 258 → 136; 790 → 318 → 167. Centraal ±115 (midden 600–711).
- Scenario's ronde 1: (4,5×500−200)/25,314 = 81; (5,5×700+30)/25,314 = 153; (6,5×800+150)/25,314 = 211; gewogen 0,3/0,5/0,2 → 143.
- Subsea7: 302,188 mln × NOK 181,5 / (11,759/1,0533) = $4.913 mln + 552 = 5.465 / 714 = 7,7×; /975 = 5,6×. DEME op schuld eind 2023: (3.448 + 512)/596,5 = 6,64×.
- Scenario's: (4,5×600−200)/25,31 = 98,8; (5,5×700+30)/25,31 = 153,3; (7×800+150)/25,31 = 227,2.
- Koers: 6-11 136,4→128,6 (−5,7%); 14-11 122,8→132,4 (+7,8%); top 171,4 (24-5-2024).
- Alle bronnen ≤ 15-11-2024 (tools/rapport.py).

## Besmetting (voor de evaluatie)
- Het profiel noemt DEME de beste belegging van de gebruiker. De hoofdanalist las dat vóór het schrijven. Ook dit rapport is dus niet blind. De hoofdanalist heeft geen gedetailleerde kennis van de koers na november 2024 gebruikt; dat wordt in de evaluatie nagegaan.

## Open vragen / blokkades
