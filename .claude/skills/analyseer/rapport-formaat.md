# Formaat van `rapport.json`

Controle: `python3 tools/rapport.py controleer <pad>` · Bouwen: `python3 tools/rapport.py bouw <pad> --pdf`.
Volledig werkend voorbeeld (fictieve data): `voorbeelden/demo/rapport.json`.

## Hoofdstructuur
```jsonc
{
  "meta": {
    "ticker": "SOF.BR", "naam": "Sofina", "type": "aandeel",   // aandeel | etf | fonds | ipo
    "datum": "2026-11-08", "beurs": "Euronext Brussel", "isin": "BE0003717312",
    "valuta": "EUR", "sector": "Investeringsholding", "defensief": false,
    "vorig_rapport": "2026-05-02",         // optioneel
    "soort": "volledig",                   // volledig (standaard) | snelle_update (zie SKILL.md; dan ook:) | terugkijk
    "basis_rapport": "2026-05-02"          // datum van het laatste volledige rapport (max 90 dagen oud)
    // terugkijktest (zie terugkijk.md): "soort": "terugkijk", "peildatum": "2021-02-15" — elke bron heeft dan een datum ≤ peildatum
  },
  "advies": {
    "oordeel": "Houden",                    // Kopen | Houden | Verkopen | Afwachten | Onvoldoende info
    "score": 6,                             // 1–10
    "reden": "1–2 zinnen, kort en direct",
    "koers_nu": 267.6, "koers_datum": "06-11-2026",
    "koopzone": {"van": 220, "tot": 240},
    "koersdoel": 300, "koersdoel_uitleg": "normaal scenario, 2 jaar",
    "stop_loss": {"waarde": 214.1, "uitleg": "−20% t.o.v. koers nu; technische steun 238,8"},
    "intrinsieke_waarde": 310,
    "score_opbouw": {                       // verplicht: hoe de score tot stand komt
      "uitleg": "1–2 zinnen voor de lezer",
      "onderdelen": [                       // gewichten samen 100; punten 0–10; uitleg verplicht
        {"naam": "Bestuur & aandeelhouders (zonder R1)", "gewicht": 15, "punten": 6, "uitleg": "waarom deze punten"},
        {"naam": "Financiële gezondheid", "gewicht": 20, "punten": 7, "uitleg": "..."}
      ],
      "correcties": [                       // aftrek voor harde regels (R1 verplicht als R1 geraakt)
        {"naam": "R1 geraakt: familie 52%", "punten": -1, "uitleg": "..."}
      ]
    },
    "scenarios": [                          // precies deze 3, in deze volgorde
      {"naam": "Slecht",  "koers": 190, "kans": "25%", "uitleg": "..."},
      {"naam": "Normaal", "koers": 300, "kans": "55%", "uitleg": "..."},
      {"naam": "Goed",    "koers": 360, "kans": "20%", "uitleg": "..."}
    ]
  },
  "aandeelhouders": {                       // verplicht voor aandeel/ipo (regel R1)
    "verdeling": [
      {"naam": "Familie X", "pct": 52.1, "stemrecht_pct": 55.0, "structuur": "via X Holding SA"},
      {"naam": "Eigen aandelen", "pct": 3.0, "eigen_aandelen": true},
      {"naam": "Vrij verhandelbaar", "pct": 44.9, "vrij_verhandelbaar": true}
    ],
    "bronnen": [1], "uitleg": "Hoe de controle in elkaar zit."
  },
  "keten_schema": {                         // aandeel/ipo: schema bovenaan het hoofdstuk 'keten' (ETF: grootste posities/landen)
    "centrum": "Sofina",
    "takken": [                             // niveau 1: 4–8 takken, belangrijkste eerst
      {"naam": "ByteDance", "gewicht": "5–10%", "toelichting": "grootste positie",
       "onder": [{"naam": "TikTok VS", "toelichting": "joint venture sinds 1-2026"}]}   // niveau 2: max 5
    ]
  },                                        // enkel korte samenvatting van wat in de sectie met bron staat: geen nieuwe feiten
  "rode_vlaggen": [
    {"ernst": "nogo", "regel": "R1", "titel": "...", "uitleg": [ <blokken> ]}
    // ernst: nogo | hoog | middel | info ; regel: R1..R6 of weglaten
  ],
  "samenvatting": [ <blokken> ],           // past op 1 gsm-scherm: 4–7 blokken
  "verkoopsignalen": ["controleerbaar signaal 1", "..."],
  "wijzigingen": [ <blokken> ],            // t.o.v. vorig rapport (optioneel bij eerste rapport)
  "onvoldoende_info": [                    // optioneel
    {"onderwerp": "...", "wat_wel": "...", "zoekrondes": ["ronde 1: ...", "ronde 2: ...", "ronde 3: ..."]}
  ],
  "secties": [
    {"id": "bestuur", "titel": "Bestuur & aandeelhouders", "kort": "1 regel zichtbaar als ingeklapt", "inhoud": [ <blokken> ]}
  ],
  "review": {                               // fase 11 — verplicht voor een definitief rapport
    "status": "afgerond",                   // bezig | afgerond
    "feiten_gecontroleerd": 42, "feiten_correct": 39,
    "rondes": [
      {"nr": 1, "oordelen": {"financieel-analist": "goedgekeurd met opmerkingen",
                             "actua-specialist": "niet goedgekeurd",
                             "kritische-belegger": "goedgekeurd met opmerkingen"},
       "opmerkingen": 14, "verwerkt": 12, "verworpen": 2},
      {"nr": 2, "oordelen": {"financieel-analist": "goedgekeurd", "actua-specialist": "goedgekeurd",
                             "kritische-belegger": "goedgekeurd met opmerkingen"},
       "opmerkingen": 3, "verwerkt": 2, "verworpen": 1}
    ],
    "open_punten": ["Meningsverschil: kritische belegger zou score 5 geven omdat ..."]
  },
  "bronnen": [
    {"id": 1, "titel": "Jaarverslag 2025", "uitgever": "Sofina", "type": "primair",
     "url": "https://...", "document": "Jaarverslag 2025, p. 34", "datum": "2026-03-27"}
    // type: primair | nieuws | data | analyse | overig   (nooit 'forum')
  ]
}
```

