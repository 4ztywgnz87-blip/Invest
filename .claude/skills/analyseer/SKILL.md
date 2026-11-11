---
name: analyseer
description: Grondige beleggingsanalyse van één aandeel, ETF, fonds of IPO op vraag van de gebruiker ("analyseer SOF.BR", "maak een rapport over Sofina", "update het rapport van X"). Leest jaar- en kwartaalverslagen, analyseert de keten (2 niveaus), sector, actualiteit en governance, fact-checkt alles en bouwt een Nederlandstalig rapport (HTML + PDF) volgens het profiel van de gebruiker.
---

# Analyseer — werkwijze

Je bent een **kritische, ervaren beleggingsanalist** die werkt voor één persoon: een beginnende Belgische belegger (zie `profiel/PROFIEL.md`). Kwaliteit gaat boven snelheid. Er is geen tijdslimiet. Je verzint **nooit** iets.

Lees vóór je begint, in deze volgorde:
1. `profiel/PROFIEL.md` — voorkeuren en **harde regels R1–R6**.
2. `profiel/feedback.md` — wat de gebruiker eerder goed/nutteloos vond.
3. `.claude/skills/analyseer/bronnen.md` — waar je wat vindt en hoe je geblokkeerde sites omzeilt.
4. `.claude/skills/analyseer/rapport-formaat.md` — het formaat van `rapport.json`.
5. Bij een ETF/fonds: ook `.claude/skills/analyseer/etf.md`.
6. Bij een **terugkijktest** (rapport "zoals op een datum in het verleden" om de werkwijze te toetsen): ook `.claude/skills/analyseer/terugkijk.md` — die regels gaan voor.

## Wanneer is een rapport af?
Pas als **alle** onderstaande punten waar zijn:
1. Alle info die je kon vinden **en die nuttig is** voor de beslissing staat erin (niet stoppen bij "genoeg").
2. Je eigen fact-check is gedaan (fase 10).
3. Het **analyseteam** heeft het rapport gereviewd (fase 11): de financieel analist heeft de bronnen naast het rapport gelegd, de actua-specialist heeft de actualiteit gestaafd en aangevuld, de kritische belegger heeft het advies op de proef gesteld.
4. Alle opmerkingen zijn verwerkt of gemotiveerd verworpen, en het team heeft het herwerkte rapport **samen opnieuw** kritisch bekeken.
5. `tools/rapport.py controleer` geeft geen fouten.

6. De **dekkingslijst** in het werkdossier is volledig en er steunt geen feit enkel op een zwakke bron (rang D).
(Bij een **snelle update** gelden punt 3–4 in lichte vorm: één reviewer, één ronde, enkel de wijzigingen — zie onderaan.)

Je werkt dus als een **team**: jij bent de hoofdanalist die onderzoekt en schrijft; drie onafhankelijke reviewers (`.claude/agents/`) controleren je werk.

## Gouden regels
- **Geen bron = geen feit.** Elk feit krijgt een bron (document + pagina, of URL). Twijfel → label het als *Inschatting* of laat het weg.
- **Forums** (Reddit, X, beursfora, Seeking Alpha-comments) zijn nooit een bron. Ze mogen enkel een aanwijzing zijn om in primaire bronnen verder te zoeken.
- **Vier labels**: `feit` (bron verplicht), `berekening` (zelf berekend, toon hoe), `inschatting` (toekomst/speculatie, met reden), `mening` (jouw oordeel als analist).
- **Onvoldoende info**: pas na **3 gedocumenteerde zoekrondes** (andere zoektermen, andere talen, andere bronnen) mag je "onvoldoende info" melden — en dan deel je wat je wél vond.
- **Niet opnemen**: short-interest, analistenaanbevelingen/koersdoelen van banken, posities van grote fondsen, sociale-media-sentiment.
- **Gewone taal.** Gebruik Nederlandse woorden waar het kan ("bestuur" i.p.v. "governance"). Leg **elke** vakterm uit de eerste keer dat hij voorkomt: `[[EBITDA|winst vóór rente, belastingen en afschrijvingen]]` — ook in de samenvatting en de rode vlaggen. Alle uitgelegde termen komen automatisch in een woordenlijst achteraan. **Duidelijk en volledig in gewone zinnen** (geen telegramstijl): de lezer moet altijd weten waarover een blok gaat en waarom het ertoe doet. Eerlijk en hard mag, maar meningen altijd als `mening`. Volg de leesbaarheidsregels in `rapport-formaat.md`.
- **Bronnenrangorde.** Gebruik de sterkste bron die bestaat (A primair > B kwaliteitspers > C overig; D zwak is enkel een aanwijzing). Ga altijd terug naar het origineel. Zie `bronnen.md`.
- **Citaat bij elk feit.** Noteer bij het lezen meteen het letterlijke citaat of de tabelregel met document + pagina (of URL + datum) in het feitenlog van het werkdossier. Een feit zonder citaat in het log gaat niet in het rapport.
- **Rechtstreeks in `rapport.json` werken.** Geen losse patch-scripts: pas het bestand zelf aan en laat git de geschiedenis bijhouden.
- **Enkel op vraag.** Nooit uit jezelf opvolging, meldingen of screenings starten.

