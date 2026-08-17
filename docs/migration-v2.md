# Migration Notes

Version 1.1.1 moves the installable Skill entrypoint from the legacy repository
root to `skills/ai-ecommerce-workflow/` so the directory name and `SKILL.md`
name form one discoverable package identity.

Consumers using the published 1.1.0 root layout should install the new package
as `ai-ecommerce-workflow` and remove only the old duplicate entry after a
successful validation. The workflow contract is unchanged: it produces
research evidence, editable listing drafts, platform image specifications, and
optional image-generation briefs; it does not publish listings or access
login-only seller pages.
