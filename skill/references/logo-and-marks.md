# Logo & Marks

> Source: ZKsync Visual Guideline v.2025.2 ("Logomark", "Logo", "Mistakes"). Assets in `assets/logos/`.

## The system
- **Logomark** — the twin opposing arrows (`←→`) built on a square grid. The atomic mark.
- **ZKsync wordmark** — logomark + `ZKsync` logotype (Inter Extra Bold "ZK" + Inter Light "sync").
- **ZK Nation lockup** — logomark + `ZK Nation`, available in **blue** and **orange**, on
  light or dark. Files: `assets/logos/svg/logo-*_{blue,orange}.svg`, `logo_white.svg`.
- **ZKsync mark (standalone)** — `zksync-mark-{dark,light}.svg`.

## Construction & clear space
- Built on a **square grid**; always use at original proportions. Do **not** redraw, rotate, or skew.
- Let **x** = the grid unit. Maintain **≥ 1× clear space** on all sides (the outermost edges of the mark).
- **Small sizes:** increase clear space to **2×**. Don't put type or elements inside the clear zone.
- **Containers:** the mark is 1:1. Center it in square/circular containers (app icons, avatars)
  without cropping or stretching.

## Color & contrast
- Use the **primary brand color**, or solid **black / white**.
- Ensure strong contrast with the background. Avoid gradients or outlines on the mark.
- On light backgrounds prefer the brand blue or Neutral-950 mark.

## Official lockup & favicon
- **`zk-nation-lockup.svg`** (+ `-navy` / `-white` variants) — the official horizontal
  "ZK Nation" lockup (mark + wordmark as one path), captured from zknation.io. Use this in
  nav bars and headers. `currentColor` in the base file; the `-navy` (`#04085F`) and `-white`
  variants are pre-colored for light/dark backgrounds.
- **`favicon/favicon.ico`** — the official ZK Nation favicon (from zknation.io). Use for site
  tabs/bookmarks. `favicon/og-image.png` is the official 1200×630 social card.

## Embedding the mark (offline / single-file — the compliant path)
The #1 rule is **never reconstruct the mark.** So that "compliant" and "easy" coincide even with no
network, the kit inlines the **real** artwork as data-URIs — use these, never redraw:
- **CSS drop-in:** `<span class="zk-logo"></span>` (square logomark) or
  `<span class="zk-logo--lockup"></span>` (full ZK Nation lockup). Both paint the original SVG from
  `--zk-logo-mark` / `--zk-logo-lockup` (in `brand.css` / `brand.inline.css`) — zero fetch, one file.
- **Direct:** `background: var(--zk-logo-mark)` on a sized box, or paste the real
  `assets/logos/svg/logo_blue.svg` / `zk-nation-lockup-navy.svg` inline.
- **If you truly cannot embed the asset,** the only sanctioned fallback is the **wordmark set in the
  brand display font** — never a redraw of the mark:
  ```html
  <span style="font-family:var(--zk-font-display); font-weight:600; letter-spacing:-.02em;
               color:var(--zk-ink)">ZK&nbsp;Nation</span>
  ```
  **Never** rebuild the logomark from shapes, pixels, or a flag/dot grid (asset gate in `dos-and-donts.md`).

## Choosing an asset
| Need | Use |
|---|---|
| Protocol / product / technical | `zksync-mark-*` or the ZKsync wordmark |
| Governance / community / DAO | `logo-*_blue` (default) or `_orange` (expressive) ZK Nation lockup |
| On dark surface | `logo_white.svg` / `*-light_*` variants |
| App icon / avatar (1:1) | Logomark centered in a square; ≥2× clear space |

## Never (from "Mistakes")
- ❌ Change proportions (stretch, squeeze, rotate, skew).
- ❌ Place in shapes/badges (e.g. circles) unless explicitly specified.
- ❌ Rebuild/stylize with patterns, pixels/dots, outlines, strokes, noise, or effects.
- ❌ Recolor outside the approved palette (no greens, arbitrary tints, gradients on the mark).
- ❌ Separate, rearrange, or redraw the arrows; or pair with unapproved typography.
- ❌ Full-bleed bright-blue backgrounds or treatments that make us look like competitors.
- ❌ Low contrast or busy imagery behind the mark.

> When in doubt: use the original artwork, keep the spacing rules, prefer light backgrounds.
