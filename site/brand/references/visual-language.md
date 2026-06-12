# Visual Language — Flags, Patterns, Icons & Illustration

> Sources: ZK Nation brand exploration (Jan 2026); brand assets folder. Assets in
> `assets/flags/`, `assets/icons/`. This is the expressive heart of the **ZK Nation** sub-brand.

## 1. The signal-flag system (the signature motif)

ZK Nation's identity is built on a set of **nautical/signal-flag tiles** — simple geometric
blue compositions in a square (or 3:2) frame. They read like a maritime flag alphabet for a
sovereign onchain "nation."

- **Vocabulary of shapes:** solid diagonal split, four-point star/sparkle, pennant triangle,
  saltire (X cross), Nordic cross, horizontal stripes, vertical bar, diamond/rhombus, circle,
  checker, hexagon (the ZK "honeycomb"), cloud, and the **twin-arrow logomark** itself as a flag.
- **Two tones per tile:** built from exactly two palette steps (e.g. Brand-300 `#8897F2` +
  Brand-500 `#0C18EC`, or Brand-500 + Brand-950). Duotone, flat, no gradients, no outlines.
- **The "main flag"** is the logomark rendered as a waving flag (`assets/flags/*/main-flag*`).
- **Color variants:** **blue** (default) and **orange** (`assets/flags/orange/`, the
  expressive/celebratory variant, pairs with the salmon accent).

**Use flags for:** hero motifs, section dividers, avatars, sticker sheets, event/social
graphics, "nation" iconography, loading/empty states. Treat them as a kit you can arrange in
grids, rows, or bunting — but keep each tile's internal geometry intact.

## 2. Flag-field textures (the signature hero texture) — these are IMAGES, not text

The hero/background texture is a **waving-flag field**: a dense lattice of tiny glyphs that fades in
density to suggest a flag in motion. **It is a shipped raster image — load the file.** The character
look is what the *rendered artwork* happens to show; it is **NOT a recipe and NOT something you type.**
Typing a grid of `z` / `x` / `k` / `i` / dots to imitate it is the **#1 reconstruction mistake** (it's
a redraw of brand artwork — see the asset gate in `dos-and-donts.md`). Always use the real file:

- **The Flag banner** — the waving flag with the ASCII treatment: **`assets/flags/blue/main-flag-ascii_blue.png`**
  (orange: `assets/flags/orange/main-flag-ascii_orange.png`). The clean (non-ASCII) flag is `main-flag_blue.png`.
- **The background field textures** live in **`assets/ascii/`** (12 fields: `group*.png`, `ascii-2-2.png`) —
  pick one by surface from the list below.
- **Single-file / offline?** Base64-embed the real PNG (the light `group-3.png` is ~8 KB). Still the real
  asset — never a typed character grid.

**The fields by surface (verified against the actual files — match the field to your background):**
- **Light field (navy chars on white) — use this for a light hero:** **`group-3.png`** is the only
  light field (640×441, right-sized to ≈8 KB). ⚠️ `group-5.png` is effectively **blank — don't use it**.
- **Dark fields (blue/white chars on black) — for dark bands/heroes:** `group.png`, `group-2.png`,
  `group-9.png`, `group-10.png` (portrait 1334×2000); `group-6.png`, `group-7.png`, `group-8.png`
  (square 1600×1600).
- **Salmon fields (salmon chars on black) — sparing governance accents, on DARK surfaces:**
  `group-4.png` (landscape 1939×1336), `group-1.png`, `ascii-2-2.png` (portrait 1334×2000). These
  sit on **black**, not light — use them in a dark governance band, never as a light hero.
- All dark/salmon fields are full-res (≈130–330 KB); the light hero `group-3.png` is right-sized (≈8 KB).

**Offline / single-file?** Still use the **real** field — never synthesize one. Embed the actual
`group-3.png` as a base64 data-URI, or link it from the hosted mirror:
```css
/* base64-embed the real asset (no fetch, still the real field): */
.hero { background: url('data:image/png;base64,<contents of assets/ascii/group-3.png>') center/cover, var(--zk-gradient-hero); }
/* or link the hosted copy: */
.hero { background: url('https://npc.here.now/zknationbrand/brand/ascii/group-3.png') center/cover, var(--zk-gradient-hero); }
```
Keep it quiet behind foreground type. Do **not** hand-roll a CSS/Unicode texture in its place
(see the Asset gate in `dos-and-donts.md`).

Rules:
- Pick the variant by surface (light vs dark) and reserve salmon for governance accents.
- Keep it **quiet behind foreground type** (it's texture, not content) — `cover`, low prominence.
- Don't recolor or rebuild the logomark out of the ASCII field (that's a logo "Mistake").

## 3. Icons

- **Style:** bold, **duotone, split-tone** glyphs in a square. Each icon splits into two
  brand-blue tones (e.g. left half Brand-500, right half Brand-300) — see
  `assets/icons/svg/icons-large_blue*.svg`. Geometric, flat, no outlines, no gradients.
- **Construction:** simple, recognizable metaphors (shield/credential, magnifier/search,
  speech bubbles/forum, upload/submit). Heavy weight; fill the square; consistent optical size.
- **Color:** stay within brand blues; the two tones must come from the palette (no arbitrary hues).

## 4. Illustration
- Prefer the **gradient panel** (`#BFEAFF → #A5C0EE`) as the backdrop; pair with **Sand-50** for warmth.
- If gradients don't suit, use a **solid brand fill (Brand-400/500)** or the **light illustration
  colors (Light-100/200)** to keep it airy.
- Keep illustrations geometric and flat, consistent with the flag/icon language.

## 5. Geometry & "feel"
- **Crisp, square-ish geometry.** Outlined boxes and thin 1px rules are a recurring device
  (see components). Radii are small (0–4px) — the brand is precise, not soft.
- **Light & airy** always wins: lots of white/Neutral-50 space around dense motifs.

## Don't
- ❌ Add gradients, outlines, or noise to flags/icons.
- ❌ Recolor outside brand blues (+ salmon as a rare accent).
- ❌ Build the logomark out of the dot/ASCII pattern (it's a "Mistake" — the mark stays solid).
- ❌ Let hero textures reduce foreground legibility.
