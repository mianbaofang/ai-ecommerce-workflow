# AI Ecommerce Workflow Skill

<p align="center">
  <img src="docs/assets/hero.svg" alt="AI Ecommerce Workflow Skill hero" width="100%">
</p>

## Why This Skill Exists

Launching a new product in ecommerce is rarely one writing task. A usable launch package needs positioning, competitor price bands, review-mined pain points, main image logic, detail page structure, SEO titles, FAQ, customer-service scripts, and a launch plan that fits budget and inventory.

This Skill turns that work into one structured Agent workflow. It is designed for operators who want an AI assistant to prepare the material before publishing, while still keeping marketplace data, compliance claims, and final business decisions under human review.

<p align="center">
  <a href="docs/site/project-intro-animation.html">
    <img src="docs/assets/intro-animation-preview.gif" alt="AI Ecommerce Workflow HTML intro preview" width="100%">
  </a>
</p>

<p align="center">
  <a href="README.zh-CN.md">中文 README</a>
  ·
  <a href="skill/">Skill</a>
  ·
  <a href="skill/templates/user-input-form.md">Input form</a>
  ·
  <a href="skill/examples/commute-backpack.md">Example output</a>
  ·
  <a href="docs/QUICK-START.md">Quick start</a>
  ·
  <a href="docs/COMPANION-SKILLS.md">Companion skills</a>
  ·
  <a href="skill/references/compliance-terms.md">Compliance terms</a>
  ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

`ai-ecommerce-workflow` is an Agent Skill for preparing ecommerce new-product launch packages across marketplaces such as Taobao, Pinduoduo, Douyin, Amazon, 1688, and similar channels.

It does not publish products to seller backends, create fake reviews, scrape without authorization, or guarantee marketplace performance. It prepares a reviewable operating package.

## What It Produces

A complete run produces 15 structured outputs plus role handoff packages:

| Layer | Output |
|---|---|
| Strategy | Product positioning, target users, core selling points, user pain points |
| Market | Competitor price-band analysis, differentiation opportunities |
| Visual | Main image planning, detail page structure, design brief |
| Traffic | Platform-specific titles, 20-title test pool, keyword layers |
| Customer service | Review insights, FAQ, customer-service scripts |
| Operations | 7-day test, 14-day scale-up, and 30-day stabilization plan |
| Delivery | Operations, design, customer service, boss approval, and material-generation packs |

Every key conclusion should carry an evidence level:

| Level | Meaning |
|---|---|
| A | User-provided fact, screenshot, export, or source document |
| B | Authorized tool export or publicly verifiable page observation |
| C | Industry/common-sense inference |
| D | Strong assumption that needs review |

## Competitor Data Sources

The workflow is designed to auto-call companion search and scrape Skills when they are installed in the user's Agent environment. These tools discover competitor candidates, read public pages, and collect content-platform signals before the Skill writes the competitor price-band analysis.

Recommended companion data Skills:

| Companion Skill / tool | Auto-used for | Not enough for |
|---|---|---|
| `multi-search-engine` | Multi-engine competitor discovery and cross-checking | Real transaction price or logged-in seller data |
| `anysearch` | Broad web search, competitor discovery, public source lookup | Real transaction price or logged-in seller data |
| `firecrawl-search` | Finding public product pages, reviews, articles, brand pages | Coupon-after price, app-only price, seller backend data |
| `firecrawl-scrape` | Reading a specific public URL as markdown/html/screenshot | Full SKU pricing when hidden behind login, popups, or anti-bot controls |
| `agent-reach` | Cross-platform search and social/content observation such as Xiaohongshu, Bilibili, Reddit, Twitter | Ecommerce backend prices, sales, or commercial analytics |
| Tavily or similar search APIs | Search and page summaries when available in the user's environment | Authorized marketplace data |
| User exports/screenshots | Seller tools, third-party analytics, price screenshots, review exports | Must still record source, time, and pricing basis |

If a companion Skill is missing, the Agent should say which one is missing, continue with the available tools, and mark affected price, sales, and review claims as pending verification. Search and scrape tools can help discover competitors and observe public page prices. They must not be described as real transaction prices unless the user provides authorized data or a reliable export.

## Capability Matrix

| Category | Feature | Dependency | Status |
|---|---|---|---|
| Core workflow | Input validation, run modes, output contract | None | Built-in ✅ |
| Core workflow | 15 launch modules | None | Built-in ✅ |
| Marketing | Competitor price-band analysis | Any companion search/scrape tool | Needs skill ⚠️ |
| Copy | Humanized copy checks | None (built-in rules) | Built-in ✅ |
| Copy | Enhanced anti-AI writing | humanizer-zh skill | Needs skill ⚠️ |
| Images | Prompt briefs and preflight | None | Built-in ✅ |
| Images | Actual image generation | User-provided model/tool | User provides 🔧 |
| Video | Storyboards and prompt briefs | None | Built-in ✅ |
| Video | Actual video generation | User-provided tool | User provides 🔧 |
| Data | Competitor discovery + page reading | companion search/scrape skills | Needs skill ⚠️ |
| Data | Sales/price from seller tools | User screenshots or authorized exports | User provides 🔧 |

