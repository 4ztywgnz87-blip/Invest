# Leesbaarheid (feedback gebruiker 2026-11-11, voorstel V1)
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-08/rapport.json'
r=json.load(open(P))
def U(t): return {"type":"uitleg","tekst":t}
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
sec={s["id"]:s for s in r["secties"]}

# ---------- rode vlaggen
v={x["regel"]:x for x in r["rode_vlaggen"]}
r1=v["R1"]["uitleg"]
v["R1"]["uitleg"]=[
 F("**Wat is er aan de hand?** Drie vennootschappen rond de familie Boël hebben afgesproken om als één blok te handelen. Samen bezitten ze meer dan de helft van alle aandelen van Sofina.",[9,3]),
 T("**Waarom is dat een probleem voor jou?** Wie meer dan de helft heeft, beslist alleen: over het bestuur, het dividend, nieuwe aandelen en eventueel een bod om alle andere aandeelhouders uit te kopen. Als kleine aandeelhouder kan je niets afdwingen, en omdat maar ±39% vrij verhandeld wordt, is de handel in het aandeel beperkter.","inschatting"),
 T("**Hoe erg is het?** Dit raakt jouw harde regel **R1** (meer dan 49% in één hand of samen): normaal niet kopen, tenzij al de rest uitzonderlijk goed is. Tot nu toe gedroeg het blok zich correct — zelfde voorwaarden voor iedereen bij de kapitaalverhoging, geen verdachte transacties — maar dat is vertrouwen, geen garantie.","mening"),
 F("**De details.** "+r1[0]["tekst"]+" "+r1[1]["tekst"],[9,3,10])]
r6=v["R6"]["uitleg"]
v["R6"]["uitleg"]=[
 F("**Wat is er aan de hand?** In oktober 2025 haalde Sofina €545 mln nieuw geld op door nieuwe aandelen uit te geven — goedkoper dan wat een aandeel volgens Sofina zelf waard was.",[3]),
 T("**Waarom is dat een probleem voor jou?** Als nieuwe aandelen goedkoper worden uitgegeven dan ze waard zijn, wordt elk bestaand aandeel een beetje minder waard ([[verwatering|elk bestaand aandeel krijgt een kleiner deel van de waarde]]). Wie niet meedeed en zijn voorrangsrechten niet verkocht, verloor zo ±2%. De raad mag dit opnieuw doen zonder dat de aandeelhouders moeten stemmen.","berekening"),
 T("**Hoe erg is het?** Middelmatig (regel **R6**: kapitaalacties). De reden — extra geld om te kunnen investeren als er kansen zijn — is begrijpelijk, maar het toont dat de familie verwatering aanvaardt als ze dat nuttig vindt.","mening"),
 dict(r6[0],tekst="**De details.** "+r6[0]["tekst"]), r6[1], r6[2], r6[3]]
r5=v["R5"]["uitleg"]
v["R5"]["uitleg"]=[
 F("**Wat is er aan de hand?** Enkele bestuurders kochten dit jaar kleine pakketjes aandelen. De CEO en een andere leider verkochten aandelen die ze via hun verloning (opties) kregen.",[11]),
 T("**Waarom is dat belangrijk voor jou?** Aankopen door mensen van binnenuit tonen vertrouwen; verkopen kunnen ook gewoon het verzilveren van verloning zijn. Hier gaat het vooral om dat laatste, maar de CEO verkocht in 2026 wel meer dan hij in 2025 bijkocht.","mening"),
 T("**Hoe erg is het?** Ter info (regel **R5**: insiders melden). Geen alarmsignaal.","mening"),
 dict(r5[0],tekst="**De details.** "+r5[0]["tekst"]), r5[1]]
r4=v["R4"]["uitleg"]
v["R4"]["uitleg"]=[
 F("**Wat is er aan de hand?** Er zijn geen rechtszaken tegen Sofina gevonden. "+r4[0]["tekst"],[3,1]),
 dict(r4[1],tekst="**Wel om te weten:** "+r4[1]["tekst"])]

# ---------- helpers
def ins(sid, plan):
    """plan: lijst (index, blok) — invoegen vóór het blok op die (oude) index."""
    inh=sec[sid]["inhoud"]
    for i,b in sorted(plan,key=lambda x:-x[0]): inh.insert(i,b)

