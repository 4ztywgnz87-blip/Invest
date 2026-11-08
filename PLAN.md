# Invest — Definitief plan (v1)

> Gebaseerd op de intake in [`ANTWOORDEN.md`](ANTWOORDEN.md). Status: **Fase 1 (fundament) gebouwd — volgende stap: eerste echte rapport (Sofina)**.

---

## 1. Wat bouwen we?

Een persoonlijke, kritische beleggingsonderzoeker. Jij geeft een **ticker** (aandeel of ETF), de app doet het werk dat jou nu 5+ uur kost:

1. Alle jaar- en kwartaalverslagen lezen en de juiste cijfers eruit halen.
2. De gelinkte bedrijven (2 niveaus diep) en hun cijfers analyseren.
3. Zelf bedenken welke actualiteit relevant is en daar gericht naar zoeken (verleden, nu, 2 jaar vooruit).
4. Alles fact-checken.
5. Een kort, direct, zakelijk rapport in het Nederlands schrijven, met kritische expertopmerkingen en jouw rode vlaggen bovenaan.

**Kernprincipes**
- **Enkel op vraag.** Geen continue scan, geen portefeuille, geen watchlist, geen meldingen.
- **Kwaliteit boven snelheid.** Geen tijdslimiet.
- **Nooit verzinnen.** Elk feit heeft een bron. Forums zijn nooit een bron van feiten.
- **Enkel advies.** De app plaatst nooit orders.
- **Labels in elk rapport:** 🟦 *Feit* (met bron) · 🟩 *Berekening* · 🟨 *Inschatting* (speculatief, met reden) · 🟥 *Mening*.

## 2. Hoe werkt het technisch? (gratis, op Claude Pro)

```
 ┌──────────────────────────────┐         ┌────────────────────────────────┐
 │ 1. ONDERZOEK  (Claude-chat)  │  ───►   │ 2. INVEST-APP  (claude.ai)     │
 │ Claude Code, gsm of pc        │ rapport │ webapp op gsm + pc              │
 │ "analyseer SOF.BR"            │         │ • archief van rapporten         │
 │ • leest verslagen (PDF)       │         │ • rapport lezen + grafieken     │
 │ • zoekt nieuws/keten/sector   │  ◄───   │ • vragen stellen over rapport   │
 │ • fact-check                  │ feedback│ • PDF downloaden                │
 │ • schrijft rapport            │ profiel │ • feedback + profiel beheren    │
 └──────────────────────────────┘         └────────────────────────────────┘
              │
              ▼
   Deze GitHub-repo = het geheugen
   (profiel, regels, rapporten, gecheckte bronnen)
```

- **Onderzoeksdeel:** een vaste werkwijze (Claude Code *skill*) in deze repo. Jij start het vanuit de Claude-app op gsm of pc. Het draait op je Pro-abonnement.
- **App:** een webapp gepubliceerd op claude.ai (privé). Vragen over een rapport gebruiken je eigen Pro-verbruik → geen extra kosten. De app kan zelf niet op internet zoeken; dat doet stap 1.
- **Opslag:** rapporten (HTML + PDF), profiel, feedback en bronnengeheugen in deze repo én in de database van de app.
- **Beperking:** Pro heeft gebruikslimieten. Een zeer grondig rapport kan over meerdere sessies verdeeld moeten worden. Voor enkele rapporten per maand is dat oké.
- **Later optioneel:** echte eigen webapp met Claude API (~€5–20/maand). De werkwijze is herbruikbaar.

## 3. Databronnen (gratis)

| Wat | Bronnen |
|-----|---------|
| Jaar-/kwartaalverslagen | Investor-relations-sites van bedrijven, SEC EDGAR (VS: 10-K, 10-Q, 20-F), EDINET (Japan), nationale registers (FSMA/NBB België, AMF, AFM, …) |
| Aandeelhouders & insiders | Transparantieverklaringen (FSMA e.a.), SEC 13D/13G en Form 4, jaarverslag (aandeelhoudersstructuur), meldingen van leidinggevenden (MAR) |
| Koersen & technische analyse | Gratis koersdata (bv. Yahoo Finance, Stooq), berekend: trend, steun/weerstand, cycliciteit |
| Nieuws & actualiteit | Zo breed mogelijk: De Tijd, Reuters, FT, Bloomberg, WSJ, AP, Nikkei, L'Echo, vakpers per sector, persberichten bedrijven, overheden/toezichthouders |
| Macro & grondstoffen | ECB, Fed/FRED, Eurostat, IEA/EIA (energie), IMF/Wereldbank |
| Rechtszaken | Persberichten, jaarverslag (geschillen/voorzieningen), rechtbankdatabanken (bv. CourtListener VS), toezichthouders |
| ETF's | Factsheet, KID, holdingslijst en jaarverslag van de uitgever |

**Fact-check regel:** belangrijke cijfers bij voorkeur uit de primaire bron (verslag) en waar mogelijk gecontroleerd met een tweede bron. Tegenstrijdigheden worden gemeld.

**Te weinig info:** eerst 3 grondige zoekrondes. Pas daarna "onvoldoende info" melden, mét wat wel gevonden werd.

**Bronnengeheugen:** per bedrijf wordt bijgehouden welke artikels/verslagen al gelezen zijn (link + datum + korte samenvatting). Bij een nieuw rapport worden die niet opnieuw geanalyseerd, tenzij ze gewijzigd zijn.

## 4. Het rapport

Zakelijk, strak, licht thema. Eerst **1 scherm samenvatting**, daarna inklapbare secties.

