"""Bereidt de Invest-app voor: overzicht van alle rapporten + bestanden om te publiceren.

Gebruik:
  python3 tools/app.py            # schrijft app/manifest.json en app/vraag/<id>.json, print de 'files'-map

De app zelf is app/index.html. Publiceren gebeurt door Claude met de Artifact-tool:
  file_path = app/index.html, url = (zie app/APP.md), files = de map die dit script print.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from common import ROOT

APP = ROOT / "app"


def rapport_id(ticker: str, datum: str) -> str:
    return re.sub(r"[^A-Za-z0-9-]", "-", f"{ticker}-{datum}")


def slank(r: dict) -> dict:
    """Rapport zonder lange koersreeksen (voor vragen aan Claude: minder tekst = sneller, zuiniger)."""
    r = json.loads(json.dumps(r))
    for s in r.get("secties", []):
        for b in s.get("inhoud", []):
            if b.get("type") == "grafiek" and len(b.get("x", [])) > 40:
                for rs in b.get("reeksen", []):
                    w = [v for v in rs["waarden"] if v is not None]
                    rs["samenvatting"] = {"eerste": w[0], "laatste": w[-1], "min": min(w), "max": max(w)} if w else {}
                    rs.pop("waarden", None)
                b["x"] = [b["x"][0], b["x"][-1]]
    return {k: v for k, v in r.items() if not k.startswith("_")}


def main():
    (APP / "vraag").mkdir(parents=True, exist_ok=True)
    items, files = [], {}
    for rj in sorted(ROOT.glob("rapporten/*/*/rapport.json")):
        map_ = rj.parent
        html, pdf = map_ / "rapport.html", map_ / "rapport.pdf"
        if not html.exists():
            continue
        r = json.loads(rj.read_text(encoding="utf-8"))
        m, a = r["meta"], r.get("advies", {})
        rid = rapport_id(m["ticker"], m["datum"])
        rel = f"rapporten/{map_.parent.name}/{map_.name}"
        agenda = []
        for s in r.get("secties", []):
            blokken = s.get("inhoud", [])
            for n, b in enumerate(blokken):
                if b.get("type") == "kop" and "letten" in b.get("tekst", "").lower():
                    for b2 in blokken[n + 1:]:
                        if b2.get("type") == "kop":
                            break
                        if b2.get("type") == "lijst":
                            agenda += [it.get("tekst", "") for it in b2.get("items", [])]
        vraag = {"rapport": slank(r)}
        for extra in ("werkdossier.md", "review.md"):
            if (map_ / extra).exists():
                vraag[extra] = (map_ / extra).read_text(encoding="utf-8")
        (APP / "vraag" / f"{rid}.json").write_text(json.dumps(vraag, ensure_ascii=False), encoding="utf-8")
        files[f"{rel}/rapport.html"] = str(html.relative_to(ROOT))
        if pdf.exists():
            files[f"{rel}/rapport.pdf"] = str(pdf.relative_to(ROOT))
        files[f"vraag/{rid}.json"] = f"app/vraag/{rid}.json"
        items.append({
            "id": rid, "ticker": m["ticker"], "naam": m["naam"], "type": m.get("type"), "datum": m["datum"],
            "sector": m.get("sector"), "defensief": m.get("defensief", False), "valuta": m.get("valuta"),
            "oordeel": a.get("oordeel"), "score": a.get("score"), "reden": a.get("reden"),
            "koers_nu": a.get("koers_nu"), "koersdoel": a.get("koersdoel"), "koopzone": a.get("koopzone"),
            "intrinsieke_waarde": a.get("intrinsieke_waarde"), "koers_datum": a.get("koers_datum"),
            "stop_loss": (a.get("stop_loss") or {}).get("waarde"), "soort": m.get("soort") or "volledig",
            "scenarios": [{"naam": s.get("naam"), "koers": s.get("koers"), "kans": s.get("kans")} for s in a.get("scenarios", [])],
            "verkoopsignalen": r.get("verkoopsignalen", []), "agenda": agenda,
            "rode_vlaggen": [{"ernst": v.get("ernst"), "regel": v.get("regel"), "titel": v.get("titel")} for v in r.get("rode_vlaggen", [])],
            "review": {k: r.get("review", {}).get(k) for k in ("feiten_gecontroleerd", "feiten_correct", "open_punten")},
            "html": f"{rel}/rapport.html", "pdf": f"{rel}/rapport.pdf" if pdf.exists() else None,
            "vraag": f"vraag/{rid}.json",
        })
    items.sort(key=lambda i: (i["naam"].lower(), i["datum"]), reverse=False)
    manifest = {"rapporten": items}
    (APP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    files["manifest.json"] = "app/manifest.json"
    for f in ("PROFIEL.md", "voorstellen.md", "feedback.md"):
        files[f"profiel/{f}"] = f"profiel/{f}"
    print(json.dumps(files, indent=1))


if __name__ == "__main__":
    main()
