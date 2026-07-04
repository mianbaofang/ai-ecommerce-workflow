# AI Ecommerce Workflow

<p align="center">
  <a href="https://mianbaofang.github.io/ai-ecommerce-workflow/docs/site/project-intro-animation.html">
    <img src="docs/assets/intro-animation-preview.gif" alt="35-second project introduction with GPT Image 2 generated visuals" width="100%">
  </a>
</p>

## Why This Skill Exists

A usable ecommerce launch package is rarely one writing task. It needs positioning, competitor price bands, review-mined pain points, main image logic, a detail page in the user's actual decision order, SEO titles, FAQ, customer-service scripts, and a launch plan that respects budget and inventory.

I built this Skill because watching a real team prepare a new product still takes several days and three people. Operators draft a brief, designers ask the same twenty questions, and service checks the listing too late. There is also a more annoying problem: the AI draft usually looks confident, but the numbers inside are guessed and the absolute statements would not survive a marketplace review.

This Skill turns that work into one structured Agent workflow. It validates the input, calls companion search and scrape tools, labels every claim with an evidence level and a source trail, blocks prohibited marketplace terms before any copy goes out, refuses to invent a closed loop when the user cannot afford paid traffic, and packages the answer by who needs to act next. Operators, designers, service and decision makers each get a focused packet instead of one long report.

It does not publish products to seller backends, write fake reviews, scrape without authorization, or guarantee marketplace performance. It prepares a reviewable operating package and stays honest about what data is real, what is observed, and what is only inferred.

<p align="center">
  <a href="README.zh-CN.md">中文 README</a>
  ·
  <a href="skill/">Skill</a>
  ·
  <a href="skill/templates/user-input-form.md">Input form</a>
  ·
  <a href="skill/examples/commute-backpack.md">Example output</a>
  ·
  <a href="docs/COMPANION-SKILLS.md">Companion skills</a>
  ·
  <a href="skill/references/compliance-terms.md">Compliance terms</a>
  ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

An Agent Skill for preparing ecommerce new-product launch packages across Taobao, Pinduoduo, Douyin, Amazon, 1688, Kuaishou, and similar channels. Built for OpenClaw, Hermes, Codex, or any Skill-compatible Agent runtime.

## Quick Start

Most users do not need to install code. Give this Skill path to a Skill-compatible Agent:

```text
https://github.com/mianbaofang/ai-ecommerce-workflow/tree/main/skill
```

Then ask:

```text
Install this Skill, then run a complete ecommerce product launch workflow for my new commute backpack.
```

Chinese invocation template:

```text
【跑电商新品上架流程】
运行模式:完整上架
产品名称:通勤收纳双肩包
产品类目:箱包 / 通勤包
一句话描述:大容量通勤双肩包,能放 15.6 寸电脑,干湿分区,防泼水面料
目标平台:淘宝 + 拼多多
售价区间:109-159元
预估成本:45元
```

The Agent should validate three required fields before running:

1. Product name plus one-line description.
2. Product category.
3. Target platform or platforms.

Optional but useful fields: product photos, price and cost, launch budget, inventory, fulfillment capacity, known competitors, desired copy tone, and whether image/video prompt briefs are needed.

## Run Modes

| Mode | Use when | Output scope |
|---|---|---|
| Quick diagnosis | Decide whether the product is worth testing | Positioning, users, pain points, competitor band, opportunity summary |
| Complete launch | Build the full pre-listing package | All 15 outputs plus 4-role handoffs |
| Material production | Direction is set and you need image/detail/title briefs | Selling points, main images, detail page, titles, design brief, optional image/video prompts |
| Post-launch optimization | Product is listed but data is weak | Competitor review, title/keyword, reviews, FAQ, customer service, optimization plan |

## Capability Matrix

| Category | Feature | Dependency | Status |
|---|---|---|---|
| Core workflow | Input validation, run modes, output contract | None | Built-in |
| Core workflow | 15 launch modules | None | Built-in |
| Marketing | Competitor price-band analysis | Companion search/scrape skill | Needs skill |
| Copy | Humanized copy checks | Built-in rules | Built-in |
| Copy | Enhanced anti-AI writing | `humanizer-zh` skill | Needs skill |
| Compliance | Auto-block prohibited marketplace terms | Built-in reference list | Built-in |
| Evidence | Source trail per competitor claim | Manual URL/time tags | Built-in |
| Traffic | 30-day plan with kill switch | Built-in budget rules | Built-in |
| Images | Prompt briefs and preflight | None | Built-in |
| Images | Actual image generation | User-provided model/tool | User provides |
| Video | Storyboards and prompt briefs | None | Built-in |
| Video | Actual video generation | User-provided tool | User provides |
| Data | Real transaction prices | User screenshots or authorized exports | User provides |

