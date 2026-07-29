# Output Quality Scorecard

This v0 scorecard compares static without-skill and with-skill outputs using assertion grading.

- Cases: `11`
- Baseline pass rate: `0.0`
- With-skill pass rate: `100.0`
- Delta: `100.0`
- Regressions: `0`
- Blind A/B pairs: `11`
- Gate pass: `True`

Blind review artifacts are generated separately so reviewers can inspect A/B outputs without seeing the answer key.
Run output review adjudication after reviewer decisions are recorded; pending cases should stay pending rather than being counted as human agreement.

## Case Results

| Case | Baseline | With Skill | Delta | Winner | Failed With-Skill Assertions |
| --- | ---: | ---: | ---: | --- | --- |
| public-research-contract | 0.0 | 100.0 | 100.0 | with_skill | None |
| provider-and-asset-boundary | 0.0 | 100.0 | 100.0 | with_skill | None |
| ten-platform-size-matrix | 0.0 | 100.0 | 100.0 | with_skill | None |
| image-only-fact-boundary | 0.0 | 100.0 | 100.0 | with_skill | None |
| generated-image-quality-gate | 0.0 | 100.0 | 100.0 | with_skill | None |
| category-module-separation | 0.0 | 100.0 | 100.0 | with_skill | None |
| marketplace-adapter-separation | 0.0 | 100.0 | 100.0 | with_skill | None |
| china-category-precedence | 0.0 | 100.0 | 100.0 | with_skill | None |
| markdown-evidence-state | 0.0 | 100.0 | 100.0 | with_skill | None |
| humanization-fact-regression | 0.0 | 100.0 | 100.0 | with_skill | None |
| contextual-listing-compliance | 0.0 | 100.0 | 100.0 | with_skill | None |

## Failure Taxonomy

- No with-skill assertion failures.

## Next Fixes

- Add holdout cases before using this as a release gate.
- Promote repeated failed assertions into the output-risk profile.
- Keep assertions tied to material deliverables, not phrasing trivia.
