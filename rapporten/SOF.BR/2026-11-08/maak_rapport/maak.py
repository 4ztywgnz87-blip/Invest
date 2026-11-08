import json
ROOT='/home/user/Invest'
k=json.load(open(f'{ROOT}/data/SOF.BR/koers.json'))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
def L(items,titel=None):
    d={"type":"lijst","items":items}
    if titel: d["titel"]=titel
    return d
def K(t): return {"type":"kop","tekst":t}
def KD(stijl,tekst,titel=None):
    d={"type":"kader","stijl":stijl,"tekst":tekst}
    if titel: d["titel"]=titel
    return d

NAV='[[NAV|intrinsieke waarde: wat alle bezittingen min de schulden waard zijn, volgens Sofina zelf]]'
KORT='[[korting|hoeveel lager de beurskoers staat dan de intrinsieke waarde per aandeel]]'

bronnen=[
 (1,"Halfjaarverslag 2026","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2026/half-year-report-2026.pdf","Halfjaarverslag 2026 (p.10–17, 30–41)","2026-09-02"),
 (2,"Presentatie halfjaarresultaten 2026","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2026/presentation-of-the-2026-half-year-results.pdf","Presentatie HY2026 (p.5–16)","2026-09-02"),
 (3,"Jaarverslag 2025","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2025/annual-report-2025-print-out-pdf.pdf","Jaarverslag 2025 (p.5–8, 26, 37, 56–75, 107, 115–137)","2026-03-26"),
 (4,"Presentatie jaarresultaten 2025","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2026/Presentation-of-the-2025-annual-results.pdf","Presentatie FY2025 (p.3–11)","2026-03-26"),
 (5,"Jaarverslag 2024","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2024/annual-report-2024-print-out-pdf.pdf","Jaarverslag 2024 (kerncijfers, aandeelhouders)","2025-03-26"),
 (6,"Jaarverslag 2023","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2023/annual-report-2023-print-out-pdf.pdf","Jaarverslag 2023 (kerncijfers, aandeelhouders)","2024-03-28"),
 (7,"Jaarverslag 2022","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2022/Annual-report-2022-single-page-PDF--30032023-1.pdf","Jaarverslag 2022 (kerncijfers 2021–2022)","2023-03-30"),
 (8,"Rapport annuel 2021","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/annual-report/2021/sofina-sa-rapport-annuel-2021-singlepage.pdf","Rapport annuel 2021 (chiffres clés)","2022-03-24"),
 (9,"Aandeelhoudersstructuur (melding van 19-08-2026)","Sofina","primair","https://www.sofinagroup.com/en/investors/shareholder-centre/shareholding-structure",None,"2026-08-19"),
 (10,"Meldingen leidinggevenden: herschikking binnen het consortium (05-10-2026)","FSMA","primair","https://www.fsma.be/en/manager-transaction/sofina-47","FSMA-meldingen sofina-46, -47, -50, -55","2026-10-05"),
 (11,"Meldingen transacties leidinggevenden Sofina 2024–2026","FSMA","primair","https://www.fsma.be/en/manager-transaction/sofina-65","FSMA-meldingen sofina-1 t/m -65","2026-10-21"),
 (12,"Koersdata SOF.BR (opgehaald 08-11-2026)","Yahoo Finance","data","https://finance.yahoo.com/quote/SOF.BR",None,"2026-11-06"),
 (13,"Transcript analistencall halfjaar 2026","Investing.com","analyse","https://www.investing.com/news/transcripts/earnings-call-transcript-sofina-h1-2025-nav-rises-as-stock-gains-39-93CH-4887840",None,"2026-09-03"),
 (14,"Here's what you should know about the US TikTok deal","TechCrunch","nieuws","https://techcrunch.com/2026/01/23/heres-whats-you-should-know-about-the-us-tiktok-deal/",None,"2026-01-23"),
 (15,"Initial public offering of SpaceX","Wikipedia","overig","https://en.wikipedia.org/wiki/Initial_public_offering_of_SpaceX",None,"2026-07"),
 (16,"Anthropic vaults to a $965 billion valuation with new funding","AP / ABC News","nieuws","https://www-cdn.abcnews.com/Technology/wireStory/anthropic-vaults-965-billion-valuation-new-funding-claude-133397439",None,"2026-05-28"),
 (17,"Anthropic IPO 2026: date, valuation & timeline","tastytrade","analyse","https://tastytrade.com/learn/markets/industry/anthropic-ipo/",None,"2026-11-05"),
 (18,"OpenAI valued at $852 billion in latest funding round","Yahoo Finance","nieuws","https://finance.yahoo.com/sectors/technology/article/openai-valued-at-852-billion-in-latest-funding-round-ahead-of-ipo-213943098.html",None,"2026-03-31"),
 (19,"ECB keeps key interest rate on hold at 2.5%","CNBC","nieuws","https://www.cnbc.com/2026/10/29/european-central-bank-interest-rates.html",None,"2026-10-29"),
 (20,"ECB hikes interest rates to 2.5%","CNBC","nieuws","https://www.cnbc.com/2026/09/10/ecb-interest-rate-hike-lagarde-iran.html",None,"2026-09-10"),
 (21,"Euro hits 4-week high","Trading Economics","data","https://tradingeconomics.com/euro-area/currency/news/598161",None,"2026-11-04"),
 (22,"GBL bouwt verder aan private portefeuille","Bolero","nieuws","https://www.bolero.be/nl/analyse-en-inzicht/blog/gbl-bouwt-verder-aan-private-portefeuille",None,"2026-07-31"),
 (23,"Holdingupdate september 2026","Bolero / KBC Securities","analyse","https://www.bolero.be/nl/analyse-en-inzicht/blog/boleros-ongemeen-interessante-maandelijkse-holdingupdate-september-2026",None,"2026-10-07"),
 (24,"Exor H1 2026 results","Exor","primair","https://mfn.se/one/a/exor/exor-press-release-h1-2026-results-18a36b7a",None,"2026-09"),
 (25,"Koersdata GBLB.BR, BREB.BR, ACKB.BR, EXO.AS (opgehaald 08-11-2026)","Yahoo Finance","data","https://finance.yahoo.com/",None,"2026-11-06"),
 (26,"Beursupdate: Sofina onderaan in rode Bel20","De Aandeelhouder","nieuws","https://www.deaandeelhouder.be/nieuws/2026/11/03/beursupdate-sofina-onderaan-in-rode-bel20/",None,"2026-11-03"),
]
B=[]
for i,t,u,ty,url,doc,dt in bronnen:
    d={"id":i,"titel":t,"uitgever":u,"type":ty,"url":url,"datum":dt}
    if doc: d["document"]=doc
    B.append(d)

