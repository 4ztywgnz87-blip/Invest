# Scoreopbouw (vraag gebruiker 2026-11-11)
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-08/rapport.json'
r=json.load(open(P))
r["advies"]["score_opbouw"]={
 "uitleg":"Elk onderdeel krijgt punten op 10 en weegt mee volgens zijn gewicht. Daarna gaan er punten af als een harde regel geraakt is. De punten zijn mijn mening op basis van de feiten in de secties hieronder.",
 "onderdelen":[
  {"naam":"Bestuur & aandeelhouders (zonder R1)","gewicht":15,"punten":6,"uitleg":"Meerderheid onafhankelijke bestuurders, redelijke verloning, geen vertrekpremies of verdachte transacties. Min: kapitaalverhoging onder de waarde, geen terugvorderingsrecht op bonussen, CEO verkoopt optie-aandelen."},
  {"naam":"Financiële gezondheid","gewicht":20,"punten":7,"uitleg":"Weinig schuld (1,9% van de portefeuille), goede kredietrating A− en ruime kredietlijnen. Min: het dividend wordt betaald uit verkopen, niet uit inkomsten."},
  {"naam":"Groei & herinvestering","gewicht":15,"punten":4,"uitleg":"Over 10 jaar 8,4% per jaar, maar de intrinsieke waarde per aandeel staat midden 2026 lager dan eind 2021, en de laatste 4 jaar deed Sofina het slechter dan de wereldindex."},
  {"naam":"Waardering (prijs nu)","gewicht":20,"punten":4,"uitleg":"18% korting ligt binnen Sofina's normale bereik; vergelijkbare holdings zijn goedkoper. Verwacht rendement hooguit ±2% per jaar."},
  {"naam":"Risico's & actualiteit","gewicht":15,"punten":3,"uitleg":"92% niet-beursgenoteerd (waarde is een schatting), ±65% in dollar, grote gevoeligheid voor AI- en techwaarderingen; de uitverkoop van 5 november zit nog niet in de cijfers."},
  {"naam":"Past bij jouw profiel","gewicht":15,"punten":4,"uitleg":"Weinig uitkering (+), maar niet defensief en via fondsen gevoelig voor hype rond AI-bedrijven."}],
 "correcties":[
  {"naam":"R1 geraakt: consortium Boël 54,6%","punten":-1,"uitleg":"Harde regel R1 (meer dan 49% in één blok). Daarbovenop geldt: normaal niet kopen, tenzij al de rest uitzonderlijk goed is — en dat is hier niet zo."}]}
# kader in waardering laten verwijzen
for s in r["secties"]:
    if s["id"]=="waardering":
        for x in s["inhoud"]:
            if x.get("type")=="kader":
                x["tekst"]="**Afwachten (niet kopen: R1) — 4/10.** Zonder R1 komt Sofina op een gewogen gemiddelde van ±4,8/10: degelijk bestuur en weinig schuld (+), maar geen defensief profiel, een waarde die je niet zelf kan controleren, AI-gevoeligheid en een verwacht rendement van hooguit ±2% per jaar. R1 kost nog een punt en maakt het een NO-GO, tenzij de rest uitzonderlijk is — dat is hier niet zo. De volledige scoreopbouw staat bovenaan bij het advies. De koopzone geldt enkel voor wie R1 bewust aanvaardt."
json.dump(r,open(P,'w'),ensure_ascii=False,indent=1)
print('patch4 ok')
