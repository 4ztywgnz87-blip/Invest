# Evaluatie terugkijktest — DEME Group (DEME.BR), peildatum 2024-11-15

> Verzegeling: rapport (deel A) afgerond in commit `02597ea` op 2026-11-12. Deel A wordt na deze commit niet meer aangepast.
> Uitkomst berekend op 2026-11-12 met `tools/terugkijk.py` (zie `uitkomst.json`), index ^BFX (BEL20, koersindex zonder dividend) en ter vergelijking IWDA.AS (wereld-ETF, met herbelegd dividend).
> Let op: de 2-jaarstermijn (15-11-2026) is nog niet helemaal voorbij; "vandaag" (12-11-2026) geldt als ±2 jaar.
> Geen claimemissie of splitsing in de periode: geen correctie nodig.

## 1. In één oogopslag
| | Rapport (toen) | Werkelijkheid |
|---|---|---|
| Oordeel / score | Afwachten (nu niet kopen), 5/10; R1 NO-GO | — |
| Koers peildatum | €136,2 | €136,2 |
| Koers na 1 jaar / ±2 jaar | — | €143,0 (+5%) / €167,0 (+23%) |
| Rendement incl. dividend ±2 jaar | scenario's samen ±€136 + dividend: ±+3% | **+29%** (BEL20 +47% zonder dividend; wereld-ETF +28%) |
| Koopzone €95–110 bereikt? | | Nee (laagste slotkoers €118,4 op 7-4-2025; binnen de dag €110,0) |
| Koersdoel €153 gehaald? | normaal scenario | Ja, 15-1-2026; hoogste koers €206,25 (6-5-2026) |
| Stop-loss €109 geraakt? | | Nee |
| Dichtste scenario | Normaal €153 (50%) | €167: tussen normaal en goed |

**Besluit:** "nu niet kopen" (door R1) kostte de gebruiker **niets tegenover een wereld-ETF** (+29% tegenover +28%), maar wel tegenover de Belgische beurs (BEL20 +47%). Wie DEME had, kreeg geen vals verkoopsignaal. De grote misser zit in de **bedrijfscijfers**: DEME deed het veel beter dan zelfs ons goede scenario, maar de beurs betaalde minder per euro winst. Daardoor kwam de koers toch maar uit tussen normaal en goed.

