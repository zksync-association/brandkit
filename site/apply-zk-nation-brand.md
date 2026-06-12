# Apply the ZK Nation brand (for agents & developers)

Machine-readable instructions to brand any document, deck, site, or component in the
**ZK Nation** (primary) or **ZKsync protocol** (secondary) brand. Canonical source:
https://github.com/zksync-association/brandkit

## TL;DR
1. Load tokens: `https://npc.here.now/zknationbrand/brand/tokens/brand.css` (CSS vars + components),
   or `tokens.json` / `tailwind.preset.js` in the same folder.
2. Surfaces light (Neutral-50 `#F7F9FC` / Brand-25 `#F3F5FE`); text Neutral-950 `#11141A`;
   **accent Brand-700 `#070FA0`** (headlines, links, primary actions). Never full-bleed blue.
3. Type: **ES Allianz for display AND body** (hero h1 extralight/200 navy; section h2 weight 400
   in Brand-500; titles tracked −2…−5%); every UI label **Avenue Mono, UPPERCASE, +0.04em** (nav,
   buttons, tags, captions, meta). **Inter** is the free fallback for body. Buttons: label box +
   a 26×26 Brand-500 square holding a Brand-300 ▸ triangle; sharp corners (radius 0).
4. Geometry: outlined boxes, 1px rules, radii 0–4px, 8px grid. Buttons end with `▸`.
5. Logo: twin arrows; original artwork; ≥1× clear space; never redraw/recolor/skew.
6. Voice: **Bold · Grounded · Dynamic · Passionate** (the four canonical traits) — takes the mission
   seriously, not itself; verifiable ("don't trust, verify"), collective ("…Together"), precise, calm.
   No hype/price/emoji. Spell **ZKsync** and **ZK Nation** exactly. Vision: Freedom → Progress →
   Prosperity. Full positioning + voice traits: `brand/references/verbal-identity.md`.

## Core tokens (hex)
- Brand: 25 `#F3F5FE` · 50 `#E7ECFC` · 100 `#D4DCFA` · 200 `#ADB9F6` · 300 `#8897F2` ·
  400 `#5C6CEC` · 500 `#0C18EC` · 600 `#0914C4` · **700 `#070FA0`** · 800 `#050B7D` · 900 `#04085F` · 950 `#02053C`
- Neutral: 50 `#F7F9FC` … **950 `#11141A`** · 975 `#0A0C10`
- Salmon (ZK Nation accent, sparing): 10 `#F6B6A6` · 50 `#EA9682` · 100 `#EE6D50`
- Gradient: `#BFEAFF → #A5C0EE`. Sand-50 `#FFF6E5` for illustration warmth.

## Fonts & licensing (IMPORTANT)
- **Inter** — free (SIL OFL). Use freely: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`.
- **ES Allianz** (Extraset, extraset.ch) and **Avenue Mono** (Boulevard LAB, boulevardlab.com)
  are **commercial, per-domain** fonts and are **not redistributed**. To use them in production
  you must license them yourself. Otherwise:
  - default → falls back to Inter; or
  - include `brand/tokens/fonts-demo.css` for free look-alikes (Archivo + Space Mono).
- Full terms: `brand/references/font-licensing.md`.

## "Apply to an existing site/app" mapping
- their primary/brand color → Brand-700; their background → Neutral-50 / Brand-25;
  their text → Neutral-950; their secondary accent → Brand-300 (or Salmon-100 for one highlight).
- swap display font → ES Allianz (or Inter); labels → Avenue Mono uppercase; body → Inter.
- replace drop-shadows with 1px outlines + small radii; tighten title tracking.
- add the logomark + a quiet flag/ASCII motif; rewrite copy in the brand voice.

## Office / Slides (PowerPoint, Google Slides, Keynote, Word, Docs)
Set theme colors: Dark1 `#11141A`, Light1 `#F7F9FC`, Accent1 `#070FA0`, Accent2 `#0C18EC`,
Accent3 `#8897F2`, Accent4 `#EE6D50`, Hyperlink `#070FA0`. Titles tracked tight; ALL-CAPS labels;
Inter body (+ Consolas for mono); 1px outlines not shadows. Ready Open XML:
`brand/tokens/office-theme-colors.xml`. Full guide: `brand/references/office-docs-and-slides.md`.

## Full reference set
`brand/references/`: 00-brand-overview · verbal-identity (+ verbal-identity-source, full text) ·
voice-tone-vocabulary · color · typography · logo-and-marks · visual-language ·
components-and-construction · office-docs-and-slides · font-licensing · dos-and-donts ·
secondary-brand-zksync-protocol.

## Install the Claude Code skill
```
git clone https://github.com/zksync-association/brandkit
cp -R brandkit/skill ~/.claude/skills/zk-nation-brand
```
Then ask: "Apply the ZK Nation brand to …". Skill zip: `zk-nation-brand-skill.zip`.
