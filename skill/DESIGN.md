---
# ZK Nation — design system, in the DESIGN.md format (design-md spec).
# Tokens below are the normative values; the prose explains how to apply them.
# Full token set + ready CSS: assets/tokens/ (tokens.css, brand.css, tokens.json, tailwind.preset.js).
colors:
  # Brand blue — descriptive name "ZK Blue". The spine of the identity.
  primary:        "#0C18EC"   # Brand-500 — full-saturation fills (not backgrounds)
  primary-accent: "#070FA0"   # Brand-700 — THE accent: headlines, links, primary actions
  primary-ink:    "#04085F"   # Brand-900 "ZK Navy" — the primary text color on light
  primary-25:     "#F3F5FE"
  primary-50:     "#E7ECFC"
  primary-100:    "#D4DCFA"
  primary-300:    "#8897F2"
  primary-500:    "#0C18EC"
  primary-700:    "#070FA0"
  primary-900:    "#04085F"
  primary-950:    "#02053C"
  # Secondary — "Governance Salmon", a SPARING ZK Nation accent (used once, deliberately).
  secondary:      "#EE6D50"   # Salmon-100 — the saturated accent (NOT a light tint)
  secondary-tint: "#F6B6A6"   # Salmon-10 — light chip fill
  # Neutral ramp
  neutral-50:     "#F7F9FC"
  neutral-200:    "#DADDE5"
  neutral-600:    "#6C7380"
  neutral-950:    "#11141A"
  # Semantic
  surface:        "{colors.neutral-50}"   # default page background — light & airy
  surface-raised: "#FFFFFF"
  on-surface:     "{colors.primary-ink}"  # navy ink
  text-muted:     "#565E72"               # navy-tinted gray, AA on every brand surface
  border:         "{colors.neutral-200}"
  gradient-hero:  "linear-gradient(180deg, #BFEAFF 0%, #A5C0EE 100%)"
  # The brand defines no dedicated error color; use a system red sparingly if required.

typography:
  fontFamily:
    display: '"ES Allianz", "Inter", system-ui, sans-serif'   # display AND body (ZK Nation)
    sans:    '"ES Allianz", "Inter", system-ui, sans-serif'
    mono:    '"Avenue Mono", "Inter", ui-monospace, monospace' # UPPERCASE UI labels
    fallback-display: '"Archivo", "Inter", sans-serif'         # free look-alike (SIL OFL)
    fallback-mono:    '"Space Mono", monospace'                # free look-alike (SIL OFL)
  headline-display: { fontFamily: "{typography.fontFamily.display}", fontSize: "5.5rem", fontWeight: 200, lineHeight: 1.05, letterSpacing: "-0.045em" }
  headline-lg:      { fontFamily: "{typography.fontFamily.display}", fontSize: "4rem",   fontWeight: 200, lineHeight: 1.05, letterSpacing: "-0.045em" } # hero h1, navy
  headline-md:      { fontFamily: "{typography.fontFamily.display}", fontSize: "3rem",   fontWeight: 400, lineHeight: 1.05, letterSpacing: "-0.03em" }  # section h2, Brand-500
  body-lg:          { fontFamily: "{typography.fontFamily.sans}",    fontSize: "1.125rem", fontWeight: 400, lineHeight: 1.55 }
  body-md:          { fontFamily: "{typography.fontFamily.sans}",    fontSize: "1rem",     fontWeight: 400, lineHeight: 1.55 }
  body-sm:          { fontFamily: "{typography.fontFamily.sans}",    fontSize: "0.875rem", fontWeight: 400, lineHeight: 1.55 }
  label-md:         { fontFamily: "{typography.fontFamily.mono}",    fontSize: "0.875rem", fontWeight: 500, letterSpacing: "0.04em", fontFeature: "uppercase" }
  label-sm:         { fontFamily: "{typography.fontFamily.mono}",    fontSize: "0.75rem",  fontWeight: 400, letterSpacing: "0.06em", fontFeature: "uppercase" }

rounded: { none: "0", sm: "2px", md: "4px", lg: "8px", full: "999px" }   # crisp, square-ish geometry

spacing: { xs: "0.5rem", sm: "0.75rem", md: "1rem", lg: "1.5rem", xl: "2rem", "2xl": "3rem" }  # 8px grid

components:
  button-primary:        { backgroundColor: "{colors.primary-900}", textColor: "#FFFFFF", typography: "{typography.label-md}", rounded: "{rounded.none}", padding: "0 14px", height: "52px" }
  button-primary-hover:  { backgroundColor: "{colors.primary-700}" }
  button-secondary:      { backgroundColor: "{colors.primary-100}", textColor: "{colors.primary-500}", typography: "{typography.label-md}", rounded: "{rounded.none}" }
  button-salmon:         { backgroundColor: "{colors.secondary}",   textColor: "{colors.primary-ink}", typography: "{typography.label-md}", rounded: "{rounded.none}" }  # on salmon, text is navy
  card:                  { backgroundColor: "{colors.surface-raised}", rounded: "{rounded.none}", borderColor: "{colors.border}" }   # 1px outline, sharp corners
  tag:                   { backgroundColor: "{colors.primary-50}", textColor: "{colors.primary-700}", typography: "{typography.label-sm}", rounded: "{rounded.full}" }
  tag-governance:        { backgroundColor: "{colors.secondary-tint}", textColor: "{colors.primary-ink}", typography: "{typography.label-sm}", rounded: "{rounded.full}" }
---

# ZK Nation — Design System

