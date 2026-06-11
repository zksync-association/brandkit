# Applying the Brand in Office & Google (PowerPoint, Slides, Docs, Word, Keynote)

> The brand is not web-only. This is how to color-code and type-set decks and documents in
> office tools, including theme-color slot mappings and font fallbacks. Values from `assets/tokens/`.

## Fonts in office tools (important)
ES Allianz and Avenue Mono are **licensed desktop fonts** — they must be installed locally
to use them in PowerPoint/Word/Keynote (license files & .otf/.ttf are in the original brand
folder). **Inter is free** (Google Fonts) and is the safe default everywhere.

| Brand font | Office fallback (if not installed) | Use |
|---|---|---|
| ES Allianz (display) | **Inter** (or Arial as last resort) | Titles, section headers |
| Inter (body) | Arial / Helvetica | Body, most text |
| Avenue Mono (labels) | **Consolas** / Courier New | Eyebrows, labels, page numbers, metadata |

- **Google Slides/Docs:** add Inter via "More fonts." ES Allianz/Avenue Mono are not in Google's
  library — use Inter for display and a mono (e.g. Roboto Mono / Spectral SC) only if you must;
  otherwise keep labels in Inter ALL-CAPS with wide letter-spacing to echo the mono look.
- Always set **titles tracked tight** (PowerPoint: Character Spacing → Condensed ~1pt; CSS −2 to −5%).
- Labels/eyebrows: **ALL CAPS, letter-spacing widened** to mimic Avenue Mono when the real font is absent.

## Theme color slots (PowerPoint / Keynote / Google Slides theme editor)
Map the palette to the theme's color roles so every chart, table, and shape inherits the brand:

| Theme slot | Brand token | Hex | RGB |
|---|---|---|---|
| Text/Background — Dark 1 (main text) | Neutral-950 | `#11141A` | 17, 20, 26 |
| Text/Background — Light 1 (page bg) | Neutral-50 | `#F7F9FC` | 247, 249, 252 |
| Text/Background — Dark 2 | Brand-900 | `#04085F` | 4, 8, 95 |
| Text/Background — Light 2 | Brand-25 | `#F3F5FE` | 243, 245, 254 |
| Accent 1 (primary) | Brand-700 | `#070FA0` | 7, 15, 160 |
| Accent 2 | Brand-500 | `#0C18EC` | 12, 24, 236 |
| Accent 3 | Brand-300 | `#8897F2` | 136, 151, 242 |
| Accent 4 | Salmon-100 | `#EE6D50` | 238, 109, 80 |
| Accent 5 | Neutral-500 | `#858C99` | 133, 140, 153 |
| Accent 6 | Sand-50 | `#FFF6E5` | 255, 246, 229 |
| Hyperlink | Brand-700 | `#070FA0` | 7, 15, 160 |
| Followed hyperlink | Brand-900 | `#04085F` | 4, 8, 95 |

> Chart series order: Brand-700 → Brand-500 → Brand-300 → Salmon-100 → Neutral-500 → Sand-50.
> A ready Office theme color block (Open XML) is in `assets/tokens/office-theme-colors.xml`.

## Slide rules (mirror the HTML deck)
- **Light slides** (Neutral-50). One idea per slide. Generous margins (≥0.6").
- **Title** = ES Allianz/Inter, large, tracked tight, Brand-700.
- **Eyebrow** above title = ALL-CAPS mono-style label, Neutral-600.
- **Body** = Inter, 18–24pt, Neutral-950.
- **Section dividers** may use a **dark slide** (Brand-950 fill, light text) — used sparingly.
- **Accents:** thin 1px rules, outlined boxes (no heavy shadows), Brand-700 highlights, a single
  flag tile or quiet ASCII texture as a motif. Salmon for one governance highlight only.
- **Footer:** page number + `◄► ZK Nation` in mono-style caps.
- **Tables:** header row Brand-25 fill + Brand-700 caps text; 1px Neutral-200 grid.

## Google Docs / Word documents
- Page: white/Neutral-50. Body Inter 11–12pt, line spacing 1.4–1.55, measure ~6.5".
- Headings: Brand-700, tracked tight; H1 ES Allianz/Inter.
- Styled quote = left border 3pt Brand-700, Neutral-600 italic.
- Captions/metadata = caps mono-style, Neutral-600.
- Set **Styles** (Heading 1/2, Normal, Caption) once to these specs so the whole doc inherits them.

## Quick "color-code this deck/doc" checklist
1. Set theme colors per the table above (or paste hexes).
2. Background → Neutral-50; text → Neutral-950; accents/headers → Brand-700.
3. Titles tracked tight; labels ALL-CAPS; body Inter.
4. Replace shadows with 1px outlines; small/no corner radius.
5. One salmon highlight max; never full-bleed brand blue.
