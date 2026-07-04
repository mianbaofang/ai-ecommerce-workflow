# Security Audit

This file is the log of a security review of the open-source `ai-ecommerce-workflow` repository. It records what was checked, what was found, and what the publish rules are.

## Audit target

- Repository: [mianbaofang/ai-ecommerce-workflow](https://github.com/mianbaofang/ai-ecommerce-workflow)
- Scope: every file tracked by git in the upstream repository
- Goal: confirm no private API keys, no response payloads, and no local tool caches reach the public repository

## Scan results

### 1. API keys and tokens

Searched all tracked files for known private provider patterns:

| Pattern | What it protects |
|---|---|
| `sk-[A-Za-z0-9]{20,}` | OpenAI / Google / generic private model keys |
| `ghp_[A-Za-z0-9]+` | GitHub personal access tokens |
| `Bearer [A-Za-z0-9]+` | Generic bearer tokens |
| `YAIROUTER_API_KEY=<value>` | Codex-only image router key |
| `CCAPI_API_KEY=<value>` | Codex-only CCAPI Direct key |
| `APIMART_API_KEY=<value>` | APIMart image key |
| `ANYSEARCH_API_KEY=<value>` | AnySearch key |
| `OPENAI_API_KEY=<value>` | OpenAI key |
| `Authorization: <header>` | All generic auth headers |

Result: no matches in tracked files.

### 2. Response payloads

Searched for raw image-generation response payloads:

| Pattern | What it would indicate |
|---|---|
| `"b64_json": "<base64>"` | Image API response with embedded image |
| `"image_url": "https://..."` | Image API response with hosted URL |
| `*.response.json` | Raw response output |

Result: no matches in tracked files. The repository-wide `*.response.json` rule in `.gitignore` blocks future accidental adds too.

### 3. Local tool caches

`.gitignore` covers:

- `.firecrawl/` — Firecrawl call cache and session
- `.mcp/` — generic MCP tool cache
- `.anysearch/` — AnySearch cache
- `.multi-search-engine/` — multi-search-engine cache
- `docs/site/frames/` — animation render frames workspace

Verified no tracked file lives inside any of those paths.

### 4. Secrets and credentials

`.gitignore` covers:

- `.env`, `.env.*`, `*.key`, `*.pem`
- Browser session data: `*.cookies.json`, `session-data/`, `.local-chromium/`
- OS noise: `.DS_Store`, `Thumbs.db`, `desktop.ini`

No tracked file contains any of these.

### 5. Build / runtime artifacts

`.gitignore` covers:

- `outputs/`, `output/`, `.tmp/`, `tmp/`, `.cache/`
- `__pycache__/`, `*.py[cod]`, `.venv/`, `venv/`
- `node_modules/`, `dist/`, `build/`, `.playwright/`
- `*.mp4`, `*.webm`, `*.mov`, `*.wav`, `*.mp3`, `*.palette.png`

No tracked file is a build artifact.

## What is intentionally kept in the repo

| File | Reason |
|---|---|
| `docs/site/*.png` (1K GPT Image 2 visuals) | Public project introduction imagery. Generated locally for README animation. |
| `docs/assets/intro-animation-preview.gif` | Public 35-second animation preview. |
| `docs/assets/hero.svg` | Public SVG hero (kept as static fallback). |
| `docs/history/` | PM iteration history and source-article references. Public. |

Generated images and the GIF are creative references, not marketplace assets. They do not contain private API responses.

## Publish rules

The repository follows these rules:

1. **No API keys in source.** All keys for `YAIROUTER`, `CCAPI`, `APIMART`, `ANYSEARCH`, `OPENAI`, etc. must stay in environment variables.
2. **No response payloads.** `*.response.json` and any embedded base64 image responses must never be committed.
3. **No local tool caches.** `.firecrawl/`, `.mcp/`, `.anysearch/`, `.multi-search-engine/`, browser session data must never be committed.
4. **No fake reviews, fabricated certifications, or unauthorized scraped data.**
5. **Generated images are creative references.** Real marketplace assets still need user-provided product photos or licensed sources.

## Re-running the audit

```bash
# API key scan (tracked files only)
git ls-files | xargs grep -lE "(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]+|Bearer [A-Za-z0-9]+)" 2>/dev/null

# Response payload scan
git ls-files | xargs grep -l '"b64_json":' 2>/dev/null

# Untracked file scan
git ls-files --others --exclude-standard
```

If any of these return results, do not push until they are removed.
