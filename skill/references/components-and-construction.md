# Components & the Construction Framework

> How to build **new** blocks, menus, cards, and components that stay in visual harmony.
> Pattern evidence: ZK Nation site mockups (Jan 2026). Tokens in `assets/tokens/`.

---

## Part A — The construction framework (use for ANY new component)

When you create something not in this kit (a new block, menu, banner, table, modal…), run
this 7-step checklist. Following it guarantees brand alignment.

1. **Pick the layer.** ZK Nation (primary) or ZKsync protocol (secondary)? That sets the type
   voice (ES Allianz + Avenue Mono vs. Inter) and whether salmon is in play.
2. **Grid & spacing.** Lay out on an **8px grid**. Use the spacing tokens (`--zk-space-*`).
   Outer padding of a block ≥ 24px (desktop). Align everything to the grid — no arbitrary gaps.
3. **Frame it.** The brand's signature container is an **outlined box**: white/Neutral-50 fill,
   **1px Neutral-200 rule**, small radius (0–4px). For emphasis, use a **1px Brand-700 rule**.
   Boxes can share edges (a bordered grid) — a recurring device. Avoid heavy drop shadows;
   prefer the crisp outline. Elevation, when needed, is a faint shadow + the border, not a glow.
4. **Assign type roles.** Heading = display/H-scale (tighten tracking −2 to −5%). Body = Inter.
   **Every interface label** (nav item, button text, tab, timestamp, tag, column header,
   metadata) = **Avenue Mono, UPPERCASE, +0.04em**. See `typography.md` for the size table.
5. **Apply color by role.** Light surface; Neutral-950 text; **Brand-700 for emphasis/links**;
   Brand-500 only for small solid fills; salmon-100 as a *single* governance accent if ZK Nation.
   Never fill the whole component with brand blue.
6. **Add brand texture (optional, sparingly).** A quiet ASCII/dot field, a flag tile, or a
   thin Brand-700 left-border "tab" can signal the brand. One motif per component, kept quiet.
7. **Check against the don'ts** (`dos-and-donts.md`) and **WCAG AA** contrast. Light & airy wins.

**Component anatomy (default):**
`[ 1px border ] → [ 24–32px padding ] → [ MONO EYEBROW ] → [ Heading ] → [ Inter body ] → [ Mono CTA ▸ ]`

---

## Part B — The standard components (observed patterns)

### Navigation bar
- White bar, 1px bottom rule (Neutral-200). ZK Nation lockup at left.
- Nav items in **Avenue Mono UPPERCASE**: `DOCS  FORUM  DELEGATE  BLOG  CODE  PROTOCOL`.
- Primary action at right: **`VOTE`** button (solid Brand-500/700, white mono label).

### Buttons / CTAs
- **Primary:** solid Brand-700 (or Brand-500) fill, white **mono uppercase** label, small
  radius, with a **▸ play/arrow glyph** at the right. e.g. `CONNECT WALLET ▸`, `SHAPE THE PROTOCOL. VOTE NOW. ▸`.
- **Secondary:** transparent/Neutral fill, 1px border, Brand-700 mono label, same arrow.
- Hover: shift fill Brand-700→Brand-500 (or border→Brand-700). Keep transitions ~200ms.
- Min height 44px; horizontal padding ≥ 20px.

### Cards / content blocks
- Outlined box (1px Neutral-200), white fill, 24–32px padding, radius ≤ 4px.
- Mono eyebrow → display/Inter heading → Inter body → mono meta footer
  (`BY ZKSYNC GOVERNANCE • 5/29/2025`).
- Optional Brand-700 left-border "tab" (4px) for governance items.

### Hero
- Gradient or Brand-25 field with a **quiet ASCII/flag texture**.
- Center a **bordered content panel** (1px rule) holding: display headline (mix weights, e.g.
  ES Allianz light + a bold key phrase), Inter sub-paragraph, then 1–2 mono CTA bars.
- Headline pattern: *light + bold mix*, e.g. "Shape the **Future of ZKsync,** Together."

### Governance feed / ticker
- Full-width strip, faint tint, 1px rules top & bottom. Mono row:
  `[+234]  PROPOSALEXECUTED · ZKPROTOCOLGOVERNOR  ……  BY ZKSYNC GOVERNANCE • DATE`.
- Monospace everywhere; numbers and event names in caps.

### Footer
- Light surface, 1px top rule. ZK Nation lockup at left.
- Three mono columns with mono headers: **GOVERNANCE · LEGAL · RESOURCES**.
  Links in mono uppercase (`ACTIVE GOVERNANCE VOTES`, `PRIVACY POLICY`, `ZK NATION BRAND ASSETS`).

### Tables / data
- 1px Neutral-200 grid. Column headers in **mono uppercase**. Numbers tabular.
  Row emphasis via Brand-25 fill, not heavy borders.

### Tags / pills / status
- Mono uppercase, small. Default: Brand-50 fill + Brand-700 text. Governance highlight:
  salmon-10 fill + salmon-100 text. Radius can be pill for status chips.

---

## Part C — Menus (nav & dropdowns), specifically
- Trigger and items: **Avenue Mono uppercase**, +0.04em.
- Dropdown = outlined box (1px Neutral-200), white, radius ≤4px, 8px item padding, no heavy shadow.
- Active/hover item: Brand-25 fill + Brand-700 text. Section labels inside menu: mono eyebrow,
  Neutral-500. Keep menus airy — generous line-height, clear 1px dividers between groups.

> Golden rule: **outlined boxes, mono labels, Brand-700 accents, light surfaces, 8px grid.**
> If a new component honors those five, it will look like it belongs.
