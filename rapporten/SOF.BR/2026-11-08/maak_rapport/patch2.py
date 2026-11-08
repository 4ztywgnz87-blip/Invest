import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-08/rapport.json'
r=json.load(open(P))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
sec={s["id"]:s for s in r["secties"]}
# samenvatting: termen
s=r["samenvatting"]
s[1]["tekst"]="**R1 geraakt — [[NO-GO|volgens jouw harde regels: niet kopen, tenzij al de rest uitzonderlijk goed is]]:** een [[consortium|groep aandeelhouders die wettelijk als één blok handelt]] rond de familie Boël bezit 54,6% (meer dan de 49%-grens)."
s[2]["tekst"]="[[Verwacht rendement|gemiddelde van de drie scenario's, gewogen met hun kans]] over 2 jaar: hooguit ±**2% per jaar** (koers + dividend), met ±30% kans op een daling naar ±€180 (−33%). De AI-uitverkoop van 5-11 zit nog niet in de cijfers."
s[4]["tekst"]="**Afwachten (niet kopen: R1) — 4/10.** Wie R1 bewust aanvaardt: pas in de [[koopzone|prijs waarbij risico en rendement aantrekkelijk worden]] €220–240 (koers ±26% of meer onder de intrinsieke waarde), met een [[stop-loss|koers waarbij je verkoopt om verdere verliezen te beperken]] 20% onder je aankoopprijs."
# rode vlag R6
rv=r["rode_vlaggen"]
rv[1]["uitleg"][0]["tekst"]=rv[1]["uitleg"][0]["tekst"].replace("onder zowel de beurskoers als de intrinsieke waarde. Sofina noemt zelf de 'mechanische verwatering'","onder zowel de beurskoers als de intrinsieke waarde. Sofina noemt zelf de '[[mechanische verwatering|elk bestaand aandeel krijgt een kleiner deel van de waarde omdat nieuwe aandelen goedkoper werden uitgegeven]]'")
rv[1]["uitleg"][1]=F("Voor de bonustest verlaagde Sofina de intrinsieke waarde per aandeel van eind 2024 van €311,77 naar €304,77 (−€7, ±2,2%) om de verwatering uit te zuiveren: zo groot was dus het verlies voor wie niet meedeed en zijn rechten niet verkocht.",[3])
rv[1]["uitleg"][2]=T("Er blijft nog €18,2 mln nominaal [[toegestaan kapitaal|bedrag waarmee de raad zelf, zonder stemming van de aandeelhouders, nieuwe aandelen mag uitgeven]] (±7,8 mln nieuwe aandelen = ±21% van het huidige aantal), waarvan max. €7,97 mln zonder voorrang voor bestaande aandeelhouders. De raad kan dus opnieuw kapitaal ophalen zonder AVA.","berekening")
rv[1]["uitleg"][3]["tekst"]="Toegestaan kapitaal resterend €18.225.130 op 31-12-2025 (limiet zonder voorkeurrecht €7.973.494); machtiging tot mei 2028."
# aandeelhouders eigen aandelen datum
for v in r["aandeelhouders"]["verdeling"]:
    if v.get("eigen_aandelen"): v["naam"]="Eigen aandelen Sofina (14-8-2026)"
# bestuur Strömberg
for x in sec["bestuur"]["inhoud"]:
    if x.get("tekst","").startswith("Op 31-12-2025: 13 bestuurders"):
        x["tekst"]=x["tekst"].replace("Charlotte Strömberg werd voorzitter.","De raad besliste Charlotte Strömberg vanaf die AVA voorzitter te maken (uitslag van de AVA zelf niet gevonden).")
# cijfers: rij hernoemen, dividend ontvangen
for x in sec["cijfers"]["inhoud"]:
    if x.get("type")=="tabel" and x["titel"].startswith("Kerncijfers"):
        for row in x["rijen"]:
            if row[0].startswith("Rendement"): row[0]="Rendement intrinsieke waarde (incl. dividend) — niet de koers"
        pass
# investeringen
iv=sec["investeringen"]
iv["kort"]="Weinig uitgekeerd (±1,1% van de waarde); groei vooral via waardestijging, niet via ingehouden winst"
iv["inhoud"][-1]["tekst"]=iv["inhoud"][-1]["tekst"].replace("en de ontvangen dividenden (±€49 mln) dekken het niet.","en het ontvangen dividend dekt het niet volledig (rechtstreekse belangen ±€49 mln; inclusief fondsen €102,6 mln in de resultatenrekening).")
for x in iv["inhoud"]:
    if x.get("tekst","").startswith("Regio:"):
        x["tekst"]="Regio: Noord-Amerika 42%, Europa 35%, Azië 23%. Beursgenoteerd 8%, niet-genoteerd 92%. In dollar: €7.632 mln van €11.831 mln (±65%)."
