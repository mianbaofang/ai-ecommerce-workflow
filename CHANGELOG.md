# Changelog

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