r={}
r["meta"]={"ticker":"SOF.BR","naam":"Sofina","type":"aandeel","datum":"2026-11-08","beurs":"Euronext Brussel","isin":"BE0003717312","valuta":"EUR","sector":"Investeringsholding (durf- en groeikapitaal)","defensief":False}
r["advies"]={
 "oordeel":"Afwachten","score":4,
 "reden":"Regel **R1 is geraakt**: de familie Boël controleert via drie vennootschappen samen **54,6%**. De rest is degelijk maar niet uitzonderlijk: de korting op de intrinsieke waarde (−18%) is kleiner dan de voorbije jaren en de waarde is moeilijk te controleren (98% niet-beursgenoteerd).",
 "koers_nu":k["koers"],"koers_datum":"06-11-2026",
 "koopzone":{"van":220,"tot":240},
 "koersdoel":290,"koersdoel_uitleg":"normaal scenario, eind 2028: intrinsieke waarde ±€360 met 20% korting",
 "stop_loss":{"waarde":214.1,"uitleg":"−20% t.o.v. koers nu (€267,6); technische steun €238,8 → technische stop €234"},
 "intrinsieke_waarde":326,
 "scenarios":[
  {"naam":"Slecht","koers":180,"kans":"25%","uitleg":"Correctie bij AI- en techbedrijven, dollar −10%, afwaardering ByteDance of Cognita: intrinsieke waarde zakt naar ±€280 en de korting loopt op tot 35% (zoals in 2022–2023)."},
  {"naam":"Normaal","koers":290,"kans":"50%","uitleg":"Intrinsieke waarde groeit ±6%/jaar naar ±€360 (onder het 10-jaarsgemiddelde van 8,4%), korting 20% (CEO: historisch 15–20%)."},
  {"naam":"Goed","koers":350,"kans":"25%","uitleg":"Beursgangen (Anthropic, ByteDance) en verkopen boven de boekwaarde: intrinsieke waarde ±€400, korting krimpt naar 12%."}
 ]}
