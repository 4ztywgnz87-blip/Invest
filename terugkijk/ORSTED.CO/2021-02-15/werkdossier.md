# Werkdossier — Ørsted (ORSTED.CO) — TERUGKIJKTEST, peildatum 2021-02-15

> **Terugkijktest** (zie `.claude/skills/analyseer/terugkijk.md`): enkel bronnen en koersen van vóór 15-02-2021. Niets over wat daarna gebeurde in dit dossier. Geschreven op 2026-11-11.

> Aantekeningen tijdens de analyse. Elke bevinding met bron (document + pagina of URL).
> Na elke fase: bijwerken + commit + push. Bij hervatten: hier verdergaan.

## Status
| Fase | Status | Opmerking |
|------|--------|-----------|
| 0 Identificatie & voorbereiding | ✅ | peildatum 15-02-2021 (12 dagen na jaarverslag 2020 van 3-2-2021) |
| 1 Koers & techniek | ✅ | `data/ORSTED.CO/koers_2021-02-15.json` (afgekapt) |
| 2 Verslagen | ✅ | jaarverslag 2020 + presentatie 3-2-2021 |
| 3 Bestuur & rode vlaggen | ✅ | R1 geraakt; R5 onvolledig |
| 4 Keten (2 niveaus) | ✅ | niveau 2 dun (beperking) |
| 5 Sector & concurrenten | ✅ | geen concurrentverslagen (beperking) |
| 6 Actualiteit | ✅ | rente, fondsinstroom, BOEM, Round 4 |
| 7 Earnings call | ✅ | enkel presentatie |
| 8 Waardering & advies | ✅ | Afwachten 4/10; IW ±475 |
| 9 Kritische expertblik | ✅ |  |
| 10 Fact-check | ✅ | zie hieronder |
| 11 Teamreview ronde 1 | ✅ | 3× niet goedgekeurd, 51 opm. |
| 11 Teamreview ronde 2 (+3) | ✅ | 3× goedgekeurd met opm.; geen ronde 3 |
| 12 Rapport bouwen | ✅ | HTML + PDF, 390 px nagekeken |
| 13 Afronding & feedback | ⬜ | |

(⬜ te doen · 🔄 bezig · ✅ klaar)

## Identificatie
- Ticker / beurs / ISIN / valuta: ORSTED.CO / Nasdaq Copenhagen / DK0060094928 / DKK (jaarverslag 2020 p.75)
- Type / soort: aandeel / terugkijktest (peildatum 2021-02-15)
- Sector / defensief: hernieuwbare energie (offshore wind) — nutssector; deels gereguleerde inkomsten (CfD, vaste subsidies), maar groeibedrijf met grote bouwprojecten → **niet** zuiver defensief (inschatting, te motiveren)
- Vorig rapport: geen

## Dekkingslijst
> ✅ nagekeken · ➖ niets gevonden / n.v.t. (reden) · ❌ geblokkeerd (alternatief) · ⬜ te doen. Geen ⬜ meer = klaar.

