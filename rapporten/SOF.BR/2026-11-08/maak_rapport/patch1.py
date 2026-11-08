import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-08/rapport.json'
r=json.load(open(P))
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
sec={s["id"]:s for s in r["secties"]}

# ---- bronnen: verwijder 26, voeg nieuwe toe
r["bronnen"]=[b for b in r["bronnen"] if b["id"] not in (24,26)]
for b in r["bronnen"]:
    if b["id"]==13: b["titel"]="Transcript analistencall halfjaar 2026 (kop op de pagina zegt foutief 'H1 2025'; inhoud is H1 2026)"
    if b["id"]==11: b["titel"]="Meldingen transacties leidinggevenden Sofina 2024–2026"; b["document"]="FSMA-meldingen sofina-1 t/m -70"; b["url"]="https://www.fsma.be/en/manager-transaction/sofina-69"; b["datum"]="2026-10-27"
    if b["id"]==24: b["titel"]="Exor H1 2026 results (persbericht)"
    if b["id"]==9: b["document"]="Aandeelhoudersstructuur + lijst transparantiemeldingen"
nieuw=[
 (26,"Transparantiemelding BlackRock (persbericht 28-09-2026)","Sofina","primair","https://www.sofinagroup.com/~/media/Files/S/Sofina-Corp/shareholding-structure/sofina-sa-press-release-publication-regarding-a-transparency-statement-28-09-2026.pdf","2026-09-28"),
 (27,"Nasdaq 100 suffers worst day since 2020","investingLive","nieuws","https://investinglive.com/stocks/nasdaq-100-suffers-worst-day-since-2020/","2026-11-05"),
 (28,"AI giant Anthropic files for an IPO that could break records","OPB / NPR","nieuws","https://www.opb.org/article/2026/10/26/ai-giant-anthropic-files-for-an-ipo-that-could-break-records/","2026-10-26"),
 (29,"Following Anthropic, OpenAI files confidentially for IPO","TechCrunch","nieuws","https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/","2026-06-08"),
 (30,"Eurozone inflation hits fresh three-year high","Trading Economics","data","https://tradingeconomics.com/euro-area/inflation-cpi/news/598103","2026-11-04"),
 (31,"Sofina ziet waardering Cognita dalen door mislukte verkoopsdeal","Bolero","nieuws","https://www.bolero.be/nl/analyse-en-inzicht/blog/sofina-ziet-waardering-cognita-dalen-door-mislukte-verkoopsdeal","2025-08-20"),
 (32,"ByteDance valuation said to hit record US$550 billion in proposed equity sale (Reuters)","South China Morning Post","nieuws","https://www.scmp.com/tech/big-tech/article/3344631/bytedance-valuation-said-hit-record-us550-billion-proposed-equity-sale","2026-02-25"),
 (33,"Oil flows are up as Iran war turmoil eases: why do prices keep rising?","Al Jazeera","nieuws","https://aljazeera.com/economy/2026/10/30/oil-flows-are-up-as-iran-war-turmoil-eases-why-do-prices-keep-rising","2026-10-30"),
 (34,"Meerwaardebelasting goedgekeurd door het parlement","KPMG België","analyse","https://kpmg.com/be/nl/insights/my-tax-compass-de-trends-die-op-uw-fiscale-radar-moeten-staan/people-services-updates/meerwaardebelasting-goedgekeurd-door-het-parlement.html","2026-04"),
 (35,"Financiële kalender","Sofina","primair","https://www.sofinagroup.com/en/investors/financial-calendar","2026-11-08"),
 (36,"Exor H1 FY26: NAV per share drops 3.9% to EUR 157.9","VZ VermögensZentrum","nieuws","https://www.vermoegenszentrum.ch/en/stock-exchange-and-markets/news/exor-h1-fy26-net-loss-widens-eur-112-billion-nav-share-drops-39-eur","2026-09"),
]
for i,t,u,ty,url,dt in nieuw: r["bronnen"].append({"id":i,"titel":t,"uitgever":u,"type":ty,"url":url,"datum":dt})

