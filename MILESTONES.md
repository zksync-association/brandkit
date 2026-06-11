# Milestones — ZK Nation Brand Kit

A summary of what's been built and the current state, for anyone (human or agent) picking this
up. For *how to contribute*, see `CLAUDE.md`. Newest first.

## Current state (shipped)
- ✅ **Comprehensive brand kit**: tokens (CSS vars / Tailwind / JSON / Office XML), 11 reference
  docs (voice, color, typography, logo, visual language, components + construction framework,
  office/slides, font licensing, do's & don'ts, secondary brand, overview), artwork (ZKsync
  wordmark + medallion, ZK Nation lockup + logomark + flags, duotone icons, 12 ASCII fields),
  and document/slide/web templates.
- ✅ **Claude Code skill** (`skill/`) — install via `cp -R skill ~/.claude/skills/zk-nation-brand`;
  redistributable and font-license-clean.
- ✅ **Public website** (`site/`, live at https://npc.here.now/zknationbrand/) — a compact landing
  page with progressive-disclosure detail panels, built entirely on `brand.css`. Hosts all assets,
  a downloadable skill zip, a ready-to-link `brand.css`, and agent-readable endpoints
  (`apply-zk-nation-brand.md`, `llms.txt`, `brand.json`, JSON-LD, custom og-image).
- ✅ **Brand fidelity verified against zknation.io** (computed styles + CSS source): navy ink,
  extralight hero / Brand-500 section headers, the two-part arrow button, ES Allianz as body font,
  sharp corners, salmon callout band.
- ✅ **Mobile + performance + a11y pass**: no horizontal overflow; lazy-loaded images
  (initial transfer ~7.4MB → ~0.4MB); flag PNGs downscaled (14MB → 4MB); safe-area insets
  (`viewport-fit=cover` + `env()`); single-row mobile nav; valid heading hierarchy (h1→h2→h3);
  `prefers-reduced-motion`; intentional kerning + optical tracking + `text-wrap: balance`.

## Build journey (high level)
1. **Inventory & sources** — local assets (ZKsync guideline PDF, ZK Nation Figma export, fonts,
   logos, flags), plus zknation.io, docs.zknation.io, and the `docs` repo. Figma was read via the
   local `.fig` (a zip); the named ASCII assets were supplied separately into `ASCII Images/`.
2. **Tokens + references** authored as the single source of truth.
3. **Skill** assembled (lightweight; heavy assets referenced via public URLs in `asset-urls.json`).
4. **Website** built to dogfood the brand, then published via here.now and pushed to GitHub.
5. **Font licensing** handled — commercial fonts excluded from the public kit; demo/trial/license paths documented.
6. **Fidelity calibration** — corrected defaults (ink, weights, button anatomy, body font) to match the live site.
7. **Redesign (v2)** — replaced the long marketing scroll with the compact, progressive-disclosure landing page; revised copy to plain statements; reorganized the footer; added a custom social card.
8. **Polish** — mobile/perf/a11y fixes, harmonized the overview cards, intentional typography.

## Known open items / ideas
- The **skill reference docs** still contain a few short fragment phrasings; could be swept to
  match the website's plain-statement copy.
- `ASCII Images/` files keep their Figma export names (`group-*.png`, `ascii-2-2.png`); the exact
  `ascii_1 / ascii_2 …` mapping from Figma was not confirmed, so they were not renamed.
- A real **ZKsync-protocol (secondary) brand** showcase page could be added (currently documented only).
- Templates (`skill/templates/`) predate the v2 button/anatomy refinements — worth re-syncing to
  the latest `brand.css` patterns if used heavily.

## Pointers
- Source of truth: `skill/assets/tokens/` · Guidelines: `skill/references/` · Site: `site/index.html`
- Sync skill → site + rebuild zip: `bash scripts/sync.sh`
- Publish: here.now from `site/` (slug `wander-karma-rxk3`, mounted at `npc.here.now/zknationbrand`)
- Push: GitHub as `rafathebuilder-ZK` (admin); `rafaeldavid` is pull-only.
