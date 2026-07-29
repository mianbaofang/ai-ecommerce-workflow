# Output Risk Profile

Skill: `ai-ecommerce-workflow`

## Why This Exists

Generated skills often fail in small output details: generic headings, cluttered citations, fragile screenshots, weak Markdown rendering, or missing execution assumptions. This profile predicts the most likely output mistakes before the skill is used heavily.

## Matched Risk Families

### Citation and footnote clutter
- Matched keywords: source, research, reference, 引用, 来源
- Score: `5`

### Markdown readability
- Matched keywords: md, brief, 报告
- Score: `3`

### Screenshot and visual capture
- Matched keywords: image, 图片, 视觉
- Score: `3`

### Tone and specificity
- Matched keywords: copy, 标题, 文案
- Score: `3`

### Code and command safety
- Matched keywords: script, api
- Score: `2`

## Likely Output Mistakes

- Footnote markers or dense citation notes can interrupt the reading flow.
- Evidence can be over-attached to obvious statements and under-attached to risky claims.
- Tables can render as dense grids with weak hierarchy or poor mobile readability.
- Long bullets can make the output look complete while hiding the actual decision logic.
- Screenshots can be captured from the wrong state, wrong viewport, or wrong crop.
- Missing screenshots can cause the skill to invent visual references instead of declaring the gap.

## Output Constraints To Apply

- Attach citations only to claims that need evidence, not to every sentence.
- Group source notes at the end of a section when inline markers would hurt readability.
- Use tables only when comparison is the main job; otherwise prefer compact cards or grouped bullets.
- Keep table cells short and move explanations below the table.
- Never invent a screenshot; state when visual evidence is missing.
- Record the source, viewport, and crop intent for any screenshot-dependent output.

## Self-Repair Checks

- Remove decorative citations that do not support a material claim.
- Move repeated source explanations into one compact source note.
- Preview whether each table still reads well when columns are narrow.
- Convert any table with paragraph-length cells into bullets or cards.
- Check that every screenshot reference points to a real provided or generated asset.
- Reword any visual instruction that depends on an unseen screen state.

## Reviewer Note

Use this report before deepening the package and again before approving example outputs.