r["aandeelhouders"]={
 "verdeling":[
  {"naam":"Société de Participations Industrielles SA (consortium Boël)","pct":24.78,"stemrecht_pct":25.77,"structuur":"lid van het referentieconsortium (sinds 2007)"},
  {"naam":"Union Financière Boël SA (consortium Boël)","pct":22.41,"stemrecht_pct":23.31,"structuur":"lid van het referentieconsortium; familieholding Boël; zit zelf in de raad van bestuur"},
  {"naam":"Mobilière et Immobilière du Centre SA (consortium Boël)","pct":7.40,"stemrecht_pct":7.70,"structuur":"lid van het referentieconsortium (sinds 2013)"},
  {"naam":"Eigen aandelen Sofina","pct":3.85,"stemrecht_pct":0,"eigen_aandelen":True},
  {"naam":"Vrij verhandelbaar (geen andere partij boven 3%)","pct":41.56,"vrij_verhandelbaar":True}
 ],
 "bronnen":[9,3,10],
 "uitleg":"De drie vennootschappen vormen samen de 'referentieaandeelhouder', een [[consortium|groep aandeelhouders die wettelijk als één blok handelt]] rond de familie Boël, met **54,6% van alle aandelen** en (berekend, zonder eigen aandelen) **±56,8% van de stemmen**. Eén aandeel = één stem, geen dubbel stemrecht. Op 5-10-2026 kocht Union Financière Boël 681.752 aandelen van de twee andere leden (à €250,51): het blok blijft even groot, maar UFB wordt de grootste (berekend ±24,3%). De tabel toont de toestand van de melding van 19-08-2026."
}
r["rode_vlaggen"]=[
 {"ernst":"nogo","regel":"R1","titel":"Familie Boël controleert 54,6% via een consortium",
  "uitleg":[
   F("Union Financière Boël (22,41%), Société de Participations Industrielles (24,78%) en Mobilière et Immobilière du Centre (7,40%) vormen samen één blok met **20.034.661 aandelen = 54,60%**. Sofina zelf heeft nog 3,85% eigen aandelen; samen 58,45%.",[9,3]),
   F("Het consortium bestaat sinds 2007; de CEO (Harold Boël) en tot mei 2026 Nicolas Boël zitten in de raad van bestuur; Union Financière Boël werd in 2026 voorgedragen als bestuurder. De raad vond een [[relationship agreement|schriftelijke afspraak tussen bedrijf en hoofdaandeelhouder over hoe zij met elkaar omgaan]] 'niet nodig'.",[3]),
   T("Kleine aandeelhouders kunnen niets afdwingen: het consortium beslist over bestuur, dividend, kapitaalverhogingen en een eventueel bod. Tot nu toe gedroeg het consortium zich correct (zelfde voorwaarden bij de claimemissie, geen opvallende transacties met verbonden partijen) — maar dat is een kwestie van vertrouwen, geen garantie.","mening")]},
 {"ernst":"middel","regel":"R6","titel":"Kapitaalverhoging onder de intrinsieke waarde (okt 2025)",
  "uitleg":[F("Op 7-10-2025 gaf Sofina 2.446.428 nieuwe aandelen uit à **€223** (totaal €545,6 mln) via een [[claimemissie|kapitaalverhoging waarbij bestaande aandeelhouders voorrang krijgen om bij te kopen]], onder zowel de beurskoers als de intrinsieke waarde. Sofina noemt zelf de 'mechanische verwatering' van de intrinsieke waarde per aandeel. Reden: extra slagkracht om 'doorheen cycli' te investeren.",[3]),
   T("Wie niet meedeed en zijn rechten niet verkocht, verloor ±2% intrinsieke waarde per aandeel: (33,05 mln × €305 + 2,45 mln × €223) / 35,5 mln ≈ €299 i.p.v. €305.","berekening")]},
 {"ernst":"info","regel":"R5","titel":"Insiders: kleine aankopen bestuurders, CEO verkoopt optie-aandelen",
  "uitleg":[F("Bestuurders kochten in 2026 kleine posten bij lage koersen: voorzitter Charlotte Strömberg 450 aandelen à €210,60 (31-3), Leslie Teo 100 à €209 (31-3), Charles Peugeot (en zijn vennootschap) samen 479 aandelen tussen €222 en €252 (juni–sept). CEO Harold Boël tekende in op de claimemissie voor 15.923 aandelen (€3,55 mln). In 2026 oefende hij [[opties|recht om aandelen te kopen aan een vooraf vastgelegde prijs]] uit à €128,12 en verkocht hij telkens dezelfde aantallen (2.000 à €246,60 in jan, 6.500 à €238,77 in juli, 5.000 à €243,20 en 4.500 à €261,36 in okt).",[11]),
   T("De verkopen van de CEO horen bij zijn verloning (opties verzilveren) en zijn klein t.o.v. zijn inschrijving in 2025. Geen alarmsignaal.","mening")]},
 {"ernst":"info","regel":"R4","titel":"Geen rechtszaken tegen Sofina gevonden",
  "uitleg":[T("In de jaarverslagen 2021–2025, het halfjaarverslag 2026 en nieuws (NL/FR/EN) vond ik geen lopende of afgesloten rechtszaak tegen Sofina zelf. Wel lopen er groepsvorderingen tegen TikTok/ByteDance (privacy, verslaving bij jongeren) — dat raakt Sofina enkel onrechtstreeks via de waarde van ByteDance.","mening")]}
]
r["samenvatting"]=[
 F(f"Sofina is een Brusselse investeringsholding van **€11,5 mld** {NAV}: €326,48 per aandeel op 30-6-2026. De beurskoers (€267,6) ligt **18% lager** — dat is de {KORT}.",[1,12]),
 F("De familie Boël bezit via drie vennootschappen **54,6%** → **regel R1 geraakt (NO-GO)**.",[9]),
 F("De portefeuille is voor **92% niet-beursgenoteerd**: half rechtstreekse belangen (ByteDance, Cognita, Nuxe, Drylock, Vinted …), half via ±90 durfkapitaalfondsen (Sequoia, Lightspeed …) met o.a. SpaceX, Stripe, Anthropic en OpenAI. 65% van de waarde zit in dollar.",[1]),
 T("Resultaten wisselvallig: +29% (2021), −16,5% (2022), +15% (2024), −1% (2025), +8% eerste helft 2026. Over 10 jaar gemiddeld **8,4%/jaar**, over de laatste 4 jaar −1,4%/jaar en 9,9% per jaar slechter dan de wereldindex.","berekening"),
 T("Positief: bijna alle winst wordt **geherinvesteerd** (dividend slechts 1,4%), lage schuld (1,9% van de portefeuille), sterke fondsen en een langetermijnfamilie. Negatief: R1, de waarde is grotendeels een schatting, hoge blootstelling aan dure AI-bedrijven en de korting is al kleiner dan in 2022–2025.","mening"),
 KD("mening","**Afwachten, score 4/10.** Door R1 normaal niet kopen. Wie toch wil: pas bij een korting van ±28% of meer (koers €220–240).","Oordeel")
]
r["verkoopsignalen"]=[
 "Korting op de intrinsieke waarde zakt onder **10%** (of er ontstaat een premie zoals in 2021): winst nemen.",
 "Twee halfjaren na elkaar **negatieve waardecreatie zonder valuta-effect** (Sofina publiceert dit in elk halfjaarverslag).",
 "[[LTV|schuld gedeeld door de waarde van de portefeuille]] boven **10%** (doel van Sofina is 5–10%) of een nieuwe kapitaalverhoging onder de intrinsieke waarde.",
 "ByteDance groeit boven **10%** van de portefeuille of wordt fors afgewaardeerd.",
 "Koers sluit onder **€214** (stop-loss −20%)."
]
r["onvoldoende_info"]=[
 {"onderwerp":"Waarde per deelneming (ByteDance, Anthropic, OpenAI …)","wat_wel":"Sofina publiceert enkel rangordes en drempels (ByteDance >5% en <10%; top 10 fondsenbelangen samen ±10%), geen bedrag per bedrijf.",
  "zoekrondes":["ronde 1: jaarverslag 2025 + halfjaarverslag 2026 (notes 2.2–2.4, lijst deelnemingen p.115–117)","ronde 2: transcript analistencall H1 2026 (CEO: ByteDance 'hoger dan 5%, niet hoger dan 10%')","ronde 3: nieuws NL/FR/EN (Bolero, Test-Aankoop, De Tijd) — enkel schattingen van derden, geen officieel cijfer"]},
 {"onderwerp":"Wie controleert Société de Participations Industrielles en Mobilière et Immobilière du Centre","wat_wel":"Sofina noemt ze enkel als consortiumleden; Union Financière Boël is de familieholding Boël. Waarom UFB op 5-10-2026 aandelen kocht van de andere twee, wordt niet uitgelegd.",
  "zoekrondes":["ronde 1: jaarverslagen 2022–2025 (corporate governance-verklaring)","ronde 2: website Sofina (aandeelhoudersstructuur) en FSMA-meldingen","ronde 3: nieuwszoektocht FR/NL ('Société de Participations Industrielles Sofina', 'Mobilière et Immobilière du Centre') — geen bruikbare bron"]}
]
# --- secties
graf_koers=k["grafiek_blok"]; graf_koers["lijnen"]=[{"naam":"Stop-loss −20%","waarde":214.1},{"naam":"Steun 238,8","waarde":238.8}]
S=[]
S.append({"id":"bestuur","titel":"Bestuur & aandeelhouders","kort":"R1 geraakt (familie Boël 54,6%); verloning redelijk; geen vertrekpremies",
 "inhoud":[
  T("**Kern:** degelijk bestuurd familiebedrijf met een meerderheid onafhankelijke bestuurders, maar de familie Boël heeft het laatste woord (54,6%). Geen tekenen van zelfverrijking.","mening"),
  K("Aandeelhouders (R1)"),
  {"type":"tabel","titel":"Referentieaandeelhouder (consortium Boël)","kolommen":["Aandeelhouder","Aandelen","% (19-08-2026)","% na herschikking 05-10-2026*"],
   "rijen":[["Union Financière Boël SA","8.225.068","22,41%","±24,27%"],["Société de Participations Industrielles SA","9.092.485","24,78%","±23,47%"],["Mobilière et Immobilière du Centre SA","2.717.108","7,40%","±6,86%"],["**Totaal consortium**","20.034.661","54,60%","54,60%"],["Eigen aandelen Sofina","1.412.381","3,85%","—"]],
   "bronnen":[9,10],"noot":"*Berekend uit de FSMA-meldingen van 5-10-2026 (UFB kocht 480.653 aandelen van SPI en 201.099 van MIC à €250,51), in de veronderstelling dat er niets anders wijzigde. Totaal: 36.696.428 aandelen."},
  F("Historiek consortium: 54,60% (2022 en 2023), 54,93% (2024, Union Financière Boël kocht bij), 54,60% na de claimemissie van 2025 (het consortium schreef in voor 1.220.965 nieuwe aandelen, iets minder dan zijn deel).",[7,6,5,3]),
  F("Geen andere aandeelhouder meldde in 2025 een belang boven 3%. Vrij verhandelbaar eind 2025: 42,04%.",[3]),
  K("Raad van bestuur"),
  F("13 bestuurders, waarvan 8 onafhankelijk; voorzitter en CEO zijn verschillende personen. Vanaf de AVA van 13-5-2026 is Charlotte Strömberg voorzitter (opvolger van Dominique Lancksweert na 29 jaar). Harold Boël is CEO sinds 2004 (mandaat tot 2028).",[3]),
  K("Verloning (R2/R3)"),
  {"type":"kerncijfers","items":[
    {"naam":"CEO-verloning 2025","waarde":"€2,03 mln","trend":"gelijk","label":"feit","toelichting":"2024: €1,98 mln; 70% variabel","bronnen":[3]},
    {"naam":"5 andere leiders samen","waarde":"€8,1 mln","trend":"op","label":"feit","toelichting":"2024: €7,6 mln","bronnen":[3]},
    {"naam":"Bestuurders","waarde":"3% van netto dividend","trend":"gelijk","label":"feit","toelichting":"vast sinds 2011; voorzitter +€150.000","bronnen":[3]},
    {"naam":"Loonkloof","waarde":"1:20","trend":"gelijk","label":"feit","toelichting":"hoogste vs laagste loon","bronnen":[3]}]},
  F("Het langetermijnplan 2022–2025 betaalde **niets** uit omdat Sofina slechter deed dan de wereldindex (MSCI ACWI). Er zijn **geen vertrek- of ontslagvergoedingen** voorzien. Er is wel geen [[clawback|recht om uitbetaalde bonussen terug te vorderen]] — een afwijking van de Belgische code.",[3]),
  F("Bij de bonustest werd de intrinsieke waarde per aandeel **gecorrigeerd** voor de verwatering door de claimemissie, zodat de kapitaalverhoging de bonussen niet drukte.",[3]),
  T("Begrijpelijk, maar management-vriendelijk: de verwatering die de kleine aandeelhouder wel voelde, telt niet mee voor de bonus.","mening"),
  F("Transacties met verbonden partijen: enkel leningen en deposito's met eigen dochters; 'belangrijke transacties buiten marktvoorwaarden: nihil'.",[3]),
  K("Rechtszaken (R4), insiders (R5), kapitaalacties (R6)"),
  T("Zie de rode vlaggen bovenaan. Bijkomend: Sofina kocht eigen aandelen in voor de optieplannen (2025: 189.068 gekocht, 236.640 afgestaan; in 2026 twee programma's, het tweede tot €23 mln). Machtiging tot inkoop van max. 20% loopt tot mei 2028.","feit") | {"bronnen":[3]}
 ]})
