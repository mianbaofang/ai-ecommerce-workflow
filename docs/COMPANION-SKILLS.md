# Companion Data Skills

`ai-ecommerce-workflow` is designed to call companion search and scrape Skills automatically when the user's Agent runtime has them installed.

These companion Skills are not bundled as code in this repository. They are runtime capabilities that the user's Agent environment should install or expose.

## Recommended Default Set

| Companion Skill / tool | Role in this workflow |
|---|---|
| `multi-search-engine` | Multi-engine competitor discovery and cross-checking. Useful for Chinese and international search coverage. |
| `anysearch` | Real-time web search, public source discovery, and page extraction when available. |
| `firecrawl-search` | Search public pages and optionally scrape result content. |
| `firecrawl-scrape` | Read specific public URLs as markdown/html/links/screenshot. |
| `agent-reach` | Cross-platform research: Exa, web reading, Xiaohongshu, Bilibili, Twitter, Reddit, and other content/social sources depending on local setup. |
| Tavily or similar search APIs | Optional extra search/page-summary route when the user's environment already provides it. |

## How The Skill Uses Them

1. Discover competitor candidates with search tools.
2. Read public product pages, brand pages, review pages, and articles.
3. Collect content-platform language and user pain points.
4. Build a competitor candidate table.
5. Mark each observation with source, URL or screenshot, time, price basis, and evidence level.
6. Ask the user for authorized data exports when transaction price, coupon-after price, sales, or keyword volume matters.

## Evidence Rules

Search and scraping tools can produce:

- competitor candidate names;
- public page URLs;
- public display prices;
- visible SKU fragments;
- product titles and selling points;
- public review snippets;
- content/social discussions.

They do not prove:

- real transaction price;
- coupon-after or live-room price;
- logged-in member price;
- regional delivery price;
- seller-backend sales data;
- accurate keyword volume;
- complete review datasets.

Those require user screenshots, seller tools, third-party analytics exports, or authorized platform APIs.

## Missing Companion Skills

If a companion Skill is missing, the Agent should not stop the whole workflow. It should report the missing capability and continue with available evidence.

Example output:

```text
Data tools available this run:
- anysearch: available
- firecrawl-search: missing
- firecrawl-scrape: missing
- agent-reach: available

Impact:
- competitor discovery can proceed;
- public page verification is limited;
- price and review claims remain pending verification unless the user provides screenshots or exports.
```

## Recommended User Inputs

For reliable price-band analysis, ask the user for at least one of:

- product links for known competitors;
- screenshots of competitor prices and SKU options;
- exported tables from seller tools;
- marketplace analytics screenshots;
- Keepa/Jungle Scout/Helium 10 exports for Amazon;
- a list of brands or stores the user already considers competitors.