# ---- advies
a=r["advies"]
a["score"]=4
a["reden"]="Regel **R1 is geraakt**: een consortium van drie vennootschappen rond de familie Boël heeft samen **54,6%**. De rest is degelijk maar niet uitzonderlijk: verwacht rendement ±2% per jaar, 92% van de portefeuille is niet-beursgenoteerd en de AI-uitverkoop van 5 november raakt de waarde nog met vertraging."
a["koopzone"]={"van":220,"tot":240}
a["koersdoel"]=290
a["koersdoel_uitleg"]="normaal scenario, eind 2028: intrinsieke waarde ±€360 (+4%/jaar) met 20% korting"
a["stop_loss"]={"waarde":184,"uitleg":"Bij aankoop in de koopzone (€220–240): −20% = €176–192 (midden €184); technisch net onder de steun van €212 → ±€205. Wie toch nu koopt aan €267,6: −20% = €214."}
a["scenarios"]=[
 {"naam":"Slecht","koers":180,"kans":"30%","uitleg":"Bredere techcorrectie (zoals begonnen op 5-11-2026) en zwakkere dollar: intrinsieke waarde −14% naar ±€280 en de korting loopt op tot 35% (zoals 2022–2024). Staartrisico: een herhaling van 2022 (waarde −25%, korting 40%) geeft ±€147 — kans ±10% (mening), zit hier in."},
 {"naam":"Normaal","koers":290,"kans":"45%","uitleg":"Intrinsieke waarde +4%/jaar naar ±€360 eind 2028 (onder het 10-jaarsgemiddelde, boven de laatste 4 jaar), korting 20%."},
 {"naam":"Goed","koers":350,"kans":"25%","uitleg":"Intrinsieke waarde +8%/jaar (≈ het 10-jaarsgemiddelde van 8,4%) naar ±€400, geholpen door beursgangen (Anthropic, ByteDance) en verkopen boven boekwaarde; korting 12%."}]

# ---- aandeelhouders
ah=r["aandeelhouders"]
ah["verdeling"][-1]={"naam":"Vrij verhandelbaar","pct":38.55,"vrij_verhandelbaar":True}
ah["verdeling"].insert(4,{"naam":"BlackRock, Inc. (passieve vermogensbeheerder)","pct":3.01,"stemrecht_pct":3.13,"structuur":"transparantiemelding 28-9-2026: 2,24% aandelen + 0,77% via gelijkwaardige financiële instrumenten"})
ah["bronnen"]=[9,3,10,26]
ah["uitleg"]=("Drie vennootschappen vormen samen de 'referentieaandeelhouder', een [[consortium|groep aandeelhouders die wettelijk als één blok handelt]] rond de familie Boël: samen **54,6% van alle aandelen** en (berekend, zonder eigen aandelen) **±56,8% van de stemmen**. Union Financière Boël is de familieholding; van de twee andere is niet publiek wie ze controleert, maar de FSMA noemt ze 'nauw verbonden' met een bestuurder. Eén aandeel = één stem, geen dubbel stemrecht. Op 5-10-2026 kocht Union Financière Boël 681.752 aandelen van de twee andere leden (à €250,51): het blok blijft even groot, maar UFB wordt de grootste (berekend ±24,3%). BlackRock meldde op 28-9-2026 3,01% (als indexbeheerder, geen strategisch belang).")

# ---- rode vlaggen
rv=r["rode_vlaggen"]
rv[0]["titel"]="Consortium rond de familie Boël controleert 54,6%"
rv[0]["uitleg"][1]=F("Het consortium bestaat sinds 2007. CEO Harold Boël zit in de raad van bestuur; Union Financière Boël zelf werd in 2026 voorgedragen als bestuurder en meldt zich bij de FSMA als lid van het bestuursorgaan. De raad vond een [[relationship agreement|schriftelijke afspraak tussen bedrijf en hoofdaandeelhouder over hoe zij met elkaar omgaan]] 'niet nodig'.",[3,10])
rv[0]["uitleg"].insert(2,T("Gevolgen voor jou: de vrije handel is klein (±39%), en het consortium kan in theorie een [[uitkoopbod|bod om alle andere aandeelhouders uit te kopen]] doen op een moment dat het hen past (bv. bij een grote korting).","inschatting"))
rv[1]["uitleg"]=[F("Op 7-10-2025 gaf Sofina 2.446.428 nieuwe aandelen uit à **€223** (totaal €545,6 mln, kosten €7,5 mln) via een [[claimemissie|kapitaalverhoging waarbij bestaande aandeelhouders voorrang krijgen om bij te kopen]], onder zowel de beurskoers als de intrinsieke waarde. Sofina noemt zelf de 'mechanische verwatering' van de intrinsieke waarde per aandeel en corrigeerde er de bonusberekening voor. Reden: extra slagkracht om 'doorheen cycli' te investeren.",[3]),
 T("Sofina's eigen correctie (ANAVPS €304,85 + 2 × €3,50 dividend ≈ €312 vs. werkelijk €305,77) toont ±2% verwatering voor wie niet meedeed en zijn rechten niet verkocht.","berekening"),
 T("Er blijft nog ±€18,2 mln nominaal toegestaan kapitaal (±7,8 mln nieuwe aandelen = ±21% van het huidige aantal): de raad kan dus opnieuw kapitaal ophalen zonder AVA.","berekening"),
 F("Toegestaan kapitaal resterend €18.225.130 (machtiging tot mei 2028).",[3])]