S.append({"id":"cijfers","titel":"Cijfers","kort":"Intrinsieke waarde €326/aandeel, in 5 jaar amper gestegen; schuld laag",
 "inhoud":[
  T(f"**Kern:** bij een holding draait alles om de {NAV} per aandeel. Die stond eind 2021 op €337,86 en midden 2026 op €326,48 — na een diepe val in 2022 grotendeels hersteld, maar netto nog niet hoger.","mening"),
  K("Intrinsieke waarde & koers"),
  {"type":"grafiek","soort":"staaf","titel":"Intrinsieke waarde per aandeel vs. koers (€)","eenheid":"€","x":["2021","2022","2023","2024","2025","H1 2026"],
   "reeksen":[{"naam":"Intr. waarde","waarden":[337.86,279.41,273.62,311.77,305.77,326.48]},{"naam":"Koers","waarden":[432.0,205.6,225.4,218.4,247.0,222.6]}],"bronnen":[7,6,5,3,1,12]},
  T("Korting/premie: 2021 **+28%** (premie), 2022 −26%, 2023 −18%, 2024 −30%, 2025 −19%, 30-6-2026 −32%, nu (koers €267,6) **−18%**.","berekening"),
  {"type":"tabel","titel":"Kerncijfers (mln €, 'look-through')","kolommen":["","2021","2022","2023","2024","2025","H1 2026"],
   "rijen":[["Intrinsieke waarde","11.354","9.313","9.083","10.305","10.843","11.534"],["Nettoresultaat","2.593","−1.872","−104","1.360","113","857"],["Rendement (incl. dividend)","29,0%","−16,5%","−0,9%","15,2%","−0,8%","—"],["Investeringen","1.284","1.013","517","951","1.139","733"],["Verkopen","1.161","1.174","590","1.211","845","237"],["Bruto kas","1.049","929","893","1.031","1.723","1.080"],["Financiële schulden","730","696","696","697","1.293","1.299"],["Netto kas (+) / schuld (−)","+319","+233","+197","+334","+430","−219"]],
   "bronnen":[8,7,6,5,3,1],"noot":"'Look-through' = alle deelnemingen meegerekend, ook die via dochters. H1 2026 = eerste halfjaar (resultaat over 6 maanden; balans op 30-6)."},
  K("Waar komt het rendement vandaan?"),
  F("2025: waardecreatie +1,9%, maar **+10,1% zonder valuta-effect**; de zwakkere dollar kostte €925 mln. Eerste helft 2026: +8,1% (zonder valuta +6,0%); de fondsen deden +16,1%, de rechtstreekse belangen maar +0,9%.",[4,2]),
  F("Over 10 jaar gemiddeld 8,4% per jaar; over 4 jaar −1,4% per jaar, 9,9% per jaar slechter dan de wereldindex MSCI ACWI in euro.",[3]),
  K("Kosten"),
  T("Bedrijfskosten 2025 €69,5 mln (2024: €63,5 mln) ≈ **0,66%** van de gemiddelde intrinsieke waarde. Daarbovenop betalen de fondsen beheerkosten en [[carried interest|winstdeel voor de fondsbeheerder, meestal 20% van de winst]]; die zitten al verrekend in de waarde en zijn niet apart zichtbaar.","berekening"),
  F("Kosten 2025 en 2024 uit de resultatenrekening ('other expenses').",[3]),
  K("Schulden"),
  F("Twee obligaties: €700 mln aan 1,000% (vervalt 2028) en €600 mln aan 3,707% (vervalt 2033). Niet-gebruikte kredietlijnen €1.375 mln. Netto schuld €219 mln = **LTV 1,9%**. Nog niet opgevraagde verplichtingen aan fondsen: **€1.456 mln**.",[2,1,3]),
  F("Sofina mikt op een netto schuld van 5–10% van de portefeuille; kredietrating A− (S&P).",[13]),
  K("Aandeelhoudersvergoeding"),
  {"type":"kerncijfers","items":[
    {"naam":"Dividend over 2025","waarde":"€3,66 bruto","trend":"op","label":"feit","toelichting":"+4,6%; stijgt elk jaar","bronnen":[4]},
    {"naam":"Dividendrendement","waarde":"1,4%","trend":"gelijk","label":"berekening","toelichting":"€3,66 / €267,6"},
    {"naam":"Uitkering t.o.v. waarde","waarde":"±1,1%","trend":"gelijk","label":"berekening","toelichting":"±€130 mln dividend / €11,5 mld"},
    {"naam":"Aandelen uitstaand","waarde":"35,3 mln","trend":"op","label":"feit","toelichting":"+7,1% nieuwe aandelen in 2025","bronnen":[1,3]}]},
  T("Netto na 30% [[roerende voorheffing|Belgische belasting op dividenden, wordt automatisch ingehouden]]: €2,56 per aandeel.","berekening")
 ]})
