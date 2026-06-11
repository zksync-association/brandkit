# Fonts — why this folder is (almost) empty

**Inter** (the body/UI font) is free (SIL OFL) — load it from Google Fonts; no file needed here.

**ES Allianz** (Extraset) and **Avenue Mono** (Boulevard LAB) are **commercial, per-domain
licensed fonts.** Their binaries are deliberately **not** included in this skill because their
licenses forbid redistribution. See `../../references/font-licensing.md`.

To get the real faces, pick a path (full details in `font-licensing.md`):

1. **Do nothing** → everything falls back to Inter. Fully on-brand layout, free.
2. **Demo look-alikes** → include `../tokens/fonts-demo.css` (free Archivo + Space Mono).
3. **Official trials** (evaluation only) → download from extraset.ch / boulevardlab.com,
   drop the `.woff2/.woff` here using the names in `../tokens/fonts-licensed.css`, include that file.
4. **Full license** → buy from the foundries, place your files here, include `fonts-licensed.css`.

Expected filenames (for options 3–4):
```
ESAllianz-Extralight.woff2 / .woff
ESAllianz-Light.woff2 / .woff
ESAllianz-Book.woff2 / .woff
ESAllianz-Medium.woff2 / .woff
ESAllianz-Bold.woff2 / .woff
AvenueMono.woff2 / .woff
```
