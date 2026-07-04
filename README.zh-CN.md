# AI 电商新品上架工作流

<p align="center">
  <a href="https://mianbaofang.github.io/ai-ecommerce-workflow/docs/site/project-intro-animation-zh.html">
    <img src="docs/assets/intro-animation-preview-zh.gif" alt="35 秒项目介绍动画中文版，含 GPT Image 2 生成的视觉" width="100%">
  </a>
</p>

<p align="center">
  <a href="README.md">English</a>
  ·
  <a href="skill/">Skill</a>
  ·
  <a href="skill/templates/user-input-form.md">调用表单</a>
  ·
  <a href="skill/examples/commute-backpack.md">完整示例</a>
  ·
  <a href="docs/COMPANION-SKILLS.md">配套数据 Skill</a>
  ·
  <a href="skill/references/compliance-terms.md">合规禁词表</a>
  ·
  <a href="SECURITY_AUDIT.md">安全审计</a>
  ·
  <a href="CHANGELOG.md">更新日志</a>
</p>

## 为什么做这个 Skill

一份真正能交给团队执行的上架资料包，通常不是一两段文案能写完的事。它包括产品定位、竞品价格带、评论里挖出的痛点、主图逻辑、按用户决策顺序排的详情页、平台 SEO 标题、FAQ、客服话术，以及一份预算和库存能承受的 30 天运营计划。

我之前见到的写法，要么是罗列十几条通用结论、数据全部估的；要么是看起来很专业，但价格是常识编的、绝对化表达一写就是几条，真到平台去交售后会被原路退回。这些问题的根源不是 Skill 不够长，而是没有强制每条结论留证据、没有强制做合规拦截、没有按预算适配投放。

所以这个 Skill 把上面这些工作整理成 Agent 可执行的一条流程。它先验证输入、调起搜索和抓取 companion skills、对每条结论标证据等级和来源迹、输出文案前过合规拦截门、没钱时不擅自排付费计划，最后按角色把交付包拆给运营、设计、客服、决策。Skill 不替你发商品、不写假评论、不裸抓数据，也不把常识包装成事实。

一个用于电商新品上架准备的 Agent Skill，覆盖淘宝、拼多多、抖音、亚马逊、1688、快手等渠道。适配 OpenClaw、Hermes、Codex 或任何支持 Skill 的 Agent 环境。

## 快速使用

普通用户不需要安装代码。把下面 Skill 路径发给支持 Skill 的 Agent：

```text
https://github.com/mianbaofang/ai-ecommerce-workflow/tree/main/skill
```

然后说：

```text
请安装这个 Skill，然后帮我跑一个电商新品完整上架流程。
```

中文调用模板：

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

开始前 Agent 必须验证 3 个必填项：

1. 产品名称 + 一句话描述。
2. 产品类目。
3. 目标平台。

其他字段都是选填，但会影响精度：产品图、售价与成本、测款预算、首批库存、发货能力、已知竞品、文案口吻、生图/视频需求。

## 运行模式

| 模式 | 适合场景 | 输出范围 |
|---|---|---|
| 快速诊断 | 只想先判断这个品值不值得做 | 定位、用户、痛点、竞品、机会摘要 |
| 完整上架 | 从零准备上架资料包 | 全 15 项 + 角色分工 |
| 素材制作 | 方向已定，只要主图/详情页/标题/素材 prompt | 卖点、主图、详情页、标题、设计 Brief、可选生图/视频 prompt |
| 上架后优化 | 已经上架，但点击或转化不好 | 竞品复盘、标题关键词、评论洞察、客服与优化计划 |

## 能力矩阵

