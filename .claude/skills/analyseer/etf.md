# Variant: ETF's en fondsen

Zelfde gouden regels, werkdossier, fact-check en afronding als `SKILL.md`. De inhoudelijke fases verschillen:

## Fases
1. **Identificatie** — exacte share class: ISIN, uitgever, notering (beurs + valuta), **accumulerend of uitkerend**, domicilie (IE, LU, …), replicatie (fysiek volledig / optimized sampling / synthetisch via swap), effectenuitlening.
2. **Kosten** (`kosten`) — TER, transactiekosten, **tracking difference** (werkelijke prestatie vs. index over 1/3/5 jaar), spread. Vergelijk met 2–4 alternatieven op dezelfde index.
3. **Index** (`index`) — welke index, methodologie, aantal posities, herweging.
4. **Samenstelling** (`samenstelling`) — top 10 posities en gewicht, verdeling per land, sector, valuta; **concentratie** (bv. aandeel VS, aandeel top 10, aandeel tech). Grafieken.
5. **Keten (aangepast)** — niveau 1 = grootste posities/landen/sectoren; niveau 2 = hun belangrijkste drijvers. Geen volledige bedrijfsanalyse per positie: enkel wat de ETF materieel beïnvloedt.
6. **Risico** (`risico`) — marktrisico, concentratie, valutarisico (EUR-belegger), tegenpartijrisico (synthetisch/uitlening), grootte en leeftijd van het fonds (sluitingsrisico).
7. **Actualiteit** — zelfde methode als bij aandelen, maar via de blootstellingskaart van de index (bv. VS-verkiezingen, Fed-rente, AI-concentratie, dollar).
8. **Techniek** — `tools/koers.py analyse` op de gekozen notering.
9. **Fiscaliteit België** (`fiscaliteit`) — beurstaks (tarief hangt af van type en registratie: 0,12% / 0,35% / 1,32%), roerende voorheffing op dividenden (uitkerend), **Reynders-taks** (> 10% obligaties → meerwaarde belast), meerwaardebelasting (vanaf 2026), bronheffing VS-dividenden binnen IE-fonds. **Controleer de actuele tarieven** op FOD Financiën of een recente betrouwbare bron — die veranderen.
10. **Waardering & advies** — geen DCF; wel: waardering van de index (koers/winst, vs. historisch), verwachte rendementsbandbreedte, scenario's (Slecht/Normaal/Goed), koopzone/koersdoel als bandbreedte. Oordeel + score.
11. **Expert & profiel** — past het bij vermogensopbouw, horizon, spreiding met wat de gebruiker al heeft (vraag eventueel welke ETF's hij al bezit om overlap te tonen)?

R1–R6 gelden niet rechtstreeks voor een ETF (geen `aandeelhouders`-blok nodig). Wel melden: rechtszaken/sancties tegen de uitgever, sluitingsrisico, en grote posities in de index met een R1-probleem als dat materieel is.

## Bronnen
Factsheet, KID, prospectus, jaarverslag fonds, website uitgever (holdings-CSV), justETF/trackingdifferences.com (data, geen feiten over fiscaliteit), FOD Financiën.