rv[2]={"ernst":"info","regel":"R5","titel":"Insiders: kleine aankopen bestuurders; CEO en leiders verkopen optie-aandelen",
 "uitleg":[F("Bestuurders kochten in 2026 kleine posten: Charlotte Strömberg (toen vicevoorzitter) 450 aandelen à €210,60 (31-3), Leslie Teo 100 à €209 (31-3), Charles Peugeot 178 à €224,66 en zijn vennootschap Gatopardi 183 à €222,49 en 118 à €251,69 (juni–sept). Bij de claimemissie (sept 2025) schreven CEO Harold Boël (15.923 aandelen, €3,55 mln), Maxence Tombeur (821), voorzitter Lancksweert (142) en andere leiders kleine aantallen in.",[11]),
  F("CEO Harold Boël oefende in 2026 **28.000** [[opties|recht om aandelen te kopen aan een vooraf vastgelegde prijs]] uit à €128,12 en verkocht **18.000** aandelen (jan–okt, à €238,77–€261,36) voor samen **€4,44 mln**; voor 10.000 uitgeoefende opties (4-9-2026) is geen verkoop gemeld. Leider Edward Koopman verkocht in oktober 2.500 aandelen (€0,66 mln) na optie-uitoefening.",[11]),
  T("Deze verkopen horen bij de optieverloning, maar zijn in 2026 groter dan de inschrijving van de CEO in 2025. Geen alarmsignaal, wel geen teken van extra vertrouwen bij deze koers.","mening")]}
rv[3]["uitleg"]=[F("Zoekbasis: jaarverslagen 2021–2025, halfjaarverslag 2026 en nieuws in NL/FR/EN. Daarin vond ik geen lopende of afgesloten rechtszaak tegen Sofina zelf.",[3,1]),
 T("Wel lopen er groepsvorderingen tegen TikTok/ByteDance (privacy, verslaving bij jongeren) — dat raakt Sofina enkel onrechtstreeks via de waarde van ByteDance.","inschatting")]

# ---- samenvatting (kort)
r["samenvatting"]=[
 F("Sofina is een Brusselse [[investeringsholding|bedrijf dat geld belegt in andere bedrijven en fondsen]]. Haar [[intrinsieke waarde|wat alle bezittingen min de schulden waard zijn, volgens Sofina zelf]] was €326 per aandeel op 30-6-2026 (4 maanden oud). De koers (€267,6) ligt **18% lager**.",[1,12]),
 F("**R1 geraakt (NO-GO):** een consortium rond de familie Boël bezit 54,6% (meer dan de 49%-grens).",[9]),
 T("Verwacht rendement over 2 jaar: ±**2% per jaar** (koers + dividend), met ±30% kans op een daling naar ±€180 (−33%).","berekening"),
 T("Positief: lage schuld, een stabiele familie-aandeelhouder en topfondsen. Negatief: 92% van de portefeuille is niet-beursgenoteerd (je kan de waarde niet zelf nagaan), 65% in dollar, veel gevoeligheid voor AI- en techwaarderingen, en geen [[defensief|bedrijf in een sector die weinig last heeft van een slechte economie]] profiel.","mening"),
 KD("mening","**Afwachten (niet kopen: R1) — 4/10.** Wie R1 bewust aanvaardt: pas bij een korting van ±26% of meer (koers €220–240).","Oordeel")]

