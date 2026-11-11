# Update 2026-11-11 (vertrekt van het definitieve rapport van 2026-11-08)
import json
ROOT='/home/user/Invest'
P=f'{ROOT}/rapporten/SOF.BR/2026-11-11/rapport.json'
r=json.load(open(f'{ROOT}/rapporten/SOF.BR/2026-11-08/rapport.json'))
k=json.load(open(f'{ROOT}/data/SOF.BR/koers.json'))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
def U(t): return {"type":"uitleg","tekst":t}

REPL=[("€267,6","€270,4"),("−20% = €214","−20% = €216"),("(€214)","(€216)"),("bij aankoop nu €214","bij aankoop nu €216"),
 ("is de korting **18%**","is de korting **17%**"),("**18% lager**","**17% lager**"),("18% korting ligt","17% korting ligt"),
 ("Sofina's korting (−18%)","Sofina's korting (−17%)"),("De korting van 18% houdt","De korting van 17% houdt"),("Bij 18% korting is","Bij 17% korting is"),
 ("hooguit ±2% per jaar","hooguit ±1,5% per jaar"),("hooguit ±**2% per jaar**","hooguit ±**1,5% per jaar**"),
 ("verwacht rendement ±2% per jaar","verwacht rendement ±1,5% per jaar"),("een verwacht rendement van hooguit ±2% per jaar","een verwacht rendement van hooguit ±1,5% per jaar")]
def walk(o):
    if isinstance(o,str):
        for a,b in REPL: o=o.replace(a,b)
        return o
    if isinstance(o,dict): return {kk:(v if kk in ('x','waarden') else walk(v)) for kk,v in o.items()}
    if isinstance(o,list): return [walk(v) for v in o]
    return o
r=walk(r)

r["meta"]["datum"]="2026-11-11"; r["meta"]["vorig_rapport"]="2026-11-08"
a=r["advies"]; a["koers_nu"]=k["koers"]; a["koers_datum"]="09-11-2026"
a["reden"]="Regel **R1 is geraakt**: een consortium van drie vennootschappen rond de familie Boël heeft samen **54,6%**. De rest is degelijk maar niet uitzonderlijk: verwacht rendement ±1,5% per jaar, 92% van de portefeuille is niet-beursgenoteerd, en de AI-waarderingen schommelen sterk (uitverkoop op 5-11, Anthropic-beursgang rond 19-11)."

# bronnen
r["bronnen"]=[b for b in r["bronnen"] if b["id"] not in (12,17)]
r["bronnen"].append({"id":12,"titel":"Koersdata SOF.BR (opgehaald 11-11-2026)","uitgever":"Yahoo Finance","type":"data","url":"https://finance.yahoo.com/quote/SOF.BR","datum":"2026-11-09"})
for b in r["bronnen"]:
    if b["id"]==25: b["titel"]="Koersdata GBLB.BR, BREB.BR, ACKB.BR, EXO.AS (opgehaald 11-11-2026)"; b["datum"]="2026-11-09"
r["bronnen"]+= [
 {"id":37,"titel":"Anthropic sets IPO price range of $70 to $78, looks to start trading Nov. 19","uitgever":"CNBC","type":"nieuws","url":"https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html","datum":"2026-11-10"},
 {"id":38,"titel":"US STOCKS-Nasdaq rebounds as chip stocks recover from steep losses (Reuters)","uitgever":"Devdiscourse / Reuters","type":"nieuws","url":"https://www.devdiscourse.com/article/international/4002927-us-stocks-nasdaq-rebounds-as-chip-stocks-recover-from-steep-losses","datum":"2026-11-06"}]
r["bronnen"].sort(key=lambda b:b["id"])

# wijzigingen
r["wijzigingen"]=[
 U("Dit is een update van het rapport van 8 november 2026. Er zijn geen nieuwe cijfers van Sofina zelf (de volgende komen op 24-3-2027); wel bewoog de markt en kwam er belangrijk nieuws over Anthropic."),
 L:=None][:1]
