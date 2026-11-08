#!/usr/bin/env python3
"""Builds the Vasco Solar static site.  Run:  python3 tools/build.py  (writes *.html at repo root)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHONE = "(714) 968-8845"
TEL = "tel:+17149688845"
ADDR = "17150 Newhope St #403, Fountain Valley, CA 92708"
LIC = "CSL# 608260"

ICON = {
 "sun":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "pool":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 17c2 0 2-1.5 4-1.5S8 17 10 17s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5M2 21c2 0 2-1.5 4-1.5S8 21 10 21s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5M8 13V5a2 2 0 0 1 4 0M16 13V5a2 2 0 0 0-4 0M8 9h8"/></svg>',
 "drop":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.7S5 10 5 15a7 7 0 0 0 14 0c0-5-7-12.3-7-12.3z"/></svg>',
 "roof":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/></svg>',
 "wrench":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
 "clip":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="4" width="14" height="17" rx="1"/><path d="M9 4V2h6v2M9 11h6M9 15h4"/></svg>',
 "building":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 21V5l8-3v19M12 9h8v12M8 8h0M8 12h0M8 16h0M16 13h0M16 17h0M2 21h20"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6v20h12V6zM14 2v4h4M9 13l2 2 4-4"/></svg>',
 "battery":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="17" height="10" rx="1"/><path d="M22 11v2M11 9l-2 3h4l-2 3"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "badge":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 22l5-3 5 3-1.5-8"/></svg>',
 "money":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="1"/><circle cx="12" cy="12" r="3"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18M7 15l4-4 3 3 5-6"/></svg>',
 "pencil":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="4"/><path d="M1 21v-1a7 7 0 0 1 14 0v1M16 3.1a4 4 0 0 1 0 7.8M23 21v-1a7 7 0 0 0-5-6.7"/></svg>',
}

NAV = [("index.html","Home"),("services.html","Services"),("go-solar.html","Go Solar"),
       ("portfolio.html","Portfolio"),("learn.html","Solar Education"),("about.html","About")]

def page(fname, title, desc, body):
    nav = "".join(f'<a href="{h}"{" class=\"active\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero.jpg">
<link rel="icon" href="assets/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<div class="topbar"><div class="wrap"><span>Serving Orange County &amp; Los Angeles County for 40+ years &nbsp;·&nbsp; {LIC}</span><span>Call for a free estimate: <a href="{TEL}">{PHONE}</a></span></div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html"><img src="assets/img/logo.png" alt="Vasco Solar"></a>
  <button class="menu-btn" aria-label="Menu">&#9776;</button>
  <nav class="main">{nav}<a class="btn btn-sun" href="contact.html">Free Estimate</a></nav>
</div></header>
<main>
{body}
</main>
<section class="cta"><div class="wrap">
  <div><h2>Ready to start saving?</h2><p>Every system is custom designed for your home.  Free, no-obligation estimates.</p></div>
  <div class="actions"><a class="btn btn-sun" href="contact.html">Schedule Your Free Estimate</a><a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div><img class="logo-bw" src="assets/img/logo-bw.png" alt="Vasco Solar">
      <p>Full-service solar for homes and businesses in Southern California: solar electricity, pool heating, hot water and battery storage.</p>
      <p>{LIC}</p></div>
    <div><h4>Services</h4><ul>
      <li><a href="services.html#solar-electricity">Solar Electricity</a></li><li><a href="services.html#pool-heating">Solar Pool Heating</a></li>
      <li><a href="services.html#hot-water">Solar Hot Water</a></li><li><a href="services.html#batteries">Battery Solutions</a></li>
      <li><a href="services.html#reroofing">Solar Re-Roofing</a></li><li><a href="services.html#repair">Repair &amp; Service</a></li></ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="about.html">About Us</a></li><li><a href="about.html#partners">Partners</a></li><li><a href="about.html#reviews">Reviews</a></li>
      <li><a href="portfolio.html">Portfolio</a></li><li><a href="go-solar.html#financing">Financing</a></li><li><a href="learn.html">Solar Education</a></li></ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="{TEL}">{PHONE}</a></li><li>{ADDR.replace(', Fountain', '<br>Fountain')}</li>
      <li><a href="https://www.facebook.com/pages/Vasco-Solar-Energy/166852197671" rel="noopener">Facebook</a> · <a href="https://instagram.com/vascosolar" rel="noopener">Instagram</a> · <a href="https://www.yelp.com/biz/vasco-solar-energy-construction-huntington-beach" rel="noopener">Yelp</a> · <a href="https://www.youtube.com/channel/UChk1ZMSTl4NAo8vS2-lmLlQ" rel="noopener">YouTube</a></li></ul></div>
  </div>
  <div class="legal"><span>&copy; <span class="year">2026</span> Vasco Solar.  All rights reserved.</span><span>Licensed California Solar Contractor · {LIC}</span></div>
</div></footer>
<div class="lightbox"><button aria-label="Close">&times;</button><img alt=""></div>
<script src="assets/js/site.js"></script>
</body>
</html>
"""
    (ROOT / fname).write_text(html)

def hero(title, sub, img):
    return f'<section class="page-hero" style="background-image:url(assets/img/{img})"><div class="wrap"><h1>{title}</h1><p>{sub}</p></div></section>'

def card(icon, title, text):
    return f'<div class="card"><div class="ico">{ICON[icon]}</div><h3>{title}</h3><p>{text}</p></div>'

