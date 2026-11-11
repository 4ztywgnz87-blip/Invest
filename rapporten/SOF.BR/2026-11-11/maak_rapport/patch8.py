# Actualiteit: besluit + impact per onderwerp (feedback gebruiker 2026-11-11)
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-11/rapport.json'
r=json.load(open(P))
def F(t,b,lab='feit'): return {"type":"tekst","label":lab,"tekst":t,"bronnen":b}
def T(t,lab): return {"type":"tekst","label":lab,"tekst":t,"bronnen":[]}
def I(t,lab,b=None): return {"label":lab,"tekst":t,"bronnen":b or []}
def U(t): return {"type":"uitleg","tekst":t}
def K(t): return {"type":"kop","tekst":t}
def KD(stijl,tekst,titel=None):
    d={"type":"kader","stijl":stijl,"tekst":tekst}
    if titel: d["titel"]=titel
    return d
s=[x for x in r["secties"] if x["id"]=="actualiteit"][0]
oud=s["inhoud"]
lijsten=[b for b in oud if b["type"]=="lijst"]
verleden,nu,komend=lijsten
s["kort"]="Op korte termijn eerder negatief (AI-correctie, rente), met de Anthropic-beursgang als lichtpunt"
s["inhoud"]=[
 U("Dit deel gaat over wat er in de wereld gebeurt en wat dat betekent voor Sofina: wat gebeurde er, wat speelt er nu en wat komt eraan? Eerst het besluit, dan per onderwerp hoe groot de impact is, daarna de tijdlijn en tot slot waar je op moet letten."),
 KD("mening","De actualiteit weegt **op korte termijn eerder negatief** op Sofina. Drie dingen bepalen het meest: (1) de **waardering van AI- en techbedrijven** — die zakte begin november fors, en Sofina zal dat met vertraging in haar cijfers zien; (2) de **rente** — in Europa en de VS komen er mogelijk renteverhogingen, wat groeibedrijven minder waard maakt; en (3) de **dollar** — twee derde van Sofina's bezit zit in dollar, dus een sterkere euro kost geld. Het grootste lichtpunt is de **beursgang van Anthropic**: die bevestigt dat de AI-bedrijven in Sofina's fondsen veel waard zijn, al is het effect voor Sofina klein. Alles samen verandert dit het advies niet, maar het maakt de kans dat de intrinsieke waarde in maart 2027 lager uitvalt iets groter.","Besluit: wat betekent de actualiteit voor Sofina?"),
 K("Impact per onderwerp"),
 U("De tabel zet de belangrijkste onderwerpen naast elkaar: wat er gebeurt, of het goed (▲) of slecht (▼) is voor Sofina, hoe groot de impact kan zijn en waarom. De grootte is een inschatting, onderbouwd met de cijfers uit het rapport."),
 {"type":"tabel","titel":"Wat betekent de actualiteit voor Sofina?","kolommen":["Onderwerp","Wat gebeurt er?","Effect","Hoe groot?","Waarom?"],
  "rijen":[
   ["AI- en techwaarderingen","Uitverkoop op 5-11 (Nasdaq 100 −6,4%), deels herstel op 6-11","▼","Middel","De tien grootste bedrijven in Sofina's fondsen (veel AI) zijn ±10% van haar waarde: −20% daar kost ±2%."],
   ["Beursgang Anthropic","Notering rond 19-11 aan $1,26–1,4 biljoen (mei: $965 mld)","▲","Klein","Zit enkel in de fondsen; geschat +0,3 tot +0,9% intrinsieke waarde, pas later zichtbaar."],
   ["Rente (ECB en VS)","Inflatie eurozone 4,0%; renteverhogingen in december mogelijk","▼","Middel","Hogere rente maakt groeibedrijven minder waard en de herfinanciering van de obligatie in 2028 duurder (±€19 mln per jaar)."],
   ["Dollar","Euro rond 1,13 dollar","▼▲","Groot","±65% van de bezittingen is in dollar: een euro die 10% stijgt kost ±6%, een daling levert evenveel op. In 2025 kostte de dollar €925 mln."],
   ["ByteDance / China–VS","TikTok VS in joint venture (jan 2026); verkoop van aandelen tot $550 mld (feb 2026)","▲","Middel","Grootste positie (5–10%): minder politiek risico en hogere marktprijzen. China blijft de grote onzekerheid."],
   ["SpaceX","Winst in oktober; vroege beleggers mogen rond 9-12 verkopen","▼","Klein","Een van de tien grootste fondsposities; extra aanbod kan de koers tijdelijk drukken."],
   ["Cognita (scholen)","Verkoop mislukte in 2025, groei moeilijker","▼","Klein","Zakte van 2de naar 6de grootste positie; nieuwe afwaardering mogelijk."],
   ["Olie en oorlog in de Golf","Olie boven $100 in september, blijft hoog","▼","Klein","Onrechtstreeks: houdt de inflatie en dus de rente hoog."]],
  "bronnen":[27,38,37,16,30,19,20,21,1,4,14,32,39,40,15,31,13,33],
  "noot":"▲ = goed voor Sofina, ▼ = slecht, ▼▲ = kan beide kanten op. 'Hoe groot' is een inschatting: klein = minder dan 1% van de intrinsieke waarde, middel = 1–5%, groot = meer dan 5%."},
 T("Wat zie je hier? De meeste pijlen wijzen naar beneden, maar bijna allemaal met een kleine of middelgrote impact. De dollar is het onderwerp met de grootste mogelijke impact, in beide richtingen.","mening"),
 K("Tijdlijn: wat gebeurde er?"),
 U("De gebeurtenissen die de laatste jaren het meeste impact hadden:"),
 verleden,
 T("**Wat betekent dit?** Sofina is sterk afhankelijk van de stemming rond technologie: in 2021 betaalde de beurs te veel, in 2022 zakte de koers dubbel zo hard als de waarde. Wie nu instapt, moet zulke schommelingen kunnen dragen.","mening"),
 K("Wat speelt er nu?"),
 U("Wat de laatste maanden gebeurde:"),
 nu,
 T("**Wat betekent dit?** De AI-markt is zenuwachtig geworden net nu Anthropic naar de beurs gaat, en de rente stijgt mogelijk. Sofina's koers steeg sinds de zomer sterk (±20%), terwijl de recente klappen nog niet in haar cijfers zitten — de korting is daardoor waarschijnlijk kleiner dan ze lijkt.","mening"),
 K("Wat komt eraan?"),
 U("Wat de komende twee jaar op de agenda staat:"),
 komend,
 T("**Wat betekent dit?** De komende weken volgen snel enkele belangrijke momenten na elkaar; de eerste cijfers van Sofina waarin je die terugziet, komen pas in maart 2027.","mening"),
 K("Waar moet je op letten?"),
 {"type":"lijst","items":[
  I("**Rond 19-11-2026 — Anthropic op de beurs.** Een vlotte notering boven de prijsvork is goed nieuws voor de stemming rond Sofina; een zwakke start het omgekeerde.","inschatting"),
  I("**Rond 9-12-2026 — SpaceX-aandelen vrij voor vroege beleggers.** Kijk of de koers van SpaceX daarna sterk zakt.","inschatting"),
  I("**17-12-2026 — ECB-vergadering** (en de Amerikaanse centrale bank in december). Een renteverhoging is licht negatief voor Sofina.","inschatting"),
  I("**24-3-2027 — jaarcijfers 2026 van Sofina.** De eerste intrinsieke waarde na de AI-correctie van november: dan zie je of de korting echt zo klein is.","feit",[35])]}]
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch8 ok')

