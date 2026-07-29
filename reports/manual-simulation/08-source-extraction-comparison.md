# 两篇规格文章读取工具对照

测试日期：2026-07-29（Asia/Shanghai）。目标是验证工具能否完整读取用户指定的两个公开 URL，不把“工具已安装”“工具出现在列表里”或一张局部截图当成全文读取成功。

测试 URL：

1. https://www.secaiyun.com/docs/ecommerce-product-image-size-specification-guide-2026-07-12.html
2. https://www.secaiyun.com/docs/cross-border-ecommerce-image-size-guide-2026-06-28.html

## 工具结果

| 工具 / 通道 | 国内文章 | 跨境文章 | 实际结果 | 结论 |
|---|---:|---:|---|---|
| AnySearch `extract` | 成功，5,276 字符 | 成功，6,683 字符 | 两篇均返回标题、正文、全部主要表格、平台详细章节、格式 / 压缩、工作流或避坑、FAQ 和相关链接 | 本轮唯一完成两篇全文结构化读取的外部搜索工具 |
| Tavily `extract` advanced | 失败 | 失败 | 当前会话能发现 Tavily 工具定义，但实际调用返回“工具不可供模型使用” | 未取得文章内容；不能写成已测通或比 AnySearch 更完整 |
| Agent Reach / Jina Reader | 超时 | 超时 | 按 Agent Reach 网页通道访问 `r.jina.ai/http(s)://目标URL`，两个请求均在 10 秒无正文返回 | 本轮不可用；未取得任何章节 |
| Agent Reach `doctor --json` | 未完成 | 未完成 | 命令在本环境中持续无输出，普通 `--help` 可正常返回 | CLI 存在不代表健康检查或后端可用 |
| AgentKey | 未测试 | 未测试 | Skill 文件已安装，但当前会话没有 `list_tools`、`find_tools`、`describe_tool`、`execute_tool` 四个 MCP 入口 | 未配置可执行服务，不能实测同 URL |
| Brave Search | 未测试 | 未测试 | 没有可调用的 Brave 工具、命令或已配置环境变量 | 未配置，不能声称测试过 |
| 内置浏览器 | 页面可打开 | 页面可打开 | 浏览器能打开指定 URL 并显示正确文章标题；正文读取过程中浏览器调用多次超时 | 可做人工可视核对，但本轮不作为全文字符级提取证据 |

## AnySearch 章节覆盖

### 国内文章

- 五个平台主图尺寸、比例、文件大小和格式；
- 淘宝第五张白底图、主体比例、禁止内容、放大镜和主图文字规则；
- 淘宝 / 天猫、京东、拼多多、抖音详情页宽度、高度、张数和文件上限；
- 推广图、信息流、视频封面、淘宝 / 京东店铺 Banner；
- JPG、PNG、WebP 使用场景，JPG 压缩、DPI、RGB / CMYK；
- FAQ 中的 600 x 600 px、白底图 70% 主体、加载和压缩细节；
- 快手只在主图表出现，文章没有提供快手详情页尺寸。

### 跨境文章

- Amazon、eBay、Etsy、Shopify、AliExpress 主图对比表；
- Amazon 副图分工、A+、品牌旗舰店 Banner；
- eBay 副图和 Gallery 提示；
- Etsy 正方形、4:3、Logo、场景风格和 FAQ 中的最低 500 x 500 px；
- Shopify 产品图、桌面 / 移动 Banner、Collection 和 Blog Featured；
- AliExpress 主图、副图、视频和文件上限；
- 高清母版、抠图、批量裁切、平台背景、压缩工作流；
- 七类常见错误、RGB、移动端和 FAQ 条件。

## 对仓库的修正

`references/platform-image-specs.md` 已从“尺寸速查表”扩展为完整规则表，加入：

- 国内白底图、放大镜、压缩、格式、DPI、RGB 和平台差异；
- 跨境辅助图分工、Etsy FAQ 最低值、Amazon 插画限制和五平台制作流程；
- 两篇文章的常见错误和上传前核对项。

截图只用于页面可视证明。来源是否完整，以章节映射和文字规则清单为验收依据。
