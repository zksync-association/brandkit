# ZK Nation Brand Kit — End-to-End Design Review

**Target:** https://npc.here.now/zknationbrand/ (website) + the Claude Code skill, templates, and token library it ships.
**Date:** 2026-06-11 · **Method:** Playwright (Chromium) + in-page DevTools instrumentation — desktop (1440px) and mobile (390px), accessibility/contrast math, performance timing, network and console capture, and a source read of the `skill/` toolkit.
**Verdict:** A genuinely strong, fast, on-brand site with a well-built toolkit. The defects are concentrated and fixable: a small cluster of **WCAG-AA contrast misses**, one **functional palette bug** (clipped hex codes), and two **responsive/navigation gaps**. None are architectural.

---

## How to read this

Every finding below is backed by a measured value from the live site, not a visual guess. Severity:

- **HIGH** — accessibility failure or broken function; fix before the next share.
- **MED** — visible defect or real usability gap; fix this pass.
- **LOW** — polish; fix when convenient.

Marked-up screenshots live in `screenshots/markup/`. Raw captures and the annotation tool are in `screenshots/`.

---

## What is already strong (keep these)

These were verified and should not regress:

- **Clean runtime.** 0 console errors, 0 console warnings, 0 failed network requests.
- **No horizontal overflow** at 1440px or 390px (document width 1425/375 against the viewport).
- **Performance is excellent.** ~369 KB total transfer, 12 requests, DOMContentLoaded ~1.17 s, full load ~1.62 s, a lean 576-node DOM.
- **Images are disciplined.** All 24 images carry `alt` text and `loading="lazy"`.
- **Document semantics are correct.** Single `h1`, then `h2 → h3` in order; `meta description` present; `viewport` includes `viewport-fit=cover`; `lang="en"`.
- **Brand fonts load for real.** ES Allianz (200 / 400 / 700) and Avenue Mono are served and applied; Inter is the declared fallback. Hero `h1` is ES Allianz **extralight 200, 64px, navy `#04085F`** — exactly the brand spec.
- **Motion is considered.** `prefers-reduced-motion` is handled in CSS.
- **Thoughtful micro-interactions.** The eight headline color swatches are real `<button>`s that copy their hex on click (`title="Copy #04085F"`). Progressive disclosure uses native `<details>` (7 of them) — no JS framework, fully keyboard-operable by default.
- **The component language is faithful.** Two-part arrow buttons (label box + Brand-500 square holding a Brand-300 ▸), 1px-outlined cards, mono uppercase labels, sharp corners — all match `zknation.io`.
- **Social/SEO basics present.** `og:image`, favicon.

---

## Findings

### HIGH

**A11Y-1 — Small white text on the salmon CTA band fails WCAG AA.**
The governance band paints white text on salmon `#EE6D50`. Measured contrast for the small text is **≈3.0:1**, below the **4.5:1** AA floor for text under ~18px. Affected: the eyebrow `GET INVOLVED · GOVERNANCE`, the sub-line *"Salmon is the governance accent…"*, and the `READ THE DOCS` button label. The large headline (*"ZK Nation is built in the open, together."*) clears the 3:1 large-text bar and is fine.
**Fix:** Set the band's small text and eyebrow to **navy ink `#04085F`** (measured **≈6.2:1** on salmon — passes AA) instead of white. This is also more on-brand: navy is the brand ink. Keep the headline as-is or also move it to navy for one consistent treatment. See `screenshots/markup/03-salmon-markup.png`.

**A11Y-2 — The muted-text token is below AA on the hero gradient and marginal elsewhere.**
Muted text uses `#6C7380`. On the light-blue hero gradient (`~#EEF2FC`) it measures **4.26:1 — fails AA**. On the standard Neutral-50 surface it is **4.52:1** — technically passing but with almost no margin, so any future surface tint will push it under. Affected: hero eyebrow + sub-paragraph, section eyebrows, card meta, footer text (12–14px).
**Fix:** Darken the muted-text token to reach **≥4.5:1 on every surface including the hero gradient** — e.g. around `#565E72` (a navy-tinted gray, ≈6:1 on Neutral-50 and ≥4.5:1 on the gradient). Fix this at the **token source** (`skill/assets/tokens/brand.css`) so the site *and* every skill consumer inherit the accessible value. See `screenshots/markup/01-hero-markup.png`.

### MED

**FUNC-1 — Full-palette hex codes are clipped.**
In the expanded "Full palette" disclosure, **30 swatches truncate their hex value** with an ellipsis (`#F3F5FE` renders as `#F3F5F…`; the visible box is 38–40px while the text needs 42px). A color reference whose entire job is to hand you an exact hex must never clip the last character.
**Fix:** Give the hex column enough width (or `min-width`) to fit a 7-char `#RRGGBB`, drop the `text-overflow: ellipsis` on that element, and keep `white-space: nowrap`. While there, mirror the headline swatches' click-to-copy onto these mini-swatches. See `screenshots/markup/02-color-markup.png`.

**FUNC-2 — Anchor jumps hide section headings under the sticky nav.**
Sections set `scroll-margin-top: 72px`, but the sticky nav is **85px** tall. Jumping to `#color` (etc.) leaves the section eyebrow tucked ~13px under the bar.
**Fix:** Set `scroll-margin-top` to **≈96px** (nav height + breathing room) on the anchored sections.

