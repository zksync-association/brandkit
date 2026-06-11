# Font Licensing — READ BEFORE USING THE FONTS

The brand uses three typefaces. **One is free. Two are commercial and licensed per-domain /
per-user — you generally need to buy your own license to use them.** This file tells you what's
allowed and how to get legal.

## At a glance

| Font | Foundry | License | Can you reuse the files? |
|---|---|---|---|
| **Inter** | rsms / Google Fonts | **SIL Open Font License (free)** | ✅ Yes — use, host, and redistribute freely. |
| **ES Allianz** | **Extraset Typefoundry** (extraset.ch, Geneva) | Commercial. ZKsync Association holds a **web license: 5 weights, ≤10,000 visitors/month, per domain.** | ❌ No. Do **not** copy, host for others, or redistribute. License your own. |
| **Avenue Mono** | **Boulevard LAB** (boulevardlab.com) | Commercial. Web license = **1 domain, ≤10,000 monthly unique visitors**; desktop = **1 user**. | ❌ No redistribution, sublicensing, lending, or giving away. |

> The ZKsync Association's licenses (per the Extraset invoice ES251013-4821 and the Boulevard
> LAB receipts) cover the **Association's own use on its own domain(s)** within the visitor cap.
> They do **not** extend to you, your client, or your project.

## Why the font files are NOT in this kit
Both EULAs prohibit redistribution: *"The Font Software … may not be sublicensed, sold, leased,
rented, lent, or given away to another person or entity."* So the `.woff2/.woff/.otf/.ttf`
binaries for ES Allianz and Avenue Mono are **intentionally excluded** from the public skill,
the public repo, and the downloadable assets. Only Inter is safe to ship.

## Four ways to handle fonts (pick one)

### 1. Default — no setup (free, legal)
Do nothing. The CSS font stacks fall back to **Inter** (display) and a system monospace (labels).
You lose the exact ES Allianz / Avenue Mono character but everything else is fully on-brand.

### 2. Demo / free look-alikes (free, legal, instant)
Include `assets/tokens/fonts-demo.css` after `brand.css`. It loads open-licensed Google Fonts
(**Archivo** for display, **Space Mono** for labels) and re-points the brand variables to them.
Great for prototypes and demos. These are approximations, not the real faces.

### 3. Official trial fonts (free, evaluation only)
Both foundries offer **trial/test fonts** for evaluation (non-commercial):
- ES Allianz trial → **https://extraset.ch** (request/download trial weights).
- Avenue Mono → **https://boulevardlab.com**.
Place the trial `.woff2/.woff` in `assets/fonts/` (matching the names in `fonts-licensed.css`)
and include `fonts-licensed.css`. **Trials may not be used in production / commercial work.**

### 4. Full license (required for production brand work)
Buy a license that matches your use:
- **ES Allianz** — Extraset (https://extraset.ch). Web license is priced by monthly visitors
  (the Association paid CHF 70/weight × 5 = CHF 350 for ≤10k MUV). Buy more for higher traffic
  or additional domains; buy a desktop license for PowerPoint/Keynote/print.
- **Avenue Mono** — Boulevard LAB (https://boulevardlab.com). Web = per domain/≤10k MUV;
  desktop = per user.
Then drop your licensed files into `assets/fonts/` and include `fonts-licensed.css`.

## Practical notes
- **Web:** licensed web fonts may be self-hosted **only on the domain(s) on your invoice**, within
  the visitor cap. Don't expose the raw files as downloads, and don't serve them to other domains.
- **PowerPoint / Word / Keynote (desktop):** needs a **desktop** license (per user). Without it,
  use Inter + Consolas fallbacks (see `office-docs-and-slides.md`).
- **Embedding in PDFs/docs:** both EULAs allow embedding only in **secured read/print-only** mode
  and **only if the document is not itself a commercial product** — otherwise buy an extra license.
- **When unsure, fall back to Inter.** It's always safe.
