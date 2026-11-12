# Evaluatie terugkijktest — Ørsted (ORSTED.CO), peildatum 2021-02-15

> Verzegeling: rapport (deel A) afgerond in commit `4c521cb` op 2026-11-12. Deel A wordt na deze commit niet meer aangepast.
> Uitkomst berekend op 2026-11-12 met `tools/terugkijk.py` (zie `uitkomst.json`), index ^OMXC25 (Deense C25).
> Correctie claimemissie 2025: Yahoo verwerkte de emissie (15 nieuwe aandelen per 7 oude aan DKK 66,6; ex-claim 17-9-2025) slechts vanaf 8-9-2025. Koersen vanaf die dag zijn ÷ 0,556 gerekend, zodat alles in de eenheid van het rapport staat (koers 15-2-2021 = 1.058). Factor = theoretische koers ex-claim / koers met claim; bevestigd door de korting die Bloomberg meldde (67% op de slotkoers, 39% op de theoretische ex-claimkoers). Bronnen: [Ørsted, prospectus 15-9-2025](https://www.investegate.co.uk/announcement/eqs/orsted-a-s--0rhe/-rsted-publishes-prospectus-and-initiates-rig-/9107246), [Bloomberg Government](https://news.bgov.com/esg/orsted-to-sell-shares-at-67-discount-in-9-4-billion-fund-raise).

## 1. In één oogopslag
| | Rapport (toen) | Werkelijkheid |
|---|---|---|
| Oordeel / score | Afwachten (nu niet kopen), 5/10; R1 NO-GO | — |
| Koers peildatum | 1.058 | 1.058 |
| Koers na 1 jaar / 2 jaar / vandaag | — | 680 (−36%) / 626 (−41%) / ±259 (−76%) |
| Rendement incl. dividend vs. index | — | 2 jaar: −40% vs C25 +5%; tot vandaag: −75% vs C25 +19% |
| Koopzone 480–600 bereikt? | | Ja, 7-10-2022 (592). Wie daar kocht, staat vandaag ±−56% |
| Koersdoel 880 (= daling) | −17% in 2 jaar | Al op 4-5-2021 onder 880; na 2 jaar −41% |
| Stop-loss 846 geraakt? | | Ja, 11-5-2021 (840) |
| Dichtste scenario na 2 jaar | Slecht (500, kans 30%) | 626: tussen slecht en normaal, dichtst bij slecht |
| Laagste koers ooit na peildatum | — | 179 (25-8-2025), −83% |

**Besluit:** het rapport zou de gebruiker **beschermd** hebben. Het zei "nu niet kopen" (door R1 en de hoge prijs), en wie het aandeel toch had, kreeg twee vroege verkoopsignalen (stop-loss in mei 2021 en de rentedrempel in januari/februari 2022) ruim vóór de grote klappen van 2023 en 2025. Twee zwakke punten: de **koopzone** bood geen bodem (kopen in oktober 2022 kostte nog ±56%), en de **2-jaarshorizon** zag de echte ramp (2023–2025) niet: het slechte scenario was te mild voor wat daarna kwam. Belangrijke kanttekening: het rapport is niet blind geschreven (zie §6); een deel van de goede uitkomst kan daardoor geflatteerd zijn. De mechanische delen (R1, stop-loss, rentesignaal) zijn dat niet.

## 2. Wat gebeurde er echt?
| Datum | Gebeurtenis | Koers (eenheid rapport) | Bron (na peildatum) |
|---|---|---|---|
| feb.–mei 2021 | Groene aandelen zakken verder; koers onder koersdoel (4-5) en stop-loss (11-5) | 1.058 → 840 | koersdata |
| 31-1-2022 / 10-2-2022 | Europese 10-jaarsrente boven 0%, Amerikaanse boven 2% | 699 / 676 | ECB-rentecurve; FRED DGS10 |
| 2022–2023 | Rente stijgt verder: VS-max 4,98% (19-10-2023), EUR AAA-max 3,03% (28-9-2023) | | FRED; ECB |
| 2023 (heel jaar) | EBITDA zonder nieuwe partnerships en annuleringskosten DKK 24,0 mld (boven guidance 20–23) — operationeel ≈ normaal scenario | | [Ørsted jaarverslag 2023 via Stockopedia/RNS](https://www.stockopedia.com/share-prices/oersted-a-s-CPH:ORSTED/news/reg-rsted-a-s-annual-report-for-2023-strong-underlying-results-and-strategic-progress-in-a-challenging-year-urn:newsml:reuters.com:20240207:nEQ9lhF2pa) |
| 29/30-8-2023 | Waarschuwing: VS-waardeverminderingen tot DKK 16 mld (leveranciers, belastingkredieten, rente); grootste koersval ooit | 559 → 421 | [BNN Bloomberg 30-8-2023](https://www.bnnbloomberg.ca/orsted-shares-plunge-as-company-warns-of-2-3-billion-us-hit-1.1965056) |
| 1-11-2023 | Stopzetting Ocean Wind 1 en 2; waardeverminderingen DKK 28,4 mld | 253 | [Ørsted bedrijfsmelding](https://orsted.com/en/company-announcement-list/2023/10/oersted-ceases-development-of-its-us-offshore-wind-73751) |
| 7-2-2024 | Dividend opgeschort (2023–2025), 600–800 banen weg, doel 2030 van 50 naar 35–38 GW, voorzitter stapt op | 379 | [Fortune 7-2-2024](https://fortune.com/europe/2024/02/07/orsted-offshore-wind-energy-writeoff-new-jersey-jobs-markets-dividends/) |
| 11-8-2025 | Claimemissie DKK 60 mld (geen koper voor 50% Sunrise Wind); Deense Staat tekent pro rata in; Hornsea 4 niet doorgezet | 309 → 217 | [offshoreWIND.biz 11-8-2025](https://www.offshorewind.biz/2025/08/11/orsted-plans-rights-issue-to-fund-building-us-offshore-wind-farm-alone-danish-state-commits-as-majority-subscriber) |
| 6-10-2025 | Emissie afgerond: DKK 59,6 mld, 99,3% ingeschreven | | [offshoreWIND.biz 7-10-2025](https://www.offshorewind.biz/2025/10/07/orsted-raises-eur-7-98-billion-in-oversubscribed-rights-issue) |

## 3. Risico's en kansen: gezien, half gezien of gemist?
| Gebeurtenis | In rapport? | Waar / hoe gewogen | Toen te vinden? | Fout van de methode? |
|---|---|---|---|---|
| Rentestijging 2022–2023 | **gezien** | Risico 1, besluit actualiteit, impact "▼ groot", waardetabel, verkoopsignaal met drempel | Ja: AR2020 p.70–72, FRED | Nee. Wel: de waardetabel ging maar tot 6,5% vereist rendement terwijl de rente zelf naar 4–5% ging (zie les 1) |
| VS: leveranciers, kosten, belastingkredieten → waardeverminderingen 2023 | **half gezien** | Risico 4, slecht scenario, verkoopsignaal; maar als "vertraging", niet als verlies van miljarden en stopzetting | Ja: AR2020 p.71, 73 (vertraging en kostenoverschrijding, vaste prijs 20 jaar) | Deels: de combinatie vaste prijs × kostenstijging × rente werd niet doorgerekend |
| Inflatie bij vaste nominale prijzen | **gezien** | Keten §1, actualiteit (inflatieverwachting) | Ja: AR2020 p.72 | Nee |
| Fondsinstroom draait om (groene "zeepbel") | **gezien** | Sector, besluit, profiel | Ja: Bloomberg 26-1-2021 | Nee |
| Kapitaalverhoging 2025 (met Staat pro rata) | **gezien als mogelijkheid** | Slecht scenario, verkoopsignaal | Logisch afgeleid uit ratingbeleid (AR p.17) | Nee, maar zie besmettingscheck |
| Dividend opgeschort 2024 | **gemist** | Dividendbeleid als stabiel beschreven | Deels: het dividend was een prioriteit ná de rating (AR p.29) | Ja, klein: bij een kapitaalintensief bedrijf moet "dividend kan wegvallen" in het slechte scenario |
| Verlies 50%-verkoopmodel (geen koper Sunrise Wind) | **half gezien** | Rentegevoeligheid farm-downs (investeringen, keten) | Ja: AR p.72 | Deels: niet als apart verkoopsignaal |
| Operationeel: projecten opgeleverd, EBITDA 2023 ≈ doel | **gezien** (normaal scenario) | Normaal scenario EBITDA ±24 mld | Ja | Nee: de winst klopte, de waardering niet |

## 4. Scenario's, advies en verkoopsignalen
- **Scenario's:** na 2 jaar 626, binnen de vork 500–1.300 en dichtst bij "slecht" (30%). De kansen waren redelijk. Maar de echte schade kwam in jaar 3–5 (tot 179): de 2-jaarshorizon van het profiel mist zulke trage, structurele risico's.
- **Advies en score:** "nu niet kopen" was juist. Zonder R1 was de score 6 (5,6) geweest: geen duidelijke koopaanbeveling bij deze prijs (mening), maar ook geen duidelijk 'niet kopen'. R1 gaf hier de doorslag.
- **Verkoopsignalen (voor wie het aandeel had):**
  1. Stop-loss 846 → 11-5-2021. Verkopen daar bespaarde ±70% tegenover vandaag. ✅ werkte.
  2. Rente: EUR > 0% op 31-1-2022 (koers 699), VS > 2% op 10-2-2022 (676). Verkopen daar bespaarde ±60%. ✅ werkte.
  3. VS-vertraging / waardevermindering → 29/30-8-2023 (559 → 421). Kwam pas bij de klap zelf. ⚠️ te laat om veel te besparen.
  4. EBITDA < 15 mld / ROCE < 8%: niet geraakt (EBITDA bleef hoog) — terwijl de koers instortte. ⚠️ cijfersignalen misten het risico.
  5. Kapitaalverhoging → 11-8-2025. ⚠️ te laat.
  → De **koers- en macrosignalen** werkten; de **bedrijfscijfersignalen** niet, omdat het probleem in de waardering en de toekomstige projecten zat, niet in de lopende winst.
- **Koopzone:** bereikt op 7-10-2022 (592), daarna nog −56%. De koopzone steunde op 5–5,5% vereist rendement; met de rente van 2023 (VS 4–5%) was dat te laag.

## 5. Cijfers en vooruitzichten
| Verwachting in rapport | Werkelijkheid | Klopte? |
|---|---|---|
| EBITDA 2023 ±24 mld (normaal) | 24,0 mld zonder partnerships en annuleringskosten | ✅ |
| Dividend groeit hoog enkelcijferig tot 2025 (beleid) | Opgeschort 2023–2025 | ❌ |
| Schuld 2023 ±64 mld, kapitaalverhoging enkel in slecht scenario | Emissie DKK 60 mld in 2025 | ❌ (te optimistisch) |
| Vereist rendement 5–5,5% centraal | Rente zelf steeg naar 3–5% | ❌ (te laag) |

## 6. Besmettingscheck (kennis van achteraf)
| Punt in rapport | Toen-bron | Risico op achteraf-kennis | Waarom |
|---|---|---|---|
| R1 → niet kopen | AR p.75 | laag | Mechanische regel |
| Stop-loss −20% | profiel | laag | Mechanische regel |
| Rente als risico 1 | AR p.70 | laag | Ørsted's eigen nr. 1; rente steeg al |
| Hoge waardering / zeepbel | Bloomberg 26-1-2021 | laag–middel | Breed besproken in januari 2021, maar de scherpte van de toon kan gekleurd zijn |
| Rentedrempels 2% / 0% | FRED/ECB niveaus eind 2019 | middel | Logische drempel, maar gekozen door iemand die wist dat de rente fors steeg |
| VS-kostenoverschrijdingen in slecht scenario | AR p.73 | middel | Gebrond, maar de nadruk kwam er mee door de review (KB-2 schrapte een ongebronde versie) |
| Kapitaalverhoging + Staat in slecht scenario | AR p.17, 113 | middel–hoog | Logisch, maar precies wat gebeurde |
| Kans slecht 30% | — | middel | Eigen inschatting |
| Profiel met "Ørsted slechtste belegging 2021" | — | hoog (proces) | De auteur had dit gelezen vóór het schrijven (review KB-3) |

**Conclusie:** de kern van het oordeel (R1, prijs, stop-loss, rente) is verdedigbaar zonder kennis van achteraf. De scherpte van het slechte scenario en de keuze van sommige drempels zijn mogelijk gekleurd. Een echt blinde test vraagt een analist die de afloop niet kent; dat is met Claude niet volledig haalbaar, wel te benaderen (zie les 5).

## 7. Lessen voor de werkwijze
| # | Vaststelling | Les (concreet, toetsbaar) | Waar aanpassen |
|---|---|---|---|
| 1 | Koopzone (5–5,5% vereist rendement) bood geen bodem toen de rente normaliseerde | **Stresstest in elke waardering**: reken ook met een vereist rendement bij "normale" rente (bv. 10-jaarsrente terug naar het gemiddelde van de voorbije 10–20 jaar). De koopzone moet onder die stresswaarde liggen, of het rapport zegt expliciet dat ze dat niet doet | SKILL.md fase 8, rapport-formaat |
| 2 | Signalen op bedrijfscijfers gingen niet af; signalen op koers en rente wel | Elk rapport heeft minstens één **koerssignaal** (stop-loss) en één **macro- of waarderingssignaal** met drempel, naast de cijfersignalen | SKILL.md fase 8 |
| 3 | De echte schade viel buiten de 2-jaarshorizon | Bij kapitaalintensieve bedrijven met een grote projectpijplijn: een **"staartscenario"** (5 jaar: projecten afgeschreven, dividend weg, kapitaalverhoging) naast de drie scenario's, als tekst, zonder kans | SKILL.md fase 8–9 |
| 4 | Dividendbeleid werd als vast aangenomen | In het slechte scenario altijd nagaan of dividend en eigen-aandelenbeleid kunnen wegvallen (volgorde van kapitaalgebruik uit het jaarverslag) | SKILL.md fase 2/8 |
| 5 | Het profiel bevatte de uitkomst; de auteur was niet blind | Bij een terugkijktest: (a) een **profielversie zonder ervaringen na de peildatum** voor reviewers, (b) liefst een aandeel kiezen waarvan de afloop minder bekend is, (c) de besmettingscheck blijft verplicht | terugkijk.md |
| 6 | Maandgemiddelde van na de peildatum glipte erdoor (bron had een "begin"-datum) | Macrocijfers enkel als **dagwaarde** of als volledig afgelopen periode die vóór de peildatum gepubliceerd was | terugkijk.md, bronnen.md |
| 7 | Yahoo verwerkt claimemissies niet consistent | Bij elke kapitaalverhoging de koersreeks nakijken op sprongen en een correctiefactor uit officiële voorwaarden gebruiken | tools/koers.py (waarschuwing bij sprong > 25% op één dag) |
| 8 | Concurrenten niet gelezen (open punt van alle reviewers) | Onbekend of het iets veranderd had; de regel blijft: minstens 3 concurrenten, ook in terugkijktests | geen wijziging |

## 8. Voorstellen aan de gebruiker
(Wijzigingen aan werkwijze of profiel: pas na akkoord doorvoeren.)
- **W1** — Stresstest van de waardering en koopzone (les 1).
- **W2** — Verplicht een koerssignaal én een macro/waarderingssignaal (les 2).
- **W3** — Staartscenario op 5 jaar bij kapitaalintensieve groeibedrijven (les 3–4).
- **W4** — Terugkijktest-regels: profiel zonder latere ervaringen, macro enkel dagwaarden, koerssprongen controleren (les 5–7).