# ---- review KB3/AS3 verwerken
r=json.load(open(P))
s=[x for x in r["secties"] if x["id"]=="actualiteit"][0]
inh=s["inhoud"]
for i,b in enumerate(inh):
    if b["type"]=="kader":
        inh[i]=KD("mening","""Drie dingen wegen het zwaarst:
1. **AI- en techbedrijven** zakten begin november fors. Sofina ziet dat pas later in haar cijfers, omdat de [[fondsen|beleggingsfondsen van andere beheerders waarin Sofina geld steekt]] hun waarde maar om de paar maanden doorgeven.
2. **De rente** stijgt mogelijk in Europa en de VS. Hogere rente maakt groeibedrijven minder waard.
3. **De dollar**: twee derde van Sofina's bezit is in dollar. Die kan de waarde fors doen schommelen, in beide richtingen.
Daartegenover staan de **beursgang van Anthropic** en hogere prijzen voor **ByteDance**: positief, maar klein of onzeker. **Netto: licht negatief.** Bovendien steeg de koers sinds 30-6 met ±21% (van €222,6 naar €270,4), terwijl die klappen nog niet in de cijfers zitten: de korting is waarschijnlijk kleiner dan ze lijkt.
**Gevolg voor het advies: het blijft Afwachten (niet kopen: R1), 4/10.** Wie R1 bewust aanvaardt, wacht op de koopzone (€220–240) of op de jaarcijfers van 24-3-2027.""","Besluit: wat betekent de actualiteit voor Sofina?")
    if b["type"]=="uitleg" and b["tekst"].startswith("De tabel zet"):
        b["tekst"]="De tabel toont per onderwerp of het goed (▲) of slecht (▼) is voor Sofina, hoe groot de impact kan zijn, en waarom. Grootte: **klein** = minder dan 1% van de [[intrinsieke waarde|wat alle bezittingen min de schulden waard zijn, volgens Sofina zelf]], **middel** = 1 tot 3%, **groot** = meer dan 3%. Het zijn inschattingen, onderbouwd met de cijfers uit dit rapport; wat er precies gebeurde, lees je in de tijdlijn verderop."
    if b["type"]=="tabel" and b["titel"].startswith("Wat betekent de actualiteit"):
        b["kolommen"]=["Onderwerp","Effect","Waarom?"]
        b["rijen"]=[
         ["AI- en techbedrijven","▼ middel tot groot (2–5%)","Uitverkoop op 5-11. De tien grootste bedrijven in de fondsen (veel AI) zijn ±10% van Sofina: −20% daar kost ±2%; zakken alle fondsen 10%, dan ±5%."],
         ["Dollar","▼▲ groot (±3% per 5% koersbeweging)","±65% van het bezit is in dollar. Een sterkere euro kost geld, een zwakkere levert op. In 2025 kostte de dollar €925 mln."],
         ["Rente (Europa en VS)","▼ middel","Inflatie in de eurozone 4,0%, verhogingen in december mogelijk. Hogere rente drukt de waarde van groeibedrijven; de nieuwe lening om de obligatie van 2028 af te lossen kost ±€19 mln per jaar extra (klein)."],
         ["Stemming rond Sofina","▼▲ groot (voor de koers)","Zakt de korting terug van 17% naar 25%, dan daalt de koers ±10% zonder dat de waarde verandert (de CEO noemde een korting 'in de twintig' in september)."],
         ["ByteDance (TikTok)","▼▲ middel","Grootste positie (5–10%). Minder politiek risico in de VS en in februari een aandelenverkoop tot $550 mld (uitkomst niet bevestigd), maar ook geraakt door de techdaling: −30% kost 1,5–3%."],
         ["Beursgang Anthropic","▲ klein (geschat 0,3–0,9%)","Prijsvork $70–78, notering gepland rond 19-11. Sofina bezit Anthropic enkel via fondsen; het effect is klein en pas later zichtbaar."],
         ["Overige: SpaceX, Cognita, olie","▼ klein","SpaceX: meer aandelen vrij rond 9-12. Cognita: verkoop mislukt in 2025. Olie: blijft hoog door de oorlog in de Golf en houdt zo de inflatie en de rente hoog."]]
        b["bronnen"]=[27,38,1,21,4,30,19,20,13,14,32,37,15,39,31,33]
        b["noot"]="▲ = goed voor Sofina, ▼ = slecht, ▼▲ = kan beide kanten op. Percentages = deel van de intrinsieke waarde, tenzij anders vermeld; inschattingen."
    if b.get("label")=="mening" and b.get("tekst","").startswith("Wat zie je hier? De meeste pijlen"):
        b["tekst"]="Wat zie je hier? Meer pijlen naar beneden dan naar boven, en de grootste onzekerheden (dollar, stemming rond Sofina) kunnen beide kanten op. **Netto: licht negatief — geen reden om het advies te wijzigen.**"
    if b.get("label")=="mening" and b.get("tekst","").startswith("**Wat betekent dit?** Sofina is sterk afhankelijk"):
        b["tekst"]="**Wat betekent dit?** Sofina is sterk afhankelijk van de stemming rond technologie: in 2021 betaalde de beurs te veel, in 2022 zakte de koers drie keer zo hard als de waarde (−52% tegenover −16,5%). Wie nu instapt, moet zulke schommelingen kunnen dragen."
    if b.get("label")=="mening" and b.get("tekst","").startswith("**Wat betekent dit?** De AI-markt"):
        b["tekst"]="**Wat betekent dit?** De markt voor AI-bedrijven is zenuwachtig geworden, net nu Anthropic naar de beurs gaat, en de rente stijgt mogelijk. Die klappen zitten nog niet in Sofina's cijfers."
    if b.get("label")=="mening" and b.get("tekst","").startswith("**Wat betekent dit?** De komende weken"):
        b["tekst"]="**Wat betekent dit?** Aan Sofina's eigen cijfers verandert er niets tot maart 2027; de komende weken zijn vooral momenten die de stemming bepalen. Dat is een reden om af te wachten, niet om je te haasten."
