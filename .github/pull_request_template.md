## Summary

Describe the Skill or documentation change.

## Changed Files

- 

## Checks

```bash
rg -n "API_KEY|Bearer|sk-|YAIROUTER|CCAPI|APIMART" .
rg -n "taobao-newproduct-launch-workflow|跑淘宝新品上架流程" .
```

## Boundary Review

- [ ] Does not hard-code private providers, keys, or endpoints.
- [ ] Does not add direct seller-backend publishing.
- [ ] Does not generate fake reviews or buyer-show comments.
- [ ] Marks inferred data and assumptions clearly.
- [ ] Updates tests or eval prompts when behavior changes.
