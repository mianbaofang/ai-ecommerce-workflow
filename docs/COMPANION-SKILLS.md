# Optional Companion Capabilities

The canonical Skill has no required companion Skill. It uses host capabilities when available and offers optional public search, selected-page Markdown extraction, Chinese humanization, and user-selected image generation without auto-installing any of them.

## Default behavior

1. Accept a product description, public product URL, or product images.
2. Use the host's public search or an already configured public search provider.
3. Normalize results into the Markdown evidence ledger before analysis.
4. Return candidate links and visible page observations with query, time, market, and price basis.
5. Continue without an external provider, but mark competitor and price evidence as `待核验` when public search cannot be run.

The Skill does not auto-install providers. It does not ask users to paste API keys into chat.

## Public search options

| Tool | User choice | Intended use | Boundary |
|---|---|---|---|
| Host public search | Default | Basic web and marketplace discovery | Depends on the host's visible search capability |
| `anysearch` | Optional | Public web search and recent source discovery | Use search mode; do not batch-extract pages |
| `multi-search-engine` | Optional | Public multi-engine candidate discovery | Search results only |
| `Tavily` | Optional | Search and cross-checking | User configures the provider in the host |
| `Brave Search` | Optional | Independent public web search | User configures the provider in the host |
| `agent-reach` | Optional | Public web and social discussion discovery | Follow the provider and platform terms |
| `agentkey` | Optional | Only a host-provided public-search route, if available | The Skill does not define or store its credentials |

## Selected-page Markdown extraction

Search results and page bodies have separate evidence states. AnySearch output that is already Markdown should be normalized directly. For a user-provided or selected public HTML page, the host may use an already installed converter:

| Tool | Intended use | Boundary |
|---|---|---|
| `huashu-md-html` | Convert one local HTML file or selected public URL to Markdown | Optional; do not package or auto-install it |
| `autocli read` | Extract the readable body of one public URL as Markdown | Optional; no pagination or catalog collection |
| Host page reader | Read an ordinary public page | Record whether the page was actually read |

If none is available, retain the search snippet as `仅发现`. Do not add a crawler dependency just to create Markdown.

## Chinese humanization

| Tool | Intended use | Boundary |
|---|---|---|
| `anti-ai-tone` | Remove visible template shells while preserving claims | Optional final pass |
| `renhua` | Rewrite Chinese product copy into direct, concrete language | Optional final pass |
| `humanizer-zh` | General Chinese humanization | Optional final pass |

Use at most one primary rewrite pass unless the user explicitly asks for comparison. After any rewrite, revalidate numbers, materials, functions, conditions, marketplace fields, and prohibited claims against the fact ledger. These Skills are never runtime dependencies of the open-source package.

## Optional publication review

The built-in listing review remains mandatory. It checks fact support, full-sentence risk meaning, category restrictions, marketplace consistency, and volatile rules that require current backend confirmation.

| Tool | Intended use | Boundary |
|---|---|---|
| `yuwen-publish-precheck` | Final semantic risk review for supported domestic content platforms | Not a Taobao, JD, Pinduoduo, or cross-border marketplace auditor |
| `media-publish-check` | Review actual short video, cover, subtitles, spoken copy, or livestream media | Use only when those real assets exist |

Any external repair re-enters the built-in fact and compliance review. Never claim guaranteed approval.

## Image generation

The package remains provider-neutral. It records the user's selected model/tool, reference-image rights, ratio, dimensions, count, text policy, output path, and review result. No personal routing Skill or private provider configuration belongs in this repository.

## Removed from the default package

The following are intentionally not recommended or auto-installed:

- `firecrawl-search`
- `firecrawl-scrape`
- browser/Playwright crawler adapters
- proxy rotation, pagination automation, login-state extraction, or anti-bot bypass

A user may still provide a public URL for manual review in a host that supports ordinary browsing. That is not permission to crawl the site or collect a catalog.

## Evidence boundaries

Public search can find:

- candidate comparable products;
- public URLs;
- visible display prices;
- titles and visible selling points;
- public review snippets or discussion language.

It cannot prove:

- transaction, coupon-after, member, or live-stream prices;
- seller-backend sales, inventory, or keyword volume;
- complete review datasets;
- stable natural ranking;
- platform authorization or compliance status.

Those require user-provided screenshots, exports, or authorized APIs and must be labeled separately.
