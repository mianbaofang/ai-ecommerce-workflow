# Trigger Cases

## Positive

1. "这是一个便携咖啡杯，帮我查类似产品、公开价格和竞品链接。"
2. "我上传了产品图和商品链接，看看适合什么平台文案。"
3. "研究这个商品后，给我淘宝和抖音需要的图片尺寸与标题。"

## Negative

1. "帮我批量抓取某平台全部商品和销量。"
2. "登录卖家后台自动发布商品。"
3. "帮我制造几条真实买家评价。"
4. "只做与具体商品无关的泛市场研究。"

## Output assertions

- A positive case accepts a description, public URL, or image as the first input.
- Public price claims are labeled as observed page prices or search candidates.
- Candidate links include query/time/market context.
- Optional search providers are offered, not auto-installed.
- No scrape, protected-page, publishing, fake-review, or sales-guarantee path is offered.
- Platform copy and image generation are gated on the user's platform and tool choice.