S.append({"id":"investeringen","titel":"Waarin investeren ze?","kort":"±99% van de waarde wordt geherinvesteerd: fondsen, groeibedrijven, familiebedrijven",
 "inhoud":[
  T("**Kern:** Sofina keert weinig uit en herinvesteert vrijwel alles — precies wat je profiel positief vindt. De vraag is vooral of de nieuwe investeringen goed geprijsd zijn.","mening"),
  K("Drie investeringsstijlen"),
  {"type":"tabel","titel":"Portefeuille op 30-6-2026 (mln €)","kolommen":["Stijl","Wat","Waarde","Aandeel"],
   "rijen":[["Langetermijn-minderheidsbelangen","€100–300 mln in familiebedrijven (Nuxe, Drylock, Cognita, Proeduca …)","2.901","25%"],["Sofina Growth","€20–100 mln in groeibedrijven (ByteDance, Vinted, Cleo AI …)","2.961","25%"],["Sofina Private Funds","€5–50 mln in >90 fondsen (Sequoia, Lightspeed, a16z …)","5.969","50%"],["**Totaal**","","11.831","100%"]],"bronnen":[1]},
  F("Regio: Noord-Amerika 42%, Europa 35%, Azië 23%. Beursgenoteerd 8%, niet-genoteerd 92%.",[1]),
  K("Investeringen 2025 en 2026"),
  F("2025: €1.139 mln geïnvesteerd en €845 mln verkocht; nieuw o.a. Proeduca, Stream, Scalable Capital, PostHog, Qargo. Eerste helft 2026: €733 mln geïnvesteerd en €237 mln verkocht; nieuw o.a. Cerealis, XBOW, Eye Security, Supabase. Verkopen: SES, Honasa (Mamaearth), deel van Lenskart, Salto (na 30-6).",[4,1,2]),
  F("Nieuwe verbintenissen aan fondsen in de eerste helft van 2026: €475 mln.",[1]),
  F("Volgens de CEO wordt het geld uit de kapitaalverhoging en de obligatie 'ongeveer zoals gepland' over ±3 jaar ingezet.",[13]),
  K("Herinvestering"),
  T("Dividend ±€130 mln per jaar tegenover €11,5 mld waarde: **±99% blijft in het bedrijf**. Over 5 jaar (2021–2025) investeerde Sofina €4,9 mld en verkocht ze €5,0 mld: het groeit dus vooral door waardestijging, en sinds 2025 door nieuw kapitaal en schuld.","berekening")
 ]})
