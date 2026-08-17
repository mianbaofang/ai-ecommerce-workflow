---
name: ai-ecommerce-workflow
description: Use when a user provides an ecommerce product description, public product URL, or product images and wants public-market research, observed price ranges, comparable product links, editable platform-specific listing drafts (listing copy), or optional image-generation briefs. Use public search results and user-provided materials only. Do not crawl or scrape in bulk, access login-only or protected pages, publish listings, invent product facts, or guarantee sales.
---

# AI 电商公开市场研究与素材包

## 工作边界

这个 Skill 从商品描述、公开链接或图片识别商品，研究公开同类、页面观察价格、卖点和讨论；先给带来源的一页结论，用户选平台后再生成文案、素材规格和可选生图方案。

不负责：真实成交价、销量或搜索量证明；登录态或受保护页面；批量抓取；绕过反爬、验证码或平台限制；自动发布；虚假评论、资质或功效；保证排名、转化或销售结果。

## 触发与输入

商品描述 / 名称、用户提供的公开商品链接、一张或多张产品图片，任一种即可开始。

目标平台、地区、语言、价格成本、品牌语气和图片用途均为可选项。若无法判断商品是什么，只询问一个聚焦问题；不要先要求用户填写结构化商品档案。

未提供目标平台时先做通用研究，生成文案或素材前再询问。链接不可访问时继续使用文字、图片和搜索结果，并说明影响。

## 首次搜索能力询问

首次使用时非阻塞询问是否配置额外公开搜索；本次先用现有能力。只记录选择，不自动安装，也不收集密钥。

无搜索能力时继续流程，但把竞品、价格和讨论标为“未完成公开核验”，不用常识补事实。默认只搜索；仅单页读取用户提供或最终引用的公开链接，不批量读取。

## 默认执行流程

### 1. 识别商品

整理一个内部商品摘要：品类、明显属性、使用场景、可能的同义搜索词、已知缺失信息。按 `references/product-copy-framework.md` 建立事实账本，把 `已确认`、`图片可见`、`市场观察` 和 `待确认` 分开；不把图片观察自动当成材质、性能、认证或功效证明。

### 2. 公开市场研究

扩展 3-6 组搜索词，覆盖品类词、属性词、场景词和问题词。对候选结果做去重和相似性说明，优先给出 5-8 个可打开的公开链接。

分析前读取 `references/research-evidence-ledger.md`，把搜索摘要和已读取正文规范成 Markdown 证据账本。严格区分 `仅发现`、`已读取公开正文`、`用户提供` 和 `读取失败`；只对最终引用的公开页面做单页读取，不保存整站 HTML。

每个价格说明平台、地区、币种、时间、运费 / 优惠 / SKU 口径、相似与不可比原因，并标明是页面观察价而非成交价。搜索顺序只写“指定查询下观察到的前 N 个结果”，同时记录引擎、关键词、地区和时间，不称为稳定自然排名。

### 3. 先交付一页结论

先输出页面观察价格区间、5-8 个相似链接与原因、公开卖点 / 痛点 / 机会、试探方向和最大不确定性，避免默认长报告。

### 4. 平台素材包

用户选平台后，输出 3 个标题、3-5 条卖点、描述、5 个 FAQ、关键词 / 禁用词提醒，以及图片尺寸、数量、构图和文字安全区。

写文案前读取 `references/product-copy-framework.md`，选择品类模块和平台适配层。关键字段缺失且会造成误购或合规风险时，最多追问 1-3 个问题；其他未知项从对外文案省略并放入内部待确认清单。

中国平台输出先确认当前叶子类目 / 具体商品类目；可取得官方类目必填属性时，官方属性覆盖通用分类表和 GitHub 研究数据。无法读取当前规则时使用用户已选后台类目，或标记上架前确认，不猜字段和值。

读取 `references/asset-output-contract.md` 与 `references/platform-image-specs.md` 后再给素材和生图要求。十平台规则只用两篇指定资料；未列项目不从其他平台猜补。正式上传前复核当前规则。

涉及材质、性能、认证、健康或绝对效果的文案，必须有用户资料或可引用的公开来源；没有依据时标为“待确认”，不得为了完整而猜测。

可选中文自然化不得新增事实。成稿后读取 `references/listing-compliance-review.md` 和禁词表，检查事实、风险词语义、功效 / 认证 / 价格 / 承诺、类目与平台一致性；修订后重跑。外部发布前审核只作支持平台的附加检查，不替代内置审核。

### 5. 可选生图

如果用户需要图片，先确认模型或工具、用途、参考图权利、比例、尺寸、数量、是否允许文字和交付方式。

优先使用真实产品图做裁切、扩图、去背景和场景适配；若调用生成模型，必须要求保持产品结构、颜色、Logo、包装文字和材质一致。一次性输出不同平台尺寸时，优先从同一份已确认的产品视觉源派生，不要为每个平台重新创造一个不同的产品。

没有可用生图工具时只输出素材清单和 prompt。AI 图是创意或制作参考，不自动等同于可发布的最终商品图。

## 输出契约

默认顺序：`一页结论`、`公开研究证据表`、`竞品链接与价格参考`、`机会点与风险`；用户需要时再追加`平台文案包`、`图片规格与生图交互记录`，最后列`待人工确认`。

每条外部结论带 `[来源: URL/搜索工具 + 关键词 + 时间 + 观察口径]`。来源不支持的内容只能标为推断或待核验。

旧版 15 项上架 SOP 不属于当前 Skill；当前流程只覆盖公开市场研究、平台文案草案和素材规格交接。

## 参考资料

- `references/public-search-policy.md`：公开搜索、来源口径和法律边界。
- `references/research-evidence-ledger.md`：搜索摘要、单页正文与 Markdown 证据账本格式。
- `references/asset-output-contract.md`：平台文案与图片素材包的输出要求。
- `references/platform-image-specs.md`：十平台完整生图要求、来源口径和复核项。
- `references/product-copy-framework.md`：事实账本、通用文案骨架、品类模块、十平台适配和硬校验。
- `references/listing-compliance-review.md`：自然化后的事实、违规词语义、品类和平台发布前审核。
- `references/copy-research-basis.md`：平台公开指南与 GitHub 开源实现的研究依据。
- `references/compliance-terms.md`：现有平台合规词表，按需读取。
- `evals/`、`reports/`：仅用于发布前回归，不进入用户任务。
