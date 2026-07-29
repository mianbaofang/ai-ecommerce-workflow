from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "site" / "readme-animation-en.html"
OUTPUT = ROOT / "docs" / "assets" / "intro-animation-preview.gif"


def main() -> None:
    with TemporaryDirectory() as temp_dir:
        frames = Path(temp_dir) / "frames"
        frames.mkdir()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 960, "height": 540}, device_scale_factor=1)
            page.goto(SOURCE.as_uri(), wait_until="load")
            for frame in range(100):
                page.evaluate("frame => window.renderAt(frame)", frame)
                page.screenshot(path=frames / f"frame-{frame:03d}.png")
            browser.close()
        palette = Path(temp_dir) / "palette.png"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", "5", "-i", str(frames / "frame-%03d.png"), "-vf", "palettegen=max_colors=96:stats_mode=diff", str(palette)], check=True)
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", "5", "-i", str(frames / "frame-%03d.png"), "-i", str(palette), "-lavfi", "paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle", "-loop", "0", str(OUTPUT)], check=True)


if __name__ == "__main__":
    main()
