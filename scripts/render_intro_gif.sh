#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LANG="${1:-en}"
case "$LANG" in
  en)
    HTML="$ROOT/docs/site/index.html"
    OUTPUT="$ROOT/docs/assets/intro-animation-preview.gif"
    FRAMES="$ROOT/docs/site/frames-en"
    ;;
  zh)
    HTML="$ROOT/docs/site/project-intro-animation-zh.html"
    OUTPUT="$ROOT/docs/assets/intro-animation-preview-zh.gif"
    FRAMES="$ROOT/docs/site/frames-zh"
    ;;
  *)
    echo "Usage: $0 [en|zh]" >&2
    exit 1
    ;;
esac

mkdir -p "$FRAMES"
rm -f "$FRAMES"/frame-*.png

HTML_URL="file:///$(cygpath -m "$HTML")"
TOTAL=175
for i in $(seq 0 $((TOTAL - 1))); do
  p=$(python -c "print(f'{${i}/(${TOTAL}-1):.5f}')")
  frame=$(printf "%s/frame-%04d.png" "$FRAMES" "$i")
  npx playwright screenshot "${HTML_URL}?p=$p" "$frame" --viewport-size=1600,900 >/dev/null
done

ffmpeg -y -framerate 5 -i "$FRAMES/frame-%04d.png" \
  -vf "scale=1200:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" \
  "$OUTPUT"