**RESP-1 — Mobile loses in-page navigation entirely.**
At 390px the section nav (`Color / Type / Logo / Visual / Voice / Components`) is `display:none` with **no hamburger or replacement** — only the logo and "Get the kit" remain. On a single-page reference this long, mobile users can only scroll to find a section.
**Fix:** Add a compact mobile menu (a disclosure/sheet) **or** a horizontally-scrollable Avenue-Mono chip bar of the six anchors pinned under the nav. See `screenshots/markup/05-mobile-markup.png`.

**PERF-1 — The hero ASCII art is a massively oversized PNG.**
`group-3.png` is **184 KB and 1939×1336**, but it renders at **~184px wide**. It is the single largest asset — roughly **half the page weight** — to paint a small decorative mark.
**Fix:** Right-size and re-encode: export at ~2× the display size and serve **AVIF/WebP** with a PNG fallback (or, since it's ASCII line art, an **SVG**). Target well under 20 KB. Add `width`/`height` to reserve layout.

**A11Y-3 — No `:focus-visible` styling anywhere.**
No stylesheet rule defines a custom focus indicator. The interactive surface is large (nav links, eight copy-buttons, seven disclosures, CTAs), and custom-styled `<button>`s can render the default ring inconsistently or invisibly against brand fills.
**Fix:** Add a single `:focus-visible` rule — e.g. `outline: 2px solid var(--brand-500); outline-offset: 2px;` — so keyboard focus is always obvious on the navy and salmon fills.

### LOW

**POL-1 — Run-on mono labels in the component card.**
Uppercased enum/contract strings concatenate into unreadable runs: `PROPOSALEXECUTED`, `ZKPROTOCOLGOVERNOR`. Authentic to the on-chain source, but illegible as a label.
**Fix:** Insert word breaks (`PROPOSAL EXECUTED`, `ZK PROTOCOL GOVERNOR`). Fix it in the component **template** too, so downstream agents that copy it inherit the readable version. See `screenshots/markup/04-components-markup.png`.

**A11Y-4 — Copy-swatch buttons lack a screen-reader label and copied-confirmation.**
The swatches expose `title="Copy #…"` (good for mouse) but no `aria-label` and no `aria-live` announcement on success, so screen-reader and keyboard users get no confirmation the hex was copied.
**Fix:** Add `aria-label="Copy <name> <hex>"` and a visually-hidden `aria-live="polite"` region that announces "Copied #RRGGBB".

**META-1 — No `theme-color` meta.**
Mobile browser chrome isn't tinted to the brand.
**Fix (optional):** Add `<meta name="theme-color" content="#04085F">` (or Brand-25 for the light surface).

> **Out of scope / intentional:** there is no dark-mode (`prefers-color-scheme`) styling. Given the brand is deliberately light-and-airy and "never full-bleed dark blue," this is a reasonable choice — noted, not a defect.

---

## Toolkit & skill assessment

The `skill/` package is well-architected: a tightly-scoped `SKILL.md` with a strong trigger description, 11 concise reference files (~753 lines total), three starter templates (document / slides / web-page), machine-readable agent endpoints (`apply-zk-nation-brand.md`, `llms.txt`, `brand.json`), an `asset-urls.json` map, and design tokens as the single source of truth mirrored to the site via `scripts/sync.sh`. Font licensing is handled responsibly (commercial fonts git-ignored, Inter fallback).

Opportunities, several of which **chain directly off the website fixes**:

- **TOOL-1 — Fix accessibility at the token source, not just on the site.** A11Y-1 and A11Y-2 are *token* problems. Correct the muted-text value (and codify "navy text on salmon, never white") in `skill/assets/tokens/brand.css` + `color.md`, then run `sync.sh`. The site and every skill consumer become AA-clean in one move.
- **TOOL-2 — Add a concrete "AA-passing pairs" table** to `references/color.md` / `dos-and-donts.md`: for each surface (Neutral-50, Brand-25, the hero gradient, **salmon**), list the text colors that pass AA and the ones that don't. The current guidance says "check WCAG AA" but doesn't hand over the passing pairs — and the live site shows that's where mistakes happen.
- **TOOL-3 — Clean the component template's labels.** The run-on mono string (POL-1) should not live in `templates/web-page.html` (or wherever the governance card originates), or agents will reproduce it.
- **TOOL-4 — Right-size the bundled/hosted ASCII art** (PERF-1) so anyone linking the hosted asset inherits the lighter file.
- **TOOL-5 — Consider a light Fable-5 trim of `SKILL.md`.** Per Anthropic's Fable 5 guidance, skills written for earlier models are "often too prescriptive" and can degrade output. `SKILL.md` is thorough but long; much of the step-by-step prescription can lean on Fable 5's stronger instruction-following while the references hold the detail. Low priority, but worth a pass.

---

## Priority order for the fix pass

1. **A11Y-1** salmon contrast → navy text *(token + site)*
2. **A11Y-2** muted-text token darken to AA-on-gradient *(token + site)*
3. **FUNC-1** un-clip palette hex codes
4. **RESP-1** mobile section navigation
5. **A11Y-3** `:focus-visible` ring
6. **FUNC-2** `scroll-margin-top` 96px
7. **PERF-1** right-size hero ASCII PNG → AVIF/SVG
8. **POL-1 / A11Y-4 / META-1** label spacing, swatch a11y, theme-color
9. **TOOL-1…4** propagate the above into tokens, `color.md`, templates, hosted assets

Items 1, 2, 3, 5, 6 are small CSS/token edits. Item 4 needs a little markup + CSS. Item 7 is an asset re-export. The whole pass is comfortably a single focused session.
