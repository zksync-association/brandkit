#!/usr/bin/env python3
"""
check-brand-assets.py — confirm every visual in a branded artifact is sourced from the ZK Nation kit.

This is the automated form of the "Asset gate" in references/dos-and-donts.md: the most common way
on-brand work goes wrong is an agent substituting CSS / Unicode / hand-drawn marks for a real shipped
asset (a dot-grid instead of an assets/ascii field, an emoji instead of a duotone icon, the logo
rebuilt from boxes). Those mistakes pass a color/type review but are mechanically detectable here.

Run it on whatever you're about to ship:
    python3 scripts/check-brand-assets.py page.html [more.html ...]   # or a directory

Exit code is non-zero if any FAIL is found. WARNs are advisory — read them, don't ignore them.
Pure stdlib; works offline; no dependencies.
"""
import re, sys, pathlib, base64

# A visual reference counts as "from the kit" if it points at kit asset paths/URLs…
KIT_SRC = re.compile(r"""(
    /brand/(?:logos|icons|flags|ascii|tokens)/   |   # hosted mirror
    (?:^|[./'"(])assets/(?:logos|icons|flags|ascii)/ |   # in-tree asset paths
    npc\.here\.now/zknationbrand                  |   # published mirror host
    raw\.githubusercontent\.com/zksync-association/brandkit   # raw repo host
)""", re.X)

# …or it's one of the kit's own inline graphics: the 26×26 CTA arrow glyph, or the real logomark /
# lockup (matched by their distinctive viewBoxes after base64-decode). Any OTHER inline data-URI image
# is flagged for review — a synthesized "texture"/icon is exactly the substitution this check catches.
ARROW_GLYPH = re.compile(r"M0 \.015h26v25\.97H0z")
KIT_MARK_VIEWBOX = ('viewBox="0 0 211 211"', 'viewBox="0 0 213 36"')  # logomark, ZK Nation lockup

def is_kit_mark(ref):
    if ARROW_GLYPH.search(ref):
        return True
    blob = ref
    if ";base64," in ref:
        try:
            blob += base64.b64decode(ref.split(",", 1)[1]).decode("utf-8", "replace")
        except Exception:
            pass
    return any(vb in blob for vb in KIT_MARK_VIEWBOX)

IMG_EXT = r"\.(?:png|jpe?g|gif|webp|avif|svg|ico)"
# Image references: <img src>, <source srcset>, <link rel=icon href>, <use href>, and CSS url(...).
REF_PATTERNS = [
    re.compile(r"<img\b[^>]*\bsrc\s*=\s*['\"]([^'\"]+)['\"]", re.I),
    re.compile(r"\bsrcset\s*=\s*['\"]([^'\"]+)['\"]", re.I),
    re.compile(r"<link\b[^>]*\brel\s*=\s*['\"][^'\"]*icon[^'\"]*['\"][^>]*\bhref\s*=\s*['\"]([^'\"]+)['\"]", re.I),
    re.compile(r"<use\b[^>]*\b(?:xlink:)?href\s*=\s*['\"]([^'\"]+)['\"]", re.I),
    re.compile(r"url\(\s*['\"]?([^'\")]+?)['\"]?\s*\)", re.I),
]
# Emoji / pictographs — the brand never uses these; treat as a fake-icon symptom (and a voice-gate miss).
# (Plain arrows U+2190–21FF are intentionally excluded so the prose twin-arrow mark "←→" isn't flagged.)
EMOJI = re.compile("[" "\U0001F000-\U0001FAFF" "\U00002600-\U000027BF" "\U0001F1E6-\U0001F1FF" "️" "]")
# Box-drawing / block / decorative-arrow runs used to "draw" a texture or icon in text.
DECOR_RUN = re.compile(r"[─-▟■-◿◀▶▸▾▴]{3,}")
# A typed ASCII "flag field" — the #1 reconstruction of brand artwork. A line made ONLY of the
# lattice glyphs (z/x/k/i + dots/marks) that carries several z/x/k/i letters is hand-typed texture,
# not prose, code, base64, or a comment divider (those carry other letters or no x/z/k/i).
LATTICE_CHARS = set("xzkiXZKI.:/+*-·°•∙oO0 \t")
def lattice_line_hits(text):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        st = line.strip()
        if len(st) >= 20 and all(c in LATTICE_CHARS for c in st) and sum(c in "xzkiXZKI" for c in st) >= 8:
            hits.append(i)
    return hits

# Component classes that brand.css OWNS. Redefining one in a page that ALSO links brand.css collides
# with the kit's rules (e.g. .zk-btn::after appends a 2nd arrow; .zk-footer's grid hijacks your layout).
RESERVED_KIT_CLASSES = ("btn", "footer", "card", "nav", "tag", "hero", "label", "eyebrow", "meta", "rule")
RESTYLE = re.compile(r"\.zk-(" + "|".join(RESERVED_KIT_CLASSES) + r")\b[^{}]*\{([^{}]*)\}")
COLLIDE_PROPS = ("background", "display", "grid-template", "padding", "width", "height", "content", "border")
LINKS_BRANDCSS = re.compile(r"(?:href|@import)[^;>]*brand\.css", re.I)

