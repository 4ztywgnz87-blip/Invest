"""Inline SVG-grafieken voor rapporten (geen externe libraries, werkt offline en in PDF).

Regels (dataviz-skill): één y-as, vaste kleurvolgorde, dunne lijnen (2px), afgeronde staafuiteinden,
legende bij >= 2 reeksen, hover-tooltip per punt (native <title>), altijd een tabelweergave.
"""
from __future__ import annotations

import html
import math

# Categorische kleuren (gevalideerde referentiepalet, licht thema), vaste volgorde.
KLEUREN = ["#2a78d6", "#eb6834", "#1baf7a"]
MAX_REEKSEN = 3
LIJN_KLEUR = "#52514e"  # referentielijnen (stop-loss, gemiddelde)


def _nice_ticks(lo: float, hi: float, n: int = 5) -> list[float]:
    if lo == hi:
        hi = lo + 1
    span = hi - lo
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n:
            step *= m
            break
    start = math.floor(lo / step) * step
    ticks, t = [], start
    while t <= hi + step * 0.5:
        ticks.append(round(t, 10))
        t += step
    return ticks


def fmt(v: float | None, eenheid: str = "") -> str:
    if v is None:
        return "–"
    a = abs(v)
    if a >= 1e9:
        s = f"{v/1e9:,.1f} mld"
    elif a >= 1e6:
        s = f"{v/1e6:,.1f} mln"
    elif a >= 1000:
        s = f"{v:,.0f}"
    elif float(v).is_integer():
        s = f"{v:,.0f}"
    else:
        s = f"{v:,.2f}"
    s = s.replace(",", " ").replace(".", ",")
    return f"{s} {eenheid}".strip()


def _xlabels(x: list[str], max_n: int = 6) -> list[int]:
    n = len(x)
    if n <= max_n:
        return list(range(n))
    stap = math.ceil(n / max_n)
    idx = list(range(0, n, stap))
    if idx[-1] != n - 1 and n - 1 - idx[-1] >= stap / 2:
        idx.append(n - 1)
    return idx


def _label_x(v: str, veel: bool) -> str:
    # Bij lange dagreeksen enkel het jaar tonen.
    return v[:4] if veel and len(v) >= 10 else v