**Kop (1 scherm)**
- Advies: **Kopen / Houden / Verkopen / Afwachten**
- Score 1–10 + korte reden
- Koopzone en koersdoel
- Scenario's (2 jaar): slecht / normaal / goed
- 🚩 Rode vlaggen (altijd bovenaan)
- Wat is er veranderd sinds het vorige rapport

**Secties**
1. **Rode vlaggen & bestuur**
   - Aandeelhouders > 49% (één of samen) → **NO-GO**, tenzij de rest uitzonderlijk positief is; altijd verdeling uitleggen (wie, %, via welke structuur).
   - Management dat geld naar zichzelf sluist (vergoedingen, related-party transacties).
   - Aandeelhoudersgeld om een topmanager uit te kopen.
   - Rechtszaken: vroeger, lopend, mogelijk — met reden.
   - Insider-aankopen/-verkopen en corporate actions — met reden.
2. **Cijfers** — laatste kwartaal en jaar, trend 5 jaar, met grafieken en uitleg in gewone taal (omzet, winst, marges, kasstroom, schulden, rendement, dividend, inkoop, verwatering, …).
3. **Waarin investeren ze?** — capex, R&D, overnames, deelnemingen; hoeveel van de winst wordt geherinvesteerd (langetermijnvisie ✔, hype ✘).
4. **De keten (2 niveaus)** — belangrijkste leveranciers, klanten, investeringen, deelnemingen en hun kerncijfers en situatie.
5. **Sector & concurrenten** — sectortrends + vergelijking met de dichtste concurrenten. Label "defensief" waar van toepassing.
6. **Actualiteit** — wat had impact, wat heeft impact, wat kan impact hebben (2 jaar), elk met bron en labels.
7. **Earnings call** — samenvatting + mening over houding/zelfzekerheid management.
8. **Waardering** — intrinsieke waarde (DCF + vergelijking multiples), aannames zichtbaar.
9. **Grafiek & trend** — technische trend, cycliciteit, voorstel stop-loss (jouw −20% + technische steunniveaus).
10. **Kritische expertblik** 🟥 — wat een ervaren, kritische investeerder hierover zou zeggen.
11. **Past dit bij jou?** — toetsing aan je profiel.
12. **Bronnen** — volledige lijst met links.

**ETF-variant:** kosten (TER), inhoud en concentratie (landen, sectoren, top-posities), indexvolging, grootte, replicatie, fiscaliteit België (beurstaks, Reynders-taks), overlap met wat je al hebt (als je dat opgeeft).

## 5. Jouw profiel & leren

- `profiel/PROFIEL.md`: je antwoorden vertaald naar regels en voorkeuren.
- Na elk rapport: score + commentaar + "let hier extra op" / "dit is nutteloos".
- De app **stelt profielwijzigingen voor**; pas na jouw akkoord worden ze doorgevoerd.
- Extra (later): beleggingsdagboek — waarom je kocht; nieuwe rapporten checken of die redenen nog kloppen.

## 6. Bouwfases

| Fase | Wat | Klaar wanneer… |
|------|-----|-----------------|
| **F1 – Fundament** | Profiel + regels, rapportsjabloon (HTML/PDF), onderzoekswerkwijze (skill), bronnengeheugen | Eerste volledig rapport over **Sofina** |
| **F2 – Diepte & kwaliteit** | Keten 2 niveaus, actualiteitsonderzoek, fact-check, ETF-variant | Rapporten over **Sofina, iShares Core MSCI World, SoftBank** die jij goedkeurt na vergelijking met je eigen kennis |
| **F3 – De app** | Webapp op claude.ai: archief, lezen (gsm + pc), grafieken, vragen stellen, PDF, feedback/profiel | Je opent en leest alle rapporten vlot op gsm én pc en kunt er vragen over stellen |
| **F4 – Terugkijktest** | Analyse "zoals het toen was": **Ørsted 2021** (zou het risico gezien zijn?) en **DEME** (zou de kans gezien zijn?) | Rapporten zijn achteraf verdedigbaar |
| **F5 – Extra's** | Beleggingsdagboek, analyse starten vanuit een nieuwsfeit, screener op vraag, eventueel eigen webapp met API | Op jouw vraag |

## 7. Definitie van "af" (versie 1)

- Ik typ een ticker in de chat → de app werkt het volledige proces af (verslagen → keten → actualiteit → fact-check → rapport) zonder dat ik zelf iets moet opzoeken.
- Het rapport bevat alle secties uit §4, elk feit met bron, alle labels correct, rode vlaggen bovenaan.
- Geen verzonnen informatie (steekproef op bronnen bij de testcases).
- Het rapport staat in de app en is goed leesbaar op OnePlus 9 Pro, iPhone en Windows-pc, en downloadbaar als PDF.
- Ik kan in de app vragen stellen over een rapport.
- Mijn feedback leidt tot voorstellen om het profiel aan te passen.
- Mijn tijd per beslissing gaat van ~5 uur naar ≤ 2 uur.

## 8. Risico's & open punten

- **Gebruikslimiet Pro:** zeer diepe rapporten kunnen meerdere sessies vragen.
- **Netwerktoegang van de cloudomgeving:** sommige sites (betaalmuren, PDF-servers) kunnen geblokkeerd zijn; testen in F1.
- **Betaalmuren** (FT, Bloomberg, De Tijd): enkel vrij toegankelijke delen; dekking via andere bronnen.
- **Europese/Japanse verslagen:** minder gestructureerde data → meer PDF-lezen (dat is net de kern).

> ⚠️ Dit is onderzoek en mening, geen gereglementeerd financieel advies. De beslissing ligt altijd bij jou.