# ---- verkoopsignalen
r["verkoopsignalen"]=[
 "Korting op de intrinsieke waarde onder **10%** of een premie (zoals 2021) → winst nemen. *Controle: koers vs. laatste NAV (24-3-2027 en 2-9-2027).*",
 "Twee halfjaren na elkaar **negatieve waardecreatie zonder valuta-effect**. *Controle: presentatie bij het (half)jaarverslag.*",
 "[[LTV|schuld gedeeld door de waarde van de portefeuille]] boven **10%** of een nieuwe kapitaalverhoging onder de intrinsieke waarde. *Controle: (half)jaarverslag, persberichten.*",
 "Sofina meldt een **grote afwaardering van ByteDance** of vermeldt een tweede positie boven 5%. *Controle: top-10-pagina in het (half)jaarverslag.*",
 "Het consortium Boël verandert van koers: **uitkoopbod**, belang boven 60% of vrije handel onder 35%. *Controle: website Sofina (aandeelhoudersstructuur), FSMA.*",
 "Koers sluit onder je **stop-loss** (−20% onder je aankoopprijs; bij aankoop €220–240 is dat €176–192)."]

# ---- bestuur
b=sec["bestuur"]["inhoud"]
for x in b:
    if x.get("type")=="tekst" and x["tekst"].startswith("13 bestuurders"):
        x["tekst"]="Op 31-12-2025: 13 bestuurders, waarvan 8 onafhankelijk; voorzitter en CEO zijn verschillende personen. Op de AVA van 13-5-2026 vertrokken Dominique Lancksweert (voorzitter, 29 jaar) en Nicolas Boël; voorgedragen waren o.a. Union Financière Boël (vertegenwoordigd door Pascal Hubinont) en Charles Peugeot (onafhankelijk). Charlotte Strömberg werd voorzitter. Harold Boël werkt sinds 2004 bij Sofina en is CEO sinds 2008 (mandaat tot 2028)."
    if x.get("type")=="tekst" and x["tekst"].startswith("Het langetermijnplan"):
        x["tekst"]=("Het [[langetermijnplan (LTIP)|bonus die pas na 4 jaar uitbetaald wordt, afhankelijk van de prestaties]] 2022–2025 betaalde **niets** uit omdat Sofina slechter deed dan de wereldindex (MSCI ACWI). Wel vestigde 31,2% van de 'overgangs-PSU's' 2024–2025; in 2025 werd zo €565.593 aan de CEO uitbetaald. Er zijn **geen contractuele vertrekvergoedingen** (wettelijke regels blijven gelden). Er is geen [[clawback|recht om uitbetaalde bonussen terug te vorderen]] — een afwijking van de Belgische code.")
    if x.get("type")=="tekst" and x["tekst"].startswith("Zie de rode vlaggen"):
        x["tekst"]="Zie de rode vlaggen bovenaan. Eigen aandelen (voor de optieplannen): 2025 189.068 gekocht en 236.640 afgestaan; eerste helft 2026 243.753 gekocht en 111.359 afgestaan; 1.367.697 eigen aandelen op 30-6-2026. Machtiging tot inkoop van max. 20% loopt tot mei 2028."
        x["bronnen"]=[3,1]
    if x.get("type")=="tekst" and x["tekst"].startswith("Geen andere aandeelhouder"):
        x["tekst"]="In 2025 meldde geen andere aandeelhouder een belang boven 3%; op 28-9-2026 meldde BlackRock 3,01%. Vrij verhandelbaar eind 2025: 42,04%."
        x["bronnen"]=[3,26]
# ---- cijfers
c=sec["cijfers"]["inhoud"]
for x in c:
    if x.get("type")=="tekst" and x["tekst"].startswith("2025: waardecreatie"):
        x["tekst"]="2025: [[waardecreatie|hoeveel de portefeuille in waarde won, na aankopen en verkopen]] +1,9%, maar **+10,1% zonder [[valuta-effect|winst of verlies door wisselkoersen, vooral de dollar]]**; de zwakkere dollar kostte €925 mln. Eerste helft 2026: waardecreatie +8,1% (zonder valuta +6,0%), intrinsieke waarde per aandeel +6,8%; de fondsen deden +16,1%, de rechtstreekse belangen maar +0,9%."
    if x.get("type")=="tekst" and x["tekst"].startswith("Over 10 jaar"):
        x["tekst"]="Over 10 jaar gemiddeld 8,4% per jaar; over de 4 jaar 2022–2025 (gemeten vanaf de piek van eind 2021) −1,4% per jaar, 9,9 procentpunt per jaar slechter dan de wereldindex MSCI ACWI in euro."
    if x.get("type")=="tekst" and x["tekst"].startswith("Bedrijfskosten 2025"):
        x["tekst"]="Bedrijfskosten 2025 €69,5 mln in de resultatenrekening (2024: €63,5 mln) ≈ **0,66%** van de gemiddelde intrinsieke waarde; in kasstroom betaald €74,2 mln (2024: €61,2 mln). Daarbovenop betalen de fondsen beheerkosten en [[carried interest|winstdeel voor de fondsbeheerder, meestal 20% van de winst]]; die zitten al verrekend in de waarde en zijn niet apart zichtbaar — de echte kost ligt dus hoger."
    if x.get("type")=="tekst" and x["tekst"].startswith("Twee obligaties"):
        x["tekst"]="Twee [[obligaties|leningen die Sofina op de kapitaalmarkt opnam]]: €700 mln aan 1,000% (vervalt 2028) en €600 mln aan 3,707% (vervalt 2033). Niet-gebruikte kredietlijnen €1.375 mln. Netto schuld €219 mln = **[[LTV|schuld gedeeld door de waarde van de portefeuille]] 1,9%**. Nog niet opgevraagde verplichtingen: **€1.456 mln** (waarvan €1.449 mln aan fondsen)."
    if x.get("type")=="tekst" and x["tekst"].startswith("Sofina mikt"):
        x["tekst"]="Sofina mikt op een netto schuld van 5–10% van de portefeuille; [[kredietrating|oordeel van S&P over hoe veilig Sofina's schuld is]] A− (sinds 24-9-2025)."
        x["bronnen"]=[13,1]
