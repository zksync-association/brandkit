# Typography & the Type-Size Framework

> Sources: ZKsync Visual Guideline v.2025.2 ("Type"); ZK Nation system (ES Allianz + Avenue Mono).
> Tokens in `assets/tokens/tokens.css`. Web fonts in `assets/fonts/`.

## The three typefaces

| Typeface | Role | Where | Weights available |
|---|---|---|---|
| **ES Allianz** | ZK Nation's primary typeface — **display AND body** | ZK Nation headlines, hero, body copy (it's `--font-sans` on zknation.io) | Extralight 200 · Light 300 · Book 400 · Medium 500 · Bold 700 (+ italics) |
| **Avenue Mono** | UI labels, nav, buttons, captions, code, tags | Nav items, CTAs, metadata, governance feed — **UPPERCASE** | Regular 400 |
| **Inter** | Free fallback for body; the ZKsync-**protocol** brand's body | Anywhere ES Allianz isn't licensed; ZKsync product/docs | 400 / 500 / 600 / 700 |

**Pairing rule (verified in the zknation.io CSS).** ZK Nation sets **ES Allianz for both display
and body** (`--font-sans: esAllianz`) and **Avenue Mono for every interface label**
(nav, buttons, timestamps, tags, captions — uppercase, `letter-spacing: 0.04em`). **Inter is the
free fallback** for body when ES Allianz isn't licensed, and is the body font for the secondary
ZKsync-protocol brand. There is **no Inter** on the ZK Nation site itself.

> Wordmark detail: the `ZKsync` logotype is **Inter Extra Bold** ("ZK", −6% spacing) +
> **Inter Light** ("sync", −7% spacing). Don't typeset the wordmark by hand — use the logo asset.

## Display weight — go light (verified against zknation.io)

The signature ZK Nation headline is **ES Allianz Extralight (200) or Light (300)** at large
sizes with **tight tracking (−4 to −5%)**, set in **navy ink (Brand-900)**, with **one or two
key words in Bold (700)** for contrast. Example: the hero "Shape the *Future of ZKsync,*
Together" — "Shape the" / "Together" are extralight, "Future of ZKsync," is bold.
- Big display / hero: ES Allianz **200**. H1: **200–300**. H2: **300**.
- Don't default large editorial headlines to semibold/bold — that's the heavier ZKsync-product
  register. ZK Nation editorial = thin + tight + navy, bolded selectively.
- Functional sub-heads (H3–H5, in Inter) stay **Semibold (600)**.

> **Mono for short marketing copy.** On zknation.io even the hero sub-paragraph and CTAs are
> **Avenue Mono**. For short, punchy strings (hero subhead, captions, callouts) mono is on-brand;
> reserve Inter for longer-form body where monospace would hurt readability.

## Tracking (letter-spacing)
- **Titles: tighten −2% to −5%** (`letter-spacing: -0.02em … -0.05em`; default token `--zk-tracking-title: -0.03em`).
- Body: `0`.
- Mono labels: `+0.04em`, set UPPERCASE.

## Typographic detail — be intentional (this is what lifts the work)

Good kerning and considered type settings are the difference between "fine" and "crafted."
`brand.css` ships these on by default; honor them anywhere you set type by hand.

1. **Kerning is always on.** `font-kerning: normal` + `font-feature-settings: "kern" 1`. Never
   let the browser fall back to no-kern (default in some engines for performance).
2. **Ligatures & contextual alternates on.** `"liga" 1, "calt" 1` — ES Allianz's `f`-ligatures
   and joins render properly. (Stylistic set `"ss01"` is enabled on headings.)
3. **Optical tracking — the larger the type, the tighter it's set.** This is the single biggest
   "pro" tell. Use a sliding scale, not one value:
   | Size | Tracking |
   |---|---|
   | Display 64–88px | **−0.045em** |
   | H2 32–48px | −0.03em |
   | H3–H5 18–36px | −0.02em |
   | Body 16px | 0 |
   | Small / caption 12–14px | +0.005em |
   | **Mono UPPERCASE labels** | **+0.04em** (uppercase always needs positive tracking) |