S.append({"id":"keten","titel":"De keten (2 niveaus)","kort":"ByteDance, Cognita, Nuxe, Drylock … en via fondsen SpaceX, Anthropic, OpenAI",
 "inhoud":[
  T("**Kern:** de 10 grootste rechtstreekse belangen zijn 27% van de waarde, de 10 grootste fondsbeheerders 24%. Geen enkele positie behalve ByteDance weegt meer dan 5%. Het grootste ketenrisico is de samenhang: veel posities hangen af van dezelfde AI- en techwaarderingen in de VS en China.","mening"),
  K("1. ByteDance (grootste positie, >5%, <10%)"),
  F("Chinees internetbedrijf achter TikTok, Douyin, CapCut en AI-chatbot Doubao. Omzet volgens publieke bronnen ±$155 mld (2024) en ±$186 mld (2025). Sofina waardeert het via vergelijkbare beursbedrijven met een [[illiquiditeitskorting|korting omdat je het aandeel niet zomaar kan verkopen]].",[3,1]),
  F("CEO: ByteDance is 'hoger dan 5%, maar niet hoger dan 10%'; Sofina heeft geen inspraak in de timing van een verkoop; een beursgang is de meest waarschijnlijke uitweg.",[13]),
  F("Niveau 2 — TikTok VS: op 22-1-2026 werd de TikTok USDS Joint Venture opgericht; ByteDance houdt minder dan 20%, Oracle, Silver Lake en MGX elk 15%. Het algoritme zou van ByteDance 'geleased' worden.",[14]),
  T("Het politieke risico in de VS is kleiner geworden, maar China (grootste markt) en de regelgeving rond jongeren blijven de grote onzekerheden.","inschatting"),
  K("2. Fondsen: Sequoia, Lightspeed, HongShan, Thrive, a16z …"),
  F("De 10 grootste onderliggende bedrijven in de fondsen (±10% van Sofina): SpaceX, ByteDance, Stripe, Anthropic, OpenAI, Databricks, Anduril, DoorDash, Ramp, Prometheus. Waarden komen uit rapporten van de fondsbeheerders, vaak 3–6 maanden oud.",[1]),
  F("Niveau 2 — SpaceX ging op 12-6-2026 naar de Nasdaq aan $135 per aandeel ($1,77 biljoen); eind juli stond het aandeel ±50% onder de piek. Andere vroege beleggers zitten 180 dagen vast ([[lock-up|periode waarin bestaande aandeelhouders niet mogen verkopen]]).",[15]),
  F("Niveau 2 — Anthropic haalde in mei 2026 $65 mld op aan een waardering van $965 mld (Sequoia mee-leider) en diende op 26-10-2026 een beursprospectus in voor de Nasdaq; de datum ligt nog niet vast.",[16,17]),
  F("Niveau 2 — OpenAI: $122 mld opgehaald aan $852 mld (maart 2026).",[18]),
  F("Sofina dekt een deel van de beursgenoteerde posities in fondsen af met [[afgeleide producten|contracten die een koers vastleggen: minder risico, maar ook minder winst als de koers verder stijgt]]. Beursgenoteerde activa in fondsen: €688 mln op 30-6-2026.",[1]),
  K("3. Cognita (scholengroep, VK)"),
  F("Belang 18,96% sinds 2019. Was eind 2025 de 2de grootste positie, zakte midden 2026 naar de 6de. CEO: Cognita 'had het moeilijker om te groeien' en drukte het resultaat.",[3,1,13]),
  K("4. Nuxe, Drylock, Proeduca, Cambridge Associates"),
  F("Nuxe (natuurcosmetica, FR) 49%; Drylock (luiers/hygiëne, BE) 25%; Proeduca (online hoger onderwijs, ES) 17,22% sinds 2025; Cambridge Associates (vermogensbeheer, VS) 23,67%.",[3]),
  F("Nuxe keerde in 2026 extra geld uit via een [[dividend recap|bedrijf leent geld en keert dat uit aan de aandeelhouders]].",[1]),
  T("Deze familiebedrijven zijn eerder stabiel (basisconsumptie, onderwijs) — het meest 'defensieve' deel van Sofina, maar slechts ±25% van de waarde.","mening"),
  K("5. Vinted, Mérieux NutriSciences, Cleo AI"),
  F("Vinted (tweedehandskleding, LT) 3,36%; Mérieux NutriSciences (voedingsveiligheidslabo's) 15,5%; Cleo AI (AI-financiële assistent, VK). Salto (elektronische sloten) werd na 30-6-2026 verkocht; de waarde stond al in de cijfers van juni.",[3,1,13])
 ]})
S.append({"id":"sector","titel":"Sector & concurrenten","kort":"Belgische holdings noteren met 20–50% korting; Sofina is de meest 'tech'",
 "inhoud":[
  T("**Kern:** bijna alle holdings noteren onder hun intrinsieke waarde. Sofina's korting (−18%) is nu kleiner dan die van GBL, Brederode en Exor — Sofina is dus relatief niet goedkoop.","mening"),
  {"type":"tabel","titel":"Vergelijking holdings (koers 06-11-2026)","kolommen":["Holding","Koers","Korting*","1 jaar","5 jaar","Dividendrend.","Volatiliteit"],
   "rijen":[["Sofina","€267,6","−18%","+11%","−29%","1,4%","21%"],["GBL","€79,05","−22%","+14%","+4%","6,5%","16%"],["Brederode","€100,8","−35%","−2%","−17%","1,4%","12%"],["Ackermans & van Haaren","€268,0","n.b.","+21%","+95%","1,7%","23%"],["Exor","€73,35","−54%","−3%","n.b.","0,7%","22%"]],
   "bronnen":[12,25,1,22,23,24],"noot":"*Korting = koers t.o.v. laatst gepubliceerde intrinsieke waarde per aandeel op 30-6-2026 (Sofina 326,48; GBL 100,77; Brederode 154,6; Exor 157,9) — berekend, dus een benadering. Rendementen zonder dividend. Bij AvH vond ik geen recente intrinsieke waarde."},
  F("Volgens KBC Securities: rendement over 10 jaar Sofina +100%, Ackermans & van Haaren +113%, Brederode +154%, BEL20 +62%.",[23]),
  T("**Brederode** lijkt het meest op Sofina (veel private equity via fondsen + beurswaarden), maar met grotere korting en minder AI. **GBL** is meer beursgenoteerd en betaalt veel meer dividend. **AvH** is industrieel (DEME!) en had het beste 5-jaarsrendement.","mening"),
  K("Sectortrends"),
  F("CEO: steeds meer transacties, maar minder 'liquiditeit in het systeem' voor verkopen; inflatie door de oorlog in de Golf drukt de waarderingsmultiples; softwarebedrijven herstelden maar zitten nog onder vorig jaar.",[13]),
  T("Private equity en durfkapitaal zijn **cyclisch**: in goede jaren stijgen waarden en beursgangen, in slechte jaren dalen ze met vertraging (fondsen herwaarderen traag). Sofina's koers reageert sneller dan haar intrinsieke waarde.","mening")
 ]})