# ---------------------------------------------------------------- HOME
SERVICES = [
 ("sun","Solar Electricity","Grid-tied PV systems that cut your electric bill, protect you from rate increases and raise property value without raising property taxes.","solar-electricity"),
 ("pool","Solar Pool Heating","Extend your swim season and drastically reduce or eliminate pool-heating costs with proven Solar Industries collectors.","pool-heating"),
 ("drop","Solar Hot Water","Custom-designed domestic hot water systems that supply most of your home's hot water, starting around $5,500 to $7,000.","hot-water"),
 ("battery","Battery Solutions","Certified FranklinWH, SolarEdge and Enphase installer: backup power for outages and stored solar for evenings.","batteries"),
 ("roof","Solar Re-Roofing","Licensed removal and reinstallation of your panels when you re-roof, with a two-year workmanship warranty.","reroofing"),
 ("wrench","Repair &amp; Service","Inverters, batteries, panels, pumps, controls and leaks: we service most types of solar systems.","repair"),
 ("clip","System Evaluations","Written condition reports for home sales, insurance work, or when you're unsure your system is performing.","evaluations"),
 ("building","HOA &amp; Commercial Pools","Clean, affordable pool heating for HOAs, hotels, apartments, health clubs, schools and water parks.","commercial"),
 ("doc","Title 24 Compliance","New homes, ADUs, additions and new pool heaters: we keep your project compliant with California's Energy Code.","title-24"),
]

REVIEWS = [
 ("Craig K.","Orange, CA","Google &amp; Yelp","A customer for 7+ years, starting with pool solar and later adding home electric solar.  The team treats them like family, responds quickly, and delivers good value and workmanship."),
 ("Paul K.","","Yelp","A repeat customer for pool and electric solar.  Friendly service, fair pricing, on-time crews and clean job sites, and he expanded from a 6 kW to a 10 kW system a year later."),
 ("Nick C.","","Yelp","No sales pressure, exactly what he wanted at a good price, and a professional crew that showed up on time both installation days."),
 ("Thomas C.","","Yelp","A 12-panel pool solar installation, including trenching and roof work, finished in about seven and a half hours, and the pool was warm that same night."),
 ("Joe Pearson","","Facebook","They did the job right, recommended only what he actually needed, and backed it with good service."),
 ("P M.","","Yelp","Fast service and reasonable prices for solar pool heating tune-ups and repairs."),
]

def review_cards(items):
    out = []
    for n,city,src,txt in items:
        loc = f" · {city}" if city else ""
        out.append(f'<div class="review"><div class="stars">★★★★★</div><p>{txt}</p><div class="who">{n}</div><div class="src">{src}{loc}</div></div>')
    return "".join(out)

LOGOS = ["logo-enphase.png","logo-solaredge.jpg","logo-sma.png","logo-aquatherm.png","logo-si.png","logo-sunearth.png",
         "logo-pentair.jpg","logo-unirac.png","logo-quickmount.png","logo-grundfos.png","cert-franklinwh.png","logo-se-battery.png"]
logo_strip = '<div class="logos">' + "".join(f'<div><img src="assets/img/{l}" alt=""></div>' for l in LOGOS) + '</div>'

home = f"""
<section class="hero" style="background-image:url(assets/img/hero.jpg)"><div class="wrap">
  <span class="eyebrow">Solar power solutions for over 40 years</span>
  <h1>Dependable, affordable, <em>best-in-class solar.</em></h1>
  <p>For more than 40 years, Vasco Solar has designed and installed custom solar systems for Southern California homeowners and businesses, with $0-down financing and monitoring from your phone.</p>
  <div class="actions"><a class="btn btn-sun" href="contact.html">Schedule Your Free Estimate</a><a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>
<div class="stats"><div class="wrap">
  <div class="stat"><b>40+</b><span>Years in business</span></div>
  <div class="stat"><b>Thousands</b><span>Of systems installed</span></div>
  <div class="stat"><b>Top 500</b><span>Solar Power World, 2016–2020, 2024 &amp; 2026</span></div>
  <div class="stat"><b>$0 Down</b><span>Financing available</span></div>
</div></div>

<section><div class="wrap">
  <div class="head center"><span class="eyebrow">What we do</span><h2>Every kind of solar, under one roof</h2>
  <p class="lede">Solar electricity, solar pool heating, solar hot water and battery storage, each one designed around your property, your usage and your goals.</p></div>
  <div class="grid g3">{''.join(card(i,t,d) for i,t,d,_ in SERVICES)}</div>
</div></section>

<section class="alt"><div class="wrap split">
  <img src="assets/img/pv-04.jpg" alt="Rooftop solar electric system in Huntington Beach installed by Vasco Solar" loading="lazy">
  <div><span class="eyebrow">Why Vasco Solar</span><h2>Built on word of mouth, not advertising</h2>
  <p>Customer satisfaction and referrals have kept Vasco Solar growing for four decades.  We pair top-of-the-line panels and equipment with experienced technicians and a system designed for your unique situation.</p>
  <ul class="checks">
    <li><b>Custom-designed systems</b>: sized to your roof, your usage and your budget</li>
    <li><b>$0 down financing</b>: credit union loans from 7 to 20 years, no prepayment penalty</li>
    <li><b>Monitoring anywhere</b>: see and share your system's production from your computer or phone</li>
    <li><b>Recognized expertise</b>: technical expert for the California Contractors State License Board</li>
  </ul></div>
</div></section>

<section><div class="wrap">
  <div class="head center"><span class="eyebrow">Reviews</span><h2>What our customers say</h2></div>
  <div class="grid g3">{review_cards(REVIEWS)}</div>
</div></section>

<section class="alt"><div class="wrap">
  <div class="head center"><span class="eyebrow">Awards &amp; affiliations</span><h2>Recognized by the industry</h2></div>
  <div class="awards"><img src="assets/img/award-top-contractor-2026.png" alt="Solar Power World Top Solar Contractor 2026"><img src="assets/img/award-top-contractor-2024.jpg" alt="Solar Power World Top Solar Contractor 2024"><img src="assets/img/seal-2025.png" alt="Vasco Solar Seal 2025"><img src="assets/img/gold-medal.png" alt="Aquatherm Gold Medal Installer"></div>
  <div style="height:56px"></div>
  <div class="head center" style="margin-bottom:28px"><h3>The brands we install</h3></div>
  {logo_strip}
</div></section>
"""
page("index.html","Vasco Solar | Solar Electricity, Pool Heating & Hot Water in Orange County",
     "Vasco Solar designs and installs solar electricity, solar pool heating, solar hot water and battery systems in Orange County and Los Angeles County.  40+ years.  Free estimates.", home)