## 2. Wat gebeurde er echt?
| Datum | Gebeurtenis | Koers | Bron (na peildatum) |
|---|---|---|---|
| 26-2-2025 | Jaarcijfers 2024: nettowinst €288 mln (+77%), vrije kasstroom €729 mln, **nettokas** €91 mln eind 2024, dividend €3,80 (was €2,10) | 128,8 → 137,0 | [Euronext/DEME 26-2-2025](https://live.euronext.com/nl/products/equities/company-news/2025-02-26-resultaten-voor-het-volledige-jaar-uitstekend-2024-sterke) |
| april 2025 | Laagste koers na de peildatum (beursdaling begin april) | 118,4 (7-4) | koersdata |
| 26-8-2025 | Halfjaar 2025: nettowinst €179 mln (+27%) | ±130 | [Euronext/DEME 26-8-2025](https://live.euronext.com/nl/products/equities/company-news/2025-08-26-halfjaarresultaten-2025-sterke-eerste-jaarhelft-zorgt) |
| jan.–feb. 2026 | Koers stijgt van ±140 naar ±200 | 139,8 → 202,0 | koersdata |
| 26-2-2026 | Jaarcijfers 2025: omzet ±€4,2 mld, EBITDA €931 mln (22,4%), nettowinst €346 mln, dividend €4,50; orderboek €7,6 mld (was €8,2 mld) | 202 | [DEME/GlobeNewswire 26-2-2026](https://www.globenewswire.com/news-release/2026/02/26/3245194/0/en/Full-year-results-2025-record-performance-marks-150-years-of-delivery.html), [Baird Maritime](https://www.bairdmaritime.com/marine-projects/dredging/deme-reports-record-turnover-and-profit-for-2025) |
| 2026 | Koers zakt terug van de top (206) | 167 (12-11) | koersdata |

## 3. Risico's en kansen: gezien, half gezien of gemist?
| Gebeurtenis | In rapport? | Hoe gewogen | Toen te vinden? | Fout van de methode? |
|---|---|---|---|---|
| Recordwinsten 2024–2025 (EBITDA 764 → 931 mln, marge 22%) | **onderschat** | Goed scenario: 800 mln en 20% (kans 15%); centrale waarde op 600–711 mln | Deels: DEME zei 16–20% marge en "omzet ≈ 2024" — DEME zelf onderschatte het ook | Ja: de review duwde de cijfers naar beneden (zie §6) |
| Vrije kasstroom €729 mln in 2024, nettokas | **gemist** | Model: €258 mln per jaar; "2021–2023 gemiddeld €37 mln" als waarschuwing | Deels: 1H24 al €278 mln | Ja: het verleden (zware investeringsjaren) woog te zwaar |
| Trump / VS wind op zee | gezien | ▼ middel | Ja | Geen zichtbare schade aan de cijfers van DEME |
| Orderboek daalt | gezien | ▼ middel | Ja | Orderboek steeg eerst naar €8,2 mld en zakte daarna naar €7,6 mld; geen impact op de winst |
| Energie-eiland | gezien | ▼ klein | Ja | Niet nagegaan |
| Beurs betaalt minder per euro winst | **gemist** | Scenario's: multiple 4,5× / 5,5× / 6,5× | — | Gedeeltelijk: in "goed" werd de hoge winst aan een hoge multiple gekoppeld; in werkelijkheid ging hoge winst samen met een lage multiple (±4–5×) |

## 4. Scenario's, advies en verkoopsignalen
- **Scenario's:** de koers (167) viel tussen normaal (153) en goed (211). Maar om de verkeerde reden: de winst overtrof "goed", de waardering per euro winst viel terug tot het niveau van "slecht". Twee fouten heffen elkaar op.
- **Advies:** "nu niet kopen" was voor de gebruiker neutraal tegenover een wereld-ETF en ongunstig tegenover de BEL20. R1 hield de gebruiker hier niet weg van een slechte belegging, maar ook niet van een uitzonderlijke: DEME deed ±hetzelfde als de wereldmarkt.
- **Koopzone (€95–110):** nooit bereikt op slotkoers. Te streng door de pessimistische waardering.
- **Verkoopsignalen:** geen enkel signaal ging af (stop-loss, orderboek < €6 mld, marge < 17%, schuld > 1,5×). Correct: er was geen reden om te verkopen.

## 5. Cijfers en vooruitzichten
| Verwachting in rapport | Werkelijkheid | Klopte? |
|---|---|---|
| EBITDA 2024 ±€717 mln (omzet +20%, marge ±18%) | €764 mln | ± (iets te laag) |
| Normaal: EBITDA ±€700 mln; goed: €800 mln | 2025: €931 mln (22,4%) | ❌ beter dan goed |
| Vrije kasstroom ±€258 mln/jaar (centraal) | 2024: €729 mln | ❌ veel beter |
| Netto schuld → kleine nettokas tegen 2026 | nettokas €91 mln al eind 2024 | ✅ (sneller) |
| Multiple 5,5× (normaal) | ±4–5× in november 2026 (inschatting op basis van koers en EBITDA 2025) | ❌ lager |
| Dividend groeit mee (uitkering 33%) | €2,10 → €3,80 → €4,50 | ✅ |

## 6. Besmettingscheck (kennis van achteraf)
| Punt | Richting | Oordeel |
|---|---|---|
| Profiel noemt DEME "beste belegging" | risico op positieve kleuring | De kritische belegger zag in ronde 1 een lichte positieve tilt; die werd weggewerkt. Het eindrapport was **pessimistischer** dan de werkelijkheid. Er is dus geen aanwijzing dat de achterafkennis het rapport te gunstig maakte; eerder het omgekeerde (overcorrectie). |
| R1 → niet kopen | neutraal | Mechanisch |
| Centrale waarde €115 (onder koers) | negatief | Gedreven door de review (KB-2/KB-3: "kapitaliseer geen recordjaar"). Verdedigbaar met de bronnen van toen, maar achteraf te voorzichtig. |

**Conclusie:** anders dan bij Ørsted werkte de review hier als een rem die te hard trok: ze maakte het rapport voorzichtiger dan de bronnen nodig maakten. Bij Ørsted was voorzichtigheid juist; hier niet.

## 7. Lessen voor de werkwijze
| # | Vaststelling | Les | Waar aanpassen |
|---|---|---|---|
| 1 | Hoge winst + lage multiple tegelijk; scenario's koppelden winst en multiple | Scenario's niet automatisch "goede winst = hoge multiple": toets ook de combinatie hoge winst / lage multiple (cyclische sectoren betalen op de piek minder per euro winst) | SKILL.md fase 8 |
| 2 | Het verleden (zware investeringsjaren) drukte de kasstroomverwachting te hard | Bij een bedrijf dat net uit een investeringsgolf komt: kasstroom ramen op basis van de nieuwe investeringsverwachting, niet op het gemiddelde van de investeringsjaren | SKILL.md fase 8 |
| 3 | De review corrigeert vooral naar voorzichtigheid | De kritische belegger moet ook uitdrukkelijk zoeken naar **te veel voorzichtigheid** (gemiste kansen), niet enkel naar optimisme | `.claude/agents/kritische-belegger.md` |
| 4 | R1 sloot een goede (niet uitzonderlijke) belegging uit; resultaat ≈ wereld-ETF | Geen wijziging aan R1 nodig op basis van deze test; zie samenvatting over beide tests | — |
| 5 | Signalen gaven terecht geen vals alarm | Behouden | — |

## 8. Voorstellen aan de gebruiker
Zie `terugkijk/SAMENVATTING.md` (beide tests samen).