# bestuur
b=sec["bestuur"]["inhoud"]
b[3]["tekst"]="Het blok houdt al jaren ongeveer even veel aandelen: 54,60% in 2022 en 2023, 54,93% in 2024 (Union Financière Boël kocht toen bij) en opnieuw 54,60% na de kapitaalverhoging van 2025, waarbij het blok iets minder dan zijn deel bijkocht (1.220.965 nieuwe aandelen)."
b[14]["tekst"]=b[14]["tekst"].replace("Zie de rode vlaggen bovenaan. ","")
ins("bestuur",[
 (0,U("Dit deel gaat over wie Sofina controleert, wie het bedrijf leidt en hoeveel de leiding verdient. Dat is belangrijk voor jou, want het bepaalt of kleine aandeelhouders eerlijk behandeld worden (jouw regels R1 tot R6).")),
 (2,U("Eerst de vraag wie de baas is. De tabel toont de drie vennootschappen die samen als één blok handelen, en hoe hun aandelen in oktober 2026 onderling verschoven.")),
 (3,U("Wat zie je hier? Samen houden ze telkens 54,6%; enkel de verdeling binnen het blok veranderde. Dat blok is al jaren stabiel:")),
 (6,U("Naast de aandeelhouders is de raad van bestuur belangrijk: die moet het management controleren namens álle aandeelhouders, ook de kleine.")),
 (8,U("Dan de verloning. Hier kijk ik of de leiding zichzelf overdreven betaalt (regel R2) of bij vertrek een premie krijgt (regel R3).")),
 (9,T("Voor een investeringsbedrijf van deze grootte is die verloning niet overdreven, en het grootste deel hangt af van de prestaties. Hoe dat in de praktijk uitpakte:","mening")),
 (14,U("De andere regels (rechtszaken, insiders, kapitaalacties) staan uitgebreid bij de rode vlaggen bovenaan. Hier enkel de aanvulling over de eigen aandelen die Sofina inkoopt."))])

# cijfers
ins("cijfers",[
 (0,U("Bij een gewoon bedrijf kijk je naar omzet en winst. Sofina is een investeringsholding: ze verkoopt geen producten, maar bezit stukken van andere bedrijven en fondsen. Daarom is het belangrijkste cijfer hier de intrinsieke waarde per aandeel — wat al die bezittingen samen waard zijn, min de schulden — en hoe de beurskoers zich daartegenover gedraagt.")),
 (2,U("De grafiek zet twee dingen naast elkaar: wat een aandeel volgens Sofina waard was, en wat je er aan het einde van elk jaar op de beurs voor betaalde.")),
 (3,U("Wat zie je hier? In 2021 betaalde de beurs méér dan de waarde (een premie). Daarna zakte de koers veel harder dan de waarde, en sindsdien noteert het aandeel onder zijn waarde (een korting). Zo groot was dat verschil elk jaar:")),
 (4,U("De tabel hieronder geeft de belangrijkste cijfers van de laatste vijf jaar. Het nettoresultaat is bij Sofina vooral de waardestijging of -daling van haar bezittingen, en schommelt daarom sterk van jaar tot jaar.")),
 (7,U("Waarom ging de waarde op en neer? Sofina splitst dat zelf op: hoeveel kwam van de bedrijven zelf, en hoeveel van de wisselkoersen.")),
 (10,U("Een holding kost ook geld — personeel, kantoren, onderzoek — en die kosten gaan van jouw rendement af.")),
 (13,U("Hoeveel heeft Sofina geleend? Weinig schuld betekent dat een slechte periode het bedrijf niet in de problemen brengt.")),
 (16,U("Tot slot: wat krijg je als aandeelhouder jaarlijks uitbetaald?"))])

# investeringen
ins("investeringen",[
 (0,U("Je profiel vindt het positief als een bedrijf zijn winst herinvesteert in plaats van alles uit te keren. Dit deel toont waarin Sofina investeert en hoeveel ze uitkeert.")),
 (2,U("Sofina werkt op drie manieren, van groot en stabiel tot klein en risicovol. De tabel toont hoeveel geld er in elke manier zit.")),
 (3,U("Wat zie je hier? De helft zit in fondsen van andere beheerders (vooral Amerikaanse durfkapitaalfondsen), de andere helft in rechtstreekse belangen in bedrijven.")),
 (5,U("Sofina koopt en verkoopt voortdurend. Dit waren de belangrijkste bewegingen van de laatste anderhalf jaar.")),
 (9,U("Houdt Sofina haar winst echt in? Het antwoord is genuanceerd:"))])

# keten
k=sec["keten"]["inhoud"]
k[1]=T("Als de dollar 10% zakt, daalt de intrinsieke waarde met ongeveer 6%. Als de fondsbeheerders hun waarderingen met 10% verlagen, kost dat ongeveer 5%. Een daling van ByteDance met 30% kost 1,5 tot 3%. En als de tien grootste bedrijven in de fondsen (vaak AI-bedrijven) 20% zakken, kost dat ongeveer 2%.","berekening")
ins("keten",[
 (0,U("Sofina is zo goed als haar bezittingen. Dit deel bekijkt de grootste posities één voor één, en daarna wat die zelf beïnvloedt. Zo zie je waar het risico echt zit.")),
 (1,U("Hoe gevoelig is Sofina voor schokken? Een paar rekenvoorbeelden:")),
 (4,U("ByteDance (het moederbedrijf van TikTok) is de grootste positie en dus het belangrijkste om te begrijpen.")),
 (10,U("Via de fondsen bezit Sofina kleine stukjes van enkele van de bekendste techbedrijven ter wereld. Samen zijn de tien grootste daarvan ongeveer 10% van Sofina's waarde.")),
 (16,U("Cognita was lang een van de grootste posities, maar het loopt er minder goed.")),
 (18,U("Dit zijn familiebedrijven waarin Sofina een groot minderheidsbelang heeft. Ze zijn minder spectaculair, maar stabieler.")),
 (22,U("Tot slot drie kleinere, maar bekende namen uit de top 10."))])