| 分类 | 功能 | 依赖 | 状态 |
|---|---|---|---|
| 核心流程 | 输入验证、运行模式、输出合同 | 无 | ✅ 内置可执行 |
| 核心流程 | 15 项上架模块 | 无 | ✅ 内置可执行 |
| 市场层 | 竞品价格带分析 | 任一 companion search/scrape tool | ⚠️ 需 Skill |
| 文案 | 去AI味质检 | 无（内置规则） | ✅ 内置可执行 |
| 文案 | 增强去AI味 | `humanizer-zh` skill | ⚠️ 需 Skill |
| 合规 | 自动拦截平台禁词 | 内置禁词表 | ✅ 内置可执行 |
| 来源 | 来源迹追溯 | 手动 URL/时间标签 | ✅ 内置可执行 |
| 流量 | 30天计划 + 止损 | 内置预算规则 | ✅ 内置可执行 |
| 生图 | Prompt 建议和 preflight | 无 | ✅ 内置可执行 |
| 生图 | 实际生成图片 | 用户指定模型/工具 | 🔧 需用户提供 |
| 视频 | 分镜和 prompt 建议 | 无 | ✅ 内置可执行 |
| 视频 | 实际生成视频 | 用户指定视频工具 | 🔧 需用户提供 |
| 数据 | 成交价/销量 | 用户截图或授权工具导出 | 🔧 需用户提供 |

默认行为：没有 companion 搜索工具时仍可运行，但价格和评论统一标注【待核验】。没给预算时，30 天计划默认只给免费/低预算动作。

## 配套 Skill

这套工作流在用户 Agent 环境里已经安装对应 companion skills 时，会自动调用。每一个 Skill 通常由支持 Skill 的 Agent 环境提供，可在需要时按需安装。

### 数据发现和抓取

| Companion Skill | 作用 | 在竞品分析中的调用样例 |
|---|---|---|
| `multi-search-engine` | 多引擎搜索（百度、Bing CN、搜狗、Google 等），用于找到候选竞品 URL，返回结构化的商品页、测评页、品牌页列表 | `搜索 "{品名} {类目} 测评"`，跨引擎返回候选 |
| `anysearch` | 实时全网搜索 + 垂直域子域探测 + 页面抽取。适合英文资料和近期内容 | 获取商品页和带观察时间的评论 |
| `firecrawl-search` | 搜索公开商品页，并支持附带回显抓取 | `搜索 "{品牌} {型号} 实拍"`，得到页面列表 |
| `firecrawl-scrape` | 把指定 URL 读成 markdown / html / links / screenshot。最适合已知候选 URL | 抽取标题、公开展示价、SKU 可见信息、评论摘要 |
| `agent-reach` | 跨平台研究：Exa 搜索、网页阅读、小红书/B站/Reddit/Twitter 讨论、抖音/快手/X 等内容平台 | 找用户真实痛点、原生表达、种草内容 |
| `Tavily` | 当 Agent 环境已提供时的可选搜索 API | 补充搜索 + 交叉验证 |

这些 Skill 帮助工作流发现候选竞品和读取公开页面观察值。**没有**一个能证明实际成交价、券后价、登录态后台数据。任何需要真实成交数据的需求，仍然要靠用户截图、卖家工具导出或授权 API。

### 去AI味

| Companion Skill | 作用 |
|---|---|
| `humanizer-zh` | 公开的中文去AI味 Skill。最终改写一轮，删除「此外 / 值得注意的是 / 综上所述」等填充短语，拆掉「不仅...更是...」这类模板结构，把「高级感 / 品质感」换成具体细节，并打散节奏让结果读起来像真人写的 |

未安装 `humanizer-zh` 时，工作流仍然跑，只用内置的 5 条人味化规则（见 [SKILL.md](skill/SKILL.md)）。

### 自动安装行为

当 Skill 在支持安装 Skill 的 Agent 运行环境（如 OpenClaw、Hermes 等）中被调用时，Agent 应：

1. 先检查当前运行环境里哪些 companion Skills 已经安装；
2. 若运行环境支持 `npx skills add` 或等价安装命令，对缺失的 companion Skills 尝试自动安装；
3. 若运行环境不支持自动安装，回退到列出缺失项 + 给出可复制的安装命令。

安装后重新跑一遍能力预检，再进入 15 项输出。如果安装失败，对应模块标注【待核验】，工作流继续按当前可用能力跑。

### Provider 中立的生图和视频

开源版不捆绑任何生图或视频生成 API。`SKILL.md` 里生图 / 视频的执行门要求用户先选好模型或工具，再做实际生成。Skill 产出可直接使用的 prompt；模型由用户挑选。

### API key

开源版不捆绑任何 API key。`anysearch`、`firecrawl`、`Tavily`、生图、视频和其它需要鉴权的集成，key 都留在环境变量。开源仓库保持 provider-neutral。

## 合规拦截门

所有文案输出前必须过合规自动检测。拦截规则包括：