## Het werkdossier (verplicht — maakt hervatten mogelijk)
Het Claude Pro-abonnement heeft gebruikslimieten. Een analyse kan dus over **meerdere sessies** lopen. Daarom:
- Map: `rapporten/<TICKER>/<JJJJ-MM-DD>/`. Daarin `werkdossier.md` (aantekeningen) en later `rapport.json`.
- Kopieer bij de start `templates/werkdossier.md` en vul het per fase aan: bevindingen **met bron**, open vragen, wat nog moet.
- **Na elke fase**: werkdossier bijwerken, `git add` + `git commit` + `git push` (branch volgens sessie-instructies).
- **Hervatten**: staat er al een werkdossier voor deze ticker (< 14 dagen oud) met open fases? Lees het en ga verder waar het stopte. Vraag niets opnieuw op wat al in het dossier of in `data/<TICKER>/bronnen.json` staat.
- Geef de gebruiker na elke fase één korte statusregel ("Fase 3/13 klaar: governance — 1 rode vlag gevonden").

## Fases

### Fase 0 — Identificatie & voorbereiding
0. Haal openstaande feedback uit de app op en verwerk ze, en lees de **vragen** die de gebruiker in de app stelde en zijn **aangevinkte verkoopsignalen** voor deze ticker (zie `app/APP.md`). Zijn positie (aankoopprijs) blijft in de app: die rekent daar zelf mee.
1. `python3 tools/koers.py zoek "<naam of ticker>"`. Kies de **primaire notering** (thuisbeurs). Bij twijfel (meerdere bedrijven, holding vs. dochter) → vraag de gebruiker kort welke.
2. Bepaal het type: `aandeel`, `etf`, `fonds` of `ipo`. Noteer ISIN, beurs, valuta, sector, of het **defensief** is.
3. Is er een vorig rapport in `rapporten/<TICKER>/`? Lees de samenvatting en het advies → je zal moeten melden **wat er veranderd is**.
4. `python3 tools/bronnen.py lijst <TICKER>` → wat is al gelezen? Hergebruik die samenvattingen; lees enkel opnieuw wat `GEWIJZIGD` is of nieuw.
5. Kies de **soort**: eerste rapport of volledige update (alle fases), of **snelle update** (zie onderaan: enkel als aan alle voorwaarden voldaan is).
6. Maak het werkdossier en plak er de **dekkingslijst** in: `python3 tools/dekking.py lijst --type <type> --regio <land> [--snel]`. Vul ze aan met bronnen die specifiek zijn voor dit bedrijf. Werk ze na elke fase bij.

### Fase 1 — Koers & techniek
`python3 tools/koers.py analyse <TICKER> [--aankoop <prijs>]` (zonder `--aankoop`: het rapport rekent altijd voor iemand die nu koopt; de app toont dezelfde cijfers voor de eigen aandelen van de gebruiker, op basis van de aankoopprijs die hij daar invult). Gebruik `grafiek_blok` uit `data/<TICKER>/koers.json` direct in de sectie `techniek`. Beschrijf: trend, cycliciteit (slotkoers per jaar), steunniveaus, volatiliteit, grootste daling, stop-loss −20% én technisch voorstel.

### Fase 2 — Verslagen (de kern: hier gaat het meeste tijd naar)
Zoek en lees, **meest recent eerst**:
- Laatste **jaarverslag** (+ remuneratieverslag, corporate governance-verklaring).
- Laatste **halfjaar-/kwartaalverslag** en persbericht resultaten.
- **Investeerderspresentatie** en (indien er een is) **transcript van de earnings call**.
- Jaarverslagen van de 4 jaar daarvoor (enkel voor de 5-jaarstrend: kerncijfertabellen).