S.append({"id":"actualiteit","titel":"Actualiteit","kort":"AI-beursgangen, dollar, rente en olie bepalen de komende 2 jaar",
 "inhoud":[
  T("**Kern:** de belangrijkste drijvers zijn niet Belgisch maar Amerikaans en Chinees: de waardering van AI-bedrijven (Anthropic-beursgang!), de dollar en de rente.","mening"),
  K("Verleden"),
  L([I("2021: koers piekte op €432 met 28% **premie** op de intrinsieke waarde.","feit",[1]),
     I("2022: techcrash — intrinsieke waarde −16,5%, koers −52% (van €432 naar €205,6).","feit",[3,12]),
     I("2025: zwakkere dollar kostte €925 mln waarde; claimemissie (€545 mln) en obligatie (€600 mln) voor extra slagkracht.","feit",[4,3]),
     I("Januari 2026: TikTok VS ondergebracht in een joint venture → politiek risico rond ByteDance kleiner.","feit",[14])]),
  K("Nu (laatste 3–6 maanden)"),
  L([I("Juni 2026: SpaceX naar de beurs aan $1,77 biljoen; eind juli ±50% onder de piek.","feit",[15]),
     I("Sept 2026: ECB verhoogde de rente naar 2,5% door de gevolgen van de oorlog VS–Iran en olie boven $100; okt 2026: rente behouden, inflatie eurozone 3,8%, markt verwacht mogelijk een verhoging in december.","feit",[20,19]),
     I("EUR/USD rond 1,13 begin november (30-6: 1,139). Een euro die 10% stijgt, kost Sofina ±€694 mln (±6% van de waarde).","feit",[21,1]),
     I("5-10-2026: herschikking binnen het consortium Boël (UFB kocht 681.752 aandelen van de twee andere leden, ±€171 mln).","feit",[10]),
     I("26-10-2026: Anthropic diende een beursprospectus in (Nasdaq, 'ANT'); laatste ronde $965 mld.","feit",[17,16]),
     I("3-11-2026: Sofina was met −2,3% de grootste daler van de Bel20.","feit",[26])]),
  K("Komende 2 jaar"),
  L([I("Anthropic-beursgang (mogelijk eind 2026): herwaardering van de fondsposities, maar met vertraging (fondsrapporten 3–6 maanden oud) en lock-ups.","inschatting"),
     I("Afloop lock-up SpaceX voor vroege beleggers (180 dagen na 12-6-2026, dus rond december 2026, gespreid): mogelijk verkoopdruk op het aandeel.","inschatting"),
     I("ByteDance: een beursgang is volgens de CEO de meest waarschijnlijke uitweg, maar timing onbekend. Groot positief als het gebeurt; China-VS-spanningen blijven het risico.","inschatting"),
     I("2028: obligatie van €700 mln (1%) vervalt. Herfinancieren aan ±3,7% kost ±€19 mln extra rente per jaar (±0,2% van de waarde).","berekening"),
     I("Rente/olie: blijft de inflatie hoog door de Golfoorlog, dan drukt dat de waardering van groeibedrijven — het hart van Sofina.","inschatting"),
     I("Nog €1,46 mld te storten in fondsen de komende jaren: verplicht geld, ook in een slechte markt.","feit",[1]),
     I("Volgende cijfers: jaarverslag 2026 op 24-3-2027, AVA 13-5-2027, halfjaar 2-9-2027.","feit",[9])])
 ]})
S.append({"id":"earnings_call","titel":"Analistencall (halfjaar 2026)","kort":"Zelfzeker en open over ByteDance; geen cijferprognose",
 "inhoud":[
  F("Call van begin september 2026 met CEO Harold Boël en het hoofd financiën; vragen van KBC Securities, Degroof Petercam, Kepler Cheuvreux en een particuliere belegger.",[13]),
  K("Kernboodschap"),
  L([I("'Onze missie is niet veranderd'; 'we zitten waar we wilden zitten, maar we zijn pas zes maanden ver'.","feit",[13]),
     I("Fondsen deden het goed; rechtstreekse portefeuille 'praktisch vlak' door Cognita en lagere softwaremultiples.","feit",[13]),
     I("Korting: is kleiner geworden maar 'nog in de twintig' vs. historisch 15–20%.","feit",[13]),
     I("Doel netto schuld 5–10% van de portefeuille; nu 1,9%.","feit",[13]),
     I("Geen cijferprognose (guidance) — normaal voor een holding.","feit",[13])]),
  K("Moeilijke vragen"),
  L([I("**ByteDance te groot?** Antwoord: >5%, <10%; pas 'in de hoge tien procent' wordt het een probleem; 'een probleem van hoge kwaliteit'.","feit",[13]),
     I("**Fondsen die over hun looptijd gaan?** Ja, enkele, maar meestal een restje van enkele procenten; beheerders die na 10 jaar nog de helft niet terugbetaalden, halen geen nieuw fonds op.","feit",[13]),
     I("**Waarom geen rechtstreekse investeringen in OpenAI/Anthropic zoals andere fondsen?** De VS is 'ongelooflijk competitief', Sofina zoekt plekken met een 'recht om te winnen'. Op de specifieke AI-constructies werd niet ingegaan.","feit",[13]),
     I("**Weerspiegelt de waarde de verkoop van Salto?** Ja, al in de cijfers van juni.","feit",[13])]),
  KD("mening","Rustig en consistent met de vorige communicatie; open over ByteDance en over zwakke punten (Cognita, software). Wel: weinig concrete cijfers per positie en de vraag over AI-co-investeringen werd half ontweken.","Mening over toon")
 ]})
S.append({"id":"waardering","titel":"Waardering & advies","kort":"Intrinsieke waarde €326; koopzone €220–240; doel €290",
 "inhoud":[
  T("**Kern:** voor een holding is de beste maatstaf de intrinsieke waarde min een redelijke korting. Bij 18% korting is Sofina niet duur, maar ook geen koopje — en R1 blijft.","mening"),
  K("Intrinsieke waarde"),
  F("Laatst gepubliceerd: **€326,48 per aandeel** (30-6-2026), €11.534 mln.",[1]),
  F("98% van de portefeuille is [[niveau 3|waarde berekend met modellen en schattingen, niet met beurskoersen]] (€11.569 mln van €11.831 mln). Een afwijking van 10% in de fondsrapporten verandert de waarde met ±€597 mln (±5%).",[1]),
  T("Sinds 30-6: SpaceX lager, euro iets sterker, Anthropic hoger gewaardeerd, Sofina betaalde ±€130 mln dividend in mei (al verwerkt). Netto is er geen reden om een sterk andere waarde aan te nemen; ik reken met **€326**.","inschatting"),
  K("Wat is een redelijke korting?"),
  T("Historisch 15–20% (CEO); 2022–2025 meestal 18–32%. Met R1 en 92% niet-genoteerde activa is **20%** een redelijk midden → faire koers nu ±€261 (326 × 0,8).","berekening"),
  {"type":"tabel","titel":"Scenario's eind 2028","kolommen":["Scenario","Intrinsieke waarde","Korting","Koers","Kans"],
   "rijen":[["Slecht","±€280","35%","€180","25%"],["Normaal","±€360","20%","€290","50%"],["Goed","±€400","12%","€350","25%"]],"bron_tekst":"Eigen berekening (inschatting) op basis van halfjaarverslag 2026"},
  T("Verwachte koers (gewogen): 0,25×180 + 0,5×290 + 0,25×350 ≈ **€278** (+4%), plus ±€7,5 bruto dividend over 2 jaar. Dat is mager voor het risico.","berekening"),
  K("Koopzone, koersdoel, stop-loss"),
  L([I("**Koopzone €220–240**: korting 26–33%, rond de steun van €238,8.","berekening"),
     I("**Koersdoel €290** (normaal scenario).","inschatting"),
     I("**Stop-loss €214** (−20%); technisch €234 (net onder steun €238,8).","berekening")]),
  KD("mening","**Afwachten — 4/10.** R1 maakt dit een NO-GO tenzij de rest uitzonderlijk is. Dat is niet zo: degelijk bestuur en herinvestering (+), maar geen defensief profiel, een waarde die je niet zelf kan controleren, veel AI-gevoeligheid en een korting die al kleiner is dan gemiddeld. De score zou ±6 zijn zonder R1.","Oordeel")
 ]})
