"""Comprehensive palette fix-up for animation HTML and related files."""
from pathlib import Path

# Remaining colors that didn't get caught by the first round
# (because regex miss / color was outside the mapping table / or wasn't in scope).
remaining_fixes = {
    # Old-yellow missed by script (script mapped #f5a400, not #f4a000)
    '#f4a000': '#C8A652',
    # Body background: old beige (#f7f4ed / #fff8ef) - convert to paper white / remove
    '#f7f4ed': '#FBF9F4',
    # Stage radial gradients still use old blue/green
    'rgba(47, 128, 237, 0.12)': 'rgba(45, 95, 92, 0.10)',  # blue -> teal
    'rgba(21, 160, 109, 0.12)': 'rgba(122, 140, 92, 0.10)',  # green -> sage
    # Old subtitle cold gray
    '#354052': '#5C5346',
    # Cold-text shadows (rgba) tied to old --ink value
    'rgba(31, 41, 55, 0.18)': 'rgba(43, 37, 32, 0.20)',
    'rgba(31, 41, 55, 0.12)': 'rgba(43, 37, 32, 0.14)',
    # Step-row borders (cold blue-gray)
    '#e9edf2': '#E0DAC9',
    # Skill chip border/background (cold blue tints)
    '#d8e6f7': '#D8DAD9',  # neutral light gray border
    '#f5faff': '#F2EFE6',  # warm light bg
    '#1d5d9d': '#2D5F5C',  # deep blue text -> deep teal text
    # Brief-box: cold gray bg/text
    '#f8fafc': '#F0E8DD',  # warm light amber tint
    '#334155': '#3F3932',  # cold text -> warm dark
    # Tag chip cold colors
    '#475569': '#5C5346',  # cold gray -> warm gray
    '#d7dce4': '#D9CFC0',  # cold border -> warm border
    # Old light tints inside mode + material SVGs
    '#eaf2fc': '#DEE7E4',  # light blue -> light teal
    '#e6f4ec': '#E5E8DC',  # light green -> light sage
    '#eef4fc': '#DEE7E4',  # light blue (materials) -> light teal
    '#ecf7ed': '#E5E8DC',  # light green (materials) -> light sage
    '#f3edfd': '#EBE5E8',  # light lavender
    # Stage gradient stops
    '#fbfdff': '#FBF9F4',  # cool white stop -> paper white
    '#eef8f1': '#E8E8E0',  # sage-tinted gradient stop
    # Brand accent bar fill rgba
    'rgba(255, 255, 255, 0.18)': 'rgba(253, 249, 244, 0.20)',
    # Generic cold border-edge leftovers
    '#f1e5dd': '#F0E8DD',
}

paths = [
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/index.html'),
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/project-intro-animation.html'),
    Path('E:/Object/taobao-newproduct-launch-workflow/docs/site/project-intro-animation-zh.html'),
]
for p in paths:
    if not p.exists():
        continue
    text = p.read_text(encoding='utf-8')
    before = text
    total = 0
    for old, new in remaining_fixes.items():
        before_lower = before.count(old)
        if before_lower:
            before = before.replace(old, new)
            total += before_lower
    if total:
        p.write_text(before, encoding='utf-8')
    print(f'{p.name}: {total} further fixes applied')