## Quick Start

Most users do not need to run commands. Give this Skill path to your Skill-compatible Agent:

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

The Agent should validate required fields before running:

1. Product name plus one-line description.
2. Product category.
3. Target platform or platforms.

Optional but useful fields include product photos, price/cost, launch budget, inventory, fulfillment capacity, known competitors, desired copy tone, and whether image/video prompt briefs are needed.

## Run Modes

| Mode | Use when | Output scope |
|---|---|---|
| Quick diagnosis | You only want to know whether the product is worth testing | Positioning, users, pain points, competitor band, opportunity summary |
| Complete launch | You need the full pre-listing package | All 15 outputs plus role handoffs |
| Material production | Direction is set and you need image/detail/title briefs | Selling points, main images, detail page, titles, design brief, optional image/video prompts |
| Post-launch optimization | Product is already listed but data is weak | Competitor review, title/keyword, reviews, FAQ, customer service, optimization plan |

## Image And Video Policy

The open-source Skill is provider-neutral. It can produce image prompts, video storyboards, material briefs, and preflight questions, but it does not hard-code private image or video tooling.

Before any generation route is used, the Agent should confirm:

1. Model or tool.
2. Purpose: main image, detail scene, comparison image, detail close-up, main video, short video, or storyboard only.
3. Reference images and their rights.
4. Ratio, size, count, style, and text policy.
5. Output path or delivery format.

Generated images and videos are creative references. Real marketplace assets still need product truth, authorization, and platform compliance review.

## Compliance Gate

Every copy output passes through an automatic compliance gate before delivery. This gate:

- Blocks absolute prohibited terms (广告法红线): superlatives, absolute claims, unsubstantiated certifications, fake authority.
- Block platform-specific prohibitions for Taobao, Pinduoduo, Douyin, Amazon, Kuaishou, and 1688.
- Detected terms trigger a full rewrite — they are not output with a warning tag.
- Health/beauty/medical claims without official certification are blocked and marked pending review.

Full prohibited term table with platform rules: [skill/references/compliance-terms.md](skill/references/compliance-terms.md).

## Evidence Traceability

Every competitor, price, sales, review, and certification claim must include a source trail:

```text
[Source: observation path + timestamp + price basis]
```

Valid source types: public page URL with observation time, search tool result, user screenshot/export, authorized analytics tool name, or a clear C/D inference label. Claims without a source trail cannot be labeled A or B evidence.

## Budget And Stop-Loss Rules

The Skill defaults to organic/low-budget strategies when no advertising budget is provided. Every paid traffic suggestion must include a kill switch:

- Daily budget cap.
- Max CPC threshold — pause when exceeded.
- Minimum ROAS — stop when below for 3 consecutive days.
- Check frequency.
- Kill action: pause plan, swap creative, lower bid, or shut down.

The 7-day test phase (D1-D7) prohibits spending more than 50% of daily budget on any single day. The 14-day scale phase (D8-D14) auto-switches to optimization-only mode when ROI stays below 1.0.

## Repository Layout

```text
skill/
  SKILL.md                         Agent-facing workflow instructions
  agents/interface.yaml            Skill UI metadata
  templates/user-input-form.md     Copy-ready input form
  examples/                        Invocation samples and complete example output
  references/                      Output contract, role handoff, price-band method, eval cases

docs/
  QUICK-START.md                   Chinese quick start
  assets/                          README hero and GIF preview
  site/                            HTML animation source
  history/                         PM iteration notes and source-article integration notes

tests/
  TEST-CASES.md                    Lightweight trigger/output regression cases
```

## Boundaries

This Skill should not:

- publish directly to seller backends;
- create fake reviews or buyer-show comments;
- fabricate certifications, safety claims, medical/health claims, or test reports;
- scrape protected or unauthorized platform data;
- present AI-generated marketplace data as verified fact;
- bake private provider API keys or private image/video routes into the open-source package.

## Development Notes

There is no runtime dependency for normal Skill users. The main artifact is the `skill/` directory.

Suggested checks before release:

```bash
rg -n "API_KEY|SECRET|TOKEN|Bearer|sk-" .
rg -n "legacy Taobao-only naming|old trigger phrase" .
```

The lightweight eval cases are in `tests/TEST-CASES.md` and `skill/references/trigger-output-eval.md`.

## License

MIT.
