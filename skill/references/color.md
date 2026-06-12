# Color System

> Source: ZKsync Visual Guideline v.2025.2, "Color system." Values live in `assets/tokens/`.

## Palettes

### Brand (blue) — the spine of the identity
`brand-25 #F3F5FE · 50 #E7ECFC · 100 #D4DCFA · 200 #ADB9F6 · 300 #8897F2 · 400 #5C6CEC ·
500 #0C18EC · 600 #0914C4 · 700 #070FA0 · 800 #050B7D · 900 #04085F · 950 #02053C`

### Neutral
`50 #F7F9FC · 100 #E8ECF2 · 200 #DADDE5 · 300 #BEC2CC · 400 #A1A7B3 · 500 #858C99 ·
600 #6C7380 · 700 #555A66 · 800 #3D424D · 900 #262B33 · 950 #11141A · 975 #0A0C10`

### Additional
- **Sand-50 `#FFF6E5`** — warmth; pair with gradients in illustration.
- **Light-100 `#EDF2FA` / Light-200 `#DAE2F2`** — alternative illustration fills.
- **Gradient `#BFEAFF → #A5C0EE`** — subtle, for hero areas / section headers / illustration panels.

### ZK Nation accent (salmon) — sub-brand only
`salmon-10 #F6B6A6 · salmon-50 #EA9682 · salmon-100 #EE6D50`. Use **sparingly** as a
governance/community accent (a CTA underline, a tag, a single highlight). Never as a page fill.

> **Scale note (avoid the wrong shade).** Salmon is a 3-step ramp, light → saturated: `10` is the
> lightest tint, `100` is the **saturated accent**. Same direction as the brand ramp (higher = darker),
> but note the contrast: brand-100 is a *light tint*, whereas **salmon-100 is the deep accent color**.
> For the governance accent itself, use **salmon-100**; for a tinted chip fill, salmon-10.

> **On salmon, text is navy ink — never white.** White on salmon-100 is only ≈3.0:1 and **fails
> WCAG AA**. Navy Brand-900 `#04085F` on salmon-100 is ≈5.8:1 (passes) and is the on-brand ink.
> Even Brand-700 dips below AA on salmon-100 (≈4.4:1) — so for salmon, use **Brand-900 only**.
> Encoded in `assets/tokens/brand.css` (`.zk-btn--salmon` → navy). See the AA pairs table below.

## Ink: ZK Nation reads in navy

A signature, verified against zknation.io: **the primary text color is brand-900 `#04085F`
(navy), not gray-black.** Headlines, body, and labels are set in navy ink on white/light
surfaces — it's what gives ZK Nation its calm, bluish, editorial feel.
- **ZK Nation (primary):** text = **Brand-900 `#04085F`**; links/emphasis may step to Brand-700.
- **ZKsync protocol (secondary):** the more corporate mode may use Neutral-950 `#11141A` for text.
Token: `--zk-ink` / `--zk-text` default to Brand-900.

## The governing idea: light & airy

> "Our interface should feel light and airy."

- **Default to light surfaces** (Neutral 50–200) or a soft gradient background.
- On light backgrounds, **use Brand-700 for emphasis** — headlines, key icons, primary actions.
- **Treat Brand-700 as the accent, not the background.** Do not flood large areas with solid
  brand blue — it causes visual fatigue and makes us look like full-bleed-blue competitors.
- For larger fills, **step down to Brand-300/400** or use neutral tones.

## Roles (semantic mapping)

| Role | Token |
|---|---|
| Page background | Neutral-50 (`--zk-surface`) or the hero gradient |
| Raised card | White |
| Primary text | Neutral-950 |
| Muted text | `--zk-text-muted` **#565E72** (navy-tinted gray — AA on every surface) |
| Headline / link / emphasis | Brand-700 |
| Solid accent fill | Brand-500 (step to 400 for big areas) |
| Soft fill | Brand-300 |
| Borders / rules | Neutral-200 (or Brand-700 for the "strong outline" look) |
| Governance accent (ZK Nation) | Salmon-100 |
| Dark / inverse section | Brand-950 (sparingly) |

## Gradients (optional)
- Keep them **subtle**: `#BFEAFF → #A5C0EE`.
- Use on **hero areas, section headers, illustration panels** — *not* as the default page background.
- In illustrations, pair the gradient with **Sand-50** for warmth and contrast.
- **Don't mix multiple gradients in one viewport** without a contrast element between them.

## Accessibility
- Meet **WCAG AA** for text and icons (≥4.5:1 normal, ≥3:1 large/bold ≥18.66px).
- On light backgrounds use **Brand-700** or **Neutral-700+** (ideally Neutral-950) for text.
- **Avoid Brand-300/400 for body copy** — insufficient contrast.
- **Muted text = `--zk-text-muted` #565E72**, *not* Neutral-600 `#6C7380`. Neutral-600 measures only
  4.26:1 on the hero gradient (#EEF2FC) — it **fails AA** — and is marginal (4.52:1) on Neutral-50.
  #565E72 clears 4.5:1 on every brand surface. Fixed at the token source so all consumers inherit it.

### AA-passing text/background pairs (normal text, ≥4.5:1)
Measured contrast ratios. ✅ passes AA · ⚠️ large/bold only (≥3:1) · ❌ fails — do not use.

| Text ↓ / Surface → | Neutral-50 `#F7F9FC` | Brand-25 `#F3F5FE` | Hero gradient `~#EEF2FC` | White | Salmon-100 `#EE6D50` | Salmon-50 `#EA9682` |
|---|---|---|---|---|---|---|
| **Brand-900 `#04085F`** (ink) | ✅ 16.5 | ✅ 16.0 | ✅ 15.6 | ✅ 17.4 | ✅ 5.8 | ✅ 7.6 |
| **Neutral-950 `#11141A`** | ✅ 17.5 | ✅ 17.0 | ✅ 16.5 | ✅ 18.4 | ✅ 6.1 | ✅ 8.1 |
| **Brand-700 `#070FA0`** | ✅ 12.6 | ✅ 12.2 | ✅ 11.8 | ✅ 13.3 | ❌ 4.4 | ✅ 5.8 |
| **Brand-500 `#0C18EC`** | ✅ 8.5 | ✅ 8.2 | ✅ 8.0 | ✅ 8.9 | ❌ 2.9 | ⚠️ 3.9 |
| **Muted `#565E72`** | ✅ 6.2 | ✅ 6.0 | ✅ 5.8 | ✅ 6.5 | ❌ 2.1 | ❌ 2.8 |
| **White `#FFFFFF`** | ❌ 1.1 | ❌ 1.1 | ❌ 1.1 | ❌ 1.0 | ⚠️ 3.0 | ❌ 2.3 |

**Reading it:** on any light surface, all blues and the muted gray pass. **On salmon, only navy
ink (Brand-900) and Neutral-950 pass** — white, muted, and even Brand-700/500 fail. That is why the
governance band and `.zk-btn--salmon` set navy text. Never put white body text on salmon.

## Don't
- ❌ Brand-700 (or darker) as a full-bleed background.
- ❌ Recolor the logomark outside the approved palette (no greens, arbitrary tints, gradients on the mark).
- ❌ Salmon as a large fill or as body text.
