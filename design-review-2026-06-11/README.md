# Design Review — ZK Nation Brand Kit (2026-06-11)

A comprehensive, end-to-end design review of the ZK Nation brand kit — the website, the toolkit, and the
Claude Code skill at **https://npc.here.now/zknationbrand/** — conducted with Playwright (Chromium) and in-page
DevTools instrumentation (contrast math, performance timing, network/console capture) plus a source read of `skill/`.

## What's here

| File | What it is |
|---|---|
| **index.html** | The review **report** — an on-brand HTML landing page. Open this first (`python3 -m http.server` in this dir, or just open the file). |
| **design-review-critique.md** | The full written critique: strengths to keep, 9 findings with measured values + fixes, toolkit assessment, priority order. |
| **execution-prompt.md** | A ready-to-paste prompt for a **new Claude (Fable 5) session** to implement the fixes, written per Anthropic's Fable 5 prompting guidance. |
| **screenshots/markup/** | Five **marked-up screenshots** (numbered pins + severity-coded descriptors) — the visual evidence behind the findings. |
| **screenshots/raw/** | The raw desktop (1440px) and mobile (390px) captures, before annotation. |
| **screenshots/markup.html** | The annotation tool used to render the marked-up screenshots over the raw captures. |
| **artifacts/measurements.json** | The measured values (contrast, performance, fonts, a11y) the findings are based on. |
| **artifacts/report-preview.png** | A full-page render of `index.html`. |

## Headline

A genuinely strong, fast, on-brand site with a well-built toolkit. The defects are concentrated and fixable:
two WCAG-AA contrast misses (white-on-salmon, and the muted-gray token on the hero gradient), one functional
palette bug (clipped hex codes), and two responsive/navigation gaps. None are architectural. See the critique for
the full list and `execution-prompt.md` to action it.