Default behavior: when no companion search tool is available, the Skill still runs but prices and reviews are marked pending verification. When no budget is given, the 30-day plan defaults to free/low-budget actions only.

## Companion Skills

This Skill is designed to auto-call companion search and scrape skills when they are installed in the Agent environment:

- `multi-search-engine` — multi-engine competitor discovery (Chinese and international)
- `anysearch` — real-time web search and page extraction
- `firecrawl-search` + `firecrawl-scrape` — find and read public product pages
- `agent-reach` — Xiaohongshu, Bilibili, Reddit, Twitter, and other content/social sources
- `humanizer-zh` — stronger anti-AI writing pass
- `Tavily` — optional search API when the environment already provides it

If a companion skill is missing, the Agent should say which one is missing, continue with available evidence, and mark affected claims as pending verification. Detailed rule: [docs/COMPANION-SKILLS.md](docs/COMPANION-SKILLS.md).

The Skill does not bundle any API keys. Keys for private tools stay in environment variables; the open-source repo is provider-neutral.

## Compliance Gate

Every copy output passes through an automatic compliance gate before delivery:

- Blocks absolute prohibited terms (advertising law red lines): superlatives, absolute claims, unsubstantiated certifications.
- Blocks platform-specific prohibited words for Taobao, Pinduoduo, Douyin, Amazon, Kuaishou, and 1688.
- Health, beauty, or medical claims without official certification are blocked and marked pending review.
- Triggered words trigger full rewrite, not just a warning tag.

Full prohibited term table with platform differences: [skill/references/compliance-terms.md](skill/references/compliance-terms.md).

## Evidence Traceability

Every competitor, price, sales, review, and certification claim must include a source trail:

```text
[Source: observation path + timestamp + price basis]
```

Valid source types: public page URL with observation time, search tool result, user screenshot or export filename, authorized analytics tool name, or a clear C/D inference label. Claims without a source trail cannot be labeled A or B evidence.

## Budget And Stop-Loss

The Skill defaults to organic/low-budget strategies when no budget is provided. Every paid traffic suggestion must include a kill switch:

- Daily budget cap.
- Max CPC threshold — pause when exceeded.
- Minimum ROAS — stop when below for 3 consecutive days.
- Check frequency.
- Kill action: pause plan, swap creative, lower bid, or shut down.

The 7-day test phase (D1-D7) limits single-day spending to no more than 50% of daily budget. The 14-day scale phase (D8-D14) auto-switches to optimization-only mode when ROI stays below 1.0.

## Image And Video Policy

The open-source Skill is provider-neutral. It outputs image prompts, video storyboards, material briefs, and preflight questions, but it does not hard-code any private image or video tooling.

Before any generation route is used, the Agent should confirm:

1. Model or tool.
2. Purpose: main image, detail scene, comparison image, detail close-up, main video, short video, or storyboard only.
3. Reference images and their rights.
4. Ratio, size, count, style, and text policy.
5. Output path or delivery format.

AI-generated images and videos are creative references only, not final marketplace assets.

## Repository Layout

```text
skill/                          Skill package (installable)
  SKILL.md                       Agent-facing workflow instructions
  agents/interface.yaml          Skill UI metadata, companion skill list
  templates/user-input-form.md   Copy-ready Chinese input form
  examples/                      Invocation samples and complete example output
  references/                    Output contract, role handoff, price-band method,
                                 compliance terms, eval cases

docs/
  QUICK-START.md                 Chinese quick-start guide
  COMPANION-SKILLS.md            Companion skill detail and missing-skill behavior
  CAPABILITY-AUDIT.md            Per-feature dependency audit
  assets/                        README hero SVG, animated GIF, 1K visuals
  site/                          Standalone HTML animation with GPT Image 2 scenes
  history/                       PM iteration notes and source-article records

tests/
  TEST-CASES.md                  Trigger/output regression cases

LICENCE                         MIT license
CONTRIBUTING.md                 How to contribute without leaking private APIs
```

## Boundaries

This Skill does not:

- Publish directly to seller backends.
- Create fake reviews or buyer-show comments.
- Fabricate certifications, safety claims, medical/health claims, or test reports.
- Scrape protected or unauthorized platform data.
- Present AI-generated marketplace data as verified fact.
- Bake private provider API keys or private image/video routes into the open-source package.

## Development Notes

There is no runtime dependency for normal Skill users. The main artifact is the `skill/` directory.

Suggested checks before release:

```bash
rg -n "API_KEY|SECRET|TOKEN|Bearer|sk-" .
rg -n "legacy Taobao-only naming|old trigger phrase" .
```

Lightweight eval cases: [tests/TEST-CASES.md](tests/TEST-CASES.md) and [skill/references/trigger-output-eval.md](skill/references/trigger-output-eval.md).

Full capability audit: [docs/CAPABILITY-AUDIT.md](docs/CAPABILITY-AUDIT.md).

## License

MIT.
