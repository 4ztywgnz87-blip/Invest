# Werkdossier — Sofina (SOF.BR) — 2026-11-11 (update)

> Update van `rapporten/SOF.BR/2026-11-08/` (werkdossier, review en bronnen daar blijven de basis). Enkel nieuwe/gewijzigde bronnen gelezen.

## Status
| Fase | Status | Opmerking |
|------|--------|-----------|
| 0 Identificatie & voorbereiding | ✅ | geen open app-feedback; vorig rapport 2026-11-08 |
| 1 Koers & techniek | ✅ | €270,4 (9-11); korting 17,2% t.o.v. NAV 30-6 |
| 2 Verslagen | ✅ | geen nieuwe verslagen (volgende 24-3-2027) |
| 3 Bestuur & rode vlaggen | ✅ | FSMA sofina-70..82: geen nieuwe meldingen; website: melding 19-08 blijft laatste |
| 4 Keten | ✅ | Anthropic prijsvork (CNBC 10-11) |
| 5 Sector & concurrenten | ✅ | peerkoersen 9-11 herberekend |
| 6 Actualiteit | ✅ | herstel 6-11, oorzaak midterms, Fed-kans 78% (Reuters via Devdiscourse) |
| 7 Earnings call | ✅ | geen nieuwe call |
| 8 Waardering & advies | ✅ | ongewijzigd 4/10; verwacht rendement ±1,5%/j |
| 9 Expert | ✅ | ongewijzigd |
| 10 Fact-check | ✅ | nieuwe feiten nagekeken bij bron (CNBC, Reuters) |
| 11 Teamreview | ✅ | 2 rondes, 3× goedgekeurd met opmerkingen |
| 12 Bouwen | ✅ | nieuwe rapportopbouw (feedback 11-11), 390 px gecontroleerd |
| 13 Afronding | ✅ | app gepubliceerd, PDF verstuurd |

## Nieuwe bevindingen
- Koers 270,4 (9-11-2026); SMA50 255,8; SMA200 236,8; 1j +12,4%; 5j −31,5% (Yahoo).
- Korting: 270,4/326,48 − 1 = −17,2%. Dividendrendement 3,66/270,4 = 1,35%.
- Verwacht rendement: (272 + 7,32)/270,4 − 1 = +3,3% in 2 j ≈ 1,6%/j.
- Peers (9-11): GBL 79,70 (NAV 100,77 → −20,9%), Brederode 100,2 (154,6 → −35,2%), AvH 270,8, Exor 74,35 (157,9 → −52,9%).
- Anthropic (CNBC 10-11): $70–78, 825 mln aandelen, tot $1,405 bn fully diluted; pricing 18-11 en handel 19-11 volgens anonieme bronnen; 9m-omzet $33,24 mld. Inschatting impact Sofina: +0,4–0,8% NAV als Anthropic 1–2% van portefeuille is (onbekend).
- Markt (Reuters 6-11): herstel chips +4,2% intraday; oorzaak uitverkoop 5-11 = overwinning Democraten midterms (datacenterstaten), vrees tragere AI-uitbouw en strengere AI-regels; Fed-december-verhoging 78% kans.
- Niet opgenomen: ByteDance "$600 mld" (SCMP, datum onduidelijk); EUR/USD 10-11 (geen betrouwbare bron); Nasdaq 9-11 +3,4% (enkel Vantage, niet bevestigd).

## Reproduceren
`rapport.json` = definitief rapport 2026-11-08 + `maak_rapport/patch5.py`.

## Teamreview ronde 1 (verwerkt met patch6.py)
- Extra bronnen: AP 20-10-2026 (SpaceX eerste winst, omzet Q3 ±$14,6 mld), RTTNews 21-10 (aandeel stijgt).
- Blootstellingskaart aangevuld: SpaceX-lock-ups (laatste grote vrijgave ±begin december), Anthropic-IPO (herwaardering fondsen), Fed december (78% volgens Reuters 6-11), ECB 17-12.
- Verworpen: Brent $98,29 / tankeraanvallen 5-11 (zwakke bron).

- Brent $98,29 / tankeraanvallen 5-11: niet bevestigd (enkel zwakke bron), niet opgenomen.
- `rapport.json` = patch5 + patch6 + patch7 (zie maak_rapport/).