r["wijzigingen"]+= [
 {"type":"lijst","items":[
  I("**Advies en score ongewijzigd**: Afwachten (niet kopen: R1), 4/10. De scoreopbouw blijft gelijk.","mening"),
  I("**Koers** van €267,6 (6-11) naar **€270,4** (9-11); de korting op de intrinsieke waarde (van 30-6) kromp van 18% naar **17%**.","berekening",[12]),
  I("**Verwacht rendement** daalt licht naar ±1,5% per jaar, omdat de koers iets hoger staat terwijl de scenario's gelijk blijven.","berekening"),
  I("**Anthropic** legde op 10-11 een prijsvork vast van $70–78 per aandeel, goed voor een waardering tot $1,405 biljoen (volledig verwaterd), tegenover $965 mld in mei. Notering naar verluidt op 19-11.","feit",[37]),
  I("**Markt**: na de AI-uitverkoop van 5-11 herstelden chipbedrijven deels op 6-11; aanleiding van de daling was de overwinning van de Democraten bij de tussentijdse verkiezingen, met vrees voor tragere bouw van datacenters en strengere AI-regels. Beleggers rekenen op ±78% kans op een Amerikaanse renteverhoging in december.","feit",[38]),
  I("**Rode vlaggen**: geen nieuwe FSMA-meldingen van leidinggevenden en geen nieuwe transparantiemeldingen sinds het vorige rapport.","feit",[11,9])]}]

# samenvatting
s=r["samenvatting"]
s[0]["tekst"]=s[0]["tekst"].replace("De koers (€270,4)","De koers (€270,4 op 9-11)")
s[2]["tekst"]="[[Verwacht rendement|gemiddelde van de drie scenario's, gewogen met hun kans]] over 2 jaar: hooguit ±**1,5% per jaar** (koers + dividend), met ±30% kans op een daling naar ±€180 (−33%). De AI-uitverkoop van 5-11 en de Anthropic-beursgang (rond 19-11) zitten nog niet in de cijfers."
sec={x["id"]:x for x in r["secties"]}

# keten: Anthropic
for x in sec["keten"]["inhoud"]:
    if x.get("tekst","").startswith("Niveau 2 — Anthropic"):
        x["tekst"]="Niveau 2 — Anthropic haalde in mei 2026 $65 mld op aan een waardering van $965 mld (Sequoia mee-leider). Op 10-11-2026 legde het de prijsvork voor zijn beursgang vast: $70–78 per aandeel, 825 mln aandelen, een waardering tot $1,405 biljoen (volledig verwaterd). Prijszetting naar verluidt op 18-11 en eerste handelsdag op 19-11 (Nasdaq, 'ANT'). Omzet de eerste negen maanden van 2026: $33,2 mld."
        x["bronnen"]=[16,37]
    if x.get("tekst","").startswith("Wachtmoment:"):
        x["tekst"]="Wachtmoment: de Anthropic-beursgang (prijs rond 18-11, handel rond 19-11) en de intrinsieke waarde van 24-3-2027, die als eerste de AI-correctie van november én de beursgang zal tonen."
ke=sec["keten"]["inhoud"]
for i,x in enumerate(ke):
    if x.get("tekst","").startswith("Niveau 2 — Anthropic"):
        ke.insert(i+1,T("Gaat Anthropic naar de beurs aan $1,3–1,4 biljoen, dan is dat ±40% boven de ronde van mei. Sofina houdt Anthropic enkel via fondsen en publiceert geen bedrag; als Anthropic 1–2% van de portefeuille zou zijn, gaat het om ±0,4–0,8% extra intrinsieke waarde — positief maar klein, en pas zichtbaar als de fondsen herwaarderen.","inschatting"))
        break

