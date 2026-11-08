# Vasco Solar website

Modern rebuild of vascosolar.com as a static site (GitHub Pages ready, no build server needed).

- Pages: `index.html`, `services.html`, `go-solar.html`, `portfolio.html`, `learn.html`, `about.html`, `contact.html`, `404.html`
- All page content lives in `tools/build.py` — edit there, then run `python3 tools/build.py` to regenerate the HTML.
- Styles: `assets/css/site.css`.  Scripts: `assets/js/site.js`.
- Images: listed in `assets/manifest.txt`.  The **Import images** GitHub Action downloads them from the current site into `assets/img/` whenever the manifest changes (or run it by hand from the Actions tab).
- `404.html` redirects the old WordPress URLs (for example `/services/solar-pool-heating/`) to the matching section of the new site.
- The estimate form posts to the URL in its `data-endpoint` attribute (`contact.html`).  It is blank until a form delivery service is chosen; until then the form tells visitors to call.
