#!/usr/bin/env python3
"""Builds brand.html: the Vasco Solar brand kit, every logo, icon and Office file ready to download.
Files come from assets/brand/kit/ (run tools/brand_kit.py and tools/office.js first).
Run from the repo root:  python3 tools/brand_page.py"""
import pathlib, html as H
ROOT = pathlib.Path(__file__).resolve().parent.parent
KITDIR = ROOT / "assets" / "brand" / "kit"
KIT = "assets/brand/kit/"
BLUE, SKY, LEMON, GOLD, NAVY, MIST, INK = "#1850a0", "#86d2ec", "#f2e600", "#f4c21c", "#0e2740", "#f5f7fa", "#1b2430"

LABELS = {
    "svg": "SVG (vector)", "png": "PNG, transparent", "jpg": "JPG", "ico": "ICO, Windows icon", "docx": "Word letterhead", "pptx": "PowerPoint template",
}
def size(n):
    return f"{n / 1024 / 1024:.1f} MB" if n > 1024 * 1024 else f"{max(1, round(n / 1024))} KB"

def btns(items):
    out = ""
    for name, label in items:
        ext = name.rsplit(".", 1)[1].upper()
        out += f'<a class="dl" href="{KIT}{name}" download><b>{ext}</b><span>{H.escape(label)}</span><i>{size((KITDIR / name).stat().st_size)}</i></a>'
    return f'<div class="dls">{out}</div>'

def card(title, note, preview, bg, items, wide=False, checker=False):
    pv = f'<div class="pv{" checker" if checker else ""}" style="background:{bg}"><img src="{KIT}{preview}" alt="{H.escape(title)}" loading="lazy"></div>'
    return f'<article class="card{" wide" if wide else ""}">{pv}<div class="body"><h3>{title}</h3><p>{note}</p>{btns(items)}</div></article>'

logos = "".join([
    card("Full color", "The main logo, for white and light backgrounds.", "logo-color.png", "#ffffff",
         [("logo-color.svg", "SVG (vector)"), ("logo-color.png", "PNG, 2400 px"), ("logo-color-on-white.jpg", "JPG on white")]),
    card("Reverse", "For dark backgrounds, like the website header and footer.", "logo-reverse.png", NAVY,
         [("logo-reverse.svg", "SVG (vector)"), ("logo-reverse.png", "PNG, 2400 px"), ("logo-reverse-on-navy.jpg", "JPG on navy")]),
    card("White only", "For photos, vehicles and colored backgrounds.", "logo-white.png", BLUE,
         [("logo-white.svg", "SVG (vector)"), ("logo-white.png", "PNG, 2400 px"), ("logo-white-on-blue.jpg", "JPG on blue")]),
    card("One color", "Vasco blue only, for print, stamps, shirts and forms.", "logo-blue.png", "#ffffff",
         [("logo-blue.svg", "SVG (vector)"), ("logo-blue.png", "PNG, 2400 px"), ("logo-blue-on-white.jpg", "JPG on white")]),
])
icons = "".join([
    card("Icon, full color", "The V with the sun rising behind it.", "icon-color.png", "#ffffff",
         [("icon-color.svg", "SVG (vector)"), ("icon-color.png", "PNG, 1024 px"), ("icon-color-on-white.jpg", "JPG on white")], checker=True),
    card("Icon, reverse", "White V and gold sun, for dark backgrounds.", "icon-reverse.png", NAVY,
         [("icon-reverse.svg", "SVG (vector)"), ("icon-reverse.png", "PNG, 1024 px"), ("favicon.ico", "ICO, browser tab")]),
    card("Icon, white", "For photos and colored backgrounds.", "icon-white.png", BLUE,
         [("icon-white.svg", "SVG (vector)"), ("icon-white.png", "PNG, 1024 px"), ("icon-white-on-blue.jpg", "JPG on blue")]),
    card("App icon", "Navy square for phones, shortcuts and desktops.", "app-icon.png", "#e3e8ef",
         [("app-icon.svg", "SVG (vector)"), ("app-icon.png", "PNG, 1024 px"), ("app-icon.ico", "ICO, Windows")]),
])
office = "".join([
    card("Word letterhead", "US Letter.  Logo in the header, address, phone and license in the footer.  Open it, replace the bracketed text, save as a new file.",
         "preview-letterhead.jpg", "#e3e8ef", [("vasco-letterhead.docx", "Word document (.docx)")]),
    card("PowerPoint template", "Widescreen, with title, section, content, two-column, numbers and closing layouts already styled.  Add slides from the Layout menu.",
         "preview-presentation.jpg", "#e3e8ef", [("vasco-presentation.pptx", "PowerPoint presentation (.pptx)")]),
])
m365 = "".join([
    card("Mailbox and Teams photo", "648 by 648, the largest photo Microsoft 365 uses.  Outlook and Teams crop it to a circle, so the mark sits centered.",
         "m365-photo.png", "#e3e8ef", [("m365-photo.jpg", "JPG, 648 square (Microsoft 365)"), ("m365-photo.png", "PNG, 648 square")]),
    card("Social share image", "1200 by 630, what Facebook, LinkedIn and text messages show when someone shares the website.",
         "social-share.jpg", NAVY, [("social-share.jpg", "JPG, 1200 x 630"), ("social-share.png", "PNG, 1200 x 630")]),
])
zoom = "".join([
    card("Zoom background, dark", "1920 by 1080 (16:9).  Logo top left, so it stays clear of you.", "zoom-dark.jpg", NAVY,
         [("zoom-dark.jpg", "JPG, 1920 x 1080"), ("zoom-dark.png", "PNG, 1920 x 1080")], wide=True),
    card("Zoom background, light", "1920 by 1080 (16:9).", "zoom-light.jpg", MIST,
         [("zoom-light.jpg", "JPG, 1920 x 1080"), ("zoom-light.png", "PNG, 1920 x 1080")], wide=True),
])
swatches = "".join(f'<div class="sw"><span style="background:{c}"></span><b>{n}</b><code>{c}</code><small>{u}</small></div>' for n, c, u in [
    ("Vasco blue", BLUE, "Letters, oval, headings"), ("Sky", SKY, "Edge around letters"), ("Sun yellow", LEMON, "Full-color logo rays"),
    ("Sun gold", GOLD, "Dark-background rays"), ("Navy", NAVY, "Header and footer"), ("Mist", MIST, "Page backgrounds")])
