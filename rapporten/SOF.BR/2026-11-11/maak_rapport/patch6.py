# Update 2026-11-11: teamreview ronde 1 verwerken
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-11/rapport.json'
r=json.load(open(P))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
def U(t): return {"type":"uitleg","tekst":t}
REPL=[("hooguit ±1,5% per jaar","hooguit ±1,6% per jaar"),("hooguit ±**1,5% per jaar**","hooguit ±**1,6% per jaar**"),
 ("verwacht rendement ±1,5% per jaar","verwacht rendement ±1,6% per jaar"),
 ("Staartrisico:","[[Staartrisico|klein maar ernstig risico op een extreme daling]]:"),
 ("92% van de portefeuille is niet-beursgenoteerd (je kan","92% van de bezittingen heeft geen beurskoers (je kan"),
 ("(economisch, 'fully diluted';","([[economisch belang|jouw deel van de winst en waarde, los van stemrecht]], met alle toekomstige aandelen meegeteld;"),
 ("(economisch belang, 30-6-2026)","(economisch belang, alle toekomstige aandelen meegeteld, 30-6-2026)"),
 ("drukt de waarderingsmultiples","drukt de [[waarderingsmultiples|hoeveel keer de winst of omzet beleggers voor een bedrijf betalen]]"),
 ("Februari 2026: secundaire verkoop ByteDance-aandelen","Februari 2026: [[secundaire verkoop|bestaande aandeelhouders verkopen aandelen aan anderen, zonder nieuw geld voor het bedrijf]] van ByteDance-aandelen"),
 ("ECB: rente naar 2,5%","[[ECB|Europese Centrale Bank, bepaalt de rente in de eurozone]]: rente naar 2,5%"),
 ("de markt rekent op een verhoging op 17-12","de markt houdt rekening met een verhoging op 17-12, al besliste de ECB op 29-10 nog unaniem om niet te verhogen"),
 ("EUR/USD rond 1,13 begin november","[[EUR/USD|hoeveel dollar je krijgt voor één euro]] rond 1,13 begin november"),
 ("lagere softwaremultiples","lagere waarderingen van softwarebedrijven"),
 ("Sinds 30-6: SpaceX lager,","Sinds 30-6: SpaceX eerst lager en nu weer boven zijn introductieprijs,")]
