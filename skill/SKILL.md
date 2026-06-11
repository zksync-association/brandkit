---
name: zk-nation-brand
description: >-
  Apply the official ZKsync Association / ZK Nation brand to any document, slide deck,
  website, component, or asset. Use whenever the user asks to "apply the ZK Nation brand",
  "make this on-brand for ZKsync/ZK Nation", brand a doc/deck/site/email, design a new
  component/block/menu in the ZK Nation style, or needs the brand's colors, fonts (Inter,
  ES Allianz, Avenue Mono), logos, flags, icons, voice/tone, vocabulary, or design tokens.
  Covers the primary ZK Nation governance brand and the secondary ZKsync protocol brand.
---

# ZK Nation / ZKsync Association Brand

Make anything look, read, and feel like the official brand. This skill is the single source
of truth for color, type, logo, visual language, voice, and reusable components.

## Two brands — pick one first
- **ZK Nation (PRIMARY, default):** governance, community, voting, the DAO, civic/expressive
  work. Fonts: **ES Allianz** (display) + **Avenue Mono** (UPPERCASE UI labels) + Inter (body).
  Flags + ASCII visual language. Salmon accent used sparingly.
- **ZKsync protocol (SECONDARY):** the technology / enterprise / developer product. Inter
  throughout, triangle CTA accents, cleaner corporate feel. See
  `references/secondary-brand-zksync-protocol.md`.

When unsure, use **ZK Nation**.

> ⚠️ **Fonts & licensing.** Inter is free (SIL OFL). **ES Allianz** (Extraset) and **Avenue
> Mono** (Boulevard LAB) are commercial, per-domain licensed fonts and are **NOT bundled** —
> using them in production requires your own license. Without one, the CSS falls back to Inter,
> or include `assets/tokens/fonts-demo.css` for free look-alikes. Always read
> `references/font-licensing.md` before shipping anything that uses the brand fonts.

## The 60-second brand (internalize this)
- **Light & airy.** Default surfaces Neutral-50 `#F7F9FC` / Brand-25 `#F3F5FE`, or a subtle
  gradient `#BFEAFF → #A5C0EE`. **Never** full-bleed bright/dark blue.
- **Brand-700 `#070FA0` is the accent** — headlines, key icons, links, primary actions. Not a background.
- **Type:** **ES Allianz** for display **and body** (it's ZK Nation's `--font-sans`); hero headline
  extralight (200) in navy, section headers weight 400 in Brand-500, titles tracked **−2 to −5%**;
  **every UI label = Avenue Mono, UPPERCASE, +0.04em** (nav, buttons, tags, captions, meta).
  **Inter** is the free fallback for body (and the ZKsync-protocol body font).
- **Be intentional with type:** kerning + ligatures on, **optical tracking** (the larger the type,
  the tighter — −0.045em display → 0 body → +0.04em mono caps), `text-wrap: balance` on headings,
  tabular numerals for data. This craft is what lifts the work — see `references/typography.md`.
- **Geometry:** outlined boxes, 1px rules, small radii (0–4px), 8px grid.
- **Mark:** twin opposing arrows (`←→`). Use the original artwork with ≥1× clear space; never
  redraw, recolor, skew, or pixel-ify it.
- **Voice:** principled, verifiable ("don't trust, verify"), collective ("…Together"), precise,
  calm. No hype/FOMO/price talk. Spell **ZKsync** and **ZK Nation** exactly.
- **Values:** the ZK Credo — **Freedom → Progress → Prosperity.**

## How to use this skill

1. **Load tokens.** Everything derives from `assets/tokens/` —
   `tokens.css` (CSS variables), `tailwind.preset.js`, or `tokens.json`. Don't hardcode hexes;
   reference tokens. For web, link `tokens.css` (it also declares the `@font-face`s).