# keten: wacht-moment
ke=sec["keten"]["inhoud"]
ke.insert(2,T("Wachtmoment: hoe de Anthropic-beursgang verloopt (volgens media mogelijk nog in november, niet bevestigd) en de intrinsieke waarde van 24-3-2027, die als eerste de AI-correctie van november zal tonen.","inschatting"))
# sector peers noot
se=sec["sector"]["inhoud"]
se[0]["tekst"]+=" Let op: Sofina's koers steeg sinds 30-6 ±20%, terwijl alle kortingen met de intrinsieke waarde van 30-6 berekend zijn."
# actualiteit: oorzaak
ac=sec["actualiteit"]["inhoud"]
for it in ac[4]["items"]:
    if it["tekst"].startswith("**5-11-2026"):
        it["tekst"]="**5-11-2026: AI- en chipuitverkoop in de VS** — [[Nasdaq|Amerikaanse technologiebeurs]] 100 −6,4%, slechtste dag sinds 2020; chipbedrijven tot −12%. Aanleiding volgens de bron: twijfels over AI-investeringen en wat de uitslag van de Amerikaanse tussentijdse verkiezingen (3-11) betekent voor de bouw van datacenters."
ac[6]["items"].insert(2,I("Amerikaans beleid na de tussentijdse verkiezingen kan de AI-investeringen (datacenters, chips) vertragen — dat raakt de duurste fondsposities.","inschatting"))
# techniek
te=sec["techniek"]
te["kort"]="Stijgende trend, maar AI-correctie; steun €238,8; stop-loss −20% onder aankoopprijs"
te["inhoud"][0]["tekst"]=te["inhoud"][0]["tekst"].replace("(6-11-2026, net na de start van de AI-uitverkoop)","(6-11-2026, de dag na de AI-uitverkoop)").replace("SMA50 €255,4","SMA50 (gemiddelde van 50 dagen) €255,4")
for x in te["inhoud"]:
    if x.get("type")=="grafiek":
        x["lijnen"]=[{"naam":"Stop-loss bij aankoop nu (€214)","waarde":214.1},{"naam":"Steun 238,8","waarde":238.8}]
    if x.get("tekst","").startswith("Steunniveaus"):
        x["tekst"]="[[Steunniveaus|koersen waar het aandeel eerder ophield met dalen]]: €238,8 (2-9-2026), €212,0 (11-6-2026), €203,6 (30-3-2026)."
te["inhoud"].append(T("Stop-loss: −20% onder je eigen aankoopprijs (bij aankoop nu €214, in de koopzone €176–192). Het slechte scenario (€180) ligt daar onder; bij een plotse koersval kan je onder je stop-loss verkopen.","berekening"))
# waardering: NAV-startpunt
for x in sec["waardering"]["inhoud"]:
    if x.get("type")=="tabel":
        x["noot"]="Startpunt: intrinsieke waarde €326 (30-6-2026). Als de AI-uitverkoop die met 5% verlaagt (±€310), wordt dit ±€173 / €274 / €334 en is het verwacht rendement ±0% per jaar."
    if x.get("tekst","").startswith("Verwachte koers (gewogen)"):
        x["tekst"]+=" Dit is eerder een bovengrens: bij een startwaarde 5% lager wordt het ±0% per jaar."
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
r=json.load(open(P))
r["review"]={"status":"afgerond","feiten_gecontroleerd":158,"feiten_correct":135,
 "rondes":[
  {"nr":1,"oordelen":{"financieel-analist":"niet goedgekeurd","actua-specialist":"goedgekeurd met opmerkingen","kritische-belegger":"goedgekeurd met opmerkingen"},"opmerkingen":47,"verwerkt":45,"verworpen":2},
  {"nr":2,"oordelen":{"financieel-analist":"goedgekeurd met opmerkingen","actua-specialist":"goedgekeurd met opmerkingen","kritische-belegger":"goedgekeurd met opmerkingen"},"opmerkingen":20,"verwerkt":17,"verworpen":3}],
 "open_punten":[
  "Alle fouten uit de controle (23 van 158 feiten) zijn verbeterd; geen kritieke opmerkingen meer.",
  "De uitslag van de AVA van 13-5-2026 (nieuwe bestuurders) is niet gevonden; benoemingen staan als 'voorgedragen'.",
  "Mogelijke renteverhoging door de Amerikaanse centrale bank in december: enkel via secundaire bronnen gevonden, niet opgenomen.",
  "Enkele feiten steunen op secundaire bronnen (Wikipedia voor de SpaceX-beursgang, VZ VermögensZentrum voor Exor).",
  "De kritische belegger vindt de AI-gevoeligheid nog licht onderschat (Sofina publiceert geen waarde per bedrijf), maar houdt het bij score 4/10."]}
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('review ok')