# Nu-lijst: overbodige details eruit
for b in inh:
    if b["type"]=="lijst":
        b["items"]=[it for it in b["items"] if not it["tekst"].startswith("5-10-2026: herschikking binnen het consortium")]
        for it in b["items"]:
            if it["tekst"].startswith("6-11-2026: gedeeltelijk herstel"):
                it["tekst"]="6-11-2026: gedeeltelijk herstel van de chipbedrijven. Door sterke Amerikaanse banencijfers werd een renteverhoging in december waarschijnlijker."
            if it["tekst"].startswith("26-10-2026: Anthropic maakte"):
                it["tekst"]="26-10-2026: Anthropic maakte zijn [[prospectus|officieel document met alle info over een beursgang]] publiek."
            if it["tekst"].startswith("10-11-2026: Anthropic legde"):
                it["tekst"]="10-11-2026: Anthropic legde de [[prijsvork|bandbreedte waarbinnen de beursprijs vastgelegd wordt]] vast: $70–78 per aandeel, een bedrijfswaarde tot $1,405 biljoen; handel naar verluidt vanaf 19-11."
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch8 review ok')

# ---- tabel → lijst (leesbaar op gsm)
r=json.load(open(P))
s=[x for x in r["secties"] if x["id"]=="actualiteit"][0]
bronmap={"AI- en techbedrijven":[27,38,1],"Dollar":[1,21,4],"Rente (Europa en VS)":[30,19,20],"Stemming rond Sofina":[13],"ByteDance (TikTok)":[14,32,13],"Beursgang Anthropic":[37],"Overige: SpaceX, Cognita, olie":[15,39,31,33]}
for i,b in enumerate(s["inhoud"]):
    if b["type"]=="tabel" and b["titel"].startswith("Wat betekent de actualiteit"):
        s["inhoud"][i]={"type":"lijst","titel":"▲ = goed voor Sofina · ▼ = slecht · ▼▲ = beide mogelijk",
          "items":[I(f"**{o} — {e}.** {w}","inschatting",bronmap[o]) for o,e,w in b["rijen"]]}
    if b["type"]=="uitleg" and b["tekst"].startswith("De tabel toont"):
        b["tekst"]=b["tekst"].replace("De tabel toont per onderwerp","Hieronder per onderwerp")
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('lijst ok')
