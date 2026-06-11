# ZKsync Association — Brand Kit

The official, comprehensive brand kit for the **ZKsync Association / ZK Nation**: colors,
typography, logo, visual language, voice & tone, design tokens, fonts guidance, ready-to-use
components, and a **Claude Code skill** so you (or an AI agent) can apply the brand to any
document, slide deck, website, or component.

**Live brand site:** https://npc.here.now/zknationbrand
**Apply the brand (agents):** https://npc.here.now/zknationbrand/apply-zk-nation-brand.md

## Two brands, one system
- **ZK Nation** (primary) — governance & community. ES Allianz + Avenue Mono + Inter; signal-flag
  visual language; salmon accent.
- **ZKsync protocol** (secondary) — the technology/enterprise product. Inter; triangle accents.

Both share one color palette and one logomark.

## What's here
```
skill/                         The Claude Code skill (lightweight, redistributable)
  SKILL.md                     Entry point — how to apply the brand
  references/                  Voice, color, type, logo, visual language, components,
                               office/slides, font-licensing, do's & don'ts, secondary brand
  assets/
    tokens/                    tokens.css · brand.css · tokens.json · tailwind.preset.js
                               office-theme-colors.xml · fonts-demo.css · fonts-licensed.css
    logos/ icons/ flags/       Brand artwork (SVG + PNG)
    fonts/                     (Inter is free; licensed fonts NOT bundled — see below)
  templates/                   document.html · slides.html · web-page.html
  asset-urls.json              Canonical public URLs for every asset
site/                          The public brand website (self-contained mirror)
  brand/                       Public copy of tokens, references, logos, flags, icons, fonts
  apply-zk-nation-brand.md     Machine-readable "apply the brand" instructions
  zk-nation-brand-skill.zip    Downloadable skill
```

## Use it

**In Claude Code** — install the skill:
```bash
git clone https://github.com/zksync-association/brandkit
cp -R brandkit/skill ~/.claude/skills/zk-nation-brand
```
then ask: *"Apply the ZK Nation brand to this deck/doc/site."*

**On the web** — link the stylesheet:
```html
<link rel="stylesheet" href="https://npc.here.now/zknationbrand/brand/tokens/brand.css">
```

**In PowerPoint / Google Slides / Keynote** — apply the theme colors in
`skill/assets/tokens/office-theme-colors.xml` (see `references/office-docs-and-slides.md`).

## ⚠️ Font licensing
- **Inter** is free (SIL OFL).
- **ES Allianz** (Extraset) and **Avenue Mono** (Boulevard LAB) are **commercial, per-domain**
  fonts. Their files are **NOT redistributed** in this kit. To use them in production, license
  your own (extraset.ch / boulevardlab.com). Without a license, the CSS falls back to Inter, or
  use `fonts-demo.css` for free look-alikes. **Read `skill/references/font-licensing.md`.**

## Contributing

New here? Read **[CLAUDE.md](CLAUDE.md)** first — it has the brand model, repo layout, the
edit→sync→publish→push workflow, and the font-licensing rules. See **[MILESTONES.md](MILESTONES.md)**
for what's been done and what's open.

Quick loop:
1. Edit the source of truth in `skill/assets/tokens/` and `skill/references/`.
2. `bash scripts/sync.sh` — mirrors the skill into `site/brand/` and rebuilds the skill zip.
3. Verify (Playwright: desktop + mobile, no overflow, valid headings, WCAG AA).
4. Publish from `site/` via the here.now skill; commit and push as `rafathebuilder-ZK`.

⚠️ Never commit the licensed font binaries (ES Allianz, Avenue Mono) — they're git-ignored.

## Sources
ZKsync Visual Guideline v.2025.2 · ZK Nation brand system (Jan 2026) · zknation.io ·
docs.zknation.io · zksync.io.
