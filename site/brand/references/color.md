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
| Muted text | Neutral-600 |
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
- Meet **WCAG AA** for text and icons.
- On light backgrounds use **Brand-700** or **Neutral-700+** (ideally Neutral-950) for text.
- **Avoid Brand-300/400 for body copy** — insufficient contrast.

## Don't
- ❌ Brand-700 (or darker) as a full-bleed background.
- ❌ Recolor the logomark outside the approved palette (no greens, arbitrary tints, gradients on the mark).
- ❌ Salmon as a large fill or as body text.