# ---------------------------------------------------------------- SERVICES
svc_nav = '<nav class="subnav"><div class="wrap">' + "".join(f'<a href="#{a}">{t}</a>' for _,t,_,a in SERVICES) + '</div></nav>'

services = hero("Our Services","Custom-designed solar systems, expert service and repair for most types of solar, and compliance help for new construction.","pv-banner.jpg") + svc_nav + f"""
<div class="wrap">

<div class="svc" id="solar-electricity"><div class="split">
 <div><span class="eyebrow">Solar Electricity (PV)</span><h2>Make your own power</h2>
 <p>Photovoltaic modules convert sunlight into electricity.  Systems generate during daylight hours, peaking in the afternoon; clouds, rain and dirty panels reduce output.  California has more homes with solar than any other state, and most systems are connected to the local utility grid.</p>
 <p>When your system produces less than you use, such as at night, the utility or a battery fills the gap.  When it produces more, the surplus flows back to the grid.  It all switches automatically.</p>
 <ul class="checks"><li>Substantially lower electric bills</li><li>Protection from future utility rate increases</li><li>Higher property value without higher property taxes</li><li>Fewer emissions and less dependence on oil</li></ul></div>
 <img src="assets/img/pv-07.jpg" alt="Solar electric system in Costa Mesa" loading="lazy">
</div></div>

<div class="svc" id="pool-heating"><div class="split">
 <img src="assets/img/pool-08.jpg" alt="Solar pool and hot water system on a tile roof in Corona del Mar" loading="lazy">
 <div><span class="eyebrow">Solar Pool Heating</span><h2>A warmer pool, for months longer</h2>
 <p>A comfortable pool becomes the gathering place for family and friends.  A Vasco system lengthens your swim season, makes the water warmer, and can drastically reduce or eliminate pool-heating costs.  We've installed thousands of systems and worked with nearly every type of solar heating system.</p>
 <h3>Solar Industries SI-2000 collectors</h3>
 <ul class="checks"><li>Survived a 23-year life expectancy test in the Arizona desert</li><li>Tens of thousands of installations worldwide since 1976</li><li>Unaffected by pool chemicals; can't rust, corrode or discolor your pool</li><li>NSF-50 listed and rated 1,100 Btu/ft² by the Florida Solar Energy Center</li><li>4 ft wide in 10 or 12 ft lengths; roof or ground-rack mounted</li></ul></div>
</div>
<h3 style="margin-top:36px">How it works</h3>
<ol class="steps"><li>You set your desired temperature on the automatic control panel.</li><li>A solar sensor checks for enough solar energy and whether the pool is below your setpoint; it works on hazy or cloudy days too.</li><li>A valve sends pool water up to the collectors, pushed by your existing pool pump.</li><li>The sun heats the water as it flows through the collector tubes, then it returns to the pool, repeating until your target temperature is reached.</li></ol>
</div>

<div class="svc" id="hot-water"><div class="split">
 <div><span class="eyebrow">Solar Hot Water</span><h2>Most of your home's hot water, from the sun</h2>
 <p>Heating water is one of the oldest uses of solar energy, and millions of homes and businesses do it today.  A single conventional water heater can generate one to two tons of carbon dioxide per year; solar displaces that, along with sulfur dioxide, carbon monoxide and nitrous oxides.</p>
 <p>Roof collectors absorb the sun's heat, a pump circulates water to a storage tank in your garage or utility room, and a differential temperature controller captures the maximum available energy.  Every system is custom designed.</p>
 <div class="note"><b>Typical two-panel system: $5,500 to $7,000</b>, including two collectors, a solar storage tank, insulation, pump and automatic control.  Payback depends on your water use and utility rates.</div></div>
 <img src="assets/img/hot-water.jpg" alt="Solar hot water collectors" loading="lazy">
</div></div>

<div class="svc" id="batteries"><div class="split">
 <img src="assets/img/battery-01.jpg" alt="Home battery storage installed by Vasco Solar" loading="lazy" style="aspect-ratio:3/4;max-height:520px">
 <div><span class="eyebrow">Battery Solutions</span><h2>Custom energy storage</h2>
 <p>Vasco Solar is a certified installer for FranklinWH, SolarEdge and Enphase.  We'll design the battery solution that best fits your situation.</p>
 <div class="grid" style="gap:16px">
  <div class="card"><h3>FranklinWH</h3><p>Whole-home energy management that integrates solar, battery, grid, generator and EV.  The new aPower 2 backs up more of your home, offsets more grid use, and carries a 15-year warranty.  Compatible with all PV inverters.</p></div>
  <div class="card"><h3>SolarEdge</h3><p>DC-coupled batteries store excess solar for nights or high-rate hours and, with the Backup Interface, power your home during outages.  One source for products, warranty and support.</p></div>
  <div class="card"><h3>Enphase</h3><p>The IQ Battery 5P is easy to expand as your needs grow, with a 15-year limited warranty.</p></div>
 </div></div>
</div></div>

<div class="svc" id="reroofing"><div class="split">
 <div><span class="eyebrow">Solar Re-Roofing</span><h2>Re-roofing?  Call a licensed solar contractor.</h2>
 <p>We specialize in removing and reinstalling solar systems for re-roofing projects, electric, hot water and pool heating alike.</p>
 <p>For pool panels we use QuickMount flashings, developed with Aquatherm Industries.  They meet or exceed roofing codes and best practices, are made in the USA, and use patented Elevated Water Seal Technology.</p>
 <div class="note"><b>Two-year warranty</b> on all work and labor.</div></div>
 <div class="pair"><figure><img src="assets/img/roof-before.jpg" alt="Solar hot water system during re-roof" loading="lazy"><figcaption>During</figcaption></figure><figure><img src="assets/img/roof-after.jpg" alt="Solar hot water system after re-roof" loading="lazy"><figcaption>After</figcaption></figure></div>
</div></div>

<div class="svc" id="repair"><span class="eyebrow">Repair &amp; Service</span><h2>We service most types of solar systems</h2>
 <div class="grid g4" style="margin-top:28px">
  <div class="card"><h3>Solar Electric</h3><ul><li>Inverter replacement</li><li>Battery replacement</li><li>Panel replacement</li><li>Upgrades and added capacity</li></ul></div>
  <div class="card"><h3>Pool Heating</h3><ul><li>Pumps, filters, heaters, chlorinators</li><li>Pipe leak repair</li><li>Panel repair</li><li>Tune-ups</li></ul></div>
  <div class="card"><h3>Hot Water</h3><ul><li>Solar storage tank replacement</li><li>Water heater repair or replacement</li><li>Controls, sensors, freeze protection</li><li>Panel repair</li></ul></div>
  <div class="card"><h3>Other</h3><ul><li>Insurance work</li><li>Maintenance contracts</li><li>Written evaluations for home sales</li></ul></div>
 </div></div>

<div class="svc" id="evaluations"><div class="split">
 <div><span class="eyebrow">System Evaluations</span><h2>A written assessment from a licensed contractor</h2>
 <p>Evaluations are often needed for real estate transactions and insurance work, or when you're simply not sure your system is operating properly, and they should only be performed by a licensed solar contractor.</p>
 <p>You'll receive a written report covering the system's condition, our observations, and any recommendations.</p></div>
 <img src="assets/img/inspection.jpg" alt="Solar system inspection form" loading="lazy">
</div></div>

<div class="svc" id="commercial"><div class="split">
 <img src="assets/img/hoa.jpg" alt="Commercial pool heated with solar" loading="lazy">
 <div><span class="eyebrow">HOA &amp; Commercial Pools</span><h2>Lower the monthly bill for heating big pools</h2>
 <p>Solar energy is a clean, affordable way to reduce the cost of heating community and commercial pools: hotels, resorts, apartment complexes, HOAs, health clubs, camps, water parks and schools.</p>
 <p><a class="btn btn-navy" href="contact.html">Schedule an evaluation</a></p></div>
</div></div>

<div class="svc" id="title-24"><div class="split">
 <div><span class="eyebrow">Title 24 Compliance</span><h2>Stay compliant with California's Energy Code</h2>
 <p>Title 24, Part 6 requires solar PV on almost all new residential buildings, and the requirement reaches new builds, major renovations, ADUs and additions.</p>
 <div class="note"><b>Pool heating, effective January 1, 2026:</b> for new pools or first-time heater installations, gas can no longer be the only primary heat source.  Options include solar thermal pool heating, heat pump pool heaters, or hybrid renewable systems.</div>
 <p>We'll help your project meet the code.</p></div>
 <img src="assets/img/title24-pool.jpg" alt="Pool heating under Title 24" loading="lazy">
</div></div>

</div>
"""
page("services.html","Services | Vasco Solar","Solar electricity, pool heating, hot water, batteries, re-roofing, repair, evaluations, commercial pools and Title 24 compliance from Vasco Solar.", services)

