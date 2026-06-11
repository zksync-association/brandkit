#!/usr/bin/env bash
# Mirror skill/ assets + references into site/brand/, then rebuild the downloadable skill zip.
# Run from anywhere:  bash scripts/sync.sh
#
# Why: site/brand/ is a PUBLIC MIRROR of the skill's assets so the website and the skill stay
# identical. The design source of truth is skill/assets/tokens/. There is no bundler.
set -euo pipefail
cd "$(dirname "$0")/.."            # -> repo root (brandkit/)

# 1. Mirror tokens, artwork, and references (NOT fonts — those are licensed, managed separately).
for d in tokens logos icons flags ascii; do
  rm -rf "site/brand/$d"
  cp -R "skill/assets/$d" "site/brand/$d"
done
rm -rf site/brand/references
cp -R skill/references site/brand/references

# 2. Licensed showcase fonts: refresh from the local-only licensed copy if present.
#    (ES Allianz + Avenue Mono are commercial; they are NOT in git. The site serves them
#     because the Association is licensed. See skill/references/font-licensing.md.)
if [ -d "_licensed-fonts-DO-NOT-REDISTRIBUTE" ]; then
  mkdir -p site/brand/fonts
  cp _licensed-fonts-DO-NOT-REDISTRIBUTE/*.woff2 _licensed-fonts-DO-NOT-REDISTRIBUTE/*.woff site/brand/fonts/ 2>/dev/null || true
fi

# 3. Rebuild the downloadable, license-clean skill zip.
find . -name .DS_Store -delete 2>/dev/null || true
rm -f site/zk-nation-brand-skill.zip
( zip -r -q site/zk-nation-brand-skill.zip skill -x '*.DS_Store' )

echo "✓ Synced skill/ -> site/brand/ and rebuilt site/zk-nation-brand-skill.zip"
echo "  Next: verify (Playwright), publish from site/ via here.now, commit, push (as rafathebuilder-ZK)."
