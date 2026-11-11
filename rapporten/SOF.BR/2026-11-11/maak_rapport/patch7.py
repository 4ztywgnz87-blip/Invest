# Update 2026-11-11: teamreview ronde 2 verwerken
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-11/rapport.json'
r=json.load(open(P))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
def U(t): return {"type":"uitleg","tekst":t}
sec={x["id"]:x for x in r["secties"]}
ke=sec["keten"]["inhoud"]
for i,x in enumerate(ke):
    t=x.get("tekst","")
    if t.startswith("Niveau 2 — SpaceX"):
        ke[i:i+1]=[
         F("Niveau 2 — SpaceX ging op 12-6-2026 naar de Nasdaq aan $135 per aandeel ($1,77 biljoen) en zakte binnen een maand onder die introductieprijs. Andere vroege beleggers mogen pas na een gespreide [[lock-up|periode waarin bestaande aandeelhouders niet mogen verkopen]] van tot 180 dagen verkopen.",[15]),
         F("Op 20-10-2026 meldde SpaceX winst na een reeks verliezen, met een omzet van ±$14,6 mld in het derde kwartaal; op 21-10 noteerde het aandeel ±$161 in de handel buiten de beursuren, boven de introductieprijs. Een recentere koers (na de uitverkoop van 5-11) vond ik niet.",[39,40]),
         T("180 dagen na de beursgang is ±9 december 2026: dan kunnen meer vroege beleggers verkopen, wat de koers kan drukken.","inschatting")]
        break
for x in ke:
    if x.get("tekst","").startswith("Gaat Anthropic naar de beurs"):
        x["tekst"]="Gaat Anthropic naar de beurs aan $1,26–1,4 biljoen, dan is dat ±31–46% boven de ronde van mei. Sofina houdt Anthropic enkel via fondsen en publiceert geen bedrag; als Anthropic 1–2% van de portefeuille zou zijn, gaat het om ±0,3–0,9% extra intrinsieke waarde — positief maar klein, en pas zichtbaar als de fondsen herwaarderen."
for x in sec["actualiteit"]["inhoud"]:
    if x.get("type")!="lijst": continue
    for it in x["items"]:
        if it["tekst"].startswith("Juni 2026: SpaceX"):
            it["tekst"]="Juni 2026: SpaceX naar de beurs aan $1,77 biljoen; binnen een maand onder de introductieprijs, op 21-10 (na winstcijfers) weer erboven."
        if it["tekst"].startswith("Laatste grote vrijgave van SpaceX"):
            it["tekst"]="Rond 9 december 2026 (180 dagen na de beursgang) mogen meer vroege SpaceX-beleggers verkopen: mogelijk verkoopdruk."
for x in sec["waardering"]["inhoud"]:
    if x.get("tekst","").startswith("Sinds 30-6"):
        x["tekst"]=x["tekst"].replace("SpaceX eerst lager en nu weer boven zijn introductieprijs","SpaceX eerst lager en op 21-10 weer boven zijn introductieprijs")
for x in sec["techniek"]["inhoud"]:
    if x.get("tekst","").startswith("Stop-loss:"):
        x["tekst"]="Stop-loss: verkoop als de koers 20% onder je eigen aankoopprijs zakt (bij aankoop nu €216, in de koopzone €176–192). Kocht je in de koopzone, dan ligt het slechte scenario (€180) ongeveer op je stop-loss; bij een plotse koersval kan je wel onder je stop-loss verkopen."
a=r["advies"]
a["stop_loss"]["uitleg"]="Verkoop als de koers 20% onder je aankoopprijs zakt. Het getal €184 geldt bij aankoop op €230 (midden van de koopzone); bij aankoop op €220–240 is het €176–192. Koop je toch nu aan €270,4, dan is het €216."
w=r["wijzigingen"]
w[0]["tekst"]="Dit is een update van het rapport van 8 november 2026. Het belangrijkste eerst: **het advies blijft Afwachten (niet kopen), 4/10.** Er was gemengd nieuws (een AI-uitverkoop, maar ook een hoge waardering voor Anthropic), maar weinig dat Sofina wezenlijk verandert. Het advies hangt vooral aan [[R1|jouw harde regel: niet kopen als één blok meer dan 49% van de aandelen heeft]] — 54,6% bij het consortium rond de familie Boël — en dat is niet veranderd. Sofina publiceerde zelf geen nieuwe cijfers; die komen pas op 24-3-2027."
its=w[1]["items"]
its[0]["tekst"]="**Koers** van €267,6 (6-11) naar **€270,4** (9-11, laatste beschikbare slotkoers). De korting op de intrinsieke waarde (de waarde die Sofina zelf berekent) kromp van 18% naar **17%** — maar die waarde dateert van 30-6, dus de echte korting is onzeker."
its[1]["tekst"]="**Verwacht rendement** (het gemiddelde van de drie scenario's, gewogen met hun kans) daalt van ±2% naar **±1,6% per jaar**: de koers staat iets hoger, terwijl de scenario's gelijk blijven. Het risico op een sterke daling zit daar al in."
its[2]["tekst"]="**Anthropic** (maker van de AI-assistent Claude; Sofina bezit het enkel onrechtstreeks via fondsen) gaat naar de beurs. De verwachte prijs ($70–78 per aandeel) waardeert het hele bedrijf op tot $1,405 biljoen, alle toekomstige aandelen meegeteld — onderaan de prijsvork ±$1,26 biljoen (eigen berekening) — tegenover $965 mld bij de geldronde van mei. Beleggers hadden eerder op meer gehoopt. Notering naar verluidt op 19-11."
r["review"]={"status":"afgerond","feiten_gecontroleerd":52,"feiten_correct":48,
 "rondes":[
  {"nr":1,"oordelen":{"financieel-analist":"goedgekeurd met opmerkingen","actua-specialist":"goedgekeurd met opmerkingen","kritische-belegger":"goedgekeurd met opmerkingen"},"opmerkingen":23,"verwerkt":21,"verworpen":2},
  {"nr":2,"oordelen":{"financieel-analist":"goedgekeurd met opmerkingen","actua-specialist":"goedgekeurd met opmerkingen","kritische-belegger":"goedgekeurd met opmerkingen"},"opmerkingen":13,"verwerkt":12,"verworpen":1}],
 "open_punten":[
  "Deze update bouwt verder op het volledig gecontroleerde rapport van 8-11-2026; de open punten van dat rapport blijven gelden (o.a. uitslag AVA mei 2026 niet gevonden).",
  "De koers van SpaceX na de uitverkoop van 5-11 en de exacte data van de SpaceX-lock-ups zijn niet met een primaire bron bevestigd.",
  "Of er tussen 8 en 11 november geen nieuwe meldingen van insiders waren, is niet sluitend te bewijzen (de FSMA-lijst is niet chronologisch); er werd niets gevonden.",
  "De kritische belegger zou de kans op het slechte scenario eerder op 30–35% zetten; dat verandert de score niet."]}
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch7 ok')
