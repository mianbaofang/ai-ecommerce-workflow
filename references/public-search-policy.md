# Public Search Policy

## Allowed default evidence

- Search-engine result pages and snippets.
- Public pages returned by a search query when the host can read them through an approved, ordinary browsing path.
- Public URLs explicitly supplied by the user.
- Public forum, review, and social discussion pages that do not require login or a bypass.

## Not a default capability

- Bulk crawling or scraping.
- Firecrawl or equivalent scrape/search adapters.
- Login-only, app-only, cookie-gated, CAPTCHA-gated, or protected pages.
- Proxy rotation, anti-bot bypass, catalog mirroring, or automated pagination.
- Claims about sales, transaction price, coupon-after price, search volume, or ranking without authorized evidence.

## Source labels

Use one of these labels in the output:

- `公开页面观察价`: visible price on a public page; not a transaction price.
- `搜索结果候选`: discovered by search; requires manual page confirmation.
- `用户提供资料`: user supplied link, screenshot, export, image, or document.
- `经验推断`: model or category inference; not execution-ready.
- `待核验`: evidence is missing or conflicting.

Every price or competitor claim records the source URL or tool, query, marketplace, region, currency, observation time, and price basis.

## Optional provider setup

At first use, ask whether the user wants to configure `anysearch`, `multi-search-engine`, `Tavily`, `Brave Search`, `agent-reach`, or a host-provided `agentkey` route. This is an opt-in question only. Do not auto-install, collect keys in chat, or treat any provider as required.
