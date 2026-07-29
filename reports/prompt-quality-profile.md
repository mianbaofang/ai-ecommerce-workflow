# Prompt Quality Profile

Skill: `ai-ecommerce-workflow`
Relevance: `prompt-heavy`
Overall quality score: `93.0/100`

## Primary Task Family

**Creative generation**
- Matched keywords: copy, 创意, 文案, 标题, 内容

## Complexity

- Band: `expert`
- Score: `22`
- Reason: multiple task families plus governance, evaluation, or expert-level constraints

## Need Model

- Explicit Need: Turn a product description, public product URL, or product images into a sourced public-market research brief and, after platform selection, a reviewable listing and asset pack.
- Implicit Need: The reusable skill needs a stable role, task, and output contract rather than a one-off prompt.
- Scenario: Product description, Public product URL, One or more product images, Optional target platform, region, language, brand voice, and image-generation request
- User Level: infer from examples and standards; ask only if it changes output depth
- Success Standard: A first useful result should not require a structured product-facts form., Unsupported claims are marked pending confirmation instead of being guessed., Platform copy and image generation wait for the user's platform and tool choice.

## RTF To Skill Mapping

- Role: Use a taste-aware creator role with clear audience, tone, and originality boundaries.
- Task: Generate variants, explain selection logic, and preserve the user's distinctive constraints.
- Format: Return options with rationale, selection criteria, and refinement paths.

## Quality Matrix

### Completeness — 100/100
- Matched signals: output, 输入, 输出
- Repair: Name missing inputs, outputs, constraints, or success standards before deepening the package.

### Clarity — 90/100
- Matched signals: specific, 明确
- Repair: Replace broad verbs with observable actions and define what done means.

### Consistency — 90/100
- Matched signals: 一致, 边界
- Repair: Check that role, task, format, exclusions, and examples do not contradict each other.

### Practicality — 95/100
- Matched signals: use, workflow, 执行, 使用
- Repair: Add runnable steps, examples, or verification cues instead of abstract advice.

### Specificity — 90/100
- Matched signals: 用户, 场景
- Repair: Anchor wording in the user's audience, domain nouns, and target outcome.

## Matched Task Families

### Creative generation
- Score: `5`
- Keywords: copy, 创意, 文案, 标题, 内容
- Role: Use a taste-aware creator role with clear audience, tone, and originality boundaries.
- Task: Generate variants, explain selection logic, and preserve the user's distinctive constraints.
- Format: Return options with rationale, selection criteria, and refinement paths.

### Execution operation
- Score: `4`
- Keywords: workflow, 流程, 执行, 清单
- Role: Use an operator role with explicit boundaries, inputs, outputs, and failure handling.
- Task: Convert the job into ordered steps with validation checks and stop conditions.
- Format: Return a runbook-like handoff with commands, checks, owners, and next actions when relevant.

### Dialogue interaction
- Score: `3`
- Keywords: support, chat, 对话
- Role: Use a conversational role that asks only high-leverage questions and remembers the user's goal.
- Task: Clarify intent, resolve uncertainty, and converge toward a recommendation instead of a long option list.
- Format: Return concise prompts, decision points, and reviewer-visible assumptions.

### Prompt engineering
- Score: `1`
- Keywords: prompt
- Role: Use a prompt engineer role only when role design materially improves execution.
- Task: Map Role, Task, and Format into skill behavior rather than copying a large prompt template.
- Format: Return a compact prompt contract plus tests, quality matrix, and usage notes.

## Self-Repair Checks

- Check explicit need, implicit need, scenario, user level, and success standard before deepening.
- Map Role, Task, and Format into skill behavior, not decorative prompt labels.
- Ask one focused clarification only when missing information changes the package boundary.
- Add tests or examples for prompt-heavy behavior before treating it as reusable.
- Keep prompt methodology in references and reports instead of bloating SKILL.md.

## Reviewer Note

Use this profile when the package depends on prompt behavior, role design, output contracts, or conversation quality.
