# Do's & Don'ts (quick gate)

> Run this before shipping anything. Sourced from the Visual Guideline "Mistakes" page,
> the color system notes, and the ZK Nation system.

> ### ⛔ Asset gate (check this first)
> This is the failure a color/type review won't catch. **Never substitute CSS, Unicode, or
> hand-drawn text for a shipped asset.** The ASCII hero fields, flags, icons, and the logomark must
> be the **real files from `assets/`** (index: `assets/MANIFEST.md`; URLs: `asset-urls.json`).
> **Detectable symptom — if any of these is true, you have a bug:** you typed a grid of `z`/`x`/`k`/`i`/dots
> (or a dot-grid / CSS-gradient "flag") to imitate the ASCII flag texture; you used a glyph/emoji/`◄►`/`←→`
> in place of an icon or the mark; you rebuilt the logo from pixels or strokes. Swap in the real asset. *(Single self-contained file with no network? Base64-embed
> the real asset — e.g. `assets/ascii/group-3.png` for the hero — or inline the real SVG marks. Never ad-hoc text.)*
> **Automate it:** for HTML/SVG/CSS output, run `python3 scripts/check-brand-assets.py <file>` — it
> confirms every visual resolves to a kit asset and fails on emoji/external/synthesized stand-ins.

## Always do
- ✅ **Light & airy.** Default to Neutral-50 / Brand-25 surfaces or a subtle gradient.
- ✅ **Brand-700 as the accent** — headlines, key icons, primary actions, links.
- ✅ **Outlined boxes + 1px rules + small radii (0–4px).** Crisp, precise geometry.
- ✅ **Mono uppercase for every interface label** (nav, buttons, tags, meta, captions).
- ✅ **Tighten title tracking −2 to −5%.**
- ✅ **8px grid** for spacing and layout.
- ✅ **WCAG AA** contrast; body text in Neutral-950 or Brand-900/700. Muted text = **#565E72**
  (`--zk-text-muted`), never Neutral-600 `#6C7380` (fails on the hero gradient).
- ✅ **On salmon, text is navy ink (Brand-900) — never white.** White on salmon is ~3.0:1 and fails
  AA. See the AA-passing pairs table in `color.md`.
- ✅ Use the **original logo artwork** with ≥1× (≥2× at small sizes) clear space.
- ✅ Keep flags/icons **flat, duotone, geometric**, within brand blues (+ rare salmon).

## Never do
- ❌ **Full-bleed bright/dark blue backgrounds** (looks like competitors; causes fatigue).
- ❌ Fill large areas with Brand-700+ — step down to Brand-300/400 or neutrals.
- ❌ Salmon as a large fill or as body text — it's a *sparing* accent.
- ❌ **White text on salmon** (fails WCAG AA) — use navy ink (Brand-900) instead.
- ❌ **Fake a shipped asset** with CSS/Unicode/text (dot-grid "flags", glyph/emoji icons, `◄►` marks)
  instead of loading the real file — see the **asset gate** above.
- ❌ Stretch, squeeze, rotate, or skew the logo; place it in circles/badges; or rebuild it
  from dots/pixels/patterns/outlines/strokes/noise/effects.
- ❌ Recolor the mark outside the palette (no greens/arbitrary tints/gradients on the mark).
- ❌ Separate/rearrange/redraw the twin arrows, or pair the logo with unapproved type.
- ❌ Mix more than the three typefaces (Inter, ES Allianz, Avenue Mono).
- ❌ Use Avenue Mono for long body copy.
- ❌ Mix multiple gradients in one viewport without a contrast element.
- ❌ Low-contrast lockups or the mark on busy imagery.

## Anti-pattern gallery (pattern-match these, then fix)
The violations that slip past a color/type review — each with its tell and the fix:

| Anti-pattern | What it looks like | Fix |
|---|---|---|
| **Rebuilt mark** | logomark drawn from a dot/pixel grid, boxes, or CSS; a "flag" made of gradients | Use the real asset — `.zk-logo` / `.zk-logo--lockup` or `assets/logos/svg/…`. Never redraw. |
| **Faked ASCII field** | a **typed grid of `z`/`x`/`k`/`i`/dots**, or a CSS dot-grid / radial-gradient, standing in for the flag texture | Load the real image — `assets/ascii/group-3.png` or the Flag banner `assets/flags/blue/main-flag-ascii_blue.png`; base64-embed for offline. The character look is rendered artwork, not text you type. |
| **Emoji / glyph icons** | 🔵 ▶ ★ or `◄►` used as icons or marks | Use the 5 duotone SVGs (`assets/icons/svg/icons-large_blue*.svg`). |
| **Salmon overuse** | salmon as a large fill, or in several places | One band / accent, **once**, deliberately. |
| **Salmon as body text** | salmon-colored paragraphs | Navy ink; salmon is an accent fill only. |
| **White on salmon** | white text on a salmon fill (~3:1, fails AA) | Navy ink (Brand-900). |
| **Full-bleed blue** | page flooded with bright/dark brand blue | Light surfaces; Brand-700 as the *accent*, not the background. |

Run `scripts/check-brand-assets.py` on HTML/SVG/CSS output to catch the asset ones automatically.

## Voice gate (see voice-tone-vocabulary.md)
- ❌ Hype, FOMO, price/return talk, emoji spam, "decentralized" without a mechanism.
- ✅ Verifiable, principled, collective, precise, calm. Spell **ZKsync** and **ZK Nation** exactly.

> When in doubt: original artwork, keep spacing rules, prefer light backgrounds, fewer elements.
