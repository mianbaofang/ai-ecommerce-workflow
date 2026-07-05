# AI Ecommerce Workflow

<p align="center">
  <a href="https://mianbaofang.github.io/ai-ecommerce-workflow/docs/site/project-intro-animation.html">
    <img src="docs/assets/intro-animation-preview.gif" alt="35-second project introduction with GPT Image 2 generated visuals" width="100%">
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
  <a href="docs/COMPANION-SKILLS.md">Companion skills</a>
  ·
  <a href="skill/references/compliance-terms.md">Compliance terms</a>
  ·
  <a href="SECURITY_AUDIT.md">Security audit</a>
  ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

## Why This Skill Exists

A usable ecommerce launch package is rarely one writing task. It needs positioning, competitor price bands, review-mined pain points, main image logic, a detail page in the user's actual decision order, SEO titles, FAQ, customer-service scripts, and a launch plan that respects budget and inventory.

I built this Skill because watching a real team prepare a new product still takes several days and three people. Operators draft a brief, designers ask the same twenty questions, and service checks the listing too late. There is also a more annoying problem: the AI draft usually looks confident, but the numbers inside are guessed and the absolute statements would not survive a marketplace review.

This Skill turns that work into one structured Agent workflow. It validates the input, calls companion search and scrape tools, labels every claim with an evidence level and a source trail, blocks prohibited marketplace terms before any copy goes out, refuses to invent a closed loop when the user cannot afford paid traffic, and packages the answer by who needs to act next. Operators, designers, service and decision makers each get a focused packet instead of one long report.

It does not publish products to seller backends, write fake reviews, scrape without authorization, or guarantee marketplace performance. It prepares a reviewable operating package and stays honest about what data is real, what is observed, and what is only inferred.

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

The Skill is designed to **auto-discover** companion data and writing Skills when invoked in an Agent runtime, and to **attempt auto-install** when the runtime supports one. Each Skill either ships with the Skill-compatible Agent or is installed on demand. This behavior is automatic, not a manual step.

### Auto-install behavior

1. Detect which of the companion Skills listed below are already installed in the current runtime.
2. If the runtime supports `npx skills add` or the equivalent installation command, attempt to install missing companion Skills automatically.
3. Re-run the capability preflight so the final `available / missing` list is accurate.
4. If the runtime does not support auto-install, fall back to listing missing companion Skills with copy-ready install commands.
5. After install (or after the missing-list fallback), the Agent proceeds with the 15 outputs. If a Skill still fails to install, the affected modules are marked pending verification and the workflow continues with whatever is available.

The Skill package itself only declares the dependency manifest in `skill/agents/interface.yaml`. The actual installer and runtime probe are owned by the host Agent runtime.

### Data discovery and scraping

| Companion Skill | Role | Example call (during competitor analysis) |
|---|---|---|
| `multi-search-engine` | Multi-engine search (Baidu, Bing CN, Sogou, Google, etc.) for candidate competitor URLs. Returns a structured list of product, review, and brand pages. | `搜索 "{品名} {类目} 测评"`, get candidate URLs across engines |
| `anysearch` | Real-time web search with vertical-domain sub-domain discovery and page extraction. Useful for English sources and recent content. | Get product pages and reviews with observed timestamps |
| `firecrawl-search` | Search public product pages and optionally scrape full content. | `搜索 "{品牌} {型号} 实拍"`, get page list |
| `firecrawl-scrape` | Read a specific URL as markdown / html / links / screenshot. Best for known candidate URLs. | Extract title, public display price, SKU visible info, review snippets |
| `agent-reach` | Cross-platform research: Exa search, web reading, Xiaohongshu / Bilibili / Reddit / Twitter discussions, and content-platform observation. | Find real user pain points, organic language, viral content |
| `Tavily` | Optional search API when the Agent runtime already provides it. | Secondary search, cross-verification |

These Skills help the workflow find competitor candidates and observe public page prices. None of them prove actual transaction prices, coupon-after prices, or logged-in seller data. Anything that needs real transaction data still requires user screenshots, seller-tool exports, or authorized APIs.

### Humanization

| Companion Skill | Role |
|---|---|
| `humanizer-zh` | Public open-source anti-AI-writing Skill focused on Chinese. Produces a final rewrite pass on the 15 outputs to remove filler phrases like 「此外 / 值得注意的是 / 综上所述」, breaks formulaic structures like 「不仅...更是...」, replaces empty claims like 「高级感 / 品质感」 with concrete details, and varies rhythm so the result reads like a real person wrote it. |

If `humanizer-zh` is not installed or cannot be auto-installed, the workflow still runs but uses the built-in humanized copy rules instead. The five built-in core principles are documented in [SKILL.md](skill/SKILL.md).

### Provider-neutral image and video

The Skill does not bundle any image-generation or video-generation API. The execution gate for `image prompt` (`skill/SKILL.md`) requires the user to choose a model or tool before any generation runs. The Skill produces ready-to-use prompts; the user picks the model.

### API keys

The Skill does not bundle any API keys. Private provider keys for `anysearch`, `firecrawl`, `Tavily`, image tools, video tools, and any other integration stay in environment variables. The open-source repo stays provider-neutral.

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

Security audit: [SECURITY_AUDIT.md](SECURITY_AUDIT.md) — confirms no private API keys or caches are tracked.

## Author

Ethan <ethan.zl@hotmail.com>

## License

MIT.
