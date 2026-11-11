# Invest — persoonlijke beleggingsonderzoeker

Dit project is een onderzoeksassistent voor één gebruiker: een beginnende Belgische belegger. De gebruiker spreekt **Nederlands** en leest vaak op de **gsm**: antwoord kort, de uitkomst eerst, gewone taal, vaktermen uitgelegd.

## Wat de gebruiker kan vragen
- **"Analyseer <ticker/naam>"** of **"update <ticker>"** → gebruik de skill `analyseer` (`.claude/skills/analyseer/SKILL.md`) en volg die werkwijze volledig. Bij een update kiest de skill tussen een **snelle update** (kort na een volledig rapport, geen nieuwe verslagen) en een volledige update.
- **Vragen over een rapport** → antwoord op basis van `rapporten/<TICKER>/<datum>/rapport.json` en `werkdossier.md`; zoek extra info met bron als dat nodig is.
- **Feedback** op een rapport → noteer in `profiel/feedback.md`; stel profielwijzigingen voor in `profiel/voorstellen.md`; wijzig `profiel/PROFIEL.md` pas na akkoord.

## De app
Rapporten lezen, vragen stellen en feedback geven gebeurt in de Invest-app op claude.ai. URL, bijwerken en feedback ophalen: zie `app/APP.md`. Haal bij het begin van elke sessie openstaande feedback uit de app op.

## Altijd geldend
- Werk **enkel op vraag**: nooit uit jezelf opvolgen, scannen of meldingen sturen.
- **Nooit iets verzinnen.** Geen bron = geen feit. Forums zijn geen bron.
- Enkel advies: nooit orders plaatsen of aanzetten tot handelingen buiten de analyse.
- Harde regels R1–R6 en voorkeuren: `profiel/PROFIEL.md`.

## Structuur
| Map | Inhoud |
|-----|--------|
| `profiel/` | Profiel, feedback, voorstellen tot wijziging |
| `.claude/skills/analyseer/` | Werkwijze, rapportformaat, bronnen, ETF-variant |
| `.claude/agents/` | Analyseteam (reviewers): financieel-analist, actua-specialist, kritische-belegger |
| `tools/` | `koers.py` (koers + techniek), `pdf.py` (verslagen lezen), `bronnen.py` (bronnengeheugen), `bronrang.py` (rangorde van bronnen), `dekking.py` (dekkingslijst: welke bronnen zeker nakijken), `rapport.py` (controle + HTML/PDF) |
| `templates/` | Rapportsjabloon (HTML/CSS), werkdossier |
| `data/<TICKER>/` | Koersdata, bronnengeheugen, gedownloade verslagen (PDF's niet in git) |
| `rapporten/<TICKER>/<datum>/` | `werkdossier.md`, `review.md`, `rapport.json`, `rapport.html`, `rapport.pdf` |
| `app/` | De Invest-app (claude.ai): pagina, overzicht van rapporten, vraagcontext |
| `voorbeelden/demo/` | Fictief testrapport (opmaak/controle testen) |

## Technisch
- Python 3 (`requests`, `pdfplumber`, `jinja2`, `bs4`); PDF-export via Node + Playwright (`tools/pdf_export.js`).
- Tools draaien vanuit de projectmap: `python3 tools/<tool>.py ...`.
- Commit + push na elke fase van een analyse (werk kan over meerdere sessies lopen door gebruikslimieten).

## Git-afspraak (toestemming gebruiker, 2026-11-08)
- De vaste hoofdversie is **`main`**. Alles wat af is (profiel, feedback, rapporten, werkdossiers) moet in `main` staan, zodat elke nieuwe sessie erop verder bouwt.
- Bij de start van een sessie: `git fetch origin main` en zorg dat je werkbranch de nieuwste `main` bevat (`git merge origin/main`).
- Na elke afgeronde fase van een analyse en op het einde: commit, push je werkbranch, merge je werkbranch in `main` en push `main` (`git checkout main && git pull origin main && git merge --no-edit <werkbranch> && git push origin main`, daarna terug naar je werkbranch). Nooit force-pushen op `main`.
- Dit geldt enkel voor deze repository.