# actualiteit Nu
ac=sec["actualiteit"]["inhoud"]
for x in ac:
    if x.get("type")=="lijst":
        for it in x["items"]:
            if it["tekst"].startswith("**5-11-2026"):
                it["tekst"]="**5-11-2026: AI- en chipuitverkoop in de VS** — [[Nasdaq|Amerikaanse technologiebeurs]] 100 −6,4%, slechtste dag sinds 2020; chipbedrijven tot −12%. Aanleiding: de overwinning van de Democraten bij de tussentijdse verkiezingen (ook in staten met veel datacenters), met vrees voor een tragere uitbouw van AI-datacenters en strengere AI-regels."
                it["bronnen"]=[27,38]
            if it["tekst"].startswith("Die daling raakt"):
                idx=x["items"].index(it)
                x["items"][idx+1:idx+1]=[
                 I("6-11-2026: gedeeltelijk herstel; chipbedrijven stegen in de loop van de dag ±4%. Door sterke banencijfers rekenden beleggers op ±78% kans op een Amerikaanse renteverhoging in december.","feit",[38]),
                 I("10-11-2026: Anthropic legde de prijsvork voor zijn beursgang vast ($70–78, tot $1,405 biljoen); handel naar verluidt vanaf 19-11.","feit",[37])]
                break
    if x.get("type")=="lijst" and any(i["tekst"].startswith("Anthropic-beursgang (mogelijk") for i in x["items"]):
        for it in x["items"]:
            if it["tekst"].startswith("Anthropic-beursgang (mogelijk"):
                it["tekst"]="Anthropic-beursgang (rond 19-11-2026): bepaalt mee hoe de AI-posities in de fondsen gewaardeerd worden, maar met vertraging en lock-ups. Een notering onder de verwachting zou het sentiment rond Sofina drukken."
        x["items"].insert(3,I("December 2026: mogelijke renteverhogingen door zowel de ECB (17-12) als de Amerikaanse centrale bank; hogere rente drukt de waardering van groeibedrijven.","inschatting"))

# sector tabel
for x in sec["sector"]["inhoud"]:
    if x.get("type")=="tabel":
        x["titel"]="Vergelijking holdings (koers 09-11-2026)"
        x["rijen"]=[["Sofina","€270,4","−17%","+12%","−32%","1,4%","21%"],["GBL","€79,70","−21%","+14%","+3%","6,4%","16%"],["Brederode","€100,2","−35%","−2%","−18%","1,5%","12%"],["Ackermans & van Haaren","€270,8","n.b.","+21%","+97%","1,7%","23%"],["Exor","€74,35","−53%","−2%","n.b.","0,7%","22%"]]
# waardering
for x in sec["waardering"]["inhoud"]:
    t=x.get("tekst","")
    if t.startswith("Sinds 30-6"):
        x["tekst"]="Sinds 30-6: SpaceX lager, euro iets sterker, Sofina betaalde ±€130 mln dividend in mei (al verwerkt), op 5-11 een scherpe AI-uitverkoop met gedeeltelijk herstel, en Anthropic mikt op een beurswaardering tot $1,4 biljoen (boven de ronde van mei). Die effecten heffen elkaar deels op; ik reken met **€326**, met een neerwaarts risico van enkele procenten."
    if t.startswith("Verwachte koers (gewogen)"):
        x["tekst"]="Verwachte koers (gewogen): 0,30×180 + 0,45×290 + 0,25×350 ≈ **€272** (+0,6% t.o.v. €270,4), plus ±€7,3 bruto dividend over 2 jaar → ±3% in 2 jaar = **±1,5% per jaar** vóór belastingen. Mager voor het risico. Dit is eerder een bovengrens: bij een startwaarde 5% lager wordt het negatief."
# techniek
te=sec["techniek"]["inhoud"]
for i,x in enumerate(te):
    if x.get("type")=="grafiek":
        g=dict(k["grafiek_blok"]); g["lijnen"]=[{"naam":"Stop-loss bij aankoop nu (€216)","waarde":216.3},{"naam":"Steun 238,8","waarde":238.8}]
        te[i]=g
    if x.get("type")=="kerncijfers":
        for it in x["items"]:
            if it["naam"]=="Rendement 1 jaar": it["waarde"]="+12,4%"
            if it["naam"]=="Rendement 5 jaar": it["waarde"]="−31,5%"
    if x.get("tekst","").startswith("Koers €270,4"):
        x["tekst"]="Koers €270,4 (9-11-2026). 52 weken: €207,8–285,0. [[SMA200|gemiddelde koers van de laatste 200 beursdagen]] €236,8 en SMA50 (gemiddelde van 50 dagen) €255,8 → **stijgende trend**, maar die kan snel keren als de techcorrectie doorzet."
r["review"]={"status":"bezig","rondes":[]}
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch5 ok')
