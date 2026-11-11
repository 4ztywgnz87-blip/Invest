# Terugkijktest — werkwijze

Doel: onze **werkwijze** toetsen. We schrijven een volledig rapport **alsof het de peildatum is** (bv. 15-02-2021), en leggen het daarna naast wat er echt gebeurde. Zo zien we wat de methode goed ziet, wat ze mist en waar ze te zeker of te voorzichtig is.

Gebruik: "terugkijktest <ticker> op <datum>". Lees eerst `SKILL.md`; alles daar geldt, met de aanpassingen hieronder.

## Het grote gevaar: kennis van achteraf
Claude weet vaak hoe het afliep. Een terugkijkrapport dat die kennis (ook onbewust) gebruikt, bewijst niets. Daarom:

1. **Twee gescheiden delen, in deze volgorde.**
   - **Deel A — het rapport** (`rapport.json`, `werkdossier.md`, `review.md`): enkel kennis van vóór de peildatum.
   - **Deel B — de evaluatie** (`uitkomst.json`, `evaluatie.md`): pas te beginnen als deel A af is en **gecommit**. Noteer die commit (de "verzegeling") bovenaan de evaluatie. Na de verzegeling wordt deel A niet meer aangepast; fouten die je later ziet, gaan in de evaluatie.
2. **Elke bron is van vóór de peildatum.** Elke bron in `rapport.json` krijgt zijn publicatiedatum; `tools/rapport.py controleer` geeft een fout bij een bron van na de peildatum.
   - Verslagen: het jaar-/kwartaalverslag dat op de peildatum gepubliceerd was (niet een latere versie of een herwerkt cijfer uit een later verslag).
   - Webpagina's die sindsdien kunnen veranderd zijn (IR-site, aandeelhoudersstructuur, Wikipedia): enkel via een archiefversie van vóór de peildatum (`web.archive.org/web/<JJJJMMDD>/<url>`), met die datum als bron.
   - Nieuws: enkel artikels met een publicatiedatum ≤ peildatum. Zoek met de periode in de zoekterm ("Ørsted januari 2021", "Ørsted 2020 results") en kijk de datum op de pagina na.
   - Koersen: `python3 tools/koers.py analyse <TICKER> --tot <peildatum>` (schrijft `data/<TICKER>/koers_<peildatum>.json`). Vermeld de bron als "… afgekapt op peildatum …".
   - Macro (rente, inflatie, wisselkoers): de waarde zoals die op de peildatum bekend was.
3. **Elk argument heeft een toen-bron.** Een risico, kans of scenario mag enkel in het rapport als een bron van vóór de peildatum het (of de bouwstenen ervan) vermeldt. "Ik weet dat dit later gebeurde" is geen reden. Bij twijfel: weglaten, of noteren in de evaluatie.
4. **Gewicht zoals toen.** Geef een risico niet meer nadruk dan de bronnen van toen rechtvaardigen. De kritische belegger toetst dat (zie teamreview).
5. **Werkdossier zonder toekomst.** Schrijf in deel A nergens wat er na de peildatum gebeurde, ook niet als notitie.
6. **Eerlijk over de grens.** Volledig blind zijn is onmogelijk. De evaluatie bevat daarom een **besmettingscheck**: per belangrijk punt in het rapport, hoe zeker zijn we dat het ook zonder kennis van achteraf zou gevonden zijn?

