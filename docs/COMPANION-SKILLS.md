# Companion Data Skills

`ai-ecommerce-workflow` is designed to discover the companion search/scrape and writing Skills automatically when the user's Agent runtime exposes them, and to attempt an auto-install when the runtime supports one.

These companion Skills are not bundled as code in this repository. They are runtime capabilities that the user's Agent environment should install or expose.

## How Resolution Works

The expected behavior is automatic, not manual:

1. Detect which companion Skills are already installed in the current Agent runtime.
2. If the runtime supports an installer such as `npx skills add` or an equivalent, attempt to install any missing companion Skill automatically.
3. Re-run the capability preflight so the final `available / missing` list is accurate.
4. If the runtime does not support auto-install, or a Skill still fails to install, fall back to a `missing-skill report` and continue the workflow with degraded evidence handling.

The Skill package itself only declares the dependency manifest in `skill/agents/interface.yaml`. The actual installer and runtime probe are owned by the host Agent runtime (for example OpenClaw, Hermes, or any other Skill-compatible Agent).

## Recommended Default Set

| Companion Skill / tool | Role in this workflow |
|---|---|
| `multi-search-engine` | Multi-engine competitor discovery and cross-checking. Useful for Chinese and international search coverage. |
| `anysearch` | Real-time web search, public source discovery, and page extraction when available. |
| `firecrawl-search` | Search public pages and optionally scrape result content. |
| `firecrawl-scrape` | Read specific public URLs as markdown/html/links/screenshot. |
| `agent-reach` | Cross-platform research: Exa, web reading, Xiaohongshu, Bilibili, Twitter, Reddit, and other content/social sources depending on local setup. |
| `humanizer-zh` | Final-pass Chinese anti-AI rewriting before delivery. Falls back to built-in humanized-copy rules when not installed. |
| Tavily or similar search APIs | Optional extra search/page-summary route when the user's environment already provides it. |

## How The Skill Uses Them

1. Auto-discover installed companion Skills before the workflow starts.
2. Attempt auto-install for any missing companion Skill if the host runtime supports it.
3. Re-run capability preflight so the available / missing list is final.
4. Use installed Skills during competitor discovery, page reading, content-platform observation, and humanized copy rewrite.
5. For each missing Skill, mark the affected module as `pending verification` and continue with the available Skills.

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

If a companion Skill is still missing after auto-install, the Agent must not stop the whole workflow. It must report the missing capability and continue with available evidence.

Example output:

```text
Data tools available this run:
- multi-search-engine: installed
- anysearch: auto-installed
- firecrawl-search: missing (auto-install not supported by this runtime)
- firecrawl-scrape: missing (auto-install not supported by this runtime)
- agent-reach: installed
- humanizer-zh: auto-installed

Impact:
- competitor discovery can proceed;
- public page verification is limited;
- price and review claims remain pending verification unless the user provides screenshots or exports.
```

When the runtime does not support auto-install, the Agent should still print a copy-ready install list so the user can install manually:

```text
npx skills add multi-search-engine
npx skills add anysearch
npx skills add firecrawl-search
npx skills add firecrawl-scrape
npx skills add agent-reach
npx skills add humanizer-zh
```

## Recommended User Inputs

For reliable price-band analysis, ask the user for at least one of:

- product links for known competitors;
- screenshots of competitor prices and SKU options;
- exported tables from seller tools;
- marketplace analytics screenshots;
- Keepa/Jungle Scout/Helium 10 exports for Amazon;
- a list of brands or stores the user already considers competitors.
