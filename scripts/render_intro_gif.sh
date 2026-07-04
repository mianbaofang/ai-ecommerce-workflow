#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HTML="$ROOT/docs/site/index.html"
FRAMES="$ROOT/docs/site/frames"
mkdir -p "$FRAMES"
rm -f "$FRAMES"/frame-*.png

HTML_URL="file:///$(cygpath -m "$HTML")"
TOTAL=250
for i in $(seq 0 $((TOTAL - 1))); do
  p=$(python -c "print(f'{${i}/(${TOTAL}-1):.5f}')")
  frame=$(printf "%s/frame-%04d.png" "$FRAMES" "$i")
  npx playwright screenshot "${HTML_URL}?p=$p" "$frame" --viewport-size=1600,900 >/dev/null
 done

ffmpeg -y -framerate 10 -i "$FRAMES/frame-%04d.png" \
  -vf "scale=1200:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" \
  "$ROOT/docs/assets/intro-animation-preview.gif"