2. **Read the relevant reference** (each is short and self-contained):
   - `references/00-brand-overview.md` — architecture, mission, the ZK Credo.
   - `references/voice-tone-vocabulary.md` — how to write (voice, tone, glossary, spelling).
   - `references/color.md` — palette + semantic roles + accessibility.
   - `references/typography.md` — the three fonts + the **type-size framework** (role→size table).
   - `references/logo-and-marks.md` — logo usage, clear space, the "never" list.
   - `references/visual-language.md` — flags, ASCII hero fields, icons, illustration.
   - `references/components-and-construction.md` — standard components **+ the 7-step framework
     for building NEW components/blocks/menus in harmony**.
   - `references/office-docs-and-slides.md` — **PowerPoint / Google Slides / Docs / Word / Keynote**:
     theme-color slot mappings, font fallbacks, color-coding a deck or doc.
   - `references/font-licensing.md` — **READ before using the fonts.** Inter is free; ES Allianz
     and Avenue Mono are commercial/per-domain and not bundled — covers the demo, trial, and
     license paths.
   - `references/dos-and-donts.md` — the final ship gate.
   - `references/secondary-brand-zksync-protocol.md` — the ZKsync protocol mode.
3. **Use real assets** from `assets/` (logos, icons, flags, fonts) — never recreate the mark.
4. **Use a template** from `templates/` as a starting point (document, slides, web page).
5. **Gate before shipping** against `references/dos-and-donts.md` and WCAG AA.

## Building NEW things (the construction framework)
For any component not already in the kit (a block, menu, banner, modal, table…), follow the
**7-step framework** in `references/components-and-construction.md`: pick layer → 8px grid →
outlined frame → assign type roles (mono labels!) → color by role (Brand-700 accent) → add one
quiet brand motif → check the don'ts. The golden rule: **outlined boxes, mono labels, Brand-700
accents, light surfaces, 8px grid.**

## Task playbooks

- **Document / report (.md, .docx, PDF, email):** Inter body at 16px/1.55; headings ES Allianz
  or Inter with tightened tracking; mono uppercase for labels/metadata; Brand-700 headings on
  Neutral-50; logo top-left with clear space. Start from `templates/document.html`.
- **Slides / deck (HTML):** light slides, one idea each; ES Allianz display headline + mono
  eyebrow + Inter body; thin rules; flag/ASCII motif on section dividers; Brand-700 accents.
  Start from `templates/slides.html`.
- **PowerPoint / Google Slides / Keynote / Word / Google Docs:** set the **theme colors** to the
  palette (mapping table in `references/office-docs-and-slides.md` + ready Open XML in
  `assets/tokens/office-theme-colors.xml`), use Inter (ES Allianz/Avenue Mono need local install;
  fall back to Inter + Consolas), titles tracked tight, ALL-CAPS labels, 1px outlines not shadows.
- **Website / app / component:** link `assets/tokens/tokens.css`; build with the components in
  `components-and-construction.md`; mono nav + `▸` CTAs + outlined cards + 3-column footer.
  Start from `templates/web-page.html`.
- **"Apply the ZK Nation brand" to an existing site/app:** map their primaries→Brand-700,
  surfaces→Neutral-50/Brand-25, text→Neutral-950; swap display→ES Allianz, labels→Avenue Mono,
  body→Inter; replace shadows with 1px outlines + small radii; add the logo + a quiet flag/ASCII
  motif; rewrite copy per `voice-tone-vocabulary.md`. The public kit also ships a ready-to-link
  `brand.css` (see the brand-kit website) so you can drop in tokens + fonts via one URL.

## Assets are hosted (the skill is lightweight)
Heavy assets (fonts, flags, logos, icons) live in the **public `brandkit` repo** and a published
mirror, not bundled here. `asset-urls.json` maps every logical asset to a canonical public URL.
- **Repo (source of truth):** https://github.com/zksync-association/brandkit
- **Raw base:** `https://raw.githubusercontent.com/zksync-association/brandkit/main`
- **Published mirror (CDN, web-font friendly):** the brand-kit website link.

For web work you can link the hosted stylesheet directly instead of copying files:
```html
<link rel="stylesheet" href="https://npc.here.now/zknationbrand/brand/tokens/brand.css">
```
A small local copy of `tokens/` lives under `assets/` for offline/iteration use; prefer the
hosted URLs (in `asset-urls.json`) when you need the full font/flag/logo set.

## Public hosting
The whole kit (assets, fonts, `tokens.css`, `brand.css`, references, this skill) is published as
a single public link. Any user or agent can fetch tokens, fonts, and the machine-readable
`apply-zk-nation-brand.md` from that URL to brand their own work — i.e. "apply the ZK Nation brand."
