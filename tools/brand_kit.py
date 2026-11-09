#!/usr/bin/env python3
"""Builds the Vasco Solar brand kit: every logo, icon and background file in assets/brand/kit/.
Artwork paths come from tools/brand/paths.json (high-definition redraw of the original logo).
Run from the repo root:  python3 tools/brand_kit.py   (needs playwright + Pillow)"""
import json, math, pathlib, tempfile
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = ROOT / "assets" / "brand" / "kit"
KIT.mkdir(parents=True, exist_ok=True)
P = json.loads((ROOT / "tools" / "brand" / "paths.json").read_text())

BLUE, SKY, LEMON, GOLD, NAVY, MIST = "#1850a0", "#86d2ec", "#f2e600", "#f4c21c", "#0e2740", "#f5f7fa"

def logo_svg(ray, letters, outline=None, oval=BLUE, oval_stroke=SKY, tag_fill="#ffffff", tag_stroke=None, knockout=False):
    """knockout=True (one-color versions): rays stop short of the letters and oval, and the tagline is cut out of a solid oval."""
    o = f'<path d="{P["outline"]}" fill="{outline}"/>' if outline else ""
    os_ = f' stroke="{oval_stroke}" stroke-width="0.8"' if oval_stroke else ""
    head = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 14 212 106" role="img" aria-label="Vasco Solar Energy">'
    if knockout:
        defs = (f'<defs><mask id="r"><rect x="0" y="0" width="220" height="140" fill="#fff"/>'
                f'<path d="{P["outline"]}" fill="#000"/><path d="{P["oval"]}" fill="#000" stroke="#000" stroke-width="2.2"/></mask>'
                f'<mask id="t"><rect x="0" y="0" width="220" height="140" fill="#fff"/>'
                f'<path d="{P["tagline"]}" fill="#000"/></mask></defs>')
        return (head + defs + f'<path d="{P["rays"]}" fill="{ray}" mask="url(#r)"/><path d="{P["letters"]}" fill="{letters}"/>'
                f'<path d="{P["oval"]}" fill="{letters}" mask="url(#t)"/></svg>')
    return (head + f'<path d="{P["rays"]}" fill="{ray}"/>{o}<path d="{P["letters"]}" fill="{letters}"/>'
            f'<path d="{P["oval"]}" fill="{oval}"{os_}/>'
            f'<path d="{P["tagline"]}" fill="{tag_fill}"' + (f' stroke="{tag_stroke}" stroke-width="0.55"' if tag_stroke else '') + '/></svg>')

# Icon: the V with the sun rising behind it
def icon_rays(cx=33.4, cy=56):
    d = []
    for i, ang in enumerate(range(190, 360, 20)):
        t = math.radians(ang); r0, r1 = 19, (46 if i % 2 == 0 else 39)
        ux, uy = math.cos(t), math.sin(t); px, py = -uy, ux
        ax, ay = cx + r0 * ux, cy + r0 * uy; bx, by = cx + r1 * ux, cy + r1 * uy
        mx, my = cx + (r0 + (r1 - r0) * .62) * ux, cy + (r0 + (r1 - r0) * .62) * uy
        d.append(f"M{ax:.2f},{ay:.2f}Q{mx+px*1.9:.2f},{my+py*1.9:.2f} {bx:.2f},{by:.2f}Q{mx-px*1.9:.2f},{my-py*1.9:.2f} {ax:.2f},{ay:.2f}Z")
    return "".join(d)
IR = icon_rays()
IVB = "-16.6 3 100 100"

def icon_svg(ray, v, outline=None, bg=None, radius=0):
    b = f'<rect x="-16.6" y="3" width="100" height="100" rx="{radius}" fill="{bg}"/>' if bg else ""
    o = f'<path d="{P["Voutline"]}" fill="{outline}"/>' if outline else ""
    inner = f'<path d="{IR}" fill="{ray}"/>{o}<path d="{P["V"]}" fill="{v}"/>'
    if bg:  # shrink the mark inside a tile
        inner = f'<g transform="translate(33.4 53) scale(.8) translate(-33.4 -53)">{inner}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{IVB}">{b}{inner}</svg>'

SVGS = {
    "logo-color.svg": logo_svg(LEMON, BLUE, outline=SKY),
    "logo-reverse.svg": logo_svg(GOLD, "#ffffff", outline=BLUE, oval_stroke=SKY),
    "logo-white.svg": logo_svg("#ffffff", "#ffffff", knockout=True),
    "logo-blue.svg": logo_svg(BLUE, BLUE, knockout=True),
    "icon-color.svg": icon_svg(LEMON, BLUE, outline=SKY),
    "icon-reverse.svg": icon_svg(GOLD, "#ffffff", outline=BLUE),
    "icon-white.svg": icon_svg("#ffffff", "#ffffff"),
    "app-icon.svg": icon_svg(GOLD, "#ffffff", outline=BLUE, bg=NAVY, radius=18),
}
for n, s in SVGS.items():
    (KIT / n).write_text(s)

def page(body, w, h, bg="transparent"):
    return f"<html><body style='margin:0;width:{w}px;height:{h}px;background:{bg};overflow:hidden'>{body}</body></html>"

