# 当前触发与输出评测入口

旧版完整上架、自动安装和 15 项评测已经退役。可执行用例位于仓库根目录：

- `../../../evals/trigger_cases.json`
- `../../../evals/semantic_config.json`
- `../../../evals/output_cases.jsonl`
- `../../../tests/TEST-CASES.md`

当前评测覆盖自然描述、公开链接、产品图片、十平台图片规格、中文类目优先、Markdown 证据状态、自然化事实回归、整句合规审核，以及批量抓取、自动发布和虚假评论边界。

```text
python C:\Users\Ethan\.agents\skills\yao-meta-skill\scripts\trigger_eval.py --description-file SKILL.md --cases evals\trigger_cases.json --semantic-config evals\semantic_config.json
python C:\Users\Ethan\.agents\skills\yao-meta-skill\scripts\run_output_eval.py --cases evals\output_cases.jsonl
```
