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
