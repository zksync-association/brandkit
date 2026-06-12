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

> **Using the kit (don't reconstruct, don't collide).** When you link `brand.css`, these classes are
> already fully implemented — **use them as-is.** Do **not** redefine a `.zk-*` class in your own
> `<style>`: you will collide with the kit's rules (e.g. `.zk-btn::after` appends the real arrow, so a
> hand-built arrow box yields *two* arrows; `.zk-footer`'s grid targets the `<footer>` element and will
> hijack a custom layout). Need a custom variant? Give it a **new** class name. The anatomy below
> describes what each component *looks like* — it is not an instruction to rebuild it.

### Navigation bar
- White bar, 1px bottom rule (Neutral-200). ZK Nation lockup at left.
- Nav items in **Avenue Mono UPPERCASE**: `DOCS  FORUM  DELEGATE  BLOG  CODE  PROTOCOL`.
- Primary action at right: **`VOTE`** button (solid Brand-500/700, white mono label).

### Buttons / CTAs (verified against zknation.io)
**Use it as ONE element:** `<a class="zk-btn">Vote now</a>` (or `.zk-btn--ghost` / `.zk-btn--salmon`).
The arrow box renders **automatically** via `.zk-btn::after` — **do not** add an arrow element, type a
`▸`, or redefine `.zk-btn`. That's the whole button.

*Anatomy (what it looks like — not a build recipe):* two boxes — a label box + a **separate arrow box
(▸)** at the right, **sharp corners (radius 0)**, Avenue Mono **uppercase, weight 500**, min-height ~48px.
- **The arrow box is the same across every variant:** a 26×26 **Brand-500 `#0C18EC`** square holding
  a **Brand-300 `#8897F2`** ▸ triangle (the data-URI baked into `.zk-btn` — matches zknation.io).
  It is *not* a white ▸ and *not* navy; only the label box changes per variant.
- **Primary:** label box **Brand-900 navy `#04085F`**, white text. e.g. `SHAPE THE PROTOCOL. VOTE NOW ▸`.
- **Secondary:** label box **Brand-100 `#D4DCFA`**, **Brand-500** text. e.g. `READ THE ZK CREDO ▸`.
- **Salmon (governance):** label box Salmon-100, **navy text** (never white — fails AA). Governance highlights.
- Hover: darken the label box one step; keep transitions ~200ms.
- Implementation: `.zk-btn` (primary) · `.zk-btn--ghost` (secondary) · `.zk-btn--salmon`.

### Cards / content blocks
- Outlined box (1px Neutral-200), white fill, 24–32px padding, radius ≤ 4px.
- Mono eyebrow → display/Inter heading → Inter body → mono meta footer
  (`BY ZKSYNC GOVERNANCE • 5/29/2025`).
- Optional Brand-700 left-border "tab" (4px) for governance items.

### Section headers
- **ES Allianz, weight 400, in vivid Brand-500 `#0C18EC`** (verified on zknation.io) — section
  titles "pop" in bright blue, distinct from the **navy (Brand-900) extralight hero headline**.
  Large (≈80px desktop), tight tracking. Pair with a mono eyebrow above.

### Salmon callout band
- A full-width **Salmon-50 `#EA9682`** section for a single governance/community call-to-action
  (e.g. "ZKsync Partners are the Cornerstone…"). White text, optional diagonal Salmon-100 flag
  stripes, a navy CTA. This is the one place salmon fills a large area — used once, deliberately.

### Hero
- Gradient or Brand-25 field with a **real ASCII flag texture** (`assets/ascii/`, light variant).
- Center a **bordered content panel** (1px rule) holding: display headline (mix weights, e.g.
  ES Allianz light + a bold key phrase), Inter sub-paragraph, then 1–2 mono CTA bars.
- Headline pattern: *light + bold mix*, e.g. "Shape the **Future of ZKsync,** Together."