## Aanpassingen aan de fases (deel A)
- **Map**: `terugkijk/<TICKER>/<peildatum>/` (niet in `rapporten/`: dit is geen advies voor vandaag en hoort niet in de app tussen de echte rapporten).
- **meta**: `"soort": "terugkijk"`, `"peildatum": "JJJJ-MM-DD"`, `"datum"`: de dag waarop je het schrijft. `advies.koers_datum` = laatste beursdag ≤ peildatum.
- **Peildatum kiezen**: kort (± 1–2 weken) na een jaar- of halfjaarpublicatie, zodat er verse cijfers zijn.
- **Fase 0**: geen app-feedback per ticker en geen bronnengeheugen van latere rapporten gebruiken (dat kan latere kennis bevatten). Dekkingslijst zoals gewoonlijk; ➖ mag met "niet beschikbaar in archief" als je 3 zoekrondes deed.
- **Fase 6 (actualiteit)**: "nu" = de 3–6 maanden vóór de peildatum; "toekomst" = wat toen gepland of verwacht was (verkiezingen, veilingen, deadlines).
- **Fase 11 (teamreview)**: zeg de reviewers in de opdracht dat het een terugkijktest is met peildatum X, en dat ze **elke bron, elk feit en elk argument van na de peildatum** als `kritiek` melden. De kritische belegger kijkt daarnaast uitdrukkelijk naar **kennis van achteraf**: wordt een risico zwaarder gewogen dan de bronnen van toen toelaten? De reviewers gebruiken zelf ook enkel bronnen van vóór de peildatum.
- **Fase 12–13**: bouwen zoals gewoonlijk (het rapport toont bovenaan "Terugkijktest"). Niet in de app zetten. Commit = verzegeling.

## Deel B — evaluatie
Sjabloon: `templates/evaluatie.md` → `terugkijk/<TICKER>/<peildatum>/evaluatie.md`.

1. **Cijfers van de uitkomst**: `python3 tools/terugkijk.py uitkomst terugkijk/<TICKER>/<peildatum>/rapport.json --index <index>`. Kies als index de thuisbeurs (bv. `^OMXC25`, `^BFX`, `^AEX`) én eventueel een wereld-ETF. Was er een claimemissie of andere actie die de koersreeks breekt? Zoek de officiële correctiefactor en geef ze mee met `--factor` (met bron in de evaluatie).
2. **Wat gebeurde er echt?** Zoek nu (wél met bronnen van na de peildatum, rang A/B) de 5–10 gebeurtenissen die de koers het meest bepaalden, met datum en bron.
3. **Punt per punt naast het rapport leggen**:
   - **Rode vlaggen en risico's**: per gebeurtenis die echt gebeurde — stond het in het rapport? `gezien` (benoemd én juist gewogen) / `half gezien` (benoemd maar te licht gewogen of verkeerd ingeschat) / `gemist`. Bij gemist: **was het toen te vinden?** (zoek een bron van vóór de peildatum). Zo ja → fout van de methode; zo nee → niet te voorzien.
   - **Kansen**: idem voor positieve gebeurtenissen.
   - **Scenario's**: welk scenario kwam uit, en lag de koers na 2 jaar binnen de vork slecht–goed? Waren de kansen redelijk?
   - **Advies, score, koopzone, koersdoel, stop-loss**: wat zou iemand die het rapport volgde gedaan hebben, en met welk resultaat (t.o.v. de index)?
   - **Verkoopsignalen**: werden ze geraakt, wanneer, en zou je daardoor op tijd verkocht hebben? (Dit is de kern voor de gebruiker: helpt het rapport tegen te lang vasthouden?)
   - **Cijfers en vooruitzichten**: welke verwachtingen uit het rapport (groei, marge, schuld, guidance) klopten?
4. **Besmettingscheck** (zie hierboven): per belangrijk punt een eerlijk oordeel.
5. **Lessen voor de werkwijze**: concreet en toetsbaar ("in fase 6 ook X zoeken", "scenario Slecht moet minstens Y", "verkoopsignaal over Z altijd opnemen"). Eén les per vaststelling; geen algemene wijsheden.
6. **Voorstellen**: wijzigingen aan de werkwijze (`SKILL.md`, `rapport-formaat.md`, tools) en het profiel gaan eerst als voorstel naar de gebruiker (`profiel/voorstellen.md`); pas na akkoord doorvoeren.
7. Na meerdere terugkijktests: een **samenvatting over alle tests** in `terugkijk/SAMENVATTING.md` (patronen: wat mist de methode telkens?).
