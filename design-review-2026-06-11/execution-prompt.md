# Execution Prompt — ZK Nation Brand Kit fix pass

This is a ready-to-paste prompt for a **new Claude (Fable 5) session** to implement the fixes from the
2026-06-11 design review. It was written against Anthropic's
[Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
guidance: give the reason (not just the request), steer with brief instructions rather than enumerating every
behavior, state boundaries explicitly, and make self-verification explicit.

**Recommended settings:** effort `high`. Run it in the repo root (`/…/ZKsync_Association_Brand/brandkit`) with
Playwright available. Paste everything in the box below.

---

```
You are improving the official ZKsync Association / ZK Nation brand kit — a single repo that is three things at
once: a public website (site/), a redistributable Claude Code skill (skill/), and the shared token/asset library
they both build on. It is used by designers and by other agents to apply the brand, so correctness and
accessibility here propagate downstream. A full end-to-end design review was just completed; your job is to
execute its fix plan faithfully and ship it.

Read these first, in order:
- design-review-2026-06-11/design-review-critique.md  — the findings, each with a measured value and a target fix
- design-review-2026-06-11/index.html                 — the same findings as a visual report (open the marked-up
                                                         screenshots under design-review-2026-06-11/screenshots/markup/)
- CLAUDE.md and MILESTONES.md                          — how this repo works, the workflow, and the hard constraints

The single most important rule of this repo: design tokens in skill/assets/tokens/ are the source of truth.
Never hardcode hexes in the site; edit the tokens, then run scripts/sync.sh to mirror skill/ assets+references
into site/brand/ and rebuild the skill zip. Several of the fixes below are deliberately token-level so they reach
the website AND every skill consumer at once.

## What to change

Work through these. The critique has the full detail and the marked-up screenshot for each; the measured values
are the acceptance targets.

1. A11Y-1 — Salmon CTA band. Small white text on salmon #EE6D50 measures ~3.0:1 and fails WCAG AA. Change the
   band's eyebrow, sub-line, and the "READ THE DOCS" button label to navy ink #04085F (~6.2:1 on salmon). Encode
   the rule "on salmon, text is navy — never white" in the tokens/references, not just the page.

2. A11Y-2 — Muted-text token. #6C7380 is 4.26:1 on the hero gradient (fails) and only 4.52:1 elsewhere. Darken the
   muted-text token (around #565E72, or whatever you verify clears 4.5:1 on the hero gradient and Neutral-50) at
   the token source so the site and skill inherit it.

3. FUNC-1 — Color palette hex codes are clipped (30 swatches show e.g. "#F3F5F…"). Give the hex element enough
   width for a full 7-char #RRGGBB, remove the ellipsis clipping, keep nowrap. While there, give the full-palette
   mini-swatches the same click-to-copy the headline swatches already have.

4. RESP-1 — Mobile (<=720px) drops the section nav (Color/Type/Logo/Visual/Voice/Components) with no replacement.
   Add in-page navigation for mobile: either a compact disclosure menu or a horizontally-scrollable Avenue-Mono
   chip bar of the six anchors. Keep it on-brand (mono uppercase labels, outlined, sharp corners).

5. A11Y-3 — There is no :focus-visible styling. Add a visible keyboard focus ring across interactive elements
   (e.g. 2px Brand-500 outline with offset).

6. FUNC-2 — Anchored sections use scroll-margin-top:72px but the sticky nav is 85px; jumps hide the section
   eyebrow. Set scroll-margin-top to ~96px.

7. PERF-1 — The hero ASCII art (group-3.png) is ~184 KB at 1939x1336 but displays ~184px wide — about half the
   page weight. Re-export it right-sized and re-encode to AVIF/WebP with a fallback, or to SVG since it is line
   art; target well under 20 KB, and set width/height so layout is reserved. Update the bundled/hosted copy too so
   anyone linking the asset benefits.

8. POL-1 / A11Y-4 / META-1 — Fix the run-on mono labels in the component card ("PROPOSALEXECUTED",
   "ZKPROTOCOLGOVERNOR") by inserting word breaks, and fix the source template so downstream copies are clean. Add
   aria-label plus a visually-hidden aria-live "Copied" confirmation to the copy-swatches. Add
   <meta name="theme-color" content="#04085F">.

9. TOOL-1…4 — Propagate the above into the toolkit: the token + salmon-text rule into references/color.md and
   dos-and-donts.md (add a short table of AA-passing text/background pairs per surface, including salmon); the
   clean component label into the template; the lighter ASCII asset into the hosted set. Run scripts/sync.sh.

## Constraints (do not violate)

- Font licensing: ES Allianz and Avenue Mono are commercial, per-domain, git-ignored, and must NOT be committed to
  the repo or the skill zip. Inter is the free fallback. See skill/references/font-licensing.md.
- Do not regress what already works: zero console errors, no horizontal overflow at 1440px or 390px, every image
  keeps alt + loading="lazy", heading order stays h1->h2->h3, prefers-reduced-motion stays handled, and the page
  stays fast (it was ~369 KB / ~1.6s). Watch the `padding: X 0` shorthand on full-bleed/.wrap elements — it zeroes
  the safe-area side padding; use padding-top/padding-bottom (this bit the project once).
- Stay in scope. Implement the fixes above and what they directly require. Don't refactor surrounding code,
  introduce a build step or framework, restyle things the review didn't flag, or add features for hypothetical
  future needs. This is a polish pass on a shipped v1, not a redesign.

## How to verify (make this explicit, not assumed)

After each change, verify it against the live behavior rather than assuming it worked. Use Playwright to load the
page at 1440px and 390px and confirm the specific fix:
- Re-measure contrast for the salmon text and the muted-text token and confirm both clear 4.5:1 on their actual
  backgrounds (the salmon band and the hero gradient specifically).
- Confirm all palette hex codes render in full with no ellipsis.
- Confirm the mobile section nav is reachable at 390px.
- Tab through the page and confirm a focus ring is always visible.
- Confirm clicking a section anchor lands with the eyebrow clear of the sticky nav.
- Confirm the hero image transfer size dropped and nothing else regressed (console clean, no overflow, load still
  fast). Re-screenshot desktop and mobile and compare against design-review-2026-06-11/screenshots/raw/.

Prefer spinning up a fresh-context verifier (a subagent or a clean Playwright pass) over trusting your own edit.
When you report progress, point each claim to a measurement you actually took this session; if something isn't
verified yet, say so plainly. If tests or checks fail, report the failure with the value, don't paper over it.

## Shipping (these are the only steps that need a human go-ahead)

Building and editing files is yours to do end to end — proceed without asking. Pause only for the two
outward/irreversible steps, because they touch a live site and a shared repo and use specific maintainer accounts:

- Publish to here.now from site/ (see CLAUDE.md for the exact publish command and slug). This updates the live
  site at npc.here.now/zknationbrand.
- Push to GitHub, which requires `gh auth switch --user rafathebuilder-ZK` (admin); restore the prior account
  after. Commit trailer: Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>.

Before either, show me the diff and your verification results, and confirm. Everything up to that point — read,
edit tokens, sync, verify locally — just do.

When you have enough to act, act; don't re-plan what's already specified here or survey options you won't take. If
you hit a genuine ambiguity or a constraint conflict, make the on-brand, accessible, minimal-change choice and note
it. Start by reading the critique and CLAUDE.md, then work the list top to bottom.
```