# ---------------------------------------------------------------- GO SOLAR
go = hero("Go Solar","Why solar still pays in California, and the ways to pay for it.","pv-02.jpg") + f"""
<section><div class="wrap">
 <div class="head center"><span class="eyebrow">Benefits</span><h2>Why go solar</h2></div>
 <div class="grid g3">
  {card("chart","Hedge against rising rates","Utility energy is expected to keep getting more expensive and is exposed to market swings.  Solar locks in your cost.")}
  {card("roof","Higher property value","Solar adds value to your home, and in California it's excluded from property tax reassessment.")}
  {card("money","Untaxed returns","Solar can outperform many long-term investments, and unlike dividends, your savings aren't taxed.")}
  {card("sun","Power or hot water","Output comes as kilowatts that offset your electricity or therms that heat your water.")}
  {card("users","Local jobs","Solar supports installers, engineers, designers, distributors and manufacturers in our community.")}
  {card("drop","A cleaner environment","Solar conserves natural resources and displaces emissions from fossil fuels.")}
 </div>
</div></section>

<section class="alt" id="incentives"><div class="wrap split">
 <div><span class="eyebrow">Rebates &amp; incentives</span><h2>The federal credit has ended.  Solar still pays.</h2>
 <p>The 30% federal Residential Clean Energy Credit for residential systems expired on December 31, 2025.  Without it, payback takes a few years longer, but total lifetime savings remain substantial for most homes with good solar potential.</p>
 <p>Most homeowners still come out ahead: net-positive savings, higher home value, and more control over their energy.</p></div>
 <img src="assets/img/pv-09.jpg" alt="Solar electric system in Dana Point" loading="lazy">
</div></section>

<section id="financing"><div class="wrap">
 <div class="head center"><span class="eyebrow">Financing</span><h2>Ways to pay</h2><p class="lede">The sooner you install, the sooner your electric bill drops.</p></div>
 <div class="grid g4">
  <div class="card"><div class="ico">{ICON['money']}</div><h3>Cash</h3><p>Savings you get sooner are worth more than the same savings later.  Customers average a pre-tax internal rate of return of 25–35% over 25 years.</p></div>
  <div class="card"><div class="ico">{ICON['badge']}</div><h3>Credit Union Loan</h3><p>$0 down, low fixed payments, 7, 12, 15 or 20-year terms.  No escalators, no prepayment penalty, and free energy once it's paid off.</p></div>
  <div class="card"><div class="ico">{ICON['roof']}</div><h3>Home Equity (HELOC)</h3><p>You may qualify for the mortgage interest deduction, and you pay down the balance at your own pace.</p></div>
  <div class="card"><div class="ico">{ICON['doc']}</div><h3>Credit Card</h3><p>Many customers pay by card to earn travel or rewards points.  Card processing fees apply.</p></div>
 </div>
</div></section>

<section class="alt"><div class="wrap split">
 <img src="assets/img/monitoring.jpg" alt="Solar production monitoring on a phone and computer" loading="lazy">
 <div><span class="eyebrow">Monitoring</span><h2>Watch your savings in real time</h2><p>See your system's generation anytime, anywhere, from your computer or phone, and share your energy production.  The monitoring interface depends on your system type.</p></div>
</div></section>
"""
page("go-solar.html","Go Solar: Benefits, Incentives & Financing | Vasco Solar","Benefits of solar, the current state of rebates and incentives, and financing options including $0-down credit union loans.", go)