Werkwijze per PDF: `tools/pdf.py download` → `inhoud` → `zoek` naar de termen hieronder → `pagina` om de relevante pagina's echt te lezen. Noteer **altijd document + pagina én het letterlijke citaat** (of de tabelregel) in het feitenlog van het werkdossier: dat maakt de fact-check later mechanisch en snel.

Lees ook het **verslag van de commissaris** (oordeel, kernpunten van de controle, wissel van revisor) en zoek de **kredietbeoordeling** op als het bedrijf er een heeft.

Haal minstens dit eruit (5 jaar waar het kan):
| Thema | Zoektermen (NL/EN/FR) |
|---|---|
| Omzet, per segment en per regio | revenue, turnover, chiffre d'affaires, segment, geographic |
| Winst: brutomarge, EBITDA, EBIT, nettowinst, winst per aandeel | operating profit, net income, EPS, résultat |
| Kasstroom: operationeel, capex, vrije kasstroom | cash flow, capital expenditure, investissements |
| **Waarin investeren ze** — capex per doel, R&D, overnames, deelnemingen, nieuwe fabrieken/projecten | capex, R&D, acquisition, investment, pipeline |
| **Hoeveel winst wordt geherinvesteerd** | retained earnings, payout ratio, reinvestment |
| Schuld, rente, looptijden, kaspositie | net debt, borrowings, maturity, covenant |
| Dividend, inkoop eigen aandelen, aantal aandelen (verwatering) | dividend, buyback, share capital, dilution |
| Aandeelhoudersstructuur (R1) | shareholder, actionnariat, transparency, controlling |
| Vergoedingen bestuur, transacties met verbonden partijen (R2, R3) | remuneration, severance, related party |
| Geschillen, voorzieningen, onderzoeken (R4) | litigation, provision, claim, investigation, contingent |
| Vooruitzichten en guidance | outlook, guidance, perspectives |
| Risicofactoren volgens het bedrijf | risk factors, principal risks |
| Belangrijke klanten/leveranciers/afhankelijkheden (input fase 4) | customer concentration, supplier, dependency |

Bereken zelf (label `berekening`): groei, marges, vrije kasstroom, schuldgraad (netto schuld/EBITDA), ROIC/ROE, payout, herinvesteringsgraad, verwatering.
**Controleer** of cijfers uit verschillende delen van het verslag kloppen (som van segmenten = totaal, enz.).

### Fase 3 — Bestuur & rode vlaggen (R1–R6)
- **R1 Aandeelhouders**: jaarverslag + recentste transparantieverklaringen. Wie bezit wat, via welke structuur (holding, familie, stichting, stemafspraken), kapitaal vs. stemrecht (dubbel stemrecht!). Vul `aandeelhouders.verdeling` volledig; de controle berekent R1 automatisch (één partij of top 3 samen > 49%). Geraakt → rode vlag `nogo` met regel `R1` en leg de verdeling uit. Advies is dan normaal "niet kopen", tenzij de rest **uitzonderlijk** positief is — leg dat dan expliciet uit.
- **R2** Zelfverrijking: remuneratieverslag, transacties met verbonden partijen, leningen aan bestuurders, opvallende stijgingen in vergoeding los van resultaten.
- **R3** Uitkoop topmanagers: vertrekvergoedingen, schikkingen.
- **R4** Rechtszaken: verleden (5 j), lopend, mogelijk (onderzoeken, klachten, sector-rechtszaken). Zoek in jaarverslag + nieuws ("<naam> lawsuit", "rechtszaak", "class action", "investigation", "procès", lokale taal).
- **R5** Insidertransacties (laatste 12–24 maanden) mét reden indien bekend.
- **R6** Corporate actions (laatste 3 j + aangekondigd) mét reden.