# sector
ins("sector",[
 (0,U("Hoe verhoudt Sofina zich tot vergelijkbare holdings? Bijna alle holdings noteren onder hun intrinsieke waarde. De vraag is dus of Sofina's korting groot of klein is in vergelijking.")),
 (2,U("Wat zie je hier? Sofina's korting is kleiner dan die van GBL, Brederode en Exor — Sofina is dus relatief niet goedkoop. Over vijf jaar deed Sofina's koers het slechtst van deze groep.")),
 (5,U("Wat speelt er in de sector zelf?"))])

# actualiteit
ins("actualiteit",[
 (0,U("Wat gebeurde er de voorbije jaren, wat speelt er nu, en wat komt eraan? Ik zocht systematisch naar alles waaraan Sofina en haar grootste posities blootstaan: de dollar, de rente, AI-bedrijven, China en de oorlog in de Golf.")),
 (2,U("De gebeurtenissen die de laatste jaren het meeste impact hadden:")),
 (4,U("Wat speelt er nu, de laatste maanden:")),
 (6,U("Wat staat er de komende twee jaar op de agenda, en wat zou het kunnen betekenen:"))])

# earnings call
ins("earnings_call",[
 (0,U("Twee keer per jaar legt de leiding de cijfers uit aan analisten, die kritische vragen mogen stellen. Hoe de leiding antwoordt, zegt iets over hoe open en zeker ze is.")),
 (2,U("Dit was de boodschap van de CEO:")),
 (4,U("De analisten stelden enkele lastige vragen. Hier telkens de vraag en het antwoord:"))])

# waardering
ins("waardering",[
 (0,U("Wat is een aandeel Sofina waard, en welke prijs is redelijk? Bij een holding vertrek je van de intrinsieke waarde en trek je er een redelijke korting van af, omdat je de bezittingen niet zelf kan verkopen en de familie de controle heeft.")),
 (2,U("Eerst het vertrekpunt: wat zegt Sofina zelf?")),
 (6,U("Hoeveel korting is redelijk? Dat bepaalt welke koers fair is.")),
 (7,U("Op basis daarvan maakte ik drie scenario's voor eind 2028: wat als het slecht, normaal of goed gaat?")),
 (8,U("Wat zie je hier? In het normale scenario stijgt de koers naar ±€290, maar het slechte scenario ligt ver onder de huidige koers. Gewogen met de kansen levert dat weinig op:")),
 (10,U("Wat betekent dat concreet, als je ondanks R1 toch zou willen kopen?"))])

# techniek
ins("techniek",[
 (0,U("De koersgrafiek zegt niets over de waarde van het bedrijf, maar helpt om de trend, de schommelingen en een verkooplimiet (stop-loss) te bepalen. In jouw profiel is dit ondersteunend.")),
 (2,U("Wat zie je hier? Een sterke daling na eind 2021, enkele jaren zijwaarts, en in 2026 een herstel. De horizontale lijnen tonen de steun en de stop-loss bij aankoop nu."))])

# expert, profiel
ins("expert",[(0,U("Hier kijk ik als een sceptische belegger: wat kan er misgaan, wat ziet de markt mogelijk over het hoofd, en waar ben ik zelf niet zeker van? Alles in dit deel is mening of inschatting."))])
ins("profiel",[(0,U("Tot slot de toets aan jouw eigen voorkeuren en harde regels."))])

json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch3 ok')
# volledige zinnen i.p.v. telegramstijl
r=json.load(open(P)); sec={s["id"]:s for s in r["secties"]}
c=sec["cijfers"]["inhoud"]
for x in list(c):
    t=x.get("tekst","")
    if t.startswith("Korting/premie:"):
        x["tekst"]="In 2021 betaalde je op de beurs **28% méér** dan de intrinsieke waarde. Daarna was het telkens minder: 26% korting in 2022, 18% in 2023, 30% in 2024, 19% in 2025 en 32% op 30-6-2026. Met de koers van nu (€267,6) is de korting **18%**."
    if t.startswith("Bedrijfskosten 2025"): x["bronnen"]=[3]
    if t.startswith("Kosten 2025 en 2024 uit de resultatenrekening"): c.remove(x)
for x in sec["investeringen"]["inhoud"]:
    if x.get("tekst","").startswith("Regio:"):
        x["tekst"]="Geografisch zit 42% in Noord-Amerika, 35% in Europa en 23% in Azië. Slechts 8% is beursgenoteerd; 92% niet. In dollar staat €7.632 mln van de €11.831 mln, ongeveer 65%."
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('zinnen ok')
