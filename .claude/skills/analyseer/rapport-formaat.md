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
```

### Grafiekregels
- Eén y-as. Twee grootheden met een andere schaal (bv. omzet en marge %) → **twee grafieken**.
- Max 3 reeksen per grafiek.
- Koersgrafiek: neem `grafiek_blok` uit `data/<TICKER>/koers.json` over.

## Opmaak in tekst
- `**vet**`
- `[[term|korte uitleg]]` → term met uitleg tussen haakjes (voor de beginnende belegger).
- Bronverwijzingen komen uit het veld `bronnen`, niet in de tekst zelf.

## Wat de controle afdwingt
Feit zonder bron · onbestaande bron-id · forum als bron · ontbrekende verplichte secties · scenario's niet Slecht/Normaal/Goed · score buiten 1–10 · R1 geraakt zonder rode vlag `R1` · aandeelhoudersverdeling ontbreekt · "onvoldoende info" met minder dan 3 zoekrondes · grafiek/tabel met verkeerd aantal waarden.