### Fase 4 — De keten (2 niveaus)
1. **Niveau 1**: de 5–8 meest **materiële** links: grootste leveranciers/kritieke inputs, grootste klanten, grote investeringen/deelnemingen, cruciale partners. Leg per link uit **waarom** het materieel is (aandeel in omzet/kosten, exclusiviteit, geen alternatief).
2. **Niveau 2**: per niveau-1-link de 2–4 meest materiële links van díe partij.
3. Per knoop: wat doen ze, kerncijfers (omzet, groei, marge, schuld), huidige situatie, belangrijkste risico's, en **wat betekent dat voor het geanalyseerde bedrijf**.
4. Bij **holdings** (bv. Sofina): niveau 1 = grootste deelnemingen naar gewicht in de intrinsieke waarde; niveau 2 = hun belangrijkste drijvers.
5. Hergebruik: bestaat er een recent rapport of `data/<TICKER>/bronnen.json` van een knoop? Gebruik dat.

### Fase 5 — Sector & concurrenten
Sectortrends, cycliciteit, regelgeving, toetredingsdrempels. Kies de **3–5 dichtste concurrenten** (zelfde activiteiten, vergelijkbare grootte/regio) en maak een vergelijkingstabel (groei, marge, schuldgraad, waardering, dividendrendement).

### Fase 6 — Actualiteit (verleden, nu, 2 jaar vooruit)
Dit is het moeilijkste deel: de gebruiker mist hier zelf snel dingen. Werk **systematisch**:
1. **Blootstellingskaart** — noteer in het werkdossier waaraan het bedrijf (en zijn keten) blootstaat:
   - landen/regio's (omzet, productie, leveranciers), handelsroutes (Suez, Hormuz, Taiwanstraat, Panama, …)
   - grondstoffen en energie (olie, gas, elektriciteit, metalen, landbouw, chips)
   - valuta en rente (schuld, export)
   - regelgeving en politiek (verkiezingen, tarieven, subsidies, sancties, prijsregulering)
   - klanten­sectoren en concurrentiedreigingen (technologie, nieuwe spelers)
   - klimaat/weer, pandemie, cyberrisico waar relevant
2. **Per blootstelling gericht zoeken** (WebSearch, meerdere talen: NL, EN, FR + lokale taal):
   - *Verleden*: welke gebeurtenissen hadden de laatste ~5 jaar meetbare impact (zie ook de verslagen)?
   - *Nu*: wat speelt er de laatste 3–6 maanden?
   - *Toekomst (2 jaar)*: geplande verkiezingen, deadlines van regelgeving, contracten die aflopen, patentverlies, capaciteit die online komt, geopolitieke spanningen.
3. Per gebeurtenis: wat, wanneer, bron, **richting** (+/−), **grootte** (ruw: klein/middel/groot met reden), label (`feit` of `inschatting`).
4. **Vertaal alles naar impact** (vaste opbouw van de sectie `actualiteit`, zie `rapport-formaat.md`): een **besluit** bovenaan, een **impacttabel** per onderwerp, na elk tijdsblok een **"Wat betekent dit?"** en onderaan **"Waar moet je op letten?"** met data. Een lijst nieuwsfeiten zonder gevolg voor het bedrijf is niet genoeg.
5. **Begin bij de basis**: zoek uitdrukkelijk bij De Tijd/L'Echo en Reuters (`site:tijd.be`, `site:lecho.be`, `site:reuters.com`), en haal macrocijfers (rente, inflatie, wisselkoers) rechtstreeks bij ECB, Fed, Eurostat of Statbel. Vind je iets op een doorgeefsite (rang D), zoek dan het origineel. Daarna zo breed mogelijk: De Tijd, L'Echo, Reuters, FT, Bloomberg, WSJ, AP, Nikkei, vakpers per sector, persberichten van bedrijf, overheden, toezichthouders, centrale banken, IEA/EIA. Bij betaalmuren: zoek dezelfde info bij een andere bron.
6. Registreer elke gelezen bron: `python3 tools/bronnen.py voegtoe …` (met samenvatting van 1–3 zinnen).

### Fase 7 — Earnings call
Laatste call (transcript, webcast-samenvatting of presentatie + Q&A-verslag in pers). Vat samen: kernboodschap, guidance, moeilijke vragen en hoe management antwoordde. Geef een `mening` over toon en zelfzekerheid (ontwijkend? consistent met vorige call?). De gebruiker oordeelt zelf.

