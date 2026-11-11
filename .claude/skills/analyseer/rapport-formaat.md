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
    "vorig_rapport": "2026-05-02"          // optioneel
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
  {"naam": "Omzet 2025", "waarde": "€1,2 mld", "trend": "op", "label": "feit", "toelichting": "+4,1%", "bronnen": [1]}]}
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

### Grafiekregels
- Eén y-as. Twee grootheden met een andere schaal (bv. omzet en marge %) → **twee grafieken**.
- Max 3 reeksen per grafiek.
- Koersgrafiek: neem `grafiek_blok` uit `data/<TICKER>/koers.json` over.

## Opmaak in tekst
- `**vet**`
- `[[term|korte uitleg]]` → term met uitleg tussen haakjes (voor de beginnende belegger).
- Bronverwijzingen komen uit het veld `bronnen`, niet in de tekst zelf.

## Opbouw van het rapport (vast, in het sjabloon)
Het sjabloon zet de delen altijd in deze volgorde, elk met een korte inleiding waarover het gaat:
0. **Hoe lees je dit rapport?** — leeswijzer met de opbouw en de vier labels.
1. **Samenvatting** — wat is dit bedrijf en wat vinden we ervan (1 scherm).
2. **Wat is er veranderd** — enkel bij een update; begint met de kernboodschap (advies gewijzigd of niet, en waarom).
3. **Het advies in cijfers** — oordeel + reden, belangrijke prijzen (koopzone, koersdoel, stop-loss), drie scenario's ("Wat kan de koers over twee jaar doen?"), verkoopsignalen en de scoreopbouw.
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
Scoreopbouw aanwezig en score klopt met de berekening; R1-correctie als R1 geraakt · Teamreview: ≥ 2 rondes, alle 3 reviewers in de laatste ronde, feiten_gecontroleerd ingevuld, open punten als een reviewer niet goedkeurt (anders enkel `bouw --concept`, met CONCEPT-markering) · Feit zonder bron · onbestaande bron-id · forum als bron · ontbrekende verplichte secties · scenario's niet Slecht/Normaal/Goed · score buiten 1–10 · R1 geraakt zonder rode vlag `R1` · aandeelhoudersverdeling ontbreekt · "onvoldoende info" met minder dan 3 zoekrondes · grafiek/tabel met verkeerd aantal waarden.