def raster(pw, html, w, h, out, transparent=True):
    tmp = pathlib.Path(tempfile.mkdtemp()) / "p.html"; tmp.write_text(html)
    pg = pw.new_page(viewport={"width": w, "height": h}); pg.goto(tmp.as_uri()); pg.wait_for_timeout(250)
    pg.screenshot(path=str(out), omit_background=transparent, clip={"x": 0, "y": 0, "width": w, "height": h}); pg.close()

def to_jpg(png, out, bg):
    im = Image.open(png).convert("RGBA"); base = Image.new("RGBA", im.size, bg); base.alpha_composite(im)
    base.convert("RGB").save(out, quality=92)

def svgimg(svg, w):  # inline svg sized by width
    return svg.replace("<svg ", f'<svg style="width:{w}px;display:block" ', 1)

with sync_playwright() as p:
    pw = p.chromium.launch()
    LW, LH = 2400, round(2400 * 106 / 212)
    for n in ["logo-color", "logo-reverse", "logo-white", "logo-blue"]:
        raster(pw, page(svgimg(SVGS[n + ".svg"], LW), LW, LH), LW, LH, KIT / f"{n}.png")
    to_jpg(KIT / "logo-color.png", KIT / "logo-color-on-white.jpg", "#ffffff")
    to_jpg(KIT / "logo-reverse.png", KIT / "logo-reverse-on-navy.jpg", NAVY)
    to_jpg(KIT / "logo-white.png", KIT / "logo-white-on-blue.jpg", BLUE)
    to_jpg(KIT / "logo-blue.png", KIT / "logo-blue-on-white.jpg", "#ffffff")
    for n in ["icon-color", "icon-reverse", "icon-white", "app-icon"]:
        raster(pw, page(svgimg(SVGS[n + ".svg"], 1024), 1024, 1024), 1024, 1024, KIT / f"{n}.png")
    to_jpg(KIT / "icon-color.png", KIT / "icon-color-on-white.jpg", "#ffffff")
    to_jpg(KIT / "icon-white.png", KIT / "icon-white-on-blue.jpg", BLUE)
    app = Image.open(KIT / "app-icon.png")
    app.save(KIT / "app-icon.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    Image.open(KIT / "icon-reverse.png").save(KIT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    app.resize((180, 180), Image.LANCZOS).save(KIT / "apple-touch-icon.png")

    # Microsoft 365 mailbox photo: navy square, mark centered for the circle crop
    raster(pw, page(f"<div style='width:648px;height:648px;background:{NAVY};display:grid;place-items:center'>{svgimg(icon_svg(GOLD,'#ffffff',outline=BLUE),430)}</div>", 648, 648), 648, 648, KIT / "m365-photo.png", False)
    to_jpg(KIT / "m365-photo.png", KIT / "m365-photo.jpg", NAVY)

    # Zoom backgrounds 1920x1080, logo top left, faint sun bottom right
    sun = f'<svg viewBox="-12.6 4 92 92" style="position:absolute;right:-180px;bottom:-260px;width:900px;opacity:.07"><path d="{IR}" fill="#ffffff"/></svg>'
    sun_l = sun.replace('fill="#ffffff"', f'fill="{BLUE}"').replace("opacity:.07", "opacity:.06")
    raster(pw, page(f"<div style='position:relative;width:1920px;height:1080px;background:{NAVY};overflow:hidden'><div style='position:absolute;left:64px;top:52px'>{svgimg(SVGS['logo-reverse.svg'],460)}</div>{sun}</div>", 1920, 1080), 1920, 1080, KIT / "zoom-dark.png", False)
    raster(pw, page(f"<div style='position:relative;width:1920px;height:1080px;background:{MIST};overflow:hidden'><div style='position:absolute;left:64px;top:52px'>{svgimg(SVGS['logo-color.svg'],460)}</div>{sun_l}</div>", 1920, 1080), 1920, 1080, KIT / "zoom-light.png", False)
    to_jpg(KIT / "zoom-dark.png", KIT / "zoom-dark.jpg", NAVY); to_jpg(KIT / "zoom-light.png", KIT / "zoom-light.jpg", MIST)

    # Social share image 1200x630
    raster(pw, page(f"<div style='position:relative;width:1200px;height:630px;background:{NAVY};overflow:hidden;font-family:Arial,sans-serif;color:#fff'>"
                    f"<div style='position:absolute;left:0;right:0;top:120px;display:flex;justify-content:center'>{svgimg(SVGS['logo-reverse.svg'],620)}</div>"
                    f"<div style='position:absolute;left:0;right:0;top:470px;text-align:center;font-size:34px;font-weight:700;letter-spacing:.5px'>Solar power solutions since 1989</div>"
                    f"<div style='position:absolute;left:0;right:0;top:522px;text-align:center;font-size:26px;color:{GOLD}'>(714) 968-8845 &nbsp;·&nbsp; CSL# 608260</div></div>", 1200, 630), 1200, 630, KIT / "social-share.png", False)
    to_jpg(KIT / "social-share.png", KIT / "social-share.jpg", NAVY)
    pw.close()
print("kit built:", len(list(KIT.iterdir())), "files")
