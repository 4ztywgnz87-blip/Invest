# Invest — Plan & Vragenlijst

> Status: **Fase 0 – Intake**. Dit document is het startpunt. Beantwoord de vragen in sectie 3 (mag kort, mag in het Nederlands, mag "weet ik niet / kies jij"). Op basis van jouw antwoorden werk ik sectie 1, 2 en 4 uit tot een definitief plan.

---

## 1. Visie (eerste versie)

Een persoonlijke onderzoeksassistent voor beleggen. Je typt een **ticker** (bv. `ASML`, `MSFT`, `UCB.BR`) en de app:

1. **Identificeert** het bedrijf eenduidig (ticker + beurs + ISIN).
2. **Verzamelt** financiële data: jaar- en kwartaalverslagen, omzet, winst, marges, kasstromen, schulden, capex (waarin investeren ze?), segmenten, dividend, inkoop eigen aandelen, waardering.
3. **Volgt de keten**: leveranciers, klanten, partners, deelnemingen en grote investeringen (bv. bedrijf koopt veel GPU's → analyseer ook NVIDIA), en concurrenten.
4. **Koppelt actualiteit**: geopolitiek (oorlogen, Straat van Hormuz, sancties), macro (rente, inflatie, olieprijs, grondstoffen), politiek (verkiezingen, tarieven, regelgeving), sectornieuws — verleden, heden én mogelijke toekomstige impact.
5. **Analyseert de sector**: trends, cycli, concurrentiepositie, marktaandeel.
6. **Schrijft een rapport** met een duidelijke conclusie (kopen / houden / verkopen / afwachten), onderbouwing, risico's, scenario's en bronnen.
7. **Kent jou**: weegt de analyse volgens jouw voorkeuren, stijl en risicoprofiel, en leert bij uit je feedback.
8. **Volgt op**: houdt je portefeuille/watchlist in de gaten en waarschuwt wanneer iets verandert dat een verkoop- of koopmoment kan zijn.

## 2. Voorlopige bouwstenen (modules)

| # | Module | Doel | Afgewerkt wanneer… |
|---|--------|------|---------------------|
| M1 | Ticker-zoeker | Aandeel opzoeken, eenduidig bedrijf kiezen | Elk gangbaar aandeel (VS, EU, …) wordt correct gevonden |
| M2 | Financiële data | Cijfers uit verslagen/API's ophalen en normaliseren | 10 jaar + laatste kwartalen, kerncijfers + ratio's correct |
| M3 | Verslag-lezer | Jaar-/kwartaalverslagen (PDF/10-K/10-Q) lezen en samenvatten, capex & strategie eruit halen | Samenvatting met verwijzing naar pagina/sectie |
| M4 | Relatie-graaf | Leveranciers, klanten, deelnemingen, concurrenten in kaart + recursief analyseren | Graaf tot diepte N, met korte analyse per knoop |
| M5 | Nieuws & actualiteit | Relevant nieuws + macro/geopolitiek verzamelen en impact inschatten | Gefilterd, gedateerd, met bron en impact-inschatting |
| M6 | Sectoranalyse | Sector-trends, peers vergelijken | Peer-tabel + sectorbeeld |
| M7 | Persoonlijk profiel | Jouw voorkeuren, regels, risico; leert uit feedback | Rapport past aantoonbaar aan op profiel |
| M8 | Rapportgenerator | Alles samenbrengen tot advies | Leesbaar rapport met score, advies, bronnen |
| M9 | Portefeuille & alerts | Posities/watchlist volgen, signalen geven | Meldingen bij relevante gebeurtenissen |
| M10 | Interface | Web/mobiel/desktop | Volgens antwoorden op sectie 3 |

Volgorde (voorstel): M1 → M2 → M8 (eenvoudig rapport) → M7 → M3 → M5 → M6 → M4 → M9. Zo heb je snel iets bruikbaars en wordt het daarna dieper.

---

## 3. Vragen

### A. Over jou (persoonlijk profiel)
1. Hoe lang belegt je al, en hoe zou je je ervaring omschrijven (beginner / gevorderd / expert)?
2. Wat is je beroep of achtergrond? (Helpt om in te schatten hoeveel uitleg / jargon je wil.)
3. In welk land woon je / ben je fiscaal inwoner? (België? → beurstaks, roerende voorheffing, meerwaardebelasting zijn relevant.)
4. Bij welke broker(s) beleg je? (Bolero, Saxo, DEGIRO, Keytrade, IBKR, …)
5. Wat is je beleggingsdoel? (vermogensopbouw, pensioen, passief inkomen/dividend, korte-termijn winst, …)
6. Wat is je typische beleggingshorizon per aandeel? (weken / maanden / jaren / "voor altijd")
7. Hoe ga je om met verlies? Bij welke daling verkoop je of koop je bij?
8. Grootteorde van je portefeuille en aantal posities? (Mag een range zijn, of overslaan.)
9. Hoeveel uur per week steek je nu in onderzoek? Hoeveel wil je er nog in steken met de app?
10. Welke beleggers, boeken, podcasts of websites inspireren jou? (bv. Buffett, Lynch, Fisher, Seeking Alpha, …)
11. Wat was je beste en je slechtste belegging, en waarom liep die zo?
12. Welke fouten maak je volgens jezelf het vaakst? (te vroeg verkopen, FOMO, te lang vasthouden, …) — de app kan je daarop wijzen.

### B. Beleggingsstijl & voorkeuren
13. Welke stijl past het best: value, growth, quality, dividend, momentum, turnaround, speculatief, mix?
14. Welke kerncijfers vind je het belangrijkst? (bv. omzetgroei, vrije kasstroom, ROIC, marges, schuldgraad, P/E, EV/EBITDA, PEG, dividendrendement, …)
15. Welke kenmerken vind je **positief** (bv. founder-led, eigen aandelen inkopen, netto kaspositie, monopolie/moat, recurring revenue)?
16. Welke zaken zijn voor jou **rode vlaggen** of absolute no-go's (bv. hoge schuld, verwatering, verlieslatend, bepaalde landen)?
17. Zijn er sectoren of thema's die je **uitsluit** (wapens, tabak, fossiel, gokken, …) of juist **zoekt** (AI, halfgeleiders, defensie, energie, gezondheid, …)?
18. Welke markten/beurzen? (VS, Euronext Brussel, rest van Europa, Azië, opkomende markten)
19. Welke bedrijfsgrootte? (megacap, midcap, smallcap, microcap)
20. Alleen aandelen, of ook ETF's, obligaties, crypto, grondstoffen, opties?
21. Hoe belangrijk is waardering voor jou: "goed bedrijf tegen elke prijs" of "alleen bij korting"?
22. Gebruik je technische analyse (grafieken, steunniveaus, RSI, …)? Moet de app dat meenemen?
23. Hoe belangrijk is ESG/duurzaamheid voor je?
24. Wat moet er gebeuren voor jij een aandeel **verkoopt**? (koersdoel bereikt, these gebroken, betere kans, stop-loss, …)

### C. Rapport & advies
25. Hoe moet het eindadvies eruitzien? (alleen kopen/verkopen, of score 1–10, of koopzone/koersdoel, of scenario's bull/base/bear)
26. Hoe lang mag een rapport zijn? Eerst een samenvatting van 1 scherm en daarna inklapbare details?
27. Wil je grafieken (omzet/winst over tijd, marges, koers, peers)?
28. Wil je bij elk cijfer/feit de **bron** zien (link naar verslag, pagina)?
29. Hoe diep moet de "keten" gaan? (bv. bedrijf → NVIDIA → TSMC → ASML …) Maximaal 1, 2 of 3 niveaus? Of laat je dat per keer kiezen?
30. Hoe ver terug moet de analyse kijken? (5 jaar, 10 jaar, maximaal)
31. Wil je een vergelijking met concurrenten/peers in elk rapport?
32. Wil je dat de app een **intrinsieke waarde** schat (DCF, multiples)? Met welke aannames?
33. Moet het rapport exporteerbaar zijn (PDF, Word, Notion, e-mail)?
34. Wil je rapporten bewaren en later vergelijken ("wat dacht ik 6 maanden geleden en wat is er veranderd")?
35. Taal van de app en rapporten: Nederlands, Engels, of beide?

### D. Actualiteit & nieuws
36. Welke nieuwsbronnen vertrouw je (De Tijd, FT, Bloomberg, Reuters, WSJ, X/Twitter, Reddit, …)? En welke absoluut niet?
37. Wil je ook "zachtere" signalen: insider-aankopen/-verkopen, short-interesse, analistenratings, posities van grote fondsen (13F), sentiment op sociale media?
38. Wil je earnings calls (transcripts) laten samenvatten, inclusief toon van het management?
39. Hoe ver vooruit moet de app "mogelijke toekomstige impact" inschatten, en hoe speculatief mag dat zijn?

### E. Portefeuille, watchlist & meldingen
40. Wil je je portefeuille in de app invoeren (handmatig, CSV-import van je broker)?
41. Wil je een watchlist met automatische opvolging?
42. Welke meldingen wil je? (nieuw kwartaalverslag, groot nieuws, koersdaling X%, waardering in koopzone, these gebroken, …)
43. Via welk kanaal? (push op gsm, e-mail, Telegram/WhatsApp, enkel in de app) en hoe vaak? (realtime, dagelijks overzicht, wekelijks)
44. Wil je dat de app zelf **nieuwe kandidaten** voorstelt (screener op basis van jouw profiel)?

### F. Gebruikers & gebruik
45. Ben jij de enige gebruiker, of ook familie/vrienden/klanten? Ooit commercieel (verkopen als product)?
46. Waar gebruik je het vooral: gsm onderweg, laptop thuis, beide?
47. Typisch gebruik: snel even een ticker checken (2 min) of grondig onderzoek (uur)? Of beide met een "snel" en "diep" modus?
48. Hoe vaak verwacht je een rapport te maken? (per dag / per week)

### G. Techniek, platform & budget
49. Wat voor app: webapp (in browser, ook op gsm), mobiele app (iOS/Android), desktop, of eerst gewoon een chat/CLI-tool?
50. Welke gsm/computer gebruik je? (iPhone/Android, Windows/Mac)
51. Heb je zelf programmeerervaring? Wil je de code zelf kunnen onderhouden? Voorkeurstaal (Python, TypeScript, …)?
52. Waar mag het draaien: lokaal op je pc, op een server/cloud (bv. Vercel, Railway, eigen VPS), of maakt het niet uit?
53. **Budget per maand** voor data en AI? (Gratis bronnen zoals SEC EDGAR, Yahoo zijn beperkt; goede data-API's zoals Financial Modeling Prep, EODHD, Polygon kosten ca. €15–100/maand; AI-gebruik (Claude API) kost per rapport ongeveer enkele cent tot ~€1 afhankelijk van diepgang.)
54. Mag de app de Claude API gebruiken voor de analyse? Heb je al een API-sleutel of account bij een data-provider?
55. Privacy: mogen portefeuillegegevens in de cloud staan, of moet alles lokaal blijven?
56. Moet het werken voor Europese aandelen (waar verslagen vaak PDF's zijn en data schaarser is) even goed als voor Amerikaanse?

### H. Stijl & uitstraling
57. Welke sfeer: zakelijk/Bloomberg-terminal, minimalistisch/Apple-achtig, speels/kleurrijk?
58. Donkere modus, lichte modus, of beide?
59. Apps of sites waarvan je het ontwerp mooi vindt (bv. Koyfin, TradingView, Finviz, Simply Wall St, Revolut)?
60. Toon van de tekst: kort en direct, of uitgebreid met uitleg? Mag de app kritisch/"eerlijk-hard" zijn tegen je?

### I. Grenzen & afspraken
61. Mag de app ooit zelf orders plaatsen bij je broker, of strikt alleen adviseren? (Voorstel: alleen adviseren.)
62. Hoe moet de app omgaan met onzekerheid: altijd een advies geven, of ook "onvoldoende info" durven zeggen?
63. Wat zijn dingen die de app absoluut **niet** mag doen of tonen?
64. Wat is voor jou de **definitie van afgewerkt**? Bv.: "Ik typ een ticker, binnen X minuten krijg ik een rapport dat minstens zo goed is als wat ik zelf in Y uur maak."
65. Wat is een **eerste versie (MVP)** waar je al blij mee zou zijn? Welke functies mogen tot later wachten?
66. Heb je een deadline of gewenst tempo?
67. Hoe wil je testen of de adviezen goed zijn? (bv. backtest op bedrijven die je al kent, vergelijken met je eigen analyses, paper trading)
68. Kun je 2–3 tickers geven die we als **testcases** gebruiken (een die je bezit, een die je overweegt, een die je afwees)? En eventueel een eigen analyse van één ervan als referentie?

### J. Leren van jou
69. Hoe wil je dat de app je voorkeuren leert: een intake-vragenlijst, duimpjes omhoog/omlaag per rapport, je eigen notities, je echte aan- en verkopen analyseren, of een combinatie?
70. Mag de app je voorkeuren automatisch aanpassen, of wil je elke wijziging eerst bevestigen?
71. Wil je een "beleggingsdagboek" waarin je per aankoop je reden (these) noteert, zodat de app later kan controleren of die these nog klopt?

### K. Vrije ruimte
72. Wat vergeten we nog? Welke stap in jouw huidige werkwijze kost het meeste tijd of vind je het vervelendst?
73. Is er een bestaande tool die je al gebruikt en wat mist daar?

---

## 4. Volgende stappen
1. Jij beantwoordt de vragen (in de chat of rechtstreeks in dit bestand).
2. Ik werk het definitieve plan uit: architectuur, databronnen, MVP-scope, testplan en mijlpalen.
3. We bouwen module per module, met na elke module een test op jouw testcases.

> ⚠️ De app geeft onderzoek en meningen, geen gereglementeerd financieel advies. De eindbeslissing blijft altijd bij jou.
