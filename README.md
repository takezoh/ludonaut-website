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

## Cloudflare Pages

- Production branch: `main`.
- Static output directory: `site`.
- No build command is required.
- Deploy only files in `site`, never this repository's tooling or local files.
- The intended custom domain is `ludonaut.ai`.

Domain registration alone does not mean a deployment is live. Preserve existing unrelated DNS records when attaching the domain. Repository commits do not automatically deploy unless a separate Cloudflare Git integration is configured.
