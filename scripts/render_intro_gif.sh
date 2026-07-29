#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LANG="${1:-zh}"
PROJECT="$ROOT/reports/manual-simulation/hyperframes-evidence"
SOURCE="$PROJECT/renders/ai-ecommerce-workflow-promo-16x9.gif"

case "$LANG" in
  en)
    if command -v python >/dev/null 2>&1; then
      PYTHON=python
    elif command -v python.exe >/dev/null 2>&1; then
      PYTHON=python.exe
    else
      echo "Python with Playwright is required to render the English README GIF." >&2
      exit 1
    fi
    PYTHON_SOURCE="$ROOT/scripts/render_english_readme_gif.py"
    if [[ "$ROOT" =~ ^/mnt/[[:alpha:]]/ ]]; then
      DRIVE="${ROOT:5:1}"
      PYTHON_SOURCE="${DRIVE^^}:/${ROOT:7}/scripts/render_english_readme_gif.py"
    fi
    "$PYTHON" "$PYTHON_SOURCE"
    exit 0
    ;;
  zh)
    OUTPUT="$ROOT/docs/assets/intro-animation-preview-zh.gif"
    ;;
  *)
    echo "Usage: $0 [en|zh]" >&2
    exit 1
    ;;
esac

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js 22 or newer is required to render the Chinese README GIF." >&2
  exit 1
fi

NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]')"
if [[ "$NODE_MAJOR" -lt 22 ]]; then
  echo "HyperFrames 0.7.80 requires Node.js 22 or newer; found $(node --version)." >&2
  exit 1
fi

(
  cd "$PROJECT"
  npx --yes hyperframes@0.7.80 render \
    --format gif \
    --fps 10 \
    --gif-loop 0 \
    --quality high \
    --output "$SOURCE"
)

ffmpeg -y -i "$SOURCE" \
  -filter_complex "fps=5,scale=960:540:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=96:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
  "$OUTPUT"

if [[ "$LANG" == "zh" ]]; then
  cp "$OUTPUT" "$ROOT/docs/assets/intro-animation-preview-zh-960.gif"
fi
