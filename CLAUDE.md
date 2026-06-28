# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ExcelinDigital (EiD)** is a static marketing website for a digital transformation consultancy, deployed at `excelindigital.com` via GitHub Pages. There is no build system, bundler, or package manager — all pages are plain HTML/CSS with inline styles and scripts.

## File Structure

- `index.html` — the primary production page (single-file, ~3,900 lines). All CSS is inlined in `<style>` tags inside the file.
- `tokens.css` — shared design token definitions (palette, typography, spacing). Referenced for authoring consistency but **not** linked by `index.html` (which inlines its own copy of these tokens).
- `about.html`, `contact.html`, `engagements.html`, `themes.html` — secondary pages.
- `images/` — favicons and hero background.
- `ClientsLogos/` — client logo PNGs used in the trust/clients section.
- `logos/` — partner/ecosystem logos.
- `index*.html`, `index-bak*.html`, `indexbak*.html` — historical snapshots and iteration backups. **Do not edit these**; they are reference copies only.
- `CNAME` — GitHub Pages custom domain (`excelindigital.com`).

## Architecture

`index.html` is a single long-scroll page composed of named `<section>` elements, each with a `data-screen-label` attribute for identification:

| Label | Content |
|---|---|
| 02 Hero | Headline + CTA |
| 03 Trust | Credential bar |
| 03a Featured Impact | Client impact card shoveler |
| 03b Clients | Client logo grid |
| 03c Themes | Practices/themes shoveler |
| 04 The gap | Problem framing |
| 05 Our Approach | 3-stage engagement timeline |
| 06 Framework | Service framework (ink band) |
| 06b Pillars | Delivery pillars |
| 09 CTA | Workshop CTA band |
| Footer | Nav + legal |

## Design System

All design tokens (colors, typography, spacing) live as CSS custom properties under the `--eid-*` namespace:

- **`--eid-ink-*`** — signature navy palette (primary brand color: `--eid-ink-800: #002E5F`)
- **`--eid-amber-*`** — accent/highlight orange (`--eid-amber-500: #E88A2C`)
- **`--eid-paper-*`** — warm off-white backgrounds
- **`--eid-n-*`** — neutral grey scale

Typography stack: **Source Serif 4** (headings/display), **IBM Plex Sans** (body), **IBM Plex Mono** (mono/labels), loaded via Google Fonts.

The `data-page` attribute on `<html>` (`data-page="web"`) controls page-level CSS scoping.

## Development Workflow

No build step — edit HTML files directly and open in a browser to preview.

To preview locally:
```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

Deployments happen automatically via GitHub Pages on push to `main`.

## Key Conventions

- Edits to the live site go to `index.html`. Never use the numbered/backup variants as the target for changes.
- When adding a new section, follow the existing pattern: `<section class="<name>-section" id="<anchor>" data-screen-label="NN Label">`.
- Inline all new CSS into `index.html`'s `<style>` block using `--eid-*` tokens. Do not create separate CSS files or link external stylesheets (other than the existing Google Fonts `@import`).
- The mobile hamburger menu and nav are at the top of the `<section class="site">` wrapper (~line 2802).