### Waardering: vaste onderdelen (W1–W3, W5)
In de sectie `waardering`: (1) verhoudingen t.o.v. peers op **hetzelfde jaar**, (2) een tabel met de waarde als bereik, inclusief een rij **"Stresstest rente"** (vereist rendement bij de gemiddelde 10-jaarsrente van de voorbije 10–20 jaar), (3) de break-even-aanname die de koers verklaart, (4) bij kapitaalintensieve groeibedrijven een `kop` **"Staartscenario (5 jaar)"** met een korte tekst (label `inschatting`, geen kans, geen koers), (5) koopzone, koersdoel en stop-loss met uitleg.

### Verplichte sectie-id's
- **aandeel**: `bestuur, cijfers, investeringen, keten, sector, actualiteit, earnings_call, waardering, techniek, expert, profiel`
- **ipo**: `bestuur, cijfers, investeringen, keten, sector, actualiteit, waardering, expert, profiel`
- **etf**: `samenstelling, kosten, index, risico, actualiteit, techniek, fiscaliteit, expert, profiel`
- **fonds**: `samenstelling, kosten, beheer, risico, actualiteit, fiscaliteit, expert, profiel`

Is er voor een sectie echt niets? Zet ze er toch in met één blok dat uitlegt waarom (bv. geen earnings call voor dit bedrijf).

## Blokken
Elk tekstelement heeft een **label**: `feit` (bronnen verplicht), `berekening`, `inschatting`, `mening`.