# ---------------------------------------------------------------- PORTFOLIO
PF = []
pool_caps = {1:"Crown Valley",2:"Huntington Beach",3:"Hillside rack",4:"Hillside racks",5:"Flat tile roof",8:"Pool &amp; hot water, Corona del Mar",11:"Rossmoor",12:"Rossmoor"}
for i in range(1,15): PF.append(("pool",f"pool-{i:02d}.jpg",pool_caps.get(i,"Solar pool heating")))
pv_caps = {2:"Three systems, Huntington Beach",4:"Huntington Beach",5:"Rossmoor",7:"Costa Mesa",9:"Dana Point",10:"Long Beach"}
for i in range(1,13): PF.append(("pv",f"pv-{i:02d}.jpg",pv_caps.get(i,"Solar electric")))
for i in range(1,5): PF.append(("battery",f"battery-{i:02d}.jpg","Battery storage"))
label = {"pool":"Solar pool heating","pv":"Solar electric","battery":"Battery storage"}
gallery = "".join(f'<figure data-cat="{c}"><img src="assets/img/{f}" alt="{label[c]}: {cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for c,f,cap in PF)
portfolio = hero("Portfolio","A few of the thousands of systems we've installed across Orange County and Los Angeles County.","pool-02.jpg") + f"""
<section><div class="wrap">
 <div class="filters"><button class="on" data-f="all">All</button><button data-f="pool">Pool Heating</button><button data-f="pv">Solar Electric</button><button data-f="battery">Batteries</button></div>
 <div class="gallery">{gallery}</div>
</div></section>
"""
page("portfolio.html","Portfolio | Vasco Solar","Solar pool heating, solar electric and battery installations by Vasco Solar across Southern California.", portfolio)

# ---------------------------------------------------------------- LEARN
def faq(items):
    return '<div class="faq">' + "".join(f'<div class="faq-item"><h3>{q}</h3>{a if a.startswith("<") else "<p>"+a+"</p>"}</div>' for q,a in items) + '</div>'

electric = [
 ("How does sunshine become electricity?","Solar cells turn sunlight into DC electricity.  The inverter, the system's brain, converts it to AC power your home uses.  It feeds your electrical panel to run lights and appliances, and your utility meter runs backward when you produce more than you're using."),
 ("Do I need south-facing exposure?","Not necessarily.  Southern exposure makes a system more effective, but many homes without it still work well for solar."),
 ("Will my property taxes go up?","Probably not.  In California, adding an active solar energy system to an existing property is automatically excluded from reassessment, usually with nothing to file, and there's no limit on how much solar you can add."),
]
pool = [
 ("What areas do you cover?","We install and service systems mainly in Orange County and Los Angeles County, including Aliso Viejo, Anaheim, Irvine, Newport Beach, Huntington Beach, Long Beach, Beverly Hills and surrounding communities."),
 ("What should I ask when comparing solar pool heating systems?","<ul><li>Have the manufacturer and contractor been in business longer than the warranty?</li><li>Is the company a licensed solar contractor with liability and workers' comp certificates?</li><li>Does the installer have experience with all types of solar heating systems?</li><li>Is the warranty backed by the original manufacturer, not a distributor?</li><li>Is the mounting system proven against hurricane-force winds?</li><li>Is the collector certified and tested by independent agencies?</li><li>Has the collector proven trouble-free over 20+ years of use?</li></ul>"),
 ("Will my HOA allow solar?","Yes.  California's Solar Rights Act makes it illegal for HOAs to prohibit solar installations."),
 ("Can one system heat both my pool and my household water?","No.  California pool collectors are unglazed and designed to heat thousands of gallons to about 80°F.  Hot water systems heat under 100 gallons to about 130°F, which takes very little energy by comparison."),
 ("Can the collectors heat a spa?","Yes.  Set the spa circulation cycle for the end of the day and the thermostat to 104°F."),
 ("Will I need a pool cover?","Not during the warm swim season.  A cover does hold heat overnight and cuts evaporative heat loss."),
 ("How much warmer will my pool be?","Following our recommended collector sizing, typically 6 to 20 degrees warmer than before under the same weather.  More collector area relative to pool surface means warmer water."),
 ("Can my home accommodate a system?  Must it face south?","Most homes can.  Collectors usually go on the roof but can go anywhere with good sun for much of the day, and they don't have to face south.  Size depends on your pool, location, orientation, shading and desired season."),
 ("How does a solar pool heater work?","Your existing pump sends water through the filter, then sensors and a motorized valve divert it through the collectors when there's heat available.  The warmed water returns to the pool, and once it reaches your setpoint, water bypasses the collectors."),
 ("What does it cost to operate and maintain?","Nothing to operate, because the sun is free.  Maintenance is minimal; normal filter cleaning is usually all that's needed, with a cleaning and service check recommended after five years."),
 ("Why heat with solar?","The U.S. Department of Energy identifies solar pool heating as one of the most cost-effective ways to cut energy use.  Gas heaters release carbon dioxide and other emissions; solar uses no fossil fuel at all."),
]
dhw = [
 ("How much does a solar hot water system cost?","On average $5,500 to $7,000, depending on the number of people in the home, system size and type, roof type and building code requirements."),
 ("Will solar affect my water heater?","Yes, in a good way.  Your water heater runs less often, which can extend its life significantly."),
 ("What about maintenance?","Minimal.  Solar water heating systems are simple, and ours need almost no maintenance."),
 ("How do solar water heaters work?","A heat-transfer fluid flows through the collectors, heats up, and transfers that heat to your household water in a storage tank.  Solar can be your only hot water source or pair with a conventional backup for heavy demand.  Systems are sized by bedrooms, occupants and household needs."),
]

learn = hero("Solar Education","Straight answers about solar electricity, pool heating, hot water, net metering and your rights as a homeowner.","pool-3.jpg") + """
<nav class="subnav"><div class="wrap"><a href="#electric">Solar Electric FAQ</a><a href="#pool">Pool Heating FAQ</a><a href="#operation">Pool System Operation</a><a href="#hot-water">Hot Water FAQ</a><a href="#net-metering">Net Metering</a><a href="#solar-rights">Solar Rights Act</a></div></nav>
<section id="electric"><div class="wrap"><span class="eyebrow">FAQ</span><h2>Solar electric</h2>""" + faq(electric) + """</div></section>
<section class="alt" id="pool"><div class="wrap"><span class="eyebrow">FAQ</span><h2>Solar pool heating</h2>""" + faq(pool) + """</div></section>
<section id="operation"><div class="wrap"><span class="eyebrow">Owner's guide</span><h2>Solar pool system operation</h2>
 <div class="note"><b>Before you start:</b> drain the system for winter before November 15 and keep it off until March 1.  Many systems drain automatically, so check with us if you're not sure.</div>
 <div class="grid g2" style="margin-top:28px">
  <div class="card"><h3>Normal startup</h3><ol class="steps"><li>Confirm the pool pump is running and the power indicator is lit.</li><li>Set the solar controller's function switch to Automatic.</li><li>Set your temperature between 60°F and 104°F.</li><li>When water enters the collectors, filter pressure rises about 4–7 psi and air purges for roughly 3 minutes (you'll see bubbles).</li></ol></div>
  <div class="card"><h3>Backwashing the filter</h3><ol class="steps"><li>Turn off the controller and wait for the solar valve to move fully to Bypass.</li><li>Turn the red-handle ball valve to Off (perpendicular to the pipe).</li><li>Backwash as usual and add diatomaceous earth.</li><li>Wait about 30 minutes, reopen the red-handle valve, and return the controller to Automatic.</li></ol></div>
  <div class="card"><h3>Winter freeze protection</h3><ol class="steps"><li>Set the solar controller to Off.</li><li>Turn off the main pump and wait at least one hour for drainage.</li><li>Close the red-handle ball valve to isolate the collectors.</li><li>Open the 1/2-inch ball valve and leave it open until spring startup.</li></ol></div>
  <div class="card"><h3>Troubleshooting &amp; tips</h3><ul><li><b>No "flow through collector" light:</b> confirm Automatic, then try the manual flow setting; if still off, call us.</li><li><b>No bubbles at startup:</b> check the pump, controller mode, connections and temperature setting.</li><li><b>Bubbles that won't stop:</b> clean or backwash the filter and empty the pump basket.</li><li>Run the pump roughly 11 AM to 5 PM, pull from the main drain, and aim return jets downward.</li></ul></div>
 </div>
</div></section>
<section class="alt" id="hot-water"><div class="wrap"><span class="eyebrow">FAQ</span><h2>Solar hot water</h2>""" + faq(dhw) + """</div></section>
<section id="net-metering"><div class="wrap"><span class="eyebrow">Your utility bill</span><h2>Net metering &amp; the Solar Billing Plan</h2>
 <p class="lede">Which program you're on depends on when your system was interconnected.  Click any column heading to sort.</p>
 <table class="data" style="margin-top:24px"><thead><tr><th>Program</th><th>Utility</th><th>Systems installed</th><th>Bill guide</th></tr></thead><tbody>
  <tr><td>NEM 1.0</td><td>SCE</td><td>Before June 30, 2017</td><td><a href="https://www.sce.com/sites/default/files/inline-files/NEM%2B1.0%2BUYB%2B0617%2Br3.pdf" rel="noopener">Understanding your NEM 1.0 bill (PDF)</a></td></tr>
  <tr><td>NEM 2.0</td><td>SCE</td><td>July 1, 2017 to April 13, 2023</td><td><a href="https://www.sce.com/sites/default/files/inline-files/Understanding_Your_NEM_2_Billing_Statement%2B%281%29.pdf" rel="noopener">Understanding your NEM 2.0 bill (PDF)</a></td></tr>
  <tr><td>Solar Billing Plan</td><td>SCE</td><td>After April 14, 2023</td><td><a href="https://www.sce.com/residential/generating-your-own-power/solar-billing-plan" rel="noopener">SCE Solar Billing Plan</a></td></tr>
  <tr><td>Net Metering</td><td>SDG&amp;E</td><td>See statement guide</td><td><a href="assets/img/doc-sdge-net-metering.pdf">Understanding your SDG&amp;E bill (PDF)</a></td></tr>
 </tbody></table>
</div></section>
<section class="alt" id="solar-rights"><div class="wrap split">
 <div><span class="eyebrow">Know your rights</span><h2>California Solar Rights Act</h2>
 <p>California law limits restrictions that HOAs and others can place on solar energy systems, and makes it illegal for an HOA to prohibit a solar installation.</p>
 <p><a class="btn btn-navy" href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&amp;sectionNum=714" rel="noopener">Read Civil Code Section 714</a></p></div>
 <img src="assets/img/pv-05.jpg" alt="Solar electric system in Rossmoor" loading="lazy">
</div></section>
"""
page("learn.html","Solar Education & FAQs | Vasco Solar","FAQs on solar electricity, solar pool heating and hot water, pool system operation, net metering and the California Solar Rights Act.", learn)

# ---------------------------------------------------------------- ABOUT
partners = [
 ("Inverters","logo-enphase.png","Enphase","Microinverter systems built on high-tech innovation for residential and commercial solar."),
 ("Inverters","logo-solaredge.jpg","SolarEdge","Inverters that pair digital control with efficient power conversion."),
 ("Inverters","logo-sma.png","SMA","PV inverter and energy-management specialist for more than 35 years."),
 ("Battery Storage","cert-franklinwh.png","FranklinWH","Home energy management focused on safety, reliability and independence."),
 ("Battery Storage","logo-se-battery.png","SolarEdge Home Battery","DC-coupled storage with backup power through the Backup Interface."),
 ("Mounting","logo-quickmount.png","Quick Mount PV","Pioneered best roofing practices in rooftop solar mounting."),
 ("Mounting","logo-unirac.png","UniRac","Leading North American PV mounting manufacturer, a Hilti Group company."),
 ("Pool Heating","logo-aquatherm.png","Aquatherm","Pool heating manufacturer since 1978, made in Lakewood, New Jersey."),
 ("Pool Heating","logo-pentair.jpg","Pentair","Pool and spa equipment and energy-efficient pool parts."),
 ("Pool Heating","logo-si.png","Solar Industries","Pioneered the original pool heating collector design."),
 ("Hot Water","logo-sunearth.png","SunEarth","Solar thermal collectors and components since 1978."),
 ("Hot Water","logo-grundfos.png","Grundfos","One of the world's leading pump manufacturers."),
]
pcards = "".join(f'<div class="card partner"><div class="lg"><img src="assets/img/{img}" alt="{n}" loading="lazy"></div><div><span class="eyebrow" style="margin-bottom:.2em">{cat}</span><h3 style="margin-bottom:.2em">{n}</h3><p>{d}</p></div></div>' for cat,img,n,d in partners)

about = hero("About Vasco Solar","A full-service Orange County solar company with more than 40 years of experience.","pool-aquatherm.jpg") + f"""
<section><div class="wrap split">
 <div><span class="eyebrow">Who we are</span><h2>Renewable energy, done right since the beginning</h2>
 <p>Vasco Solar is a full-service solar company serving homeowners and businesses throughout Southern California, primarily Orange County, with a focus on saving energy and reducing utility costs.</p>
 <p>We design every type of solar application: solar electricity, solar pool heating, solar hot water and battery storage, each optimally designed for your unique situation.  Innovative technology, top-of-the-line equipment, skilled technicians and our commitment to customers have kept us going strong, and word of mouth remains our main source of new business.</p>
 <ul class="checks"><li>Technical expert for the California Contractors State License Board</li><li>Aquatherm Industries Gold Medal Installer</li><li>Solar Power World Top Solar Contractor, 2016–2020, 2024 and 2026</li><li>Proud member of CALSSA, the California Solar &amp; Storage Association</li><li>Licensed California contractor, {LIC}</li></ul></div>
 <img src="assets/img/pool-aquatherm.jpg" alt="Rick Vasquez of Vasco Solar with Aquatherm CEO Dave Sizelove at the Aquatherm plant, 2014" loading="lazy">
</div></section>

<section class="alt"><div class="wrap">
 <div class="awards"><img src="assets/img/award-top-contractor-2026.png" alt="Solar Power World Top Solar Contractor 2026"><img src="assets/img/award-top-contractor-2024.jpg" alt="Solar Power World Top Solar Contractor 2024"><img src="assets/img/seal-2025.png" alt="Vasco Solar Seal 2025"><img src="assets/img/gold-medal.png" alt="Aquatherm Gold Medal Installer"><img src="assets/img/cert-franklinwh.png" alt="FranklinWH Certified Installer"><img src="assets/img/cert-solaredge.png" alt="SolarEdge Certified Installer"><img src="assets/img/cert-enphase.jpg" alt="Enphase Certified Installer"></div>
</div></section>

<section id="partners"><div class="wrap">
 <div class="head center"><span class="eyebrow">Partners</span><h2>The manufacturers we trust</h2></div>
 <div class="grid g2">{pcards}</div>
</div></section>

<section class="alt" id="reviews"><div class="wrap">
 <div class="head center"><span class="eyebrow">Reviews</span><h2>Our favorite reviews</h2></div>
 <div class="grid g3">{review_cards(REVIEWS)}</div>
</div></section>
"""
page("about.html","About Us | Vasco Solar","Vasco Solar is a full-service Orange County solar company with 40+ years of experience, Top 500 Solar Contractor honors and CALSSA membership.", about)

# ---------------------------------------------------------------- CONTACT
chips = "".join(f'<label><input type="checkbox" name="interest" value="{v}"> {v}</label>' for v in ["Solar Electricity","Pool Heating","Hot Water","Batteries","Re-Roofing","Repair / Service"])
contact = hero("Get Your Free Estimate","Tell us a little about your project and we'll schedule a free, no-obligation estimate.","pv-10.jpg") + f"""
<section><div class="wrap split" style="align-items:start">
 <div>
  <form class="estimate" data-endpoint="">
   <div><label for="n">Name *</label><input id="n" name="name" required placeholder="First Last" autocomplete="name"></div>
   <div><label for="e">Email *</label><input id="e" name="email" type="email" required autocomplete="email"></div>
   <div><label for="p">Phone</label><input id="p" name="phone" type="tel" autocomplete="tel"></div>
   <div><label for="z">ZIP code</label><input id="z" name="zip" inputmode="numeric" autocomplete="postal-code"></div>
   <div class="full"><label for="a">Street address</label><input id="a" name="address" autocomplete="street-address"></div>
   <fieldset class="full"><label>I'm interested in</label><div class="chips">{chips}</div></fieldset>
   <div class="full"><label for="c">Comments</label><textarea id="c" name="comments" rows="5"></textarea></div>
   <input type="text" name="company" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
   <div class="full"><button class="btn btn-sun" type="submit">Get Your Free Estimate Now</button></div>
  </form>
  <div class="form-msg" style="margin-top:16px"></div>
 </div>
 <div><h2>Contact us</h2><p class="lede">A leader in innovative solar solutions for more than 40 years.  Start saving today.</p>
  <ul class="info-list">
   <li>{ICON['phone']}<div><b>Phone</b><br><a href="{TEL}">{PHONE}</a></div></li>
   <li>{ICON['pin']}<div><b>Office</b><br>{ADDR}</div></li>
   <li>{ICON['badge']}<div><b>License</b><br>California {LIC}</div></li>
  </ul>
  <iframe class="map" loading="lazy" title="Vasco Solar office map" src="https://maps.google.com/maps?q=17150+Newhope+St+%23403,+Fountain+Valley,+CA+92708&amp;output=embed"></iframe>
 </div>
</div></section>
"""
page("contact.html","Contact & Free Estimate | Vasco Solar","Request a free, no-obligation solar estimate from Vasco Solar in Fountain Valley, CA.  Call (714) 968-8845.", contact)

# ---------------------------------------------------------------- 404 with old-URL redirects
REDIRECTS = {
 "/services/solar-electricity-pv/":"services.html#solar-electricity","/services/solar-pool-heating/":"services.html#pool-heating",
 "/services/solar-hot-water-systems/":"services.html#hot-water","/services/solar-reroofing/":"services.html#reroofing",
 "/services/repair-and-service/":"services.html#repair","/services/system-evaluations/":"services.html#evaluations",
 "/services/hoa-commercial-pools/":"services.html#commercial","/services/hybrid-systems/":"services.html#title-24",
 "/services/battery-solutions/":"services.html#batteries","/services/":"services.html",
 "/go-solar/benefits/":"go-solar.html","/go-solar/rebates-and-incentives/":"go-solar.html#incentives","/go-solar/financing/":"go-solar.html#financing","/go-solar/":"go-solar.html",
 "/portfolio/":"portfolio.html","/solar-education/faq/electric-faq/":"learn.html#electric","/solar-education/faq/solar-pool-heating/solar-system-operation-procedures/":"learn.html#operation",
 "/solar-education/faq/solar-pool-heating/":"learn.html#pool","/solar-education/faq/domestic-hot-water-systems-faq/":"learn.html#hot-water",
 "/solar-education/net-metering/":"learn.html#net-metering","/solar-education/california-solar-rights-act/":"learn.html#solar-rights","/solar-education/":"learn.html",
 "/contact-us/about-us/":"about.html","/contact-us/partners/":"about.html#partners","/contact-us/reviews/":"about.html#reviews","/contact-us/":"contact.html",
}
import json
nf = hero("Page not found","That page has moved.  Taking you to the right place…","hero.jpg") + f"""
<section><div class="wrap center"><p class="lede">If you aren't redirected, head to the <a href="index.html">home page</a> or call <a href="{TEL}">{PHONE}</a>.</p></div></section>
<script>(function(){{var m={json.dumps(REDIRECTS)};var p=location.pathname.toLowerCase();if(!p.endsWith('/'))p+='/';
var keys=Object.keys(m).sort(function(a,b){{return b.length-a.length}});for(var i=0;i<keys.length;i++){{var k=p.indexOf(keys[i]);if(k!==-1){{location.replace(location.pathname.slice(0,k)+'/'+m[keys[i]]);return;}}}}}})();</script>
"""
page("404.html","Page not found | Vasco Solar","Page not found.", nf)
print("built")
