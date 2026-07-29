# Changelog

## v1.1.0 - 2026-07-29

### Changed

- Made the repository-root `SKILL.md` the canonical Agent Skill entrypoint, with `agents/interface.yaml`, `manifest.json`, references, and evaluations following the standard Skill layout.
- Replaced the default 15-item launch-report route with a public-search-first flow: description, public URL, or images in; market research first; platform copy and image planning only after the user selects a marketplace.
- Kept the nested `skill/` path as a compatibility redirect for existing links. It no longer activates the former 15-item workflow.

### Search and Trust Boundaries

- Public search providers remain optional and user-configured. The Skill asks about them but never auto-installs a provider or collects API keys in chat.
- Removed Firecrawl, crawler/scrape adapters, login-state access, proxy rotation, and anti-bot bypass from the default package path.
- Clarified that displayed prices and search result order are observations, not transaction prices or stable rankings.

### Discovery

- Added a bilingual GitHub Pages source with canonical URLs, reciprocal language links, meta descriptions, Open Graph/Twitter metadata, and `SoftwareSourceCode` JSON-LD.
- Added `robots.txt`, `sitemap.xml`, and `llms.txt` with the verified Skill scope and explicit boundaries.
- Added a GitHub Pages deployment workflow and aligned the repository description and topics with the current public-search-first workflow.

## v1.0 - 2026-07-04

Initial open-source release of `ai-ecommerce-workflow`.

### Added

- Short public Skill name: `ai-ecommerce-workflow`.
- Agent-facing Skill package under `skill/`.
- Four run modes: quick diagnosis, complete launch, material production, and post-launch optimization.
- 15-part ecommerce launch output contract:
  - product positioning;
  - target users;
  - core selling points;
  - user pain points;
  - competitor price-band analysis;
  - differentiation opportunities;
  - main image planning;
  - detail page structure;
  - platform-specific titles and a 20-title test pool;
  - keyword layers;
  - review insights;
  - FAQ;
  - customer-service scripts;
  - design brief;
  - 30-day launch plan.
- Evidence levels: A user-provided, B tool/link verified, C inferred, D strong assumption.
- Delivery packs for operations, design, customer service, boss approval, and material generation.
- Humanized Chinese copywriting checks inspired by public anti-AI-writing principles.
- Provider-neutral image and video preflight rules.
- Category adaptation matrix for bags/apparel, beauty, 3C, food/health, home goods, mother-and-baby/toys, 1688/B2B, and cross-border/Amazon scenarios.
- English and Chinese README files.
- MIT license and contribution guide.
- Lightweight trigger/output eval cases.

### Changed

- Generalized the project from a Taobao-only workflow to a broader ecommerce workflow.
- Kept Taobao as one supported marketplace in the platform rule matrix.
- Moved historical iteration notes into `docs/history/`.

### Boundaries

- No direct product publishing.
- No fake reviews.
- No unauthorized scraping.
- No hard-coded private image/video providers or secrets.
- Generated image/video outputs are creative references, not final listing assets without review.