```jsonc
{"type": "tekst", "label": "feit", "tekst": "Omzet steeg 4,1% tot **€1,2 mld**.", "bronnen": [1]}

{"type": "lijst", "titel": "optioneel", "items": [
  {"label": "feit", "tekst": "...", "bronnen": [2]},
  {"label": "inschatting", "tekst": "..."}]}

{"type": "kerncijfers", "items": [
  {"naam": "Omzet 2025", "waarde": "€1,2 mld", "trend": "op", "label": "feit", "toelichting": "+4,1%", "bronnen": [1],
   "wat": "Alles wat het bedrijf in 2025 verkocht, vóór kosten.",          // knop "Uitleg": wat is dit cijfer? (altijd invullen)
   "hoe": "Verkochte volumes × prijs, alle segmenten opgeteld.",           // optioneel: hoe berekend (verplicht bij label berekening)
   "beoordeling": "goed",                                                  // optioneel: goed | normaal | zwak (is een mening)
   "beoordeling_uitleg": "Groeit sneller dan de sector (+2,5%)."}]}        // verplicht als er een beoordeling is; verwijs naar feiten uit het rapport
  // trend: op | neer | gelijk

{"type": "tabel", "titel": "...", "kolommen": ["(mln EUR)", "2024", "2025"],
 "rijen": [["Omzet", 1153, 1200]], "bronnen": [1], "noot": "optioneel"}

{"type": "grafiek", "soort": "staaf",       // staaf (per jaar/kwartaal) | lijn (tijdreeks)
 "titel": "Omzet en nettowinst (mln EUR)", "eenheid": "mln EUR",
 "x": ["2021","2022","2023","2024","2025"],
 "reeksen": [{"naam": "Omzet", "waarden": [1010,1060,1105,1153,1200]}],   // max 3 reeksen, null = ontbrekend
 "lijnen": [{"naam": "Stop-loss −20%", "waarde": 214.1}],                  // optioneel, horizontale referentie
 "bronnen": [1]}                                                           // of "bron_tekst": "..."

{"type": "kader", "stijl": "info", "titel": "optioneel", "tekst": "..."}  // stijl: info | waarschuwing | mening

{"type": "kop", "tekst": "Tussentitel"}                                   // structuur binnen een sectie

{"type": "uitleg", "tekst": "Inleiding of overgangszin in gewone taal."}  // GEEN label en GEEN nieuwe feiten/cijfers: enkel uitleg, structuur en "wat zie je hier?"
```

### Structuur binnen een sectie (vaste opbouw)
1. **Inleiding** — 2–3 gewone zinnen: waarover gaat dit deel en waarom is het belangrijk voor de beslissing? Daarna de **kern**: de conclusie (wat moet de lezer onthouden?).
2. **Tussentitels** (`kop`) per deelonderwerp, bv. in `cijfers`: *Omzet & groei*, *Winstgevendheid*, *Kasstroom*, *Schulden*, *Aandeelhouders­vergoeding*; in `actualiteit`: *Verleden*, *Nu*, *Komende 2 jaar*; in `keten`: één tussentitel per niveau-1-partij.
3. **Onder elke tussentitel eerst een overgangszin** (wat volgt en hoe het samenhangt met het vorige), dan kerncijfers/grafiek/tabel, dan de uitleg.
4. **Na elke tabel of grafiek** één zin: wat zie je hier en wat betekent het?
5. **Nooit twee feiten-, tabel- of lijstblokken direct na elkaar** zonder verbindende uitleg.
6. **Volledige zinnen**, geen opsommingen met puntkomma's of afkortingen. Kort mag in de samenvatting, niet in de uitleg.

### Rode vlaggen (vaste opbouw)
Elke rode vlag heeft in `uitleg` deze volgorde, telkens als apart blok met een vetgedrukte aanloop:
1. **Wat is er aan de hand?** — 1–2 gewone zinnen, zonder cijferdetail.
2. **Waarom is dat een probleem voor jou?** — het gevolg voor een kleine belegger.
3. **Hoe erg is het?** — ernst en welke regel van het profiel (R1–R6).
4. **De details** — cijfers, data en bronnen.
Een `info`-vlag mag korter, maar begint altijd met stap 1.
Elke sectie heeft een `kort`-regel (verschijnt in de inhoudstafel en als ingeklapt).

