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

## Cloudflare Workers with Wrangler

`wrangler.jsonc` configures a static-assets-only Worker named `ludonaut-website`.

- Public assets: `site` only. No Worker script, bindings, or secrets.
- Custom domain: `ludonaut.ai`.
- workers.dev and preview URLs are disabled.
- No build command is required.
- Validate the intended Cloudflare account and existing DNS before deployment.

Using the official Wrangler CLI, after completing authorized authentication:

```sh
npx --yes wrangler@4.158.0 deploy --dry-run
CLOUDFLARE_ACCOUNT_ID="<verified account ID>" npx --yes wrangler@4.158.0 deploy
```

Keep credentials outside the repository. Do not publish tooling or private workspace files. Preserve unrelated DNS and services. A successful dry run does not mean the site is live; verify HTTPS and the delivered content after deployment. Repository commits do not automatically deploy unless a separate Cloudflare Git integration is configured.