Copy-paste hero — uses the **real** light field `group-3.png` (paths: `assets/…` in the skill tree,
or the `asset-urls.json` hosted URLs in production). Do not hand-draw the texture:
```html
<header class="zk-hero" style="position:relative; background:var(--zk-gradient-hero); overflow:hidden;">
  <div style="position:absolute; inset:0; background:url('assets/ascii/group-3.png') center/cover no-repeat;
              mix-blend-mode:multiply; opacity:.6;"></div>
  <div class="zk-hero__panel" style="position:relative;">
    <p class="zk-eyebrow">ZK NATION</p>
    <h1>Shape the <strong>Future of ZKsync,</strong> Together.</h1>
    <p>One Inter sub-line in the brand voice.</p>
    <a class="zk-btn" href="#">Get involved</a>
  </div>
</header>
<!-- Single-file / offline: keep the real field — base64-embed assets/ascii/group-3.png into the
     url() above (no fetch, still the real asset). Don't synthesize a CSS/Unicode texture. -->
```

Icon row — the **5 real duotone SVGs**, never glyph/emoji stand-ins:
```html
<ul style="list-style:none; display:flex; gap:var(--zk-space-8); margin:0; padding:0;">
  <li><img src="assets/icons/svg/icons-large_blue.svg"   alt="" width="48" height="48"></li>
  <li><img src="assets/icons/svg/icons-large_blue-1.svg" alt="" width="48" height="48"></li>
  <li><img src="assets/icons/svg/icons-large_blue-2.svg" alt="" width="48" height="48"></li>
  <li><img src="assets/icons/svg/icons-large_blue-3.svg" alt="" width="48" height="48"></li>
  <li><img src="assets/icons/svg/icons-large_blue-4.svg" alt="" width="48" height="48"></li>
</ul>
```

### Governance feed / ticker
- Full-width strip, faint tint, 1px rules top & bottom. Mono row:
  `[+234]  PROPOSAL EXECUTED · ZK PROTOCOL GOVERNOR  ……  BY ZKSYNC GOVERNANCE • DATE`.
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
  salmon-10 fill + **navy ink (Brand-900) text** — *not* salmon-100 text, which is only ~1.75:1
  on salmon-10 and fails AA (on salmon, text is navy). Radius can be pill for status chips.
- When tags share a row with taller elements (e.g. arrow buttons in a flex row), set the row to
  `align-items:center` — otherwise the default `stretch` pulls a pill to the button's height and
  the rounded ends turn into a distorted capsule.

### Docs / long-form layout (reference & developer sites)
A whole genre (e.g. docs.zknation.io). **Canonical classes ship in `brand-docs.css`** — link it after
`brand.css` and use them rather than hand-rolling (which drifts from the system): `.zk-doc` (3-col
frame), `.zk-sidenav`, `.zk-toc`, `.zk-breadcrumb`, `.zk-linklist`, `.zk-dl`, `.zk-callout`
(`--info` / `--gov`), `.zk-pager`. Start from `templates/docs-page.html`. The treatments they encode:
- **Three-column frame:** left sidebar nav, centered content (max ~72ch), right "on this page" TOC.
  1px Neutral-200 rules between columns; light surface; never full-bleed blue.
- **Sidebar nav:** mono UPPERCASE section headers (Avenue Mono, `--zk-text-muted`); item list in
  body type. **Active item:** Brand-25 fill + Brand-700 text + a 4px Brand-700 left tab (reuse the
  `.zk-card--tab` left-border idea). Hover: Brand-25 fill.
- **On-this-page TOC:** mono eyebrow "ON THIS PAGE", anchor links in `--zk-text-muted`, active
  heading steps to Brand-700.
- **Breadcrumb:** mono uppercase, ` / ` or `›` separators, `--zk-text-muted`, last crumb in ink.
- **Prev / next:** two outlined `.zk-card`s at the page foot, each a mono label + the page title;
  the "next" card right-aligned with a `▸`.
- **Headings:** h1 ES Allianz; h2/h3 with tightened tracking; `scroll-margin-top` to clear any sticky
  header. Code blocks: Brand-950 surface, mono, 1px frame (see the site's `pre.code`).

---

## Part C — Menus (nav & dropdowns), specifically
- Trigger and items: **Avenue Mono uppercase**, +0.04em.
- Dropdown = outlined box (1px Neutral-200), white, radius ≤4px, 8px item padding, no heavy shadow.
- Active/hover item: Brand-25 fill + Brand-700 text. Section labels inside menu: mono eyebrow,
  Neutral-500. Keep menus airy — generous line-height, clear 1px dividers between groups.

> Golden rule: **outlined boxes, mono labels, Brand-700 accents, light surfaces, 8px grid.**
> If a new component honors those five, it will look like it belongs.