def walk(o):
    if isinstance(o,str):
        for a,b in REPL: o=o.replace(a,b)
        return o
    if isinstance(o,dict): return {k:(v if k in ('x','waarden','bronnen') else walk(v)) for k,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    return o
r=walk(r)
r["bronnen"]+= [
 {"id":39,"titel":"SpaceX turns a profit after a string of losses as its satellite and computer leasing businesses soar","uitgever":"AP (via Spectrum News 13)","type":"nieuws","url":"https://mynews13.com/fl/orlando/ap-top-news/2026/10/20/spacex-turns-a-profit-after-a-string-of-losses-as-its-satellite-and-computer-leasing-businesses-soar","datum":"2026-10-20"},
 {"id":40,"titel":"SpaceX shares climb as Q3 turns to profit","uitgever":"RTTNews","type":"nieuws","url":"https://www.rttnews.com/3700949/spacex-shares-climb-as-q3-turns-to-profit-on-connectivity-si-strength.aspx","datum":"2026-10-21"}]
a=r["advies"]
a["reden"]="Regel **R1 is geraakt**: een consortium van drie vennootschappen rond de familie Boël heeft samen **54,6%**. De rest is degelijk maar niet uitzonderlijk: verwacht rendement ±1,6% per jaar, 92% van de bezittingen heeft geen beurskoers (de waarde is dus een schatting), en de waarderingen van AI-bedrijven schommelen sterk."
a["stop_loss"]={"waarde":184,"uitleg":"Verkoop als de koers 20% onder je aankoopprijs zakt. Koop je in de koopzone (€220–240), dan is dat €176–192. Koop je toch nu aan €270,4, dan is dat €216."}
for o in a["score_opbouw"]["onderdelen"]:
    if o["naam"].startswith("Waardering"): o["uitleg"]="17% korting ligt binnen Sofina's normale bereik; vergelijkbare holdings zijn goedkoper. Verwacht rendement hooguit ±1,6% per jaar."
    if o["naam"].startswith("Risico"): o["uitleg"]="92% van de bezittingen heeft geen beurskoers (de waarde is een schatting), ±65% in dollar, grote gevoeligheid voor AI- en techwaarderingen; de uitverkoop van 5 november zit nog niet in de cijfers."
s=r["samenvatting"]
s[2]["tekst"]="[[Verwacht rendement|gemiddelde van de drie scenario's, gewogen met hun kans]] over 2 jaar: hooguit ±**1,6% per jaar** (koers + dividend), met ±30% kans op een daling naar ±€180 (−33%). De recente schommelingen bij AI-bedrijven zitten nog niet in Sofina's cijfers."

# wijzigingen
r["wijzigingen"]=[
 U("Dit is een update van het rapport van 8 november 2026. Het belangrijkste eerst: **het advies blijft Afwachten (niet kopen), 4/10.** Het goede en het slechte nieuws van de voorbije dagen heffen elkaar ongeveer op, en het advies hangt vooral aan regel R1 (54,6% bij het consortium rond de familie Boël) — en dat is niet veranderd. Sofina publiceerde zelf geen nieuwe cijfers; die komen pas op 24-3-2027."),
 {"type":"lijst","items":[
  I("**Koers** van €267,6 (6-11) naar **€270,4** (9-11, laatste beschikbare slotkoers). De korting op de intrinsieke waarde kromp van 18% naar **17%** — maar die waarde dateert van 30-6, dus de korting is in werkelijkheid onzeker.","berekening",[12]),
  I("**Verwacht rendement** daalt van ±2% naar **±1,6% per jaar**: de koers staat iets hoger, terwijl de scenario's gelijk blijven.","berekening"),
  I("**Anthropic** (maker van de AI-assistent Claude; Sofina bezit het enkel onrechtstreeks via fondsen) gaat naar de beurs. De verwachte prijs ($70–78 per aandeel) komt neer op een bedrijfswaarde van ±$1,26 tot $1,405 biljoen, tegenover $965 mld bij de geldronde van mei. Beleggers hadden eerder op meer gehoopt. Notering naar verluidt op 19-11.","feit",[37,16]),
  I("Gevolg voor Sofina: klein en pas later zichtbaar, naar schatting enkele tienden van een procent extra waarde (Sofina publiceert geen bedrag per bedrijf).","inschatting"),
  I("**Markt**: op 5-11 zakten technologie- en chipaandelen fors. Volgens Reuters vreesden beleggers na de overwinning van de Democraten bij de [[tussentijdse verkiezingen|Amerikaanse verkiezingen halverwege de ambtstermijn van de president]] voor strengere AI-regels en een tragere bouw van datacenters. Op 6-11 herstelden ze deels. Door sterke banencijfers zagen beleggers toen ±78% kans op een Amerikaanse renteverhoging in december — en hogere rente drukt de waarde van groeibedrijven, waarvan Sofina er veel bezit.","feit",[38]),
  I("**Rode vlaggen**: ongewijzigd. Bij de toezichthouder FSMA en op de website van Sofina vond ik (gecontroleerd op 11-11) geen nieuwe meldingen van aan- of verkopen door bestuurders en geen nieuwe meldingen van grote aandeelhouders.","feit",[11,9])]}]

sec={x["id"]:x for x in r["secties"]}
for x in sec["keten"]["inhoud"]:
    t=x.get("tekst","")
    if t.startswith("Niveau 2 — SpaceX"):
        x["tekst"]="Niveau 2 — SpaceX ging op 12-6-2026 naar de Nasdaq aan $135 per aandeel ($1,77 biljoen) en zakte in juli onder die introductieprijs. Op 20-10 meldde SpaceX zijn eerste winst sinds de beursgang (omzet ±$14,6 mld in het derde kwartaal) en het aandeel noteerde weer boven $135. Vroege beleggers mogen gespreid verkopen ([[lock-up|periode waarin bestaande aandeelhouders niet mogen verkopen]]); de laatste grote vrijgave valt rond 180 dagen na de beursgang, begin december."
        x["bronnen"]=[15,39,40]
    if t.startswith("Gaat Anthropic naar de beurs"):
        x["tekst"]="Gaat Anthropic naar de beurs aan $1,26–1,4 biljoen, dan is dat ±31–45% boven de ronde van mei. Sofina houdt Anthropic enkel via fondsen en publiceert geen bedrag; als Anthropic 1–2% van de portefeuille zou zijn, gaat het om ±0,3–0,9% extra intrinsieke waarde — positief maar klein, en pas zichtbaar als de fondsen herwaarderen."
for x in sec["actualiteit"]["inhoud"]:
    if x.get("type")!="lijst": continue
    its=x["items"]
    for it in its:
        if it["tekst"].startswith("Juni 2026: SpaceX"):
            it["tekst"]="Juni 2026: SpaceX naar de beurs aan $1,77 biljoen; in juli onder de introductieprijs, na de eerste winst (20-10) weer erboven."; it["bronnen"]=[15,39,40]
        if it["tekst"].startswith("**5-11-2026"):
            it["tekst"]=it["tekst"].replace("Aanleiding: de overwinning","Aanleiding volgens Reuters: de overwinning")
        if it["tekst"].startswith("6-11-2026: gedeeltelijk herstel"):
            it["tekst"]="6-11-2026: gedeeltelijk herstel; chipbedrijven stegen in de loop van de dag ±4%. Door sterke banencijfers zagen beleggers volgens Reuters toen ±78% kans op een Amerikaanse renteverhoging in december (een momentopname)."
        if it["tekst"].startswith("Afloop van de gespreide lock-ups"):
            it["tekst"]="Laatste grote vrijgave van SpaceX-aandelen voor vroege beleggers rond begin december 2026 (180 dagen na de beursgang): mogelijk verkoopdruk."
    x["items"]=[it for it in its if not it["tekst"].startswith("17-12-2026: ECB-vergadering")]
    for it in x["items"]:
        if it["tekst"].startswith("December 2026: mogelijke renteverhogingen"):
            it["tekst"]="December 2026: mogelijke renteverhogingen door zowel de ECB (vergadering 17-12) als de Amerikaanse centrale bank; hogere rente drukt de waardering van groeibedrijven."
for x in sec["waardering"]["inhoud"]:
    t=x.get("tekst","")
    if t.startswith("Verwachte koers (gewogen)"):
        x["tekst"]="Verwachte koers (gewogen): 0,30×180 + 0,45×290 + 0,25×350 ≈ **€272** (+0,6% t.o.v. €270,4), plus ±€7,3 bruto dividend over 2 jaar → ±3,3% in 2 jaar = **±1,6% per jaar** vóór belastingen. Mager voor het risico. Dit is eerder een bovengrens: als de intrinsieke waarde nu al 5% lager ligt (en alle scenario's dus ook), kom je op ±−2% in 2 jaar."
    if x.get("type")=="tabel" and x.get("noot","").startswith("Startpunt"):
        x["noot"]="Startpunt: intrinsieke waarde €326 (30-6-2026). Als die nu al 5% lager ligt (±€310), worden de scenario's ±€173 / €274 / €334 en is het verwachte rendement licht negatief."
r["review"]={"status":"bezig","rondes":[]}
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch6 ok')