S.append({"id":"techniek","titel":"Koers & techniek","kort":"Stijgende trend; steun €238,8; stop-loss €214",
 "inhoud":[
  F("Koers €267,6 (6-11-2026). 52 weken: €207,8–285,0. [[SMA200|gemiddelde koers van de laatste 200 beursdagen]] €236,6 en SMA50 €255,4 → **stijgende trend**.",[12]),
  graf_koers,
  {"type":"kerncijfers","items":[
    {"naam":"Rendement 1 jaar","waarde":"+11,1%","trend":"op","label":"feit","bronnen":[12]},
    {"naam":"Rendement 5 jaar","waarde":"−29,4%","trend":"neer","label":"feit","bronnen":[12]},
    {"naam":"Volatiliteit","waarde":"21,3%/jaar","trend":"gelijk","label":"feit","toelichting":"[[volatiliteit|hoe sterk de koers schommelt]]","bronnen":[12]},
    {"naam":"Grootste daling 5 j","waarde":"−60,3%","trend":"neer","label":"feit","toelichting":"van €432 (eind 2021)","bronnen":[12]}]},
  F("Steunniveaus: €238,8 (2-9-2026), €212,0 (11-6-2026), €203,6 (30-3-2026).",[12]),
  T("Cycliciteit: de koers volgt de technologiecyclus (top 2021, bodem 2022, zijwaarts 2023–2025, herstel 2026). Na +25% in 6 maanden is een terugval naar de steun van €238,8 niet ongewoon.","mening")
 ]})
S.append({"id":"expert","titel":"Kritische expertblik","kort":"Pre-mortem: AI-correctie + dollar + bredere korting",
 "inhoud":[
  K("Pre-mortem: stel dat Sofina in 2028 50% lager staat"),
  T("Meest waarschijnlijke oorzaak: een **correctie bij AI- en techwaarderingen** (Anthropic/OpenAI/SpaceX/ByteDance), samen met een zwakkere dollar. De fondsen waarderen met vertraging af, de markt rekent het onmiddellijk in, en de korting schiet terug naar 35–40% zoals in 2022. Een halvering vraagt dan 'maar' −25% intrinsieke waarde en een korting van 40%.","inschatting"),
  K("Wat ziet de markt mogelijk over het hoofd?"),
  L([I("Positief: Sofina zit vroeg in enkele van de grootste bedrijven ter wereld (via topfondsen). Beursgangen maken die waarde zichtbaar en liquide.","mening"),
     I("Negatief: de waarde is grotendeels een schatting van fondsbeheerders die zelf belang hebben bij hoge waarderingen; afgeleide producten beperken de winst op beursgenoteerde posities.","mening"),
     I("Negatief: de kapitaalverhoging onder de intrinsieke waarde toont dat de familie verwatering aanvaardt als ze kansen ziet — en ze kan het opnieuw doen.","mening")]),
  K("Waar ben ik het minst zeker van?"),
  T("De echte waarde van ByteDance en de AI-fondsposities: Sofina publiceert geen bedragen per bedrijf, en schattingen van derden lopen ver uiteen.","mening")
 ]})
S.append({"id":"profiel","titel":"Toets aan jouw profiel","kort":"R1 NO-GO; herinvestering ✅; niet defensief; AI-hype-gevoelig",
 "inhoud":[
  L([I("❌ **R1**: consortium Boël 54,6% → NO-GO tenzij uitzonderlijk.","feit",[9]),
     I("✅ **Herinvestering**: ±99% van de waarde blijft in het bedrijf; langetermijnvisie van een familie die al 5 generaties actief is.","berekening"),
     I("❌ **Niet defensief**: groeibedrijven, durfkapitaal, tech. Het familiebedrijvendeel (Drylock, Nuxe, scholen) is wel stabieler.","mening"),
     I("⚠️ **Hype**: een groeiend deel zit in AI-bedrijven met zeer hoge waarderingen (Anthropic, OpenAI). Geen hypebedrijf zelf, wel hype-gevoelig.","mening"),
     I("✅ **Crypto**: geen crypto als kernactiviteit gevonden in de grootste posities.","feit",[1]),
     I("✅ R2/R3/R4: geen zelfverrijking, geen vertrekpremies, geen rechtszaken gevonden.","mening"),
     I("💶 Fiscaal: 30% roerende voorheffing op het dividend; beurstaks bij aankoop/verkoop; geen Reynderstaks (geen fonds).","mening")]),
  T("Vergelijking met je ervaringen: Sofina lijkt meer op **Ørsted** (2021) dan op DEME — een kwaliteitsbedrijf dat in 2021 met een premie noteerde en daarna −50% deed. Wie toen kocht, staat nog altijd verlies.","mening")
 ]})
r["secties"]=S
r["review"]={"status":"bezig","rondes":[]}
r["bronnen"]=B
json.dump(r,open(f'{ROOT}/rapporten/SOF.BR/2026-11-08/rapport.json','w'),ensure_ascii=False,indent=1)
print("ok")
