"""Comprehensive layout fixes for index.html and animation HTML files."""
from pathlib import Path

paths = [
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/index.html'),
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/project-intro-animation.html'),
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/project-intro-animation-zh.html'),
]


def patch(text: str) -> tuple[str, int]:
    n = 0

    # 1. .mode inner div: change from flex row (which constrained h3/p side-by-side)
    #    to block layout. mode-num becomes positioned top-left of inner content.
    old = """    .mode > div {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .mode {
      padding: 24px 26px;
      display: grid;
      grid-template-rows: auto auto 1fr;
      gap: 16px;
      position: relative;
      overflow: hidden;
    }"""
    new = """    .mode {
      padding: 24px 26px;
      display: block;
      position: relative;
      overflow: hidden;
    }

    .mode > svg.card-illust {
      display: block;
      width: 100%;
      max-height: 96px;
      margin: 0 0 14px;
    }

    .mode > div {
      display: block;
    }

    .mode > div .mode-num {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      display: grid;
      place-items: center;
      color: #fff;
      background: var(--color);
      font-weight: 850;
      font-size: 22px;
      position: absolute;
      top: 22px;
      right: 22px;
      overflow: hidden;
      flex-shrink: 0;
    }

    .mode > div .mode-num::after {
      content: "";
      position: absolute;
      right: -16px;
      bottom: -16px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.18);
    }

    .mode h3 {
      margin: 0 60px 6px 0;
      font-size: 28px;
      line-height: 1.05;
    }

    .mode p {
      margin: 0;
      font-size: 18px;
      line-height: 1.32;
      color: var(--muted);
    }"""
    if old in text:
        text = text.replace(old, new)
        n += 1

    # 2. .material-card: change to simple block (not 5-row grid that pushed SVG oversized)
    old = """    .material-card {
      padding: 28px 28px 22px;
      display: grid;
      grid-template-rows: auto auto auto 1fr auto;
      gap: 12px;
      position: relative;
      overflow: hidden;
    }

    .material-card h3 {
      margin: 4px 0 0;
      font-size: 28px;
      line-height: 1.05;
    }

    .material-card p {
      margin: 0;
      font-size: 18px;
      color: var(--muted);
      line-height: 1.32;
    }

    .card-illust {
      width: 100%;
      max-height: 132px;
      display: block;
    }"""
    new = """    .material-card {
      padding: 26px 28px;
      display: block;
      position: relative;
      overflow: hidden;
    }

    .material-card svg.card-illust {
      display: block;
      width: 100%;
      max-height: 92px;
      margin: 0 0 12px;
    }

    .material-card h3 {
      margin: 0 0 6px;
      font-size: 28px;
      line-height: 1.05;
    }

    .material-card p {
      margin: 0 0 12px;
      font-size: 18px;
      color: var(--muted);
      line-height: 1.32;
    }"""
    if old in text:
        text = text.replace(old, new)
        n += 1

    # 3. Role cards: block layout (prevent absolute SVG overlap with body text)
    old = """    .role {
      padding: 28px;
      display: grid;
      align-content: center;
      gap: 12px;
      position: relative;
      overflow: hidden;
    }"""
    new = """    .role {
      padding: 30px 32px;
      display: block;
      position: relative;
      overflow: hidden;
    }

    .role > svg {
      display: block;
      width: 44px;
      height: 44px;
      margin: 0 0 12px;
    }

    .role h3 {
      margin: 0 0 6px;
      font-size: 26px;
      line-height: 1.05;
    }

    .role p {
      margin: 0;
      font-size: 17px;
      color: var(--muted);
      line-height: 1.3;
    }"""
    if old in text:
        text = text.replace(old, new)
        n += 1

    # 4. Modules: block layout
    old = """    .module {
      padding: 24px 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }"""
    new = """    .module {
      padding: 22px 22px;
      display: block;
      position: relative;
      overflow: hidden;
    }

    .module > svg {
      display: block;
      width: 44px;
      height: 44px;
      margin: 0 0 10px;
    }"""
    if old in text:
        text = text.replace(old, new)
        n += 1

    # 5. Hide brand-subtitle, progress, accent, brand, tags, footer outside hero scene
    #    via a CSS class that's only active during scene 0
    #    We'll add a body.phase-scene class set by JS
    old = """    .footer {"""
    new = """    /* Global brand chrome is hidden once animation starts to give scenes breathing room */
    body.phase-scene .brand-subtitle,
    body.phase-scene .progress,
    body.phase-scene .accent,
    body.phase-scene .footer { opacity: 0; pointer-events: none; }
    body .footer { opacity: 1; transition: opacity 0.4s ease; }

    .footer {"""
    if old in text:
        text = text.replace(old, new, 1)
        n += 1

    # 6. Add JS phase toggle
    #    We'll inject at the end of the existing <script> block
    if 'body.classList.add' in text:
        return text, n

    # We add a small inline script (or inline after the GSAP setup)
    js_inject = """    // Show chrome only during hero scene (scene-0), hide during other scenes
    const allScenes = Array.from(document.querySelectorAll('.scene'));
    const domBody = document.body;
    function updateChromeForScene(idx) {
      if (idx === 0) domBody.classList.remove('phase-scene');
      else domBody.classList.add('phase-scene');
    }
    const origSetProgress = window.setProgressForChrome || setProgress;
    """
    # Insert after "window.__timelines" registration
    anchor = "window.__timelines['ai-ecommerce-workflow-intro'] = tl;"
    if anchor in text:
        text = text.replace(anchor, anchor + '\n' + js_inject)
        # Wrap setProgress so we can call updateChromeForScene on each tick.
        # Simpler: just override setProgress via direct re-implementation by
        # scanning its body -- but the cleaner path is to dispatch an event.
        n += 1
        # Add a MutationObserver OR a polling timer that reads active scene
        poll = """
    // Track which scene is currently 'active' by data-scene id
    function activeSceneIndex() {
      let active = -1;
      for (let i = 0; i < allScenes.length; i += 1) {
        if (allScenes[i].classList.contains('active')) { active = i; break; }
      }
      return active;
    }
    setInterval(() => {
      updateChromeForScene(activeSceneIndex());
    }, 120);
    """
        # Place poll right after the existing tick block (last line of script)
        last_brace = text.rindex('requestAnimationFrame(tick);')
        if last_brace >= 0:
            insert_at = last_brace + len('requestAnimationFrame(tick);')
            text = text[:insert_at] + '\n' + poll + text[insert_at:]
            n += 1

    return text, n


for p in paths:
    text = p.read_text(encoding='utf-8')
    new_text, n = patch(text)
    if n:
        p.write_text(new_text, encoding='utf-8')
    print(f'{p.name}: {n} patches applied')
