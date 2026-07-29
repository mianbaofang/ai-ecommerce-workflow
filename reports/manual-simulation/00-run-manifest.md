# Manual Simulation Run

- Run date: 2026-07-29 03:50 +08:00
- Last regression verification: 2026-07-29 18:43 +08:00
- Skill entry: repository-root `SKILL.md`
- Search capability: AnySearch `batch_search` (anonymous public search path)
- Test product: portable coffee cup; leak performance unverified
- User-provided test facts: 420 ml, matte white, flip lid, no brand, intended for commuting
- Search queries:
  - `portable leakproof coffee cup price`
  - `travel coffee tumbler leakproof price`
  - `便携 防漏 咖啡杯 价格`
  - `portable coffee cup user complaints leakproof`
- Raw search evidence: [01-search-results.md](01-search-results.md)
- Image provider test: GPT Image 2 via CCAPI; the open-source Skill remains provider-neutral.
- Generated master: [ccapi-product-master.png](ccapi-product-master.png), 1024×1024.
- HyperFrames redesign assets: [charger-fixture.png](hyperframes-evidence/assets/charger-fixture.png) (1:1 generated test fixture) and [proofreading-desk.png](hyperframes-evidence/assets/proofreading-desk.png) (4:3 generated editorial surface).
- Deterministic platform derivatives: 800×800, 1200×900, and 1080×1440.
- Conservative Taobao delivery derivative: [taobao-main-800x800.jpg](taobao-main-800x800.jpg), 800×800, 17,055 bytes; the original PNG is 520,836 bytes and exceeds the 500 KB target.
- HyperFrames proof project: [hyperframes-evidence](hyperframes-evidence/); the 20-second composition check passed with 0 errors, 0 warnings, 9 layout samples, 300 motion samples, 78/78 contrast checks, and 5 inspected final-GIF midpoint snapshots.
- README animation: [intro-animation-preview-zh.gif](../../docs/assets/intro-animation-preview-zh.gif), 960×540, 16:9, 20 seconds, 5 fps, 100 frames, 1,933,236 bytes; SHA-256 `99B3DCC4DD2A29476D3CC7EE38C6556319D550718CFD7D5282D92001B4536634`.
- Static animation page: [docs/site/hyperframes-promo/index.html](../../docs/site/hyperframes-promo/index.html).
- Browser artifact: [index.html](index.html)
- Browser screenshots:
  - [run-report-desktop-viewport.png](run-report-desktop-viewport.png)
  - [run-report-desktop-sources.png](run-report-desktop-sources.png)
  - [run-report-mobile-viewport.png](run-report-mobile-viewport.png)
  - [run-report-mobile-sources.png](run-report-mobile-sources.png)
  - [hyperframes-promo-desktop.png](hyperframes-promo-desktop.png)
  - [hyperframes-promo-mobile.png](hyperframes-promo-mobile.png)
- User-designated platform-size sources:
  - https://www.secaiyun.com/docs/ecommerce-product-image-size-specification-guide-2026-07-12.html
  - https://www.secaiyun.com/docs/cross-border-ecommerce-image-size-guide-2026-06-28.html
- Complete ten-platform image-generation matrix: [../../references/platform-image-specs.md](../../references/platform-image-specs.md)
- Category-copy regression: [09-category-copy-regression.md](09-category-copy-regression.md)
- Chinese category, Markdown evidence, naturalization, and contextual compliance regression: [10-china-category-evidence-humanization.md](10-china-category-evidence-humanization.md)
- Workflow verdict: [07-workflow-regression.md](07-workflow-regression.md)
- In-app browser source screenshots:
  - [source-domestic-10-platforms.png](source-domestic-10-platforms.png)
- [source-crossborder-10-platforms.png](source-crossborder-10-platforms.png)

- Redesign review: [hyperframes-evidence/HUASHU-DESIGN-REVIEW.md](hyperframes-evidence/HUASHU-DESIGN-REVIEW.md)
- Design truth: [hyperframes-evidence/design.md](hyperframes-evidence/design.md)
- Rendered GIF contact sheet: [github-spec-contact-sheet.png](hyperframes-evidence/github-spec-contact-sheet.png)

This is a manual end-to-end simulation. It is evidence for route behavior, generated assets, browser rendering, and output shape; it is not a published listing or a sales claim. Current verdict is `CORE PASS / GENERATED-ASSET QA MIXED`: the tested Amazon adaptations remain rejected drafts.