### Beeld vóór tekst
- **Elke reeks van 3 of meer cijfers over tijd of over vergelijkbare partijen** (5-jaarcijfers, concurrenten, verdeling van omzet/portefeuille) krijgt ook een grafiek, niet enkel een tabel. Richtgetal: minstens één grafiek in `cijfers`, `investeringen`, `sector` en `techniek`.
- De **aandeelhoudersbalk** (met de 49%-grens) maakt het sjabloon zelf uit `aandeelhouders.verdeling`.
- Het **ketenschema** komt uit `keten_schema`.

### Grafiekregels
- Eén y-as. Twee grootheden met een andere schaal (bv. omzet en marge %) → **twee grafieken**.
- Max 3 reeksen per grafiek.
- Koersgrafiek: neem `grafiek_blok` uit `data/<TICKER>/koers.json` over.

## Opmaak in tekst
- `**vet**`
- `*cursief*` → kleine grijze regel (bv. "*Controle: halfjaarverslag.*" onder een verkoopsignaal).
- `[[term|korte uitleg]]` → de term wordt een **knop**: onderlijnd, en de uitleg verschijnt pas als de lezer erop tikt (in de PDF staat de uitleg tussen haakjes). Schrijf de zin dus zo dat hij ook zonder de uitleg vlot leest, en hou de uitleg kort (geen zin met een punt).
- Bronverwijzingen komen uit het veld `bronnen`, niet in de tekst zelf.

## Sectie `actualiteit` (vaste opbouw)
1. `uitleg`: waarover gaat dit deel.
2. `kader` (stijl `mening`) met titel **"Besluit: wat betekent de actualiteit voor <bedrijf>?"** — de 2–3 belangrijkste drijvers als genummerde regels (nieuwe regel met `\n`), daarna de positieve tegenwichten, het netto-effect en altijd **het gevolg voor het advies** (oordeel + score).
3. `kop` "Impact per onderwerp" + `uitleg` met de schaal (klein <1% / middel 1–3% / groot >3% van de waarde of winst) + een **`lijst`** (geen brede tabel: onleesbaar op gsm) met per onderwerp één item, label `inschatting`, in de vorm `**Onderwerp — ▲/▼/▼▲ grootte (cijfer).** Waarom, met cijfers uit het rapport.` Daarna één `mening`-zin "Wat zie je hier?" met het netto-effect.
4. Tijdlijn: `kop` + lijst voor *Wat gebeurde er?*, *Wat speelt er nu?*, *Wat komt eraan?*, elk afgesloten met een `tekst` (label `mening`) **"Wat betekent dit?"**.
5. `kop` "Waar moet je op letten?" + lijst met concrete data en wat goed/slecht nieuws zou zijn. Begin elk punt met `**<d-m-jjjj> — <wat>.**` (bv. `**Rond 19-11-2026 — Anthropic op de beurs.**`): de app toont deze lijst onder "Opvolgen" en de eerstvolgende datum op de startpagina.

