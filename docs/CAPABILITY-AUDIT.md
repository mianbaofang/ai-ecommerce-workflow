# Capability Audit

## Canonical package

The standard Skill package is rooted at:

- `SKILL.md`
- `agents/interface.yaml`
- `manifest.json`

The former `skill/` entrypoint remains only as a compatibility redirect for older links; it does not run the legacy 15-item workflow.

## Current contract

| # | Module | Status | Boundary |
|---|---|---|---|
| 1 | Description/link/image intake | ✅ Built-in | Accept one natural product input; ask focused clarification only when identification fails |
| 2 | Public market research flow | ✅ Built-in | Search public sources and return candidate links, visible observations, and opportunities |
| 3 | Price evidence labels | ✅ Built-in | Page observation only; never call it transaction price without authorized evidence |
| 4 | Public-search provider question | ✅ Built-in | Ask user at first use; no auto-install and no key collection in chat |
| 5 | Platform asset pack | ✅ Representative run passed | Category framework plus Taobao and Amazon regressions are recorded under `reports/manual-simulation/` |
| 6 | Compliance and claim caution | ✅ Built-in | Unsupported claims stay out of buyer-facing copy and move to the internal `待确认` review list |
| 7 | Image preflight | ✅ Built-in | Confirm model, reference rights, size, ratio, count, and delivery |
| 8 | Actual image generation | ⚠️ Route passed, asset QA mixed | GPT Image 2 through CCAPI produced saved 1:1 and 4:3 files; two Amazon adaptations were rejected for fidelity / white-background failures |
| 9 | Optional public search providers | ⚠️ Optional | `anysearch`, `multi-search-engine`, Tavily, Brave Search, agent-reach, agentkey |
| 10 | Crawler/scrape adapters | ❌ Removed from default | No Firecrawl, crawler, login-state, proxy, or anti-bot path |
| 11 | Legacy 15-item SOP | ❌ Retired | Nested `skill/` path redirects to the root Skill |

## Original built-in rules

The original Skill already included useful operating rules. They were reviewed individually instead of being discarded with the former product flow.

| Original rule group | Current treatment | Reason |
|---|---|---|
| Evidence grades and source trails | Kept and rebuilt as a Markdown evidence ledger | Public observations remain traceable without pretending to be transaction data |
| Category adaptation | Kept and expanded to Chinese leaf-category precedence plus ten marketplace adapters | Prevents one generic template from being reused across products and platforms |
| First-image focus and five-screen persuasion path | Kept as a buyer-decision sequence; fixed counts are no longer mandatory | Preserves the useful visual logic while respecting each platform's actual surfaces and limits |
| Humanized copy and prohibited-claim gate | Kept; naturalization is followed by fact, full-sentence risk, category, marketplace, and target-market review | A word hit locates risk but does not by itself prove a violation |
| Image-generation preflight and fidelity review | Kept and strengthened | The user chooses the tool; generated products must preserve the approved source and pass per-asset checks |
| Mandatory 15-item report, required intake form, auto-install, crawler routes, fixed title folklore, and default 30-day operations plan | Retired | These caused the high-friction product logic, legal exposure, stale platform claims, or work the user did not request |

## Verification expectations

- Positive trigger accepts a description, public URL, or image.
- Negative trigger rejects bulk crawling, protected-page access, automatic publishing, fake reviews, and unrelated generic market research.
- Every price and candidate claim includes URL/tool, query, time, market, and observation basis.
- Missing public search capability causes `待核验`, not invented data.
- Platform copy and image generation wait for the user's platform and tool choice.

## Current release status

Core workflow status is `PASS`; generated-asset QA is `MIXED`. Trigger evaluation passes 6/6 positive and 4/4 negative cases; output evaluation passes 11/11 cases with a 0% baseline, 100% with-Skill rate, and no regressions. Public search, category copy, the complete ten-platform image-generation matrix, contextual listing review, CCAPI invocation, responsive browser views, and HyperFrames evidence have real artifacts. Publishing and seller-console access are out of scope. Human blind review is optional extra evidence, not a release blocker. See `reports/manual-simulation/07-workflow-regression.md`.