c.insert(5,T("Let op: de koersen zijn jaareindes (H1 2026 = 30-6). Sinds 30-6 steeg de koers ±20%; de korting kromp vooral door die koersstijging, niet door een hogere intrinsieke waarde. Bij een intrinsieke waarde die nu 5% lager/hoger ligt, is de korting −14% / −22%.","berekening"))
# extra tabelrijen
for x in c:
    if x.get("type")=="tabel" and x["titel"].startswith("Kerncijfers"):
        x["rijen"].append(["Dividend per aandeel (over het jaar)*","3,13","3,24","3,35","3,50","3,66","—"])
        x["rijen"].append(["LTV","−2,9%","−2,6%","−2,2%","−3,3%","−4,1%","+1,9%"])
        x["noot"]+=" *Dividend over het jaar wordt het jaar erna betaald. LTV berekend als netto schuld / portefeuille (negatief = netto kas)."
# ---- investeringen herinvestering
inv=sec["investeringen"]["inhoud"]
inv[0]=T("**Kern:** Sofina keert weinig uit t.o.v. haar waarde (±1,1% per jaar) en houdt het meeste in. Maar het dividend is niet gedekt door de inkomsten: het wordt betaald uit verkopen van deelnemingen.","mening")
inv[-1]=T("Dividend ±€130 mln per jaar = ±1,1% van de intrinsieke waarde. Over 2021–2025 was het nettoresultaat samen ±€2,09 mld en het betaalde dividend ±€0,55 mld: ±75% ingehouden. Maar in 2025 was het dividend (€115,8 mln) groter dan de winst (€113 mln) en de ontvangen dividenden (±€49 mln) dekken het niet. Over 2021–2025 investeerde Sofina €4,9 mld en verkocht ze €5,0 mld: netto verkoper; groei kwam uit waardestijging en sinds 2025 uit nieuw kapitaal en schuld.","berekening")
for x in inv:
    if x.get("type")=="tekst" and x["tekst"].startswith("2025: €1.139"):
        x["tekst"]="2025: €1.139 mln geïnvesteerd en €845 mln verkocht; nieuw o.a. Proeduca, Stream, Scalable Capital, PostHog, Qargo. Eerste helft 2026: €733 mln geïnvesteerd en €237 mln verkocht; nieuw o.a. Cerealis, XBOW, Eye Security, Supabase, Primer. Verkopen: SES, Honasa (Mamaearth), deel van Lenskart; [[dividend recap|bedrijf leent geld en keert dat uit aan de aandeelhouders]] bij opseo en Nuxe. Na 30-6: verkoopovereenkomsten voor Salto en Kopi Kenangan (onder voorwaarden), nieuwe investering in Exein."