## Wat klapt open? (doet het sjabloon automatisch)
Het rapport toont eerst het korte antwoord; alles daaronder klapt open bij een tik. Schrijf de inhoud daarop:
- **Hoofdstuk**: de blokken **vóór de eerste `kop`** (inleiding + kern) blijven altijd zichtbaar; elke `kop` wordt een uitklapbaar onderdeel met alle blokken tot de volgende `kop`. → De kern moet dus vóór de eerste `kop` staan, en een tussentitel moet zeggen wat eronder zit.
- **Rode vlag** (`nogo`/`hoog`/`middel`): stap 1–3 zichtbaar; alles vanaf het blok dat begint met **"De details"** zit onder een uitklapper. Vlaggen met ernst `info` staan apart onder "Nagekeken, geen alarm", dichtgeklapt.
- **Wat is er veranderd**: het **eerste blok** (kernboodschap) is zichtbaar, de rest zit onder "Alle wijzigingen in detail".
- **Kerncijfers**: elk vakje met `wat`/`hoe`/`beoordeling_uitleg` krijgt een knop "Uitleg".
- **Advies**: prijzen staan op één prijsbalk (stop-loss, koopzone, koers nu, koersdoel, intrinsieke waarde, drie scenario's) met per prijs een uitklapbare uitleg; `stop_loss.uitleg` en `koersdoel_uitleg` verschijnen daar. De uitleg van elk scenario zit onder "Waarom?". De scoreopbouw is dichtgeklapt.
- Woordenlijst en bronnen zijn dichtgeklapt. In de PDF staat alles open.

## Opbouw van het rapport (vast, in het sjabloon)
Het sjabloon zet de delen altijd in deze volgorde, elk met een korte inleiding waarover het gaat:
0. **Het oordeel** (oordeel, score, `advies.reden`, rode vlaggen als label) — altijd helemaal bovenaan; daaronder de dichtgeklapte leeswijzer **Hoe lees je dit rapport?**.
1. **Samenvatting** — wat is dit bedrijf en wat vinden we ervan (1 scherm).
2. **Wat is er veranderd** — enkel bij een update; begint met de kernboodschap (advies gewijzigd of niet, en waarom).
3. **Het advies in cijfers** — prijsbalk en belangrijke prijzen (koopzone, koersdoel, stop-loss), drie scenario's ("Wat kan de koers over twee jaar doen?"), verkoopsignalen en de scoreopbouw.
4. **Rode vlaggen** — wat botst met de harde regels.
5. **Details per thema** — inhoudstafel + uitklapbare secties.
6. **Achteraan** — woordenlijst, kwaliteitscontrole (teamreview) en bronnen.
Schrijf de inhoud zo dat elk deel op zichzelf leesbaar is: een update wordt vaak los gelezen, dus leg termen ook daar uit.

## Scoreopbouw (verplicht)
`advies.score` = afronding (half naar boven) van **gewogen gemiddelde van de onderdelen + correcties**, begrensd op 1–10. `tools/rapport.py controleer` rekent dit na en geeft een fout als het niet klopt.

**Vaste onderdelen** (zelfde namen en gewichten in elk rapport, zodat rapporten vergelijkbaar zijn):

| Type | Onderdelen (gewicht) |
|---|---|
| aandeel / ipo | Bestuur & aandeelhouders (zonder R1) 15 · Financiële gezondheid 20 · Groei & herinvestering 15 · Waardering (prijs nu) 20 · Risico's & actualiteit 15 · Past bij jouw profiel 15 |
| etf / fonds | Kosten 20 · Samenstelling & spreiding 20 · Index/beheer & spoorvolging 15 · Waardering (prijs nu) 15 · Risico's & actualiteit 15 · Past bij jouw profiel 15 |

**Correcties**: R1 geraakt → minstens **−1** (en oordeel normaal "niet kopen"); andere rode vlaggen met ernst `hoog` → −0,5 tot −1, met uitleg. Positieve correcties enkel uitzonderlijk en met reden.
Per onderdeel: punten zijn een `mening`, maar de uitleg verwijst naar de feiten in de secties. De scoreopbouw verschijnt automatisch onder het advies.

## Wat de controle afdwingt
**Fouten** — Dekkingslijst in het werkdossier onvolledig (⬜ of notitie ontbreekt) · snelle update zonder vorig rapport, ouder dan 90 dagen of zonder `wijzigingen` · snelle update: minstens 1 reviewer in 1 ronde · kerncijfer met ongeldige `beoordeling` of zonder `beoordeling_uitleg`.
**Waarschuwingen (wegwerken of reden noteren)** — bron van rang D · feit dat enkel op een D-bron steunt · geen enkele bron van De Tijd/L'Echo/Reuters · kerncijfer zonder `wat` · werkdossier zonder dekkingslijst.
Verder: Scoreopbouw aanwezig en score klopt met de berekening; R1-correctie als R1 geraakt · Teamreview: ≥ 2 rondes, alle 3 reviewers in de laatste ronde, feiten_gecontroleerd ingevuld, open punten als een reviewer niet goedkeurt (anders enkel `bouw --concept`, met CONCEPT-markering) · Feit zonder bron · onbestaande bron-id · forum als bron · ontbrekende verplichte secties · scenario's niet Slecht/Normaal/Goed · score buiten 1–10 · R1 geraakt zonder rode vlag `R1` · aandeelhoudersverdeling ontbreekt · "onvoldoende info" met minder dan 3 zoekrondes · grafiek/tabel met verkeerd aantal waarden.