- 广告法红线词：最、第一、顶级、100%、纯天然、零添加、永不、永久、国家级、世界级、全网、全国、全球 等极限词和绝对词——检测到直接退回改写，不配警告标签。
- 平台特定禁词：淘宝、拼多多、抖音、亚马逊、快手、1688 各有不同的标题和描述规则，输出时按目标平台自动匹配。
- 功效/认证/安全类宣称，没有官方资质文件时标注【人工复核】、不允许直接输出。
- 完整规则表和平台差异：[skill/references/compliance-terms.md](skill/references/compliance-terms.md)。

## 来源迹追溯

每条涉及竞品、价格、销量、评论、认证、材质来源的结论，必须附带来源迹：

```text
[来源: 观察路径 + 时间 + 口径]
```

有效来源包括：公开 URL 和观察时间、工具搜索记录、用户截图或导出文件名、授权工具名称、或明确的 C/D 推断标注。没有来源迹的结论不得进入 B 级以上证据。

## 预算与止损

未提供预算时默认只输出免费/低预算方案（≤100 元/天）。任何付费投流建议必须附带 Kill Switch：

- 日预算上限。
- 单次点击成本上限（CPC），超过暂停。
- 投产比下限（ROI），连续 3 天未达标关停。
- 检查周期。
- 停止动作：暂停计划、换素材、降价、关停。

测款期（D1-D7）禁止单日消耗超过预算 50%。起量期（D8-D14）如果 ROI 持续低于 1.0，自动转入只优化不消耗模式。

## 生图与视频原则

开源版不绑定任何私有生图或视频工具。Skill 只定义素材生成前必须确认的信息、prompt 结构和质量检查标准。

进入生图或视频分支前，Agent 必须确认：

1. 使用哪个模型/工具。
2. 用途：主图、详情页场景图、对比图、细节图、主图视频、短视频、分镜。
3. 参考图与授权来源。
4. 比例、尺寸、张数、风格、是否允许文字。
5. 输出路径或交付方式。

AI 图和 AI 视频只作为创意参考，真实上架素材仍然需要实拍、授权和平台合规复核。

## 仓库结构

```text
skill/                          Skill 包（可安装）
  SKILL.md                       Agent 流程主入口
  agents/interface.yaml          Skill 元数据、配套 Skill 列表
  templates/user-input-form.md   可复制的中文调用表单
  examples/                      调用样例和完整输出示例
  references/                    输出合同、角色分工、价格带方法、
                                 合规禁词表、触发评测

docs/
  QUICK-START.md                 中文快速上手
  COMPANION-SKILLS.md            配套 Skill 说明和缺失降级
  CAPABILITY-AUDIT.md            每个功能模块的可执行性审计
  assets/                        README 封面 SVG、动画 GIF、1K 视觉图
  site/                          单文件 HTML 动画（带 GPT Image 2 场景）
  history/                       PM 迭代记录和文章方法论融合记录

tests/
  TEST-CASES.md                  触发与输出回归用例

LICENCE                         MIT 许可证
CONTRIBUTING.md                 贡献指南（防泄漏私有 API）
```

## 边界

这个 Skill 不做以下事情：

- 直接登录平台后台发布商品；
- 生成假评论、买家秀或刷单话术；
- 编造认证、检测报告、功效、安全承诺；
- 未授权抓取受保护平台数据；
- 把 AI 推断出来的市场数据写成已核验事实；
- 把私有 API key 或私有生图/视频路线写进开源仓库。

## 开发者说明

普通使用不需要安装依赖。核心交付物是 `skill/` 目录。

发布前建议跑两类检查：

```bash
rg -n "API_KEY|SECRET|TOKEN|Bearer|sk-" .
rg -n "legacy Taobao-only naming|old trigger phrase" .
```

轻量评测用例：[tests/TEST-CASES.md](tests/TEST-CASES.md) 和 [skill/references/trigger-output-eval.md](skill/references/trigger-output-eval.md)。

完整的能力审计：[docs/CAPABILITY-AUDIT.md](docs/CAPABILITY-AUDIT.md)。

安全审计：[SECURITY_AUDIT.md](SECURITY_AUDIT.md) — 确认仓库没有泄露任何私有 API key 或工具缓存。

## License

MIT.
