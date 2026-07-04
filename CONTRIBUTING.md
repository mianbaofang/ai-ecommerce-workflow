# Contributing

Thanks for improving `ai-ecommerce-workflow`.

This repository is an Agent Skill, not a marketplace automation bot. Contributions should keep the Skill safe, reviewable, and provider-neutral.

## Good Contributions

- Better output contracts for ecommerce launch work.
- Clearer platform-specific title and keyword rules.
- More category adaptation rules with compliance notes.
- Better examples and test prompts.
- Provider-neutral image/video preflight improvements.
- Documentation fixes in English or Chinese.

## Boundaries

Do not add:

- hard-coded private API keys, bearer tokens, or private provider endpoints;
- direct seller-backend publishing automation;
- fake review generation;
- scraping logic for protected marketplace data without authorization;
- claims that generated data is verified when it is not;
- medical, safety, certification, or compliance claims without an explicit manual-review gate.

## Before Opening A Pull Request

Run these checks from the repository root:

```bash
rg -n "API_KEY|SECRET|TOKEN|Bearer|sk-" .
rg -n "legacy Taobao-only naming|old trigger phrase" .
```

If you change the Skill behavior, also update:

- `skill/SKILL.md`
- `skill/templates/user-input-form.md` when inputs change
- `skill/references/trigger-output-eval.md` when triggers or boundaries change
- `tests/TEST-CASES.md` when expected outputs change
- `CHANGELOG.md`

## Style

- Keep the main `SKILL.md` actionable.
- Move long methods, examples, and history into `skill/references/`, `skill/examples/`, or `docs/history/`.
- Mark evidence level and verification status explicitly.
- Keep image/video guidance provider-neutral unless a user chooses a provider at runtime.