def svg(blok: dict) -> str:
    soort = blok.get("soort", "lijn")
    x = [str(v) for v in blok["x"]]
    reeksen = blok["reeksen"][:MAX_REEKSEN]
    eenheid = blok.get("eenheid", "") or ""
    lijnen = blok.get("lijnen", [])
    W, H = 480, 270
    L, R, T, B = 52, 10, 12, 30
    pw, ph = W - L - R, H - T - B

    alle = [v for r in reeksen for v in r["waarden"] if v is not None] + [l["waarde"] for l in lijnen if l.get("waarde") is not None]
    lo, hi = min(alle), max(alle)
    if soort == "staaf":
        lo, hi = min(0, lo), max(0, hi)
    else:
        pad = (hi - lo) * 0.06 or 1
        lo, hi = lo - pad, hi + pad
    ticks = _nice_ticks(lo, hi)
    lo, hi = min(lo, ticks[0]), max(hi, ticks[-1])

    def Y(v):
        return T + ph - (v - lo) / (hi - lo) * ph

    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(blok.get("titel",""))}" class="grafiek-svg">']
    # Raster + y-as
    for t in ticks:
        y = Y(t)
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" class="g-raster"/>')
        out.append(f'<text x="{L-6}" y="{y+4:.1f}" text-anchor="end" class="g-as">{html.escape(fmt(t))}</text>')
    if lo < 0 < hi:
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" class="g-nul"/>')

    n = len(x)
    veel = n > 24
    if soort == "staaf":
        groep = pw / n
        bw = min(28, (groep - 6) / len(reeksen) - 2)
        for i in range(n):
            gx = L + i * groep + (groep - (bw + 2) * len(reeksen) + 2) / 2
            for k, r in enumerate(reeksen):
                v = r["waarden"][i]
                if v is None:
                    continue
                bx = gx + k * (bw + 2)
                y0, y1 = Y(0), Y(v)
                top, h = min(y0, y1), max(1, abs(y1 - y0))
                rr = min(4, bw / 2, h)
                # Afgerond uiteinde weg van de basislijn.
                if v >= 0:
                    d = f"M{bx:.1f},{y0:.1f} V{top+rr:.1f} Q{bx:.1f},{top:.1f} {bx+rr:.1f},{top:.1f} H{bx+bw-rr:.1f} Q{bx+bw:.1f},{top:.1f} {bx+bw:.1f},{top+rr:.1f} V{y0:.1f} Z"
                else:
                    bot = top + h
                    d = f"M{bx:.1f},{y0:.1f} V{bot-rr:.1f} Q{bx:.1f},{bot:.1f} {bx+rr:.1f},{bot:.1f} H{bx+bw-rr:.1f} Q{bx+bw:.1f},{bot:.1f} {bx+bw:.1f},{bot-rr:.1f} V{y0:.1f} Z"
                tip = html.escape(f'{r["naam"]} {x[i]}: {fmt(v, eenheid)}')
                out.append(f'<path d="{d}" fill="{KLEUREN[k]}"><title>{tip}</title></path>')
        for i in _xlabels(x, 6):
            cx = L + (i + 0.5) * groep
            out.append(f'<text x="{cx:.1f}" y="{H-12}" text-anchor="middle" class="g-as">{html.escape(_label_x(x[i], veel))}</text>')
    else:
        def X(i):
            return L + (i / max(1, n - 1)) * pw
        for k, r in enumerate(reeksen):
            pts, seg = [], []
            for i, v in enumerate(r["waarden"]):
                if v is None:
                    if seg:
                        pts.append(seg); seg = []
                    continue
                seg.append(f"{X(i):.1f},{Y(v):.1f}")
            if seg:
                pts.append(seg)
            for s in pts:
                out.append(f'<polyline points="{" ".join(s)}" fill="none" stroke="{KLEUREN[k]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
            # Laatste punt markeren + direct label
            laatste = max((i for i, v in enumerate(r["waarden"]) if v is not None), default=None)
            if laatste is not None:
                v = r["waarden"][laatste]
                out.append(f'<circle cx="{X(laatste):.1f}" cy="{Y(v):.1f}" r="4" fill="{KLEUREN[k]}" stroke="#fff" stroke-width="2"/>')
        # Referentielijnen
        for l in lijnen:
            if l.get("waarde") is None:
                continue
            y = Y(l["waarde"])
            out.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" stroke="{LIJN_KLEUR}" stroke-width="1.2" stroke-dasharray="5 4"/>')
            out.append(f'<text x="{W-R-4}" y="{y-5:.1f}" text-anchor="end" class="g-ref">{html.escape(l["naam"])}: {html.escape(fmt(l["waarde"]))}</text>')
        # Hover-doelen (onzichtbaar, groter dan het merkteken)
        stap = max(1, n // 120)
        for i in range(0, n, stap):
            tip = "; ".join(f'{r["naam"]}: {fmt(r["waarden"][i], eenheid)}' for r in reeksen if r["waarden"][i] is not None)
            out.append(f'<rect x="{X(i) - pw/ max(1,(n/stap))/2:.1f}" y="{T}" width="{pw/max(1,(n/stap)):.1f}" height="{ph}" fill="transparent"><title>{html.escape(x[i])} — {html.escape(tip)}</title></rect>')
        for i in _xlabels(x, 5):
            anker = "start" if i == 0 else "end" if i == n - 1 else "middle"
            out.append(f'<text x="{X(i):.1f}" y="{H-12}" text-anchor="{anker}" class="g-as">{html.escape(_label_x(x[i], veel))}</text>')
    out.append("</svg>")

    legende = ""
    if len(reeksen) >= 2:
        legende = '<div class="g-legende">' + "".join(
            f'<span><i style="background:{KLEUREN[k]}"></i>{html.escape(r["naam"])}</span>' for k, r in enumerate(reeksen)) + "</div>"

    # Tabelweergave (toegankelijkheid + exacte cijfers). Lange reeksen: enkel jaar-einde.
    rij_idx = list(range(n))
    if n > 40:
        per_jaar = {}
        for i, v in enumerate(x):
            per_jaar[v[:4]] = i
        rij_idx = list(per_jaar.values())
    kop = "".join(f"<th>{html.escape(r['naam'])}</th>" for r in reeksen)
    rijen = "".join(
        f"<tr><td>{html.escape(x[i])}</td>" + "".join(f"<td>{fmt(r['waarden'][i], eenheid)}</td>" for r in reeksen) + "</tr>"
        for i in rij_idx)
    tabel = f'<details class="g-tabel"><summary>Toon als tabel</summary><table><thead><tr><th></th>{kop}</tr></thead><tbody>{rijen}</tbody></table></details>'
    return "".join(out) + legende + tabel