# ---- keten
ke=sec["keten"]["inhoud"]
for x in ke:
    t=x.get("tekst","")
    if t.startswith("Niveau 2 — TikTok VS"):
        x["tekst"]="Niveau 2 — TikTok VS: op 22-1-2026 werd de TikTok USDS [[joint venture|gezamenlijke onderneming van meerdere eigenaars]] opgericht; ByteDance houdt minder dan 20%, Oracle, Silver Lake en MGX elk 15%. Het algoritme wordt van ByteDance in licentie genomen."
    if t.startswith("Het politieke risico in de VS"):
        x["tekst"]="Het politieke risico in de VS lijkt kleiner geworden, maar China (grootste markt) en de regelgeving rond jongeren blijven de grote onzekerheden."
    if t.startswith("Niveau 2 — SpaceX"):
        x["tekst"]="Niveau 2 — SpaceX ging op 12-6-2026 naar de Nasdaq aan $135 per aandeel ($1,77 biljoen) en zakte binnen een maand onder die introductieprijs. Andere vroege beleggers zitten gespreid tot 180 dagen vast ([[lock-up|periode waarin bestaande aandeelhouders niet mogen verkopen]])."
    if t.startswith("Niveau 2 — Anthropic"):
        x["tekst"]="Niveau 2 — Anthropic haalde in mei 2026 $65 mld op aan een waardering van $965 mld (Sequoia mee-leider) en maakte op 26-10-2026 zijn beursprospectus publiek (Nasdaq, 'ANT'); een notering kan al in november, maar datum en prijs liggen niet vast."
        x["bronnen"]=[16,28,17]
    if t.startswith("Niveau 2 — OpenAI"):
        x["tekst"]="Niveau 2 — OpenAI: $122 mld opgehaald aan $852 mld (maart 2026); diende op 8-6-2026 vertrouwelijk een beursgang in, timing onbekend."
        x["bronnen"]=[18,29]
    if t.startswith("Belang 18,96%"):
        x["tekst"]="Belang ±14,06% (economisch, 'fully diluted'; 18,96% van de tussenholding Lernen Midco 1) sinds 2019. Eind 2025 de 2de grootste rechtstreekse positie, midden 2026 de 6de. Een verkoop van een meerderheidsbelang (biedingen tot €6 mld) mislukte in 2025, o.a. door de btw op Britse privéschoolgelden; de waardering werd verlaagd. CEO: Cognita 'had het moeilijker om te groeien'."
        x["bronnen"]=[3,1,31,13]
    if t.startswith("Nuxe (natuurcosmetica"):
        x["tekst"]="Nuxe (natuurcosmetica, FR) 49%; Drylock (luiers/hygiëne, BE) 25%; Proeduca (online hoger onderwijs, ES) 17,22% sinds 2025; Cambridge Associates (vermogensbeheer, VS) 21,40% (economisch belang, 30-6-2026)."
        x["bronnen"]=[1]
    if t.startswith("Vinted (tweedehandskleding"):
        x["tekst"]="Vinted (tweedehandskleding, LT) 2,88%; Mérieux NutriSciences (voedingsveiligheidslabo's) 15,49%; Cleo AI (AI-financiële assistent, VK). Voor Salto (elektronische sloten) werd na 30-6-2026 een verkoopovereenkomst getekend; volgens het hoofd financiën zat die waarde al in de cijfers van juni."
        x["bronnen"]=[1,13]