| Bron | Waarvoor | Status | Wat gevonden / waarom niet (zoektermen, talen, datum) |
|---|---|---|---|
| Laatste jaarverslag + kerncijfers 4 jaar ervoor | cijfers, trend | ✅ | Annual report 2020 (3-2-2021); 5-jaarstabel p.43 dekt 2016–2020 |
| Laatste halfjaar-/kwartaalverslag + persbericht | recentste cijfers | ✅ | Q4 2020 zit in jaarverslag (p.44) en presentatie 3-2-2021 |
| Investeerderspresentatie | strategie, vooruitzichten | ✅ | Investor presentation Q4/FY2020 (3-2-2021), kopie energiesdelamer.eu; orsted.com gaf 403 |
| Earnings call (transcript of verslag) | toon management | ❌ | transcript achter login (GuruFocus, roic.ai); alternatief: presentatie van de call gelezen |
| Verslag van de commissaris (oordeel, kernpunten, wissel revisor) | betrouwbaarheid cijfers | ✅ | AR2020 p.187–188: PwC sinds 2010, zonder voorbehoud, kernpunten farm-downs en belastingen |
| Remuneratieverslag | R2, R3 | ❌ | afzonderlijk verslag niet bereikbaar (orsted.com 403); alternatief: vergoedingstabel AR2020 p.104 en verbonden partijen p.159 |
| Aandeelhouders: nationale toezichthouder (aandeelhouders) | R1 | ✅ | AR2020 p.74–75 (Staat 50,1%, Andel 5,01%, Capital Group 5–10%); Finanstilsynet/OAM niet apart bevraagd |
| Insiders: nationale toezichthouder (insiders) | R5 | ❌ | orsted.com-meldingen laden enkel met JavaScript, GlobeNewswire 403; enkel titels gevonden (3 rondes, zie onvoldoende_info) |
| Corporate actions: beurs / officieel publicatieblad + persberichten bedrijf | R6 | ✅ | AR2020 p.74 (aandelenkapitaal ongewijzigd, verkoop RBC/LNG) |
| Rechtszaken: jaarverslag + zoekronde nieuws (NL/EN/FR/lokaal) + mededingingsautoriteit/EC | R4 | ✅ | AR2020 p.11, 113, 126–127 (Elsam-claim, belastinggeschil, naamgeschil); nieuwsronde EN: niets nieuws |
| Kredietbeoordeling (S&P, Moody's, Fitch: persbericht) | schuld | ❌ | persberichten ratingbureaus niet gezocht/bereikbaar; alternatief: AR2020 p.17 (rating in lijn met beleid min. BBB+/Baa1) |
| Persberichten van het bedrijf (laatste 12 maanden; snelle update: sinds vorig rapport) | actualiteit | ✅ | selectie bedrijfsmeldingen 2020 in AR2020 p.74 |
| Basisnieuws: De Tijd / L'Echo | actualiteit | ❌ | sites laten Claude niet toe; Belgische pers weinig over Ørsted; alternatief Bloomberg/Reuters overgenomen |
| Basisnieuws: Reuters (originele URL) | actualiteit | ❌ | reuters.com geblokkeerd; Reuters-bericht 3-2-2021 via OE Digital (bron 9) |
| Internationale kwaliteitspers (FT, Bloomberg, WSJ, AP) | actualiteit | ✅ | Bloomberg 26-1-2021 via WealthManagement (bron 8) |
| Vakpers van de sector | sector, keten | ✅ | WindEurope 8-2-2021 (bron 7) |
| Macro rechtstreeks bij de bron (ECB, Fed, Eurostat, Statbel) | rente, inflatie, valuta | ✅ | FRED DGS10, T10YIE, DFII10 (dagwaarden ≤12-2-2021); ECB AAA-rentecurve 10j (dagwaarden). Maandgemiddelde OECD februari geschrapt (na peildatum, review AS-1/KB-1/FA-1) |
| Verslagen van de 3–5 dichtste concurrenten | vergelijking | ➖ | bewuste beperking van deze terugkijktest (tijd); enkel sectorindex uit AR2020 p.74 en Bloomberg; genoteerd voor evaluatie |
| Keten: verslagen/IR-site van de niveau-1-partijen | keten | ✅ | Siemens Gamesa Q1 FY21 (offshorewind.biz 25-1-2021; persbericht SGRE 404); BOEM; Eversource niet gelezen |
| Short-seller-onderzoek (enkel aanwijzing, nooit bron) | R2, R4 | ➖ | zoekronde 'Orsted short seller report' vóór 2021: niets gevonden |
| Sancties en sectorregelgeving (EU-sanctielijst, sectorregulator) | risico | ➖ | geen sanctierisico; sectorregels (CfD, BOEM) in keten verwerkt |
| Fiscaliteit België (FOD Financiën) | netto rendement | ➖ | niet nagekeken in officiële bron; in rapport als mening met waarschuwing |
| Koersdata (tools/koers.py) | techniek, waardering | ✅ | koers.py --tot 2021-02-15 |


## Gelezen documenten
| Document | Pagina's gelezen | Waar opgeslagen |
|----------|------------------|-----------------|
| Ørsted Annual report 2020 (gepubliceerd 3-2-2021, financiële kalender p.74) | 3, 10–17, 29, 33, 43, 52, 62–63, 70–75, 104, 111, 113, 126–127, 187–188 | `data/ORSTED.CO/docs/annualreport2020.pdf` (bron: https://orsted.com/annualreport2020) |

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
| Rente & inflatie (VS, eurozone) | risico 1 volgens Ørsted; farm-down-prijzen | FRED DGS10/T10YIE/DFII10, ECB YC | VS 10j 0,52→0,93→1,20; breakeven 1,57→2,21; reëel −1,01; EUR AAA −0,42 |
| VK: CfD, stroomprijs, GBP | grootste markt; risico 2 | AR p.70–72, presentatie dia 6/20 | Brexit-akkoord, GBP-risico blijft; CfD AR4 tot 12 GW H2 2021; zeebodem Round 4 8-2-2021 |
| VS: vergunningen, beleid | risico 4; ±5 GW pijplijn | "BOEM Vineyard Wind February 2021", "Biden executive order offshore wind January 2021" | EO 27-1-2021; BOEM hervat VW 3-2-2021; Ørsted-bouwstarts schuiven op (AR p.52) |
| Taiwan (Changhua, TSMC, TWD) | 2 grote projecten | AR p.52, 71; presentatie dia 30; WebSearch "Changhua Orsted 2021 risk" | bouw volgens plan; TWD afgedekt; staartrisico tyfoon/aardbeving (AR p.71); geen specifiek nieuw risico gevonden |
| Polen | nieuwe markt | "Orsted PGE Baltica February 2021" | JV 50/50 Baltica 2&3 (10-2-2021) |
| Denemarken (politiek, Staat) | R1, thuismarkt | "Denmark energy island February 2021" | energie-eiland Noordzee goedgekeurd 4-2-2021; spelregels onbekend |
| Toeleveringsketen (turbines, schepen, havens) | bouwkosten en planning | "Siemens Gamesa Q1 2021 results" | SGRE: geen offshore-orders Q1, marge 5,3%; AR noemt havens/schepen als VS-risico |
| Concurrentie in veilingen | risico 3 | WindEurope, RenewableUK 8-2-2021 | hoge option fees; oliemaatschappijen (BP) winnen |
| Fondsinstroom / waardering sector | koers | "clean energy bubble January 2021" | Bloomberg 26-1-2021 |
| Wind (volume), COVID 2021 | EBITDA | AR p.15, 71 | 2020 9,7 m/s vs normaal 9,3; COVID-risico door Ørsted 'laag' ingeschat |
| Belastingen (DK) | R4 | AR p.11, 127 | DKK 5,1 mld eis; CFC-regels in voorbereiding |

### Actualiteit

### Earnings call

### Waardering (aannames)

## Feitenlog (vul aan tijdens het lezen; basis voor de fact-check)
| Feit (zoals in het rapport) | Letterlijk citaat / tabelregel | Bron + pagina of URL + datum | Rang | 2e bron | Status |
|------|------|------|------|------|------|
| EBITDA 2020 DKK 18,1 mld (BP), 2019 17,5; 2018 30,0 | "EBITDA 18,124 17,484 30,029 22,519 19,109" | AR2020 p.43 | A | | |
| Offshore = 14,75 mld van 18,1 mld EBITDA (81%) | "Offshore 14,750 15,161 28,046" | AR2020 p.43 | A | | berekening 14,75/18,12 |
| Winst 2020 16,7 mld, waarvan 10,9 mld meerwaarde verkoop Deense distributie (RBC) | "Profit for the year was DKK 16.7 billion ... resulting in a gain of DKK 10.9 billion" | AR2020 p.12 | A | | |
| Omzet 52,6 mld (2019 67,8) | "Revenue 52,601 67,842 76,946" | AR2020 p.43 | A | | |
| Netto schuld 12,3 mld (2019 17,2) | "Interest-bearing net debt 12,343 17,230 (2,219)" | AR2020 p.43 | A | | |
| FFO/aangepaste netto schuld 48,3% (doel ~30%) | "FFO/adjusted net debt2, % 48.3 31.0 69.0" + "well above our target of around 30 %" | AR2020 p.43, p.12 | A | | |
| Bruto-investeringen 27,0 mld 2020; guidance 2021 32–34 mld | "Gross investments 27.0 32-34" | AR2020 p.15 | A | | |
| Vrije kasstroom 2020 8,5 mld; 2019 −6,9 mld | "Free cash flow 8,538 (6,897) 5,812 261 5,367" | AR2020 p.43 | A | | |
| Operationele kasstroom 16,5 mld | "Cash flows from operating activities 16,466 13,079" | AR2020 p.43 | A | | |
| ROCE 9,7% (doel ~10% gem. 2019-2025) | "Return on capital employed (ROCE)1, % 9.7 10.6 32.1" | AR2020 p.43, p.17 | A | | |
| Guidance EBITDA 2021 15–16 mld excl. nieuwe partnerships (lager) | "Operating profit (EBITDA), excluding new partnership agreements, is expected to be DKK 15-16 billion in 2021" | AR2020 p.15 | A | | |
| Investeringsplan DKK 200 mld 2019-2025, >95% groeiplatform | "invest DKK 200 billion from 2019 to 2025, with more than 95 % earmarked for our growth platform" | AR2020 p.29 | A | | |
| Volgorde kapitaalallocatie: 1 rating BBB+/Baa1, 2 dividend +hoog enkelcijferig %, 3 groei, 4 overschot terug | "First, we adhere ... credit ratings ... Second ... dividend ... Third, we invest ..." | AR2020 p.29 | A | | |
| Dividend 2020 DKK 11,5 (+9,5%), totaal 4,8 mld; rendement 0,9% op 1.244 | "dividend of DKK 11.5 per share ... increase of 9.5 % ... DKK 4.8 billion" | AR2020 p.17, p.74 | A | | |
| WPA 2020 (BP) 38,8 DKK; 2019 12,7 | "Earnings per share (EPS) (BP), DKK 38.8 12.7 45.3" | AR2020 p.43 | A | | |
| Aandelen 420,4 mln, 1 klasse, eigen aandelen 312.844 | "Number of shares 420,381,080 ... Share classes 1 ... treasury shares 312,844" | AR2020 p.75 | A | | |
| **Deense Staat 50,1% (meerderheidsaandeelhouder)**; Andel 5,01%; Capital Group 5–10% | grafiek "Danish State (majority shareholder) ... 50.1 %"; "bringing their shareholding to 5.01 %" | AR2020 p.75, p.74 | A | | |
| Retail ±2%; 63% Deense eigenaars; 71.807 aandeelhouders | "Approximately 2 % ... owned by retail investors" | AR2020 p.74 | A | | |
| Koers eind 2020 1.244 (2019: 689); marktwaarde 522 mld; +80% in 2020; peers −5%, OMXC25 +34% | p.43 + p.74 | AR2020 | A | | |
| Top-5 risico's: 1 inflatie & rente, 2 valuta & grondstoffen, 3 concurrentie/prijsdruk, 4 VS-offshore ontwikkeling & bouw, 5 cyber | "Inflation and interest rates are considered our number one risk" | AR2020 p.70–71 | A | | |
| Rente-risico op farm-down-model: windparken minder aantrekkelijk voor kopers als rente stijgt | "Our farm-down model ... is exposed to interest rate risks as wind assets are more attractive to buyers when interest rates are low" | AR2020 p.72 | A | | |
| VS-parken vaste prijs ±20 jaar; vaste nominale subsidies → inflatie verlaagt reële waarde | "guaranteed a fixed price for a period of approximately 20 years"; "an increase in inflation will adversely impact the expected real value" | AR2020 p.72 | A | | |
| VS: vertraging BOEM-vergunningen had nadelige impact op portefeuille | "continued delays in the permitting process from the Bureau of Ocean Energy Management (BOEM) ... had an adverse impact" | AR2020 p.71 | A | | |
| Concurrentie veilingen: prijsdruk groter dan kostendaling verklaart | "put pressure on prices in auctions and tenders in excess of what can be explained by the LCoE development" | AR2020 p.71 | A | | |
| CEO Henrik Poulsen weg (15-6-2020), Mads Nipper CEO (aangesteld 9-9-2020); CMD 2-6-2021 | p.74, p.17 | AR2020 | A | | |
| Beroep tegen Deense belastingdienst over 2 UK-parken (1-12-2020) | "Ørsted appeals against decision from the Danish Tax Agency" | AR2020 p.74 | A | | R4 uit te diepen |
| Capaciteit 11,3 GW; 4,0 GW in aanbouw; 5,0 GW toegekend; doel >30 GW in 2030 | p.33 | AR2020 | A | | |
| Bestuurscontrole: wijziging statuten/ontbinding vereist dat Deense Staat deelneemt en steunt (bijzondere quorumregel) | "proposals to amend the Articles of Association or dissolve the company require that the Danish State participates in the general meeting and supports the proposals" | AR2020 p.63 | A | | R1 |
| Staat oefent eigendom uit via AV, professionele bestuurders; eigendomsbeleid fm.dk 2015 | p.63 | AR2020 | A | | R1 |
| Change of control: vergunningen/schuld kunnen herzien worden als Staat < 50% | "if the Danish State holds less than 50 % of the share capital or voting rights in Ørsted A/S" | AR2020 p.113 | A | | R1 |
| Raad van bestuur 9 leden (6 AV + 3 werknemers), voorzitter Thomas Thune Andersen | p.63, p.62 | AR2020 | A | | |
| Vergoeding Executive Board 2020 DKK 22,0 mln (2019 26,0); RvB 4,6 mln totaal | tabel "Total 22,011 25,981 ... 4,593 4,779" | AR2020 p.104 | A | | R2: niet buitensporig (mening) |
| Poulsen verloor aandelentoekenningen 2018-2020 bij vertrek (−4,6 mln) | "Henrik Poulsen lost the right to the 2018, 2019, and 2020 grant upon his resignation" | AR2020 p.104 | A | | R3: geen uitkoop |
| 2019: opzegperiode 11,6 mln + vertrekvergoeding 4,5 mln voor 2 ex-leden (Dalsgaard, Kjems Sørensen) | tabel p.104 voetnoot 2 | AR2020 p.104 | A | | R3 (2019) |
| Retentiebonus/aankoopprijs Lincoln Clean Energy 9,8 mln aan ander directielid | "Short-term retention-dependent purchase price related to the acquisition of Lincoln Clean Energy ... 9,810" | AR2020 p.104 | A | | R2 context |
| R4 Elsam: schadeclaim ±DKK 4,4 mld + interest (2007), maart 2020 vrijgesproken, beroep hangend bij het Hof van West-Denemarken (High Court of Western Denmark) | p.113 | AR2020 | A | | |
| R4 Belastingdienst DK: geen arm's-length vergoedingen Walney Ext. & Hornsea 1, extra belasting; Ørsted in beroep; voorziening aangelegd | p.126–127, p.188 | AR2020 | A | | |
| R4 Naamgeschil (afstammelingen Ørsted): mei 2019 gewonnen, november 2020 definitief gewonnen voor het Hooggerechtshof, zaak gesloten | p.11 | AR2020 | A | | |
| Commissaris PwC sinds 2010, oordeel zonder voorbehoud; kernpunten: farm-downs, belastingen | p.187–188 | AR2020 | A | | |
| Geen bijzondere waardeverminderingen 2020 | "We have not impaired any property, plant, and equipment in 2020" | AR2020 p.111 | A | | |
| VS: start bouw Revolution Wind, Ocean Wind 1, Skipjack, Sunrise wellicht later dan 2023/2024 door BOEM; South Fork eind 2023 ongewijzigd; "satisfactory returns" verwacht | p.52 | AR2020 | A | | |
| Greater Changhua 1&2a: funderingen Q1 2021, oplevering 2022; 50% Changhua 1 verkocht aan CDPQ/Cathay PE (dec 2020) | p.52 | AR2020 | A | | |
| TSMC-contract 20 jaar vaste prijs, Changhua 2b&4 (920 MW), oplevering 2025/26 | p.52 | AR2020 | A | | |
| 25% Ocean Wind 1 verkocht aan PSEG (dec 2020) | p.52 | AR2020 | A | | |
| 2021 plannen: farm-down 50% Borssele 1&2, sluiten Changhua 1; CMD 2-6-2021 | p.15, p.17 | AR2020 | A | | |
| Schuld excl. hybriden DKK 37,1 mld, >51% groen; hybride kapitaal 13,2 mld | p.29, p.43 | AR2020 | A | | |
| Rating-beleid min. Baa1/BBB+/BBB+ | p.17 | AR2020 | A | | |

## Fact-check (fase 10)
- Alle cijfers uit AR2020 nagekeken tegen het feitenlog (p.12, 15, 17, 29, 43, 63, 74–75, 104, 113).
- Herberekend: beurswaarde 420,07 × 1.058 = 444,4 mld; EV 472,6 mld; EV/EBITDA 2021 (15,5) = 30,5×; winst zonder meerwaarde 16.727 − 10.831 = 5.896 mln → 14,0/aandeel → K/W 75; FCF zonder verkopen 16,5 − 27,0 = −10,5; uitkering 4,8/5,9 = 81%; daling vanaf top 1.355 → 1.058 = −21,9%.
- DCF (eerste versie, vervangen door de tabel hieronder): 5,5% → 473/aandeel.
- Ronde 2 (definitief): slecht (13×21−64)/420 = 497 → 500; normaal (18×24−64)/420 = 876 → koersdoel 880; goed (24×25−55)/420 = 1.298 → 1.300. Waardetabel 3,5–6,5%: 1.421 / 1.006 / 757 / 592 / 475 / 319; break-even 3,92%; centraal 5,25% → 529.
- Winnaars Round 4 nagekeken in WindEurope-bericht (bron 7).
- Alle bronnen hebben een datum ≤ 15-02-2021 (gecontroleerd door tools/rapport.py).

## Waardering (aannames)
Zie sectie `waardering`: CE 110 → ±200 mld (2025), ROCE 10%, belasting 22%, WACC 5,5%, groei 2%. WACC is een inschatting (ECB AAA 10j −0,42% op 12-2-2021, VS 10j 1,20%; kost van de schuld ±2,8% volgens presentatie; projectrisico). Gevoeligheid in rapport: 3,5–6,5%, break-even ±3,9%; Ørsted publiceert geen WACC in het jaarverslag.

### Scenario-ankers (ronde 1)
- EBITDA 2023: doel Ørsted 25–26 mld uit draaiende parken (AR p.17, 33) + Markets & Bioenergy ±1,2 mld − overige/ontwikkelkosten ±2,3 mld (AR p.15, 43) → groep ±24 mld bij doel. Slecht 21, goed 25.
- Schuld 2023 (netto + hybride + minderheden): nu 28,2 mld. 2021–2023: investeringen ±100 mld (32–34/jaar) + dividend ±16 mld − operationele kasstroom ±55 mld − verkopen van belangen ±25 mld → +36 mld → 28,2 + 36 = ±64 mld (inschatting; correctie ronde 2, was 60). Goed scenario ±55 mld: ±9 mld extra verkopen van belangen (inschatting).
- Multiple nu op dezelfde basis: (445 + 64) / 24 ≈ 21×.
- Bronnen van toen per element van het slechte scenario (KB2-5): VS-vertraging/kostenoverschrijding AR p.73; ratingbeleid BBB+/Baa1 en FFO/schuld ~30% AR p.17; change of control bij Staat < 50% AR p.113; kost van het kapitaal: rentebronnen 4, 5, 10.

## Besmetting (voor de evaluatie)
- Het profiel (`profiel/PROFIEL.md` §1) vermeldt dat Ørsted (2021) de slechtste belegging van de gebruiker was. De hoofdanalist heeft dat gelezen vóór het schrijven (bij het opstarten van de taak). Dit rapport is dus **niet blind** geschreven; te vermelden in de besmettingscheck van de evaluatie (review KB-3). Volgende terugkijktests: profiel zonder ervaringen van na de peildatum aan reviewers geven.

## Open vragen / blokkades