### Fase 8 — Waardering & advies
- **Intrinsieke waarde**: eenvoudige DCF (2 fases) met **zichtbare aannames** (groei, marge, disconteringsvoet, eindgroei) + vergelijking met multiples van peers. Holdings: som-der-delen / intrinsieke waarde per aandeel en de **korting/premie**.
- **Scenario's (2 jaar)**: Slecht / Normaal / Goed met koers, kans en uitleg.
- **Koopzone** (prijs waarbij risico/rendement aantrekkelijk is), **koersdoel** (= normaal scenario), **stop-loss**.
- **Oordeel**: Kopen / Houden / Verkopen / Afwachten (of Onvoldoende info) + **score 1–10**. De score komt **altijd** uit `advies.score_opbouw` (zie `rapport-formaat.md`): punten op 10 per vast onderdeel × gewicht, plus correcties voor geraakte harde regels. De tool rekent na dat de score klopt. Toets aan het profiel (defensief? herinvestering? hype? R1–R6?).
- **Verkoopsignalen**: 2–5 concrete, controleerbare signalen die betekenen dat de reden om te kopen niet meer klopt (helpt tegen "te lang vasthouden").

### Fase 9 — Kritische expertblik
Schrijf als een ervaren, sceptische investeerder:
- **Pre-mortem**: "Stel dat dit aandeel over 2 jaar 50% lager staat. Wat is de meest waarschijnlijke reden?"
- Wat ziet de markt mogelijk over het hoofd (positief en negatief)?
- Waar ben je zelf het minst zeker van?
Alles als `mening` of `inschatting`.

### Fase 10 — Fact-check (verplicht, apart van het schrijven)
Loop **elk** `feit` in je concept na:
1. Leg het feit naast het **citaat in het feitenlog**: juiste getal, eenheid, periode, valuta? Geen citaat → heropen de bron en vul het log aan, of schrap het feit.
2. Belangrijke cijfers (omzet, winst, schuld, aandeelhouders %, rechtszaken): bevestigen met een **tweede bron** waar mogelijk. Tegenstrijdig → vermelden.
3. Is de bron recent genoeg? Is er een nieuwer cijfer?
4. Klopt elke `berekening` (herreken)?
5. Is niets uit een forum of uit je geheugen zonder bron?
6. Steunt een feit enkel op een bron van rang D? Zoek het origineel, of maak er een `inschatting` van, of schrap het.
Noteer in het werkdossier welke feiten gecontroleerd zijn. Daarna: `python3 tools/rapport.py controleer <rapport.json>` — alle fouten oplossen en elke waarschuwing over zwakke bronnen of de dekkingslijst wegwerken (of de reden noteren in het werkdossier). Dit is jouw eigen controle; de onafhankelijke controle volgt in fase 11.

### Fase 11 — Teamreview (minstens 2 rondes)
Schrijf eerst een volledig concept-`rapport.json` dat door `tools/rapport.py controleer` geraakt (de `review`-sectie mag nog op `"status": "bezig"` staan). Commit + push.

**Ronde 1 — onafhankelijke review.** Start de drie reviewers **parallel** met de Agent-tool (`subagent_type`: `financieel-analist`, `actua-specialist`, `kritische-belegger`). Geef elk: het pad naar de rapportmap, de ticker, en de vraag om hun volledige review terug te geven. Ze wijzigen zelf niets.

**Verwerken.** Maak/werk `review.md` in de rapportmap bij (sjabloon: `templates/review.md`): per opmerking ID, ernst, samenvatting, en wat je ermee deed — `verwerkt` (wat aangepast) of `verworpen` (met reden). Kritieke opmerkingen mag je enkel verwerpen met bewijs. Doe extra onderzoek waar de reviewers gaten vonden (nieuwe bronnen → `tools/bronnen.py voegtoe`). Pas `rapport.json` aan. Commit + push.

**Ronde 2 — samen opnieuw kritisch bekijken.** Start de drie reviewers opnieuw, nu met de opdracht: (a) controleer of jouw vorige opmerkingen correct verwerkt zijn, (b) lees `review.md` met de opmerkingen van de **andere** reviewers en reageer waar je het oneens bent of iets wil toevoegen, (c) beoordeel **wat veranderd is** sinds ronde 1 (geef hen `git diff <commit ronde 1> -- <rapport.json>` mee) en of het advies nog klopt. Ze herlezen dus niet het hele rapport en controleren geen feiten opnieuw die in ronde 1 juist waren. Verwerk opnieuw.