ke.insert(4,F("ByteDance-marktreferentie: volgens Reuters bood General Atlantic in februari 2026 aandelen aan tegen een waardering tot $550 mld (uitkomst niet bevestigd).",[32]))
ke.insert(1,T("Wat kost wat? Dollar −10% → intrinsieke waarde ±−6%. Fondsrapporten −10% → ±−5%. ByteDance −30% → −1,5% tot −3% (positie 5–10%). Top-10 bedrijven in de fondsen (o.a. AI) −20% → ±−2%.","berekening"))
# ---- sector
se=sec["sector"]
se["kort"]="Holdings noteren met 20–55% korting; Sofina is de meest 'tech'"
se["inhoud"][0]=T("**Kern:** bijna alle holdings noteren onder hun intrinsieke waarde. Sofina's korting (−18%) is nu kleiner dan die van GBL, Brederode en Exor — Sofina is dus relatief niet goedkoop, al ligt de korting wel in Sofina's eigen historische bereik (15–20%).","mening")
se["inhoud"][1]["bronnen"]=[12,25,1,22,23,36]
se["inhoud"][1]["noot"]="*Korting = koers t.o.v. laatst gepubliceerde intrinsieke waarde per aandeel op 30-6-2026 (Sofina 326,48; GBL 100,77; Brederode 154,6; Exor 157,9) — berekend en verouderd, dus een benadering. Rendementen zonder dividend. Bij AvH vond ik geen recente intrinsieke waarde. Investor AB (Zweden) en Eurazeo/Wendel liet ik weg: geen recente intrinsieke waarde met bron gevonden en minder gelijkend (weinig durfkapitaal)."
# ---- actualiteit
ac=sec["actualiteit"]["inhoud"]
ac[2]["items"].insert(2,I("2025: verkoop van een meerderheidsbelang in Cognita (biedingen tot €6 mld) mislukt; waardering verlaagd.","feit",[31]))
ac[2]["items"].append(I("Februari 2026: secundaire verkoop ByteDance-aandelen aan een waardering tot $550 mld (Reuters).","feit",[32]))
nu=[I("Juni 2026: SpaceX naar de beurs aan $1,77 biljoen; binnen een maand onder de introductieprijs.","feit",[15]),
 I("Golfoorlog VS–Iran: olie boven $100 in september; eind oktober stromen de olietransporten weer meer, maar de prijs blijft hoog.","feit",[20,33]),
 I("ECB: rente naar 2,5% in september, behouden op 29-10. Inflatie eurozone oktober **4,0%** (hoogste in 3 jaar); de markt rekent op een verhoging op 17-12.","feit",[20,19,30]),
 I("EUR/USD rond 1,13 begin november (30-6: 1,139). Een euro die 10% stijgt, kost Sofina ±€694 mln (±6% van de waarde).","feit",[21,1]),
 I("5-10-2026: herschikking binnen het consortium Boël (UFB kocht 681.752 aandelen van de twee andere leden, ±€171 mln).","feit",[10]),
 I("26-10-2026: Anthropic maakte zijn beursprospectus publiek; notering mogelijk nog in november.","feit",[28]),
 I("**5-11-2026: AI- en chipuitverkoop in de VS** — Nasdaq 100 −6,4%, slechtste dag sinds 2020; chipbedrijven tot −12%.","feit",[27]),
 I("Die daling raakt de AI-posities in de fondsen pas met vertraging in Sofina's cijfers (fondsrapporten zijn 3–6 maanden oud). De korting van 18% houdt daar nog geen rekening mee.","inschatting")]
ac[4]["items"]=nu
ac[6]["items"]=[
 I("Anthropic-beursgang (mogelijk november 2026, na de uitverkoop onzeker): herwaardering van de fondsposities, met vertraging en lock-ups. Sofina houdt Anthropic enkel via fondsen.","inschatting"),
 I("Afloop van de gespreide lock-ups bij SpaceX (tot 180 dagen na 12-6-2026, dus rond december 2026): mogelijk verkoopdruk.","inschatting"),
 I("17-12-2026: ECB-vergadering; een renteverhoging drukt de waardering van groeibedrijven.","inschatting"),
 I("ByteDance: een beursgang is volgens de CEO de meest waarschijnlijke uitweg, maar timing onbekend; China–VS-spanningen blijven het risico.","inschatting"),
 I("2028: obligatie van €700 mln (1%) vervalt. Herfinancieren aan ±3,7% kost ±€19 mln extra rente per jaar (±0,2% van de waarde).","berekening"),
 I("Nog €1,46 mld te storten in fondsen de komende jaren: verplicht geld, ook in een slechte markt (gedekt door kas €1,08 mld + kredietlijnen €1,375 mld).","feit",[1,2]),
 I("Volgende cijfers: jaarverslag 2026 op 24-3-2027, AVA 13-5-2027, halfjaar 2-9-2027.","feit",[35])]
# ---- techniek
te=sec["techniek"]["inhoud"]
te[0]["tekst"]="Koers €267,6 (6-11-2026, net na de start van de AI-uitverkoop). 52 weken: €207,8–285,0. [[SMA200|gemiddelde koers van de laatste 200 beursdagen]] €236,6 en SMA50 €255,4 → **stijgende trend**, maar die kan snel keren als de techcorrectie doorzet."
# ---- waardering
wa=sec["waardering"]["inhoud"]
for x in wa:
    t=x.get("tekst","")
    if t.startswith("Sinds 30-6"):
        x["tekst"]="Sinds 30-6: SpaceX lager, euro iets sterker, Sofina betaalde ±€130 mln dividend in mei (al verwerkt), en op 5-11 een scherpe AI-uitverkoop. De Anthropic-ronde van mei zat grotendeels al in de juni-cijfers. Ik reken met **€326**, maar met een neerwaarts risico van enkele procenten."
    if t.startswith("Historisch 15–20%"):
        x["tekst"]="Historisch 15–20% (CEO); 2022–2025 meestal 18–32%; vergelijkbare holdings 22–35%. Met R1 en 92% niet-genoteerde activa is **20%** een redelijk midden → faire koers nu ±€261 (326 × 0,8). Met de korting van GBL/Brederode (22–35%) zou dat €212–254 zijn."
    if t.startswith("Verwachte koers (gewogen)"):
        x["tekst"]="Verwachte koers (gewogen): 0,30×180 + 0,45×290 + 0,25×350 ≈ **€272** (+2%), plus ±€7,5 bruto dividend over 2 jaar → ±4% in 2 jaar = **±2% per jaar** vóór belastingen. Mager voor het risico."