> The official ZKsync Association / ZK Nation brand, expressed in the DESIGN.md format. The YAML
> tokens above are normative; this prose explains intent and application. For the full kit (assets,
> fonts, references, the Claude Code skill), see `SKILL.md` and `references/`.

## Overview

ZK Nation is the governance and community layer of the ZKsync protocol — civic, sovereign, and
optimistic, like a maritime "nation" built onchain. The feel is **light and airy, calm, and
precise**: pale surfaces, a single deep-blue accent, crisp 1px-outlined geometry on an 8px grid, and
mono UPPERCASE labels. It is editorial, not flashy; confident, not loud. Two layers share one palette
and one logomark: **ZK Nation (primary)** — governance/community, ES Allianz + Avenue Mono, the
signal-flag visual language, a sparing salmon accent; and the **ZKsync protocol (secondary)** —
tech/enterprise, Inter, triangle accents (use only when the content is about the protocol).

## Colors

A blue spine on light surfaces, with one governance accent.
- **Primary — "ZK Blue."** `primary-700` `#070FA0` is **the accent** (headlines, key icons, links,
  primary actions) — never a full-bleed background. `primary-500` `#0C18EC` is for solid fills; step
  down to `primary-300/400` for large areas. `primary-900` `#04085F` ("ZK Navy") is the **ink**:
  ZK Nation reads in navy, not gray-black.
- **Surfaces** default to `surface` (Neutral-50) or `primary-25`/Brand-25, or the subtle
  `gradient-hero`. **Never** flood large areas with bright/dark blue.
- **Secondary — "Governance Salmon"** `#EE6D50` is used **once, deliberately** (one band/accent),
  never as body text or a large fill. NOTE: unlike the brand ramp where `-100` is a light tint,
  `secondary` (salmon-100) is the *saturated* accent.
- **Muted text** = `text-muted` `#565E72` (not Neutral-600, which fails AA on the hero gradient).
- **Accessibility:** meet WCAG AA. On any light surface, all blues and the muted gray pass. **On
  salmon, only navy ink (`primary-ink`) and Neutral-950 pass — white fails (~3:1).** See
  `references/color.md` for the full AA-passing pairs table.

## Typography

- **ES Allianz** sets both display and body (ZK Nation's `--font-sans`, verified on zknation.io);
  **Avenue Mono** sets every UI label (nav, buttons, tags, captions, meta) — UPPERCASE, +0.04em.
  Both are commercial/per-domain and **not bundled**; **Inter** is the free fallback for body, and
  `Archivo` + `Space Mono` (SIL OFL) are the free display/mono look-alikes.
- **Hierarchy:** hero `headline-lg` is ES Allianz **extralight (200)** in navy; section
  `headline-md` is weight **400 in `primary-500`**. Emphasize key words with weight 700 inside a
  light headline ("Shape the **Future of ZKsync,** Together.").
- **Craft:** optical tracking (tighter as type grows: −0.045em display → 0 body → +0.04em mono caps),
  kerning + ligatures on, `text-wrap: balance` on headings, tabular numerals for data.

## Layout

8px grid for all spacing and layout (`spacing` scale). Generous whitespace around dense motifs —
light & airy always wins. Block outer padding ≥24px on desktop; align everything to the grid.
Content columns cap around 68–72ch for readability. Full-bleed dark sections are used sparingly.

## Elevation & Depth

**Flat by design — no shadows.** Hierarchy comes from **1px outlines (`border`), tonal layers
(Neutral-50 vs white vs Brand-25), and the accent color**, not drop shadows or blur. Replace any
"card shadow" instinct with a 1px rule + small/zero radius. This is a defining brand trait.

## Shapes

**Crisp and square-ish.** Default corner radius is `0`–`4px` (`rounded.none`/`sm`/`md`); buttons and
cards use **radius 0**. The only pill (`rounded.full`) is the small status `tag`. Outlined boxes are
the signature container.

## Components

- **Buttons** are two boxes: a label box + a separate **26×26 arrow box** — a `primary-500` square
  holding a `primary-300` ▸ triangle (a fixed glyph; not white, not navy). Variants change only the
  label box: `button-primary` (navy, white text), `button-secondary` (Brand-100, Brand-500 text),
  `button-salmon` (salmon, **navy** text). Sharp corners, Avenue Mono 500, min-height ~52px.
- **Cards** (`card`): 1px outline, sharp corners, white surface; a left 4px Brand-700 tab marks
  emphasis (`.zk-card--tab`).
- **Tags/pills** (`tag`): mono uppercase, small, Brand-50 fill + Brand-700 text; governance variant
  (`tag-governance`) is salmon-10 fill + **navy** text (salmon-100 text fails AA).
- **Logo:** use the original artwork only (`assets/logos/…`, or the inlined `--zk-logo-mark` /
  `.zk-logo` for offline). Never reconstruct it.
- **Visual language:** the signal-flag tiles and the flag-field **image** textures (`assets/flags/`,
  `assets/ascii/`) — load the files; never type a character grid to imitate them.

## Do's and Don'ts

- ✅ Light surfaces; Brand-700 as the accent; 1px outlines + small radii; mono UPPERCASE labels;
  8px grid; WCAG AA; original logo artwork; real asset images.
- ❌ Full-bleed bright/dark blue; shadows; salmon as a large fill or body text; **white text on
  salmon**; more than the three typefaces; reconstructing the logomark or typing a `z/x/k/i`
  character grid for the ASCII field. Full gate: `references/dos-and-donts.md` (+ the asset linter
  `scripts/check-brand-assets.py`).
