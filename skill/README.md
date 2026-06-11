# ZK Nation Brand — Claude Code skill

Apply the official ZKsync Association / ZK Nation brand to any document, slide deck, website,
component, or asset.

## Install
```bash
cp -R skill ~/.claude/skills/zk-nation-brand      # user-level
# or:  cp -R skill <project>/.claude/skills/zk-nation-brand
```
Claude Code auto-discovers `SKILL.md`. Then ask, e.g., *"Apply the ZK Nation brand to this deck."*

## What it gives Claude
- **Design tokens** (`assets/tokens/`): `tokens.css`, `brand.css`, `tokens.json`,
  `tailwind.preset.js`, `office-theme-colors.xml`, plus `fonts-demo.css` / `fonts-licensed.css`.
- **References** (`references/`): brand overview & mission, voice/tone/vocabulary, color,
  typography (+ type-size framework), logo, visual language (flags/ASCII/icons),
  components & a 7-step construction framework, office & slides, font licensing, do's & don'ts,
  and the secondary ZKsync-protocol brand.
- **Assets** (`assets/`): logos, icons, flags (SVG/PNG). Fonts: Inter is free; the licensed
  fonts are not bundled — see `references/font-licensing.md`.
- **Templates** (`templates/`): document, slides, and web-page starters.

## Notes
- Heavy/canonical assets are also hosted publicly; see `asset-urls.json`.
- This skill is intentionally **font-license-clean** — safe to share and redistribute.
