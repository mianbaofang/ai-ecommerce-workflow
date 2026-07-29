# 分类文案框架回归

测试日期：2026-07-29（Asia/Shanghai）。测试目标：证明文案由“事实账本 + 分类字段 + 平台适配”约束，而不是让 Agent 对所有产品自由发挥。

## 案例 A：通勤咖啡杯 / 淘宝

### 事实账本

| 状态 | 内容 |
|---|---|
| 已确认 | 420 ml、哑光白、翻盖、无品牌、用于通勤 / 办公 |
| 待确认 | 材质、耐温、保温、密封、杯底直径、重量、清洁方式、包装内容 |
| 分类模块 | 家居、厨房与小家电 |

### 输出草案

**标题**：420ml翻盖通勤咖啡杯 哑光白办公随行杯

**一句话定位**：一只面向上班路上和办公桌使用的 420 ml 翻盖咖啡杯，哑光白外观简洁。

**卖点**：

- 420 ml 容量，适合日常带一杯咖啡去上班；是否满足个人饮量仍取决于使用习惯。
- 翻盖结构，开合动作直观。
- 哑光白外观适合简洁的通勤和办公场景。

**规格**：容量 420 ml；颜色哑光白；杯盖为翻盖结构。

**内部复核**：补充材质、杯体尺寸、重量、耐温、清洁说明、包装内容和密封测试后，才能决定是否加入“保温、防漏、可机洗、适配杯架”等词。

### 校验

- 没有从外观推断食品级、塑料 / 不锈钢或保温结构：通过。
- 家居饮具字段识别出耐温、容量、材质、清洁和密封，而不是电子产品字段：通过。
- `待确认` 只在内部复核出现一次，没有把消费者文案写成 QA 报告：通过。

## 案例 B：USB-C 充电器 / Amazon US

公开事实源：[Anker Nano Charger (30W)](https://www.anker.com/products/a2147)，AnySearch 于 2026-07-29 读取。

### 事实账本

| 状态 | 内容 |
|---|---|
| 已确认 | 品牌 Anker；产品 Anker Nano Charger (30W)；型号 A2147；1 个 USB-C 口；最高 30W；输出档位 5V/3A、9V/3A、15V/2A、20V/1.5A；PPS 3.3-11V/3A Max、3.3-16V/2A Max；尺寸 1.12 x 1.12 x 1.39 in |
| 待确认 | 本次具体 SKU 颜色、包装内是否含线、插脚 / 地区版本、正式 Listing 的保修表述、目标站点认证字段 |
| 分类模块 | 消费电子与数码配件 |

### Output draft

**Title**: Anker Nano Charger (30W), A2147 Compact 1-Port USB-C Charger

**Bullets**:

- Delivers up to 30W through one USB-C port for compatible devices; actual charging power depends on the device, cable, and supported protocol.
- Supports fixed output profiles of 5V/3A, 9V/3A, 15V/2A, and 20V/1.5A, plus the PPS ranges listed in the product specification.
- Supports published PPS ranges of 3.3-11V/3A max and 3.3-16V/2A max.
- Measures 1.12 x 1.12 x 1.39 inches for a compact single-port setup.
- Model A2147 helps buyers check the exact charger version before ordering.

**Description**: The Anker Nano Charger (30W), model A2147, is a compact single-port USB-C charger with up to 30W output. Its published output profiles and dimensions are listed above so buyers can compare them with their device and cable requirements. Charging speed depends on the connected device, cable, protocol, and power conditions.

**Internal review**: Confirm the sellable SKU color, regional plug version, package contents, warranty wording, and marketplace certification fields before publishing.

### 校验

- 电子模块覆盖型号、端口、功率、输出档位、PPS、尺寸、兼容条件和包装：通过。
- 没有使用 `charges everything`、`universal compatibility` 或保证充电时间：通过。
- Amazon 结构与淘宝杯子结构不同，但两者使用同一证据规则：通过。
- 包装内容和地区版本没有从品牌页面猜补：通过。

## 回归结论

两个案例使用不同的分类字段和不同的平台结构；事实账本、未知项处理和逐句校验保持一致。分类框架能阻止明显的跨品类字段错配，也能让平台文案不再只是替换平台名称。

仍未完成：真实商家后台字符 / 违禁词校验和上架预览。因此这些是可审阅草案，不是“已通过平台发布”的宣传证据。
