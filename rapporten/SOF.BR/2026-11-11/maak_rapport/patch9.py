# Kerncijfers: uitleg onder de knop (wat is dit / hoe berekend / goed of slecht) — nieuwe rapportopmaak 2026-11-11.
# Geen nieuwe feiten: enkel uitleg en beoordelingen die al elders in het rapport staan.
import json
P='/home/user/Invest/rapporten/SOF.BR/2026-11-11/rapport.json'
r=json.load(open(P))
X={
 "CEO-verloning 2025":{"wat":"Alles wat de CEO over dat jaar kreeg: het vaste loon en het deel dat afhangt van de prestaties.",
   "beoordeling":"normaal","beoordeling_uitleg":"Voor een investeringsbedrijf van deze grootte is dat niet overdreven, en het grootste deel hangt af van de prestaties. Regel R2 (zelfverrijking) is hier niet geraakt."},
 "5 andere leiders samen":{"wat":"Het loon van de vijf andere leden van de directie, opgeteld."},
 "Bestuurders":{"wat":"De vergoeding van de bestuurders (de raad die toezicht houdt op de directie). Die is geen vast bedrag, maar een vast percentage van het uitgekeerde dividend."},
 "Loonkloof":{"wat":"De verhouding tussen het hoogste en het laagste loon in het bedrijf: de best betaalde verdient 20 keer zoveel als de minst betaalde."},
 "Dividend over 2025":{"wat":"Het bedrag dat je per aandeel uitbetaald krijgt, vóór belasting. Na 30% Belgische roerende voorheffing blijft €2,56 per aandeel over."},
 "Dividendrendement":{"wat":"Hoeveel procent van je inleg je per jaar als dividend terugkrijgt, vóór belasting.","hoe":"Het dividend (€3,66) gedeeld door de koers (€270,4).",
   "beoordeling":"normaal","beoordeling_uitleg":"Laag, maar dat is hier bewust: Sofina belegt het grootste deel opnieuw, en dat past bij jouw voorkeur voor bedrijven die hun winst herinvesteren. Wie een inkomen uit dividend zoekt, vindt hier weinig."},
 "Uitkering t.o.v. waarde":{"wat":"Welk deel van al haar bezittingen Sofina per jaar aan de aandeelhouders uitkeert. De rest blijft belegd.","hoe":"±€130 mln dividend gedeeld door ±€11,5 mld bezittingen."},
 "Aandelen uitstaand":{"wat":"Het totale aantal aandelen van Sofina. Komen er nieuwe aandelen bij, dan wordt jouw deel van het bedrijf kleiner.",
   "beoordeling":"zwak","beoordeling_uitleg":"De 7,1% nieuwe aandelen in 2025 werden uitgegeven onder de intrinsieke waarde. Dat staat als rode vlag (regel R6, ernst middel) in dit rapport."},
 "Rendement 1 jaar":{"wat":"Hoeveel je de laatste 12 maanden verdiende of verloor met dit aandeel: koersverandering en dividend samen."},
 "Rendement 5 jaar":{"wat":"Hoeveel je de laatste vijf jaar verdiende of verloor met dit aandeel: koersverandering en dividend samen.",
   "beoordeling":"zwak","beoordeling_uitleg":"Wie vijf jaar geleden kocht, staat nog altijd op verlies. De koers piekte eind 2021 op €432 en herstelde sindsdien maar gedeeltelijk."},
 "Volatiliteit":{"wat":"Hoe sterk de koers schommelt. Hoe hoger het getal, hoe groter de uitschieters naar boven én naar beneden.","hoe":"De spreiding van de dagelijkse koersveranderingen van het laatste jaar, omgerekend naar een jaar."},
 "Grootste daling 5 j":{"wat":"De grootste val van een top naar de bodem erna in de laatste vijf jaar. Het toont hoeveel je in het slechtste geval tijdelijk kon verliezen.",
   "beoordeling":"zwak","beoordeling_uitleg":"Een val van meer dan de helft is fors en gaat veel verder dan je stop-loss van −20%. Dit is geen defensief aandeel."},
}
n=0
for s in r["secties"]:
    for b in s["inhoud"]:
        if b["type"]=="kerncijfers":
            for it in b["items"]:
                if it["naam"] in X: it.update(X[it["naam"]]); n+=1
                if it["naam"]=="Volatiliteit": it.pop("toelichting",None)
assert n==len(X), n
json.dump(r,open(P,"w"),ensure_ascii=False,indent=1)