for x in wa:
    if x.get("type")=="tabel":
        x["rijen"]=[["Slecht","±€280 (−14%)","35%","€180","30%"],["Normaal","±€360 (+4%/jaar)","20%","€290","45%"],["Goed","±€400 (+8%/jaar)","12%","€350","25%"]]
        x["bron_tekst"]="Eigen berekening (inschatting; kansen = mening) op basis van halfjaarverslag 2026"
    if x.get("type")=="lijst":
        x["items"]=[I("**Koopzone €220–240**: korting 26–33% t.o.v. €326 — genoeg marge om bij een normaal verloop ±10%/jaar te halen.","berekening"),
          I("**Koersdoel €290** (normaal scenario).","inschatting"),
          I("**Stop-loss**: −20% onder je aankoopprijs (bij €220–240: €176–192); technisch net onder de steun van €212 (±€205).","berekening")]
    if x.get("type")=="kader":
        x["tekst"]="**Afwachten (niet kopen: R1) — 4/10.** Kwaliteit en prijs samen zouden zonder R1 ±5/10 geven: degelijk bestuur en lage schuld (+), maar geen defensief profiel, een waarde die je niet zelf kan controleren, AI-gevoeligheid en een verwacht rendement van ±2%/jaar. R1 maakt het een NO-GO tenzij de rest uitzonderlijk is — dat is hier niet zo. De koopzone geldt enkel voor wie R1 bewust aanvaardt."
# ---- expert
ex=sec["expert"]["inhoud"]
ex.insert(2,L([I("De vrije handel is klein en het consortium kan ooit een uitkoopbod doen op een moment dat het hen past.","inschatting"),
  I("De €1,46 mld verplichte stortingen moeten ook in een slechte markt betaald worden; kas en kredietlijnen dekken dat, maar dan stijgt de schuld.","inschatting"),
  I("Het valutarisico is groter dan het lijkt: in 2025 was de waardecreatie +10,1% zonder dollareffect en maar +1,9% mét.","feit",[4])],"Bijkomende risico's"))
# ---- profiel
pr=sec["profiel"]["inhoud"]
pr[0]["items"][1]=I("⚠️ **Herinvestering**: Sofina keert weinig uit (±1,1% van de waarde) en hield over 5 jaar ±75% van het resultaat in. Maar het dividend wordt betaald uit verkopen, niet uit inkomsten.","berekening")
pr[0]["items"][3]=I("⚠️ **Hype**: Sofina is zelf geen hypebedrijf, maar via fondsen gevoelig voor dure AI-bedrijven (top-10 fondsposities samen ±10% van de waarde; ByteDance 5–10%).","mening")
pr[0]["items"][6]=I("💶 Fiscaal: 30% [[roerende voorheffing|Belgische belasting op dividenden, wordt automatisch ingehouden]] op het dividend; [[beurstaks|kleine taks bij elke aankoop en verkoop]]; geen Reynderstaks (geen fonds).","mening")
pr.insert(1,F("**Meerwaardebelasting**: sinds 1-1-2026 betaal je in België 10% op gerealiseerde winst op aandelen, met een vrijstelling van €10.000 per persoon per jaar; de waarde op 31-12-2025 geldt als startpunt. Bij een kleine positie blijft de winst tot het koersdoel meestal onder de vrijstelling.",[34]))
pr[-1]["tekst"]="Vergelijking met je ervaringen: zoals **Ørsted** in 2021 noteerde Sofina toen met een premie (+28%) en zakte daarna meer dan 50%. Verschil: Sofina noteert nu met korting en is gespreid over ±90 bedrijven en ±90 fondsen, Ørsted was één verhaal. Met **DEME** (je beste belegging) heeft Sofina weinig gemeen: DEME is een industrieel bedrijf met zichtbare orders en kasstromen."
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