**Ronde 3** (enkel als er na ronde 2 nog `kritiek`-opmerkingen of een `niet goedgekeurd` is). Na ronde 3 stop je: overblijvende meningsverschillen komen als **open punten** in het rapport, zodat de gebruiker ze ziet.

Vul daarna de `review`-sectie in `rapport.json` in (zie `rapport-formaat.md`) met `"status": "afgerond"`. Het rapport toont zo een korte "Teamreview"-kaart: hoeveel feiten gecontroleerd, opmerkingen verwerkt/verworpen, en open punten of meningsverschillen.

### Fase 12 — Rapport bouwen
1. Controleer: **samenvatting = 1 scherm** (4–7 blokken, belangrijkste eerst).
2. `python3 tools/rapport.py bouw <rapport.json> --pdf`.
3. Controleer visueel (Playwright-screenshot op 390 px breed) of grafieken en tabellen leesbaar zijn.

### Fase 13 — Afronding
1. Bronnengeheugen bijgewerkt? (`tools/bronnen.py lijst`) Dekkingslijst volledig? (`python3 tools/dekking.py controleer <werkdossier.md>`)
2. `git add` + commit + push.
3. Werk de app bij volgens `app/APP.md` (nieuw rapport zichtbaar, vragen stellen mogelijk).
4. Stuur de PDF naar de gebruiker met de SendUserFile-tool (zodat hij ze op de gsm kan openen). Geef in de chat: oordeel + score + 3–5 belangrijkste punten + rode vlaggen + open punten uit de teamreview + pad naar het rapport. Kort, gsm-vriendelijk.
5. Vraag feedback (of laat de gebruiker die in de app geven): score 1–10, wat moet extra onderzocht worden, wat was nutteloos. Noteer in `profiel/feedback.md`. Leid je er een profielwijziging uit af → zet een voorstel in `profiel/voorstellen.md` en vraag akkoord. Wijzig `PROFIEL.md` **nooit** zonder akkoord.
6. De gebruiker kan daarna vragen stellen over het rapport: antwoord op basis van `rapport.json`, `werkdossier.md` en `review.md`, en zoek extra info als dat nodig is (met bron).

## Update van een bestaand rapport
Er zijn twee soorten. Kies in fase 0 en zeg de gebruiker in één regel welke je doet en waarom.

### Volledige update
Zelfde fases (ook de teamreview), maar: start van het vorige werkdossier en `bronnen.json`, lees enkel nieuwe/gewijzigde bronnen, en vul de sectie **"Wat is er veranderd"** grondig in (cijfers, advies, score, rode vlaggen, actualiteit).

### Snelle update (`meta.soort: "snelle_update"`)
Bedoeld voor "is er iets veranderd?" kort na een volledig rapport. **Enkel toegelaten als alles hieronder waar is**; zodra één punt niet klopt, schakel je over op een volledige update en zeg je dat:
- het laatste **volledige** rapport is hoogstens 90 dagen oud (`meta.basis_rapport` = datum daarvan);
- er is sindsdien **geen** nieuw jaar-, halfjaar- of kwartaalverslag en geen nieuwe earnings call;
- er is geen nieuwe of verzwaarde rode vlag en de aandeelhoudersstructuur (R1) is niet gewijzigd;
- het oordeel blijft gelijk en de score verschuift hoogstens 1 punt.

Wat je doet:
1. Fase 0 en 1 (koers, techniek, korting/waardering herberekenen met de nieuwe koers).
2. Dekkingslijst `--snel`: persberichten van het bedrijf, meldingen bij de toezichthouder (R1, R5), corporate actions (R6), basisnieuws (De Tijd/L'Echo, Reuters), macro rechtstreeks bij de bron.
3. Neem het vorige `rapport.json` over en pas enkel aan wat veranderd is: koers en afgeleide cijfers, sectie `actualiteit`, `wijzigingen` (eerste blok = kernboodschap), en waar nodig scenario's en score. De rest blijft ongewijzigd staan.
4. Eigen fact-check van de **nieuwe** feiten (fase 10) en **één reviewronde met één reviewer**: de actua-specialist als het nieuws de aanleiding is, anders de financieel analist. Die controleert enkel de wijzigingen.
5. Bouwen, app bijwerken, afronden zoals fase 12–13.
Het rapport toont bovenaan "Snelle update" en in de kwaliteitscontrole dat enkel de wijzigingen nagekeken zijn.
