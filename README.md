# Ludonaut website

The minimal public teaser for **Ludonaut**, prepared for `https://ludonaut.ai`.

## Source

`site/index.html` is a static export of the approved Claude Design Version 4. It preserves the five lines of copy, black/red visual treatment, typography, grain, scanlines, and reduced-motion support. No JavaScript, backend, forms, analytics, or product credentials are included.

Fonts are loaded from Google Fonts (Archivo and JetBrains Mono). Visitors' browsers connect to `fonts.googleapis.com` and `fonts.gstatic.com`; system fonts are used if those requests fail.

## Local preview

```sh
python3 -m http.server 8080 --directory site
```

Open `http://localhost:8080` in a browser. Check desktop and narrow mobile layouts before deployment.

## Validation

```sh
python3 -m unittest discover -s tests -v
```

These checks validate markup, exact copy, asset boundaries, and the absence of scripts, forms, template syntax, or apparent secrets. They do not replace visual browser testing.

## GitHub Pages

The publishing source is `main` / `docs`, with the custom domain `ludonaut.ai`.

- `docs/index.html` is a byte-for-byte copy of `site/index.html`.
- `docs/.nojekyll` disables Jekyll processing.
- `docs/CNAME` declares the intended custom domain.
- Only `docs` is published; tooling, tests, and the repository README are excluded from the website.
- Keep the two HTML files identical when making changes.

Publishing requires GitHub Pages to be enabled for this repository and the domain's DNS to point to GitHub Pages. DNS changes preserve unrelated records. Verify HTTPS and the delivered HTML after deployment; committed configuration alone does not mean the site is live.

The earlier `wrangler.jsonc` is retained only as unused deployment history. Wrangler authentication and Cloudflare Workers deployment are not part of the active GitHub Pages setup.