fonts = "".join(f'<div class="font"><div class="spec" style="font-family:{fam}">{sample}</div><b>{name}</b><small>{use}</small></div>' for fam, sample, name, use in [
    ("Outfit, Arial, sans-serif", "Vasco Solar", "Outfit", "Website headings (Google Fonts, free)"),
    ("Inter, Arial, sans-serif", "Vasco Solar", "Inter", "Website body text (Google Fonts, free)"),
    ("Arial, sans-serif", "Vasco Solar", "Arial", "Word and PowerPoint headings"),
    ("Calibri, Arial, sans-serif", "Vasco Solar", "Calibri", "Word and PowerPoint body text")])

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Brand Kit | Vasco Solar</title>
<link rel="icon" href="{KIT}favicon.ico"><link rel="apple-touch-icon" href="{KIT}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Outfit:wght@600;700&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:{MIST};color:{INK};font:400 16px/1.55 Inter,Arial,sans-serif}}
.top{{background:{NAVY};border-bottom:3px solid {GOLD}}} .top .wrap{{display:flex;align-items:center;justify-content:space-between;height:96px}}
.top img{{height:72px;display:block}} .top a.back{{color:#e3eaf2;text-decoration:none;font:600 15px Outfit,Arial}} .top a.back:hover{{color:#fff}}
.wrap{{max-width:1240px;margin:0 auto;padding:0 20px}}
h1{{font:700 clamp(32px,4vw,44px)/1.1 Outfit,Arial;margin:44px 0 10px;color:{NAVY}}}
.lead{{color:#3c4a5c;max-width:780px;margin:0}}
nav.jump{{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 0}}
nav.jump a{{text-decoration:none;color:{INK};font:600 14px Inter;padding:.5em .9em;border:1px solid #c9d0da;border-radius:3px;background:#fff}}
nav.jump a:hover{{border-color:{GOLD}}}
h2{{font:700 26px Outfit,Arial;margin:52px 0 16px;padding-bottom:10px;border-bottom:2px solid {NAVY};color:{NAVY};scroll-margin-top:16px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;align-items:stretch}}
@media (max-width:1100px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
.grid.g2{{grid-template-columns:repeat(2,1fr)}}

.card{{background:#fff;border:1px solid #c9d0da;border-radius:3px;overflow:hidden;display:flex;flex-direction:column}}
.pv{{height:220px;display:grid;place-items:center;padding:24px;border-bottom:1px solid #c9d0da}}
.tall .pv{{height:320px}} .tall .pv img{{max-height:272px;box-shadow:0 2px 10px rgba(14,39,64,.18)}}
.card.wide .pv{{height:auto;padding:0}} .card.wide .pv img{{width:100%;max-height:none}}
.pv img{{max-width:100%;max-height:172px;object-fit:contain}}
.checker{{background-image:linear-gradient(45deg,#eef1f5 25%,transparent 25%),linear-gradient(-45deg,#eef1f5 25%,transparent 25%),linear-gradient(45deg,transparent 75%,#eef1f5 75%),linear-gradient(-45deg,transparent 75%,#eef1f5 75%);background-size:20px 20px;background-position:0 0,0 10px,10px -10px,-10px 0}}
.body{{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1}}
.body h3{{font:700 19px Outfit,Arial;margin:0 0 4px;color:{NAVY}}} .body p{{margin:0 0 16px;color:#4a5869;font-size:15px}}
.dls{{display:flex;flex-direction:column;gap:8px;margin-top:auto}}
.dl{{display:grid;grid-template-columns:46px 1fr auto;align-items:center;gap:10px;text-decoration:none;color:{INK};border:1px solid #c9d0da;border-radius:3px;padding:9px 12px;transition:.15s}}
.dl:hover{{border-color:{BLUE};background:#f2f6fc}}
.dl b{{font:700 12px Inter;letter-spacing:.06em;color:#fff;background:{BLUE};border-radius:2px;text-align:center;padding:4px 0}}
.dl span{{font-size:14px}} .dl i{{font-style:normal;font-size:13px;color:#6b7888}}
.topcolors{{margin:22px 0 0;scroll-margin-top:16px}}
.sws{{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}}
.sw{{background:#fff;border:1px solid #c9d0da;border-radius:3px;padding:12px;display:flex;flex-direction:column}}
.sw span{{height:84px;border-radius:2px;border:1px solid rgba(0,0,0,.08);margin-bottom:10px}}
.sw b{{font:700 15px Outfit,Arial}} .sw code{{font:13px ui-monospace,Consolas,monospace;color:{BLUE};margin:2px 0}} .sw small{{color:#5b6878}}
.fonts{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}
.font{{background:#fff;border:1px solid #c9d0da;border-radius:3px;padding:18px;display:flex;flex-direction:column}}
.font .spec{{font-size:30px;font-weight:700;color:{NAVY};line-height:1.2;margin-bottom:10px}}
.font b{{font:700 15px Inter}} .font small{{color:#5b6878}}
.rules{{background:#fff;border:1px solid #c9d0da;border-radius:3px;padding:20px 24px}} .rules ul{{margin:0;padding-left:1.2em}} .rules li{{margin:.35em 0}}
footer{{margin:60px 0 0;padding:26px 0;background:{NAVY};color:#a9b8c8;font-size:14px}}
@media (max-width:1100px){{.fonts{{grid-template-columns:repeat(2,1fr)}}.sws{{grid-template-columns:repeat(3,1fr)}}}}
@media (max-width:600px){{.grid,.grid.g2,.fonts{{grid-template-columns:1fr}}.sws{{grid-template-columns:repeat(2,1fr)}}}}
.dl span{{min-width:0;font-size:13.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
</style></head><body>
<header class="top"><div class="wrap"><img src="{KIT}logo-reverse.svg" alt="Vasco Solar Energy"><a class="back" href="index.html">Back to the website</a></div></header>
<main class="wrap">
<h1>Vasco Solar brand kit</h1>
<p class="lead">Every approved Vasco Solar logo, icon and template, ready to download.  The logo is a high-definition redraw of the original, so it stays sharp at any size, from a business card to a truck wrap.</p>
<nav class="jump"><a href="#colors">Colors</a><a href="#logo">Logo</a><a href="#icon">Icon</a><a href="#office">Word and PowerPoint</a><a href="#m365">Microsoft 365 and social</a><a href="#zoom">Zoom backgrounds</a><a href="#fonts">Fonts</a><a href="#use">Using the logo</a></nav>
<section id="colors" class="topcolors"><div class="sws">{swatches}</div></section>
<h2 id="logo">Logo</h2><div class="grid">{logos}</div>
<h2 id="icon">Icon</h2><div class="grid">{icons}</div>
<h2 id="office">Word and PowerPoint</h2><div class="grid g2 tall">{office}</div>
<h2 id="m365">Microsoft 365 and social</h2><div class="grid g2">{m365}</div>
<h2 id="zoom">Zoom backgrounds</h2><div class="grid g2">{zoom}</div>
<h2 id="fonts">Fonts</h2><div class="fonts">{fonts}</div>
<h2 id="use">Using the logo</h2><div class="rules"><ul>
<li>Use the full-color logo on white or light backgrounds, and the reverse logo on navy or other dark backgrounds.</li>
<li>Leave clear space around the logo at least as wide as the letter O on every side.</li>
<li>Don't stretch, recolor, rotate or add effects to the logo.  Pick the version that fits the background instead.</li>
<li>Keep the logo at least 1 inch wide in print and 120 pixels wide on screen, so "SOLAR ENERGY" stays readable.  Below that, use the icon.</li>
</ul></div>
</main>
<footer><div class="wrap">Vasco Solar · 17150 Newhope St #403, Fountain Valley, CA 92708 · (714) 968-8845 · CSL# 608260</div></footer>
</body></html>'''
(ROOT / "brand.html").write_text(page)
print("brand.html built")