def classify(path):
    text = pathlib.Path(path).read_text(errors="replace")
    lines = text.splitlines()
    fails, warns, infos = [], [], []

    def loc(idx):  # 1-based line number for a string index
        return text.count("\n", 0, idx) + 1

    # 1. Image references must resolve to a kit asset (or a known brand data-URI).
    for pat in REF_PATTERNS:
        for m in pat.finditer(text):
            ref = m.group(1).strip()
            # only judge things that are actually images (skip fonts, anchors, js)
            is_img = re.search(IMG_EXT + r"(?:$|[?#])", ref, re.I) or ref.startswith("data:image")
            if not is_img:
                continue
            if ref.startswith("data:image"):
                if is_kit_mark(ref):
                    continue  # kit's own inline mark (arrow glyph / logomark / lockup) ✓
                warns.append((loc(m.start()), f"inline data-URI image — confirm it's a real brand mark, not a synthesized texture/icon: {ref[:48]}…"))
                continue
            if KIT_SRC.search(ref):
                continue  # sourced from the kit ✓
            fails.append((loc(m.start()), f"image not sourced from the kit: {ref[:80]}"))

    # 2. Emoji / pictographs anywhere = off-brand fake icon.
    for m in EMOJI.finditer(text):
        fails.append((loc(m.start()), f"emoji/pictograph used as a visual (the brand uses real icons, never emoji): {m.group()!r}"))

    # 3. Decorative-glyph runs (drawing a flag/texture/icon in text).
    for m in DECOR_RUN.finditer(text):
        warns.append((loc(m.start()), f"decorative glyph run — looks like a hand-drawn texture/mark; use assets/ascii or a real SVG: {m.group()[:24]!r}"))

    # 3b. Typed ASCII flag-field (z/x/k/i lattice) — a redraw of brand artwork. Fail on >=2 such lines.
    lat = lattice_line_hits(text)
    if len(lat) >= 2:
        fails.append((lat[0], f"{len(lat)} lines look like a typed ASCII/character flag field (z/x/k/i grid) — "
                              f"load the real image (assets/ascii/ or assets/flags/…/main-flag-ascii_*.png), never type the texture"))

    # 3c. Redefining a kit class while linking brand.css → collision (only in consumer HTML, not the kit's own CSS).
    if str(path).lower().endswith((".html", ".htm")) and LINKS_BRANDCSS.search(text):
        seen = set()
        for m in RESTYLE.finditer(text):
            cls, body = m.group(1), m.group(2)
            if cls not in seen and any(p in body for p in COLLIDE_PROPS):
                seen.add(cls)
                warns.append((loc(m.start()), f"redefines kit class .zk-{cls} while linking brand.css — this collides with the "
                                              f"kit's own rules (e.g. .zk-btn::after arrow, .zk-footer grid). Use the class as-is, "
                                              f"or give your custom variant a NEW name."))

    # 4. Faked texture heuristic: radial-gradient (the brand gradient is linear) often stands in for an ASCII field.
    for m in re.finditer(r"radial-gradient\(", text, re.I):
        warns.append((loc(m.start()), "radial-gradient background — confirm it isn't standing in for a real assets/ascii field"))

    # info: inline <svg> blocks are fine (inlining real marks is encouraged) — just surface the count.
    n_svg = len(re.findall(r"<svg\b", text, re.I))
    if n_svg:
        infos.append((0, f"{n_svg} inline <svg> block(s) — fine if they're real brand marks (arrow glyph, value icons, logo)"))
    return fails, warns, infos

def gather(paths):
    out = []
    for p in paths:
        pp = pathlib.Path(p)
        if pp.is_dir():
            out += [q for q in pp.rglob("*") if q.suffix.lower() in {".html", ".htm", ".svg", ".css"}]
        else:
            out.append(pp)
    return out

def main(argv):
    if len(argv) < 2:
        print("usage: check-brand-assets.py <file-or-dir> [...]"); return 2
    files = gather(argv[1:])
    total_fail = 0
    for f in files:
        fails, warns, infos = classify(f)
        if not (fails or warns):
            print(f"PASS  {f}")
        else:
            status = "FAIL" if fails else "WARN"
            print(f"{status}  {f}")
        for ln, msg in fails: print(f"   ✗ L{ln}: {msg}")
        for ln, msg in warns: print(f"   ! L{ln}: {msg}")
        for ln, msg in infos: print(f"   · {msg}")
        total_fail += len(fails)
    print(f"\n{'FAILED' if total_fail else 'OK'}: {total_fail} hard issue(s) across {len(files)} file(s)."
          + ("  No visual was faked — every image is kit-sourced." if not total_fail else
             "  Replace each flagged visual with the real asset from assets/ (see dos-and-donts.md → Asset gate)."))
    return 1 if total_fail else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
