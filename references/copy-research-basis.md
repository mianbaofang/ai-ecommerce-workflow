# 文案框架研究依据

检索日期：2026-07-29（Asia/Shanghai）。这里区分平台规则、平台教程和开源实现；教程或 GitHub 项目只用于提炼方法，不冒充平台强制规则。

## 中国平台官方类目与属性体系

这部分用于实际的中国平台类目路由和字段核对，优先级高于 GitHub 数据集、通用分类表和模型推断。公开文档不能替代登录后的商家后台，但能证明这些平台并不是只靠一张通用分类表发布商品。

| 平台与来源 | 已核实的公开能力 | 在本 Skill 中怎样用 | 当前限制 |
|---|---|---|---|
| [淘宝商品发布编辑示例](https://open.taobao.com/doc.htm?docId=108956&docType=1) | 官方文档列出 `taobao.itemcats.get`、`taobao.itemprops.get`、`taobao.itempropvalues.get`；商品挂在叶子类目，区分关键属性、普通属性和销售属性，不同类目有不同必填项。 | 淘宝 / 天猫文案先确认叶子类目，再按当前类目属性决定需要追问和填写的字段。 | 部分接口和类目需要店铺授权；正式发布仍以当前后台为准。 |
| [淘宝达尔文商品管理](https://open.taobao.com/doc.htm?docId=102155&docType=1) | 官方说明以 CSPU、SPU、SKU 和品牌 / 型号归一管理商品，并列出类目、属性、产品和规格接口。 | 用于理解为什么类目、关键属性和 SKU 不能混成一段自由文案。 | 文档较早，只作模型与流程背景，不当作当前字段清单。 |
| [拼多多商品授权类目](https://open.pinduoduo.com/application/document/api?id=pdd.goods.authorization.cats) | 官方开放平台存在授权类目、`pdd.goods.spec.get`、`pdd.goods.spec.id.get`、`pdd.goods.spu.search` 和 `pdd.goods.template.property.value.search` 等入口。 | 拼多多输出优先使用用户选定的后台类目、规格和模板属性；没有当前值时只列待确认。 | 页面为动态文档，本次只验证入口可访问；未完整抽取字段结构，不硬编码易变参数。 |
| [抖店类目属性规则查询](https://op.jinritemai.com/docs/api-docs/53/6323) | 官方 `/supplyChain/queryCatePropList` 明确用于查询类目属性规则；调用需要店铺授权。另有[类目查询入口](https://op.jinritemai.com/docs/api-docs/13/1820)。 | 抖音商品卡和文案以当前类目属性规则为字段约束，再做口播化表达。 | 未授权时只能使用公开文档与用户提供的后台类目，不能假装已读取店铺规则。 |
| [快手商品类目表](https://open.kuaishou.com/docs/develop/IndustrySolutions/introduction/productCategory.html) | 官方页面公开一至三级商品类目及 ID；[商品对接](https://open.kuaishou.com/docs/develop/IndustrySolutions/introduction/saas/productMount.html)要求 `product_specific_category`。 | 快手输出先映射具体商品类目，再组织标题、规格和直播卖点。 | 类目表和对接要求可能更新，正式提交前复核当前文档 / 后台。 |
| [京东开放平台](https://open.jd.com/) | 官方开放平台提供商品与类目相关文档入口。 | 京东文案仍按用户选择的当前后台类目和参数模板生成。 | 本次没有从动态页面核实稳定的具体接口名，因此不在 Skill 中杜撰 API 或固定字段。 |

检索记录：2026-07-29 使用 AnySearch 公开搜索核实淘宝、抖店和快手的官方正文 / 摘要；拼多多五个官方 API 链接返回 HTTP 200，但正文动态加载；京东只确认官方入口。`发现链接`、`抽取正文` 和 `获得店铺授权数据` 是三种不同状态，不能混写。

## 跨境平台与公开写作指南

| 来源 | 类型 | 采用的规则或方法 |
|---|---|---|
| [Google Merchant Center: Tips to optimize your product data](https://support.google.com/merchants/answer/7380908?hl=en) | 官方公开指南 | 标题前置重要属性；提供完整准确的产品数据；保持落地页一致；从品牌、年龄、性别、尺码、颜色等与品类有关的属性中选择。 |
| [Amazon: How to create Amazon product listings](https://sell.amazon.com/blog/amazon-product-listings) | 官方公开教程 | 商品页包含身份、描述、要点、图片、关键词和变体；信息完整帮助买家判断。 |
| [Amazon SEO guide](https://sell.amazon.com/blog/amazon-seo) | 官方公开教程 | 关键词、标题、描述、要点、后台搜索词和图片各有分工；描述应清楚说明对象、问题和利益。 |
| [eBay Listing best practices](https://www.ebay.com/sellercenter/listings/create-listings/best-practices) | 官方卖家中心 | 准确标题、Item specifics、物品状态、清晰描述和图片共同构成可发现且可判断的 Listing。 |
| [eBay Item specifics](https://www.ebay.com/sellercenter/listings/item-specifics) | 官方卖家中心 | 分类属性不应全部塞进正文或标题，应进入结构化 Item specifics。 |
| [Etsy: The Anatomy of a Well-Crafted Etsy Listing](https://www.etsy.com/seller-handbook/article/1347574487014) | 官方卖家手册 | 标题、图片、描述、属性和标签共同服务于理解与搜索；描述需覆盖买家关心的材料、尺寸和制作信息。 |
| [Etsy: New Guidance for Listing Titles](https://www.etsy.com/seller-handbook/article/1399426136697) | 官方卖家手册 | 标题以清晰、易读、准确说明商品为先，不把标签列表堆成标题。 |
| [Shopify: How to Write a Product Description That Sells](https://www.shopify.com/blog/8211159-9-simple-ways-to-write-product-descriptions-that-sell) | 平台公开教程 | 面向具体买家，把功能连接到实际利益，回答异议，保持品牌语气、可扫描和独立页面文案。 |
| [淘宝官方学习中心：商品发布规范变更](https://daxue.taobao.com/information/detail.jhtml?id=577) | 官方规则入口 | 正式上架以当前发布后台和规则中心为准。检索到的发布规范强调标题、属性、图片和详情真实、一致、完整。 |

## 中文 GitHub 与开放数据

这些项目适合做中文商品识别、候选类目预测或字段提问提示，**不代表任何平台的当前上架类目**。

| 项目 | 已核实内容 | 可以复用 | 不得当成 |
|---|---|---|---|
| [ChenDelong1999/MEP-3M](https://github.com/ChenDelong1999/MEP-3M) | MIT；超过 300 万条中国电商商品，简体中文图文对，14 个一级类、599 个细分类和层级标签。 | 图片 / 标题的中文粗分类、同义词与类目候选研究。 | 淘宝、京东或其他平台的当前叶子类目和必填属性。 |
| [OpenBGBenchmark/OpenBG](https://github.com/OpenBGBenchmark/OpenBG) | 中文开放商业知识图谱基准，包含多模态电商实体、关系与商品数据。 | 发现商品实体关系、属性关系和研究型 schema。 | 商家后台字段、商品事实或现行平台规则。 |
| [jingpeicomp/product-category-predict](https://github.com/jingpeicomp/product-category-predict) | 中文商品名三级分类示例，仓库说明含 962 个三级类目和 `category.json`；最后活跃较早且未检测到许可证。 | 理解“先预测候选类目，再人工 / 平台规则确认”的实现思路。 | 可直接分发的依赖、2026 平台分类或自动上架依据。 |
| [xiaozhou-alt/Products_Name_Classification](https://github.com/xiaozhou-alt/Products_Name_Classification) | 中文商品名称 BERT / RoBERTa 一级、二级分类示例；项目较小且 GitHub API 未检测到许可证。 | 研究多级中文文本分类和错误样本分析。 | 生产规则、官方类目或无需复核的分类器。 |
| [阿里天池：Goods and its Category data from Alibaba](https://tianchi.aliyun.com/dataset/55) | 可确认数据集标题与阿里商品分类主题。 | 作为进一步数据研究入口。 | 未核实字段、许可和更新频率前的直接生产输入。 |

## 国际 GitHub 与开放分类

| 项目 | 可复用做法 | 不直接照搬的部分 |
|---|---|---|
| [Shopify/product-taxonomy](https://github.com/Shopify/product-taxonomy) | 用公开类别、属性和属性值帮助决定“该品类应该追问什么”，而不是给所有商品同一张表。 | 分类属性不是商品事实；没有输入值时不得自动补值。 |
| [google-marketing-solutions/feedgen](https://github.com/google-marketing-solutions/feedgen) | 把标题、描述、属性补全和输出验证拆开；以产品 Feed 为事实输入。 | 项目声明并非 Google 官方产品；其模型、云基础设施和批量工作流不是本 Skill 的依赖。 |
| [google-marketing-solutions/description_genius](https://github.com/google-marketing-solutions/description_genius) | 从产品特征、说明书、评论等明确来源生成，并用示例约束输出格式。 | 评论只能用来发现问题或在获授权时作为引用，不能生成虚假评价或把评论内容写成产品规格。 |
| [Nutlope/description-generator](https://github.com/Nutlope/description-generator) | 图片可以作为低摩擦入口，适合先生成候选标题、描述和标签。 | 图片识别不能证明容量、材质、性能、认证、兼容或精确尺寸。 |

## 明确排除的来源

- 不采用 [wkunzhi/TaoBaoAttributeSpider](https://github.com/wkunzhi/TaoBaoAttributeSpider) 等旧爬虫仓库：项目久未更新、未检测到许可证，而且采集方式与本 Skill 的公开搜索、无批量抓取和不绕过平台限制的边界冲突。
- 不把搜索结果里的第三方类目转载表当作官方字段；最多用于发现待核实的类目名称。

## 综合结论

公开资料的共同点不是某个万能文案公式，而是四个可执行约束：

1. **事实先于语气**：产品字段、来源和未知项先固定，营销表达随后生成。
2. **分类决定字段**：服装看尺码和面料，电子看型号、协议和兼容，食品看成分、过敏原和日期；中国平台输出还要优先遵守当前叶子类目和官方必填属性。
3. **平台决定版式**：Amazon 的要点、eBay 的 Item specifics、Etsy 的材料 / 制作信息、Shopify 的品牌页面承担不同任务。
4. **生成必须有校验**：检查事实落地、长度、禁用声明、跨字段一致性和人工复核，而不是把模型输出直接当成可发布内容。

因此本仓库使用 `product-copy-framework.md` 的“事实账本 + 通用骨架 + 品类模块 + 平台适配 + 硬校验”，不让 Agent 完全自由发挥。
