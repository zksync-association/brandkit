# CLAUDE.md — ZKsync Association / ZK Nation Brand Kit

Project context for Claude Code and future agent contributors. Read this before editing.

## What this repo is

The official **ZKsync Association / ZK Nation brand kit**. Three things in one repo:
1. **A Claude Code skill** (`skill/`) so any agent can apply the brand to docs, decks, sites, components.
2. **A public website** (`site/`) that presents the brand and hosts everything at one link.
3. **The asset + token library** the other two share.

- **Live site:** https://npc.here.now/zknationbrand/
- **Repo:** https://github.com/zksync-association/brandkit
- Sources of truth for the brand: ZKsync Visual Guideline v.2025.2, the ZK Nation Figma
  (Jan 2026), zknation.io, docs.zknation.io.

## Brand model (know this first)

Two layers share one color palette and one logomark:
- **ZK Nation = PRIMARY.** Governance/community. Fonts: **ES Allianz** (display *and* body) +
  **Avenue Mono** (UPPERCASE UI labels). Signal-flag + ASCII visual language. Salmon accent (used once).
- **ZKsync protocol = SECONDARY.** Tech/enterprise. Inter, triangle accents. Use only when explicitly about the protocol.

Key, non-obvious facts (all verified against the live site/CSS):
- **Ink is navy** (`#04085F` / Brand-900), not gray-black. Hero h1 = navy **extralight (200)**.
- **Section headers = vivid Brand-500 `#0C18EC`, weight 400.**
- **Buttons** = a label box + a **26×26 Brand-500 square holding a Brand-300 ▸ triangle**; sharp corners (radius 0).
- **ES Allianz is also the body font** on zknation.io (`--font-sans`); Inter is only the free fallback.
- **Copy style:** plain, full statements — NOT punchy "Fragment. Fragment." headlines. (Authentic brand quotes like "Don't trust, verify." are kept.)
- **On salmon, text is navy** (Brand-900), never white. White on salmon ≈3:1 fails WCAG AA; navy
  ≈5.8:1 passes. Encoded in `.zk-btn--salmon` / `.zk-tag--gov` and the governance band.
- **Muted text = `#565E72`** (`--zk-text-muted`), not Neutral-600 `#6C7380` — the lighter gray
  fails AA (4.26:1) on the hero gradient. See the AA-passing pairs table in `references/color.md`.

## Repo layout
```
skill/                         The Claude Code skill (lightweight, redistributable)
  SKILL.md                     Entry point + the 60-second brand + playbooks
  references/*.md              The full guidelines (voice, color, typography, logo, visual,
                               components, office/slides, font-licensing, dos-and-donts, secondary brand)
  assets/
    tokens/                    SOURCE OF TRUTH for design: tokens.css, brand.css, tokens.json,
                               tailwind.preset.js, office-theme-colors.xml, fonts-demo.css, fonts-licensed.css
    logos/ icons/ flags/ ascii/   Brand artwork
    fonts/                     Inter is free; licensed fonts are NOT here (see Fonts below)
  templates/                   document.html, slides.html, web-page.html
  asset-urls.json              Canonical public URLs for every asset
site/                          The public website (deployed to here.now)
  index.html                   The landing page (compact, progressive-disclosure; built on brand.css)
  brand/                       MIRROR of skill assets + references (served publicly)
  apply-zk-nation-brand.md · llms.txt · brand.json   Agent-readable endpoints
  og-image.png · favicon.ico   Social card + favicon
  zk-nation-brand-skill.zip    Downloadable skill (rebuilt by scripts/sync.sh)
scripts/sync.sh                Mirrors skill/ assets+refs into site/brand/ and rebuilds the zip
README.md · CLAUDE.md · MILESTONES.md
```

## How to make changes (workflow)

1. **Design tokens are the source of truth** in `skill/assets/tokens/`. Edit `brand.css` /
   `tokens.css` there — never hardcode hexes in the site; reference CSS variables.
2. `site/brand/` is a **mirror** of `skill/` assets + references. After editing the skill,
   **run `scripts/sync.sh`** to copy changes into the site and rebuild the skill zip. (There is
   no bundler — the site is plain HTML/CSS that links `brand/tokens/brand.css`.)
3. The site landing page is `site/index.html`. It links `brand/tokens/brand.css` + `fonts-licensed.css`.
4. **Verify with Playwright** before shipping — screenshot desktop + mobile (390px), and check:
   no horizontal overflow, headings increase by one level, images lazy-load, safe-area padding,
   contrast (WCAG AA). The site is already tuned for these; don't regress them.
5. **Caution with `padding: X 0` shorthands** on `.wrap`/full-bleed elements — the shorthand zeroes
   the safe-area side padding. Use `padding-top`/`padding-bottom` instead (this bit us once).

## Fonts & licensing (IMPORTANT — do not violate)

- **Inter** — free (SIL OFL). Committed, redistributable.
- **ES Allianz** (Extraset, extraset.ch) and **Avenue Mono** (Boulevard LAB, boulevardlab.com)
  are **commercial, per-domain** fonts. Their binaries are **git-ignored and NOT committed**
  (see `.gitignore`). The live site serves them because the Association is licensed; **do not
  add the font files to the repo or the skill zip.** A local-only copy lives in
  `_licensed-fonts-DO-NOT-REDISTRIBUTE/` (git-ignored). Full terms: `skill/references/font-licensing.md`.
- The CSS degrades to Inter automatically; `fonts-demo.css` offers free look-alikes (Archivo + Space Mono).

## Publishing & GitHub

- **Publish** the site with the `here.now` skill from `site/`:
  `~/.claude/skills/here-now/scripts/publish.sh . --slug wander-karma-rxk3 --client claude-code`
  It's mounted on the `npc` handle at `npc.here.now/zknationbrand`. (This uses the maintainer's
  here.now account; a different environment won't have it — re-publish to a new slug if so.)
- **Push** requires the **`rafathebuilder-ZK`** GitHub account (admin on the repo). `rafaeldavid`
  is pull-only. Switch with `gh auth switch --user rafathebuilder-ZK`, push, then switch back.
- Commit trailer used on this project: `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.

## Conventions
- Plain-statement copy; spell **ZKsync** and **ZK Nation** exactly; values = Freedom → Progress → Prosperity.
- Mono uppercase for all UI labels; outlined boxes; 8px grid; light surfaces; never full-bleed blue.
- Intentional type: kerning/ligatures on, optical tracking (tighter as type grows), `text-wrap: balance`
  on headings, tabular numerals for data. See `skill/references/typography.md`.
- Keep the skill **redistributable and font-license-clean**; keep the site **on-brand and performant**.
