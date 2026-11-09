#!/usr/bin/env python3
"""Builds 25 numbered tagline options for the Vasco logo into assets/brand/options/.
Same V, letters and rays as the main logo; only the "SOLAR ENERGY" oval changes.
Fonts (SIL Open Font License) live in tools/brand/fonts.  Run: python3 tools/logo_options.py"""
import json, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "brand" / "options"
OUT.mkdir(parents=True, exist_ok=True)
P = json.loads((ROOT / "tools/brand/paths.json").read_text())
FD = ROOT / "tools/brand/fonts"
BLUE, SKY, LEMON, GOLD = "#1850a0", "#86d2ec", "#f2e600", "#f4c21c"
FONTS = [("Michroma", "michroma-latin-400-normal.woff2"), ("Krona One", "krona-one-latin-400-normal.woff2"),
         ("Syncopate Bold", "syncopate-latin-700-normal.woff2"), ("Montserrat Bold", "montserrat-latin-700-normal.woff2"),
         ("Exo 2 Bold", "exo-2-latin-700-normal.woff2")]
OVAL = "M49.5,92C86,82.2 176,82.4 210.5,91.4C176,101 86,101.6 49.5,92Z"   # taller and wider than the original
CX, CY = 130, 91.8


def tagline(fontfile, cap=6.0, width=112.0):
    f = TTFont(FD / fontfile)
    gs = f.getGlyphSet(); cm = f.getBestCmap()
    capu = getattr(f["OS/2"], "sCapHeight", 0) or 700
    sc = cap / capu
    text = "SOLAR ENERGY"
    adv = [gs[cm[ord(c)]].width * sc for c in text]
    track = (width - sum(adv)) / (len(text) - 1)
    x = CX - width / 2; base = CY + cap / 2; parts = []
    for c, w in zip(text, adv):
        if c != " ":
            pen = SVGPathPen(gs)
            gs[cm[ord(c)]].draw(TransformPen(pen, (sc, 0, 0, -sc, x, base)))
            parts.append(pen.getCommands())
        x += w + track
    return "".join(parts)


STYLES = [
    ("Solid white", dict(fill="#ffffff")),
    ("White, sky edge", dict(fill="#ffffff", oval_stroke=SKY)),
    ("Gold", dict(fill=GOLD)),
    ("Outlined, original style", dict(fill="none", stroke="#ffffff")),
    ("White, wide spacing", dict(fill="#ffffff", width=126.0)),
]

items = []; n = 0
for fname, ffile in FONTS:
    for sname, st in STYLES:
        n += 1
        t = tagline(ffile, width=st.get("width", 112.0))
        stroke = f' stroke="{st["stroke"]}" stroke-width="0.55" stroke-linejoin="round"' if st.get("stroke") else ""
        ovs = f' stroke="{st["oval_stroke"]}" stroke-width="0.8"' if st.get("oval_stroke") else ""
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 14 212 106" role="img" aria-label="Vasco Solar Energy, option {n}">'
               f'<path d="{P["rays"]}" fill="{LEMON}"/><path d="{P["outline"]}" fill="{SKY}"/><path d="{P["letters"]}" fill="{BLUE}"/>'
               f'<path d="{OVAL}" fill="{BLUE}"{ovs}/><path d="{t}" fill="{st["fill"]}"{stroke}/></svg>')
        name = f"option-{n:02d}.svg"
        (OUT / name).write_text(svg)
        items.append(dict(n=n, file=name, font=fname, style=sname))
(OUT / "options.json").write_text(json.dumps(items, indent=1))
print(n, "options")
