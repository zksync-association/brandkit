# Typography & the Type-Size Framework

> Sources: ZKsync Visual Guideline v.2025.2 ("Type"); ZK Nation system (ES Allianz + Avenue Mono).
> Tokens in `assets/tokens/tokens.css`. Web fonts in `assets/fonts/`.

## The three typefaces

| Typeface | Role | Where | Weights available |
|---|---|---|---|
| **Inter** | Master-brand sans; all body copy; product UI | ZKsync product, docs, anywhere | 400 / 500 / 600 / 700 |
| **ES Allianz** | Editorial display headlines | ZK Nation headlines, hero, posters | Extralight 200 · Light 300 · Book 400 · Medium 500 · Bold 700 (+ italics) |
| **Avenue Mono** | UI labels, nav, buttons, captions, code, tags | Nav items, CTAs, metadata, governance feed — **UPPERCASE** | Regular 400 |

**Pairing rule.** Body is always Inter. Headlines are Inter (ZKsync) **or** ES Allianz
(ZK Nation editorial). Anything that reads as an *interface label* — navigation, buttons,
timestamps, tags, captions — is **Avenue Mono, uppercase**, with `letter-spacing: 0.04em`.

> Wordmark detail: the `ZKsync` logotype is **Inter Extra Bold** ("ZK", −6% spacing) +
> **Inter Light** ("sync", −7% spacing). Don't typeset the wordmark by hand — use the logo asset.

## Tracking (letter-spacing)
- **Titles: tighten −2% to −5%** (`letter-spacing: -0.02em … -0.05em`; default token `--zk-tracking-title: -0.03em`).
- Body: `0`.
- Mono labels: `+0.04em`, set UPPERCASE.

## The type-size framework (use these roles, not arbitrary sizes)

A single modular scale (~1.25 ratio, 8px-aligned). Pick the **role**, not a pixel value.
Sizes are `rem` (1rem = 16px). Tokens: `--zk-text-*`.

| Role | Token | Size | Line-height | Weight | Tracking | Font |
|---|---|---|---|---|---|---|
| Display / Hero | `6xl` | 5.5rem / 88px | 1.05 | 600–700 | −0.04em | ES Allianz / Inter |
| H1 | `5xl` | 4rem / 64px | 1.05 | 600–700 | −0.03em | ES Allianz / Inter |
| H2 | `4xl` | 3rem / 48px | 1.1 | 600 | −0.03em | ES Allianz / Inter |
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