4. **Balanced headlines, no orphans.** `text-wrap: balance` on headings (even line lengths,
   no lonely last word); `text-wrap: pretty` on paragraphs (no single-word last lines).
5. **Tabular, lining numerals for data.** `font-variant-numeric: tabular-nums lining-nums` on
   labels, tables, code, and metadata so figures align in columns and don't jump.
6. **Measure & rhythm.** Body measure **60–75 characters** (`max-width: ~68ch`); line-height
   1.5–1.55 for body, ≤1.1 for display. Space blocks on the 8px grid.
7. **Crisp smoothing.** `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`
   so the light ES Allianz weights stay clean (especially navy-on-light).
8. **The wordmark is kerned by hand** in the artwork (Inter ExtraBold "ZK" −6%, Inter Light
   "sync" −7%). Never re-typeset it — use the logo file.

> Rule of thumb: if a headline looks "a little loose," it usually is — tighten it. If uppercase
> mono looks cramped, it needs more tracking. Trust the scale above before eyeballing.

## The type-size framework (use these roles, not arbitrary sizes)

A single modular scale (~1.25 ratio, 8px-aligned). Pick the **role**, not a pixel value.
Sizes are `rem` (1rem = 16px). Tokens: `--zk-text-*`.

| Role | Token | Size | Line-height | Weight | Tracking | Font |
|---|---|---|---|---|---|---|
| Display / Hero | `6xl` | 5.5rem / 88px | 1.05 | **200** (bold key words) | −0.04em | ES Allianz |
| H1 | `5xl` | 4rem / 64px | 1.05 | **200–300** | −0.04em | ES Allianz |
| H2 | `4xl` | 3rem / 48px | 1.1 | **300** | −0.03em | ES Allianz |
| H3 | `3xl` | 2.25rem / 36px | 1.15 | 600 | −0.02em | Inter |
| H4 | `2xl` | 1.75rem / 28px | 1.2 | 600 | −0.02em | Inter |
| H5 | `xl` | 1.375rem / 22px | 1.25 | 600 | −0.01em | Inter |
| Lead / intro | `lg` | 1.125rem / 18px | 1.5 | 400 | 0 | Inter |
| Body | `base` | 1rem / 16px | 1.55 | 400 | 0 | Inter |
| Body small | `sm` | 0.875rem / 14px | 1.5 | 400 | 0 | Inter |
| Caption / footnote | `xs` | 0.75rem / 12px | 1.4 | 400 | 0 | Inter |
| **UI label / nav / button** | `sm`–`xs` | 14–12px | 1 | 400 | **+0.04em** | **Avenue Mono, UPPERCASE** |
| **Eyebrow / tag / meta** | `xs` | 12px | 1 | 400 | +0.06em | **Avenue Mono, UPPERCASE** |

**Responsive rule.** Step display/H1/H2 down one slot on screens < 768px (e.g. Hero 88→48px,
H1 64→40px). Body never goes below 16px. Use `clamp()` for fluid headlines, e.g.
`font-size: clamp(2.5rem, 6vw, 5.5rem);`.

**Vertical rhythm.** Space between blocks in multiples of 8px. Headline → body gap = 0.5–0.75×
the headline size. Paragraph measure: **60–75 characters** (`max-width: ~68ch`).

## Quick CSS recipe
```css
h1 { font-family: var(--zk-font-display); font-size: var(--zk-text-5xl);
     line-height: var(--zk-leading-tight); letter-spacing: var(--zk-tracking-title);
     font-weight: 600; color: var(--zk-text-accent); }
body, p { font-family: var(--zk-font-sans); font-size: var(--zk-text-base);
     line-height: var(--zk-leading-body); color: var(--zk-text); }
.zk-label { font-family: var(--zk-font-mono); text-transform: uppercase;
     letter-spacing: var(--zk-tracking-mono); font-size: var(--zk-text-sm); }
```

## Don't
- ❌ Mix more than the three families.
- ❌ Use Avenue Mono for long body copy (it's for labels/short strings).
- ❌ Leave default (loose) tracking on large titles — always tighten.
- ❌ Pair the logo with unapproved type, or rebuild the wordmark by hand.
