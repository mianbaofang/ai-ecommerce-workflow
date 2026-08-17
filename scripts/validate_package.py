#!/usr/bin/env python3
"""Validate the canonical source tree and its installable Skill package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "ai-ecommerce-workflow"
PACKAGE_ROOT = ROOT / "skills" / PACKAGE_NAME
PACKAGE_REQUIRED = (
    "SKILL.md",
    "VERSION",
    "LICENSE",
    "manifest.json",
    "agents/interface.yaml",
)
PACKAGE_ARCHIVE_FILES = PACKAGE_REQUIRED + (
    "references/asset-output-contract.md",
    "references/compliance-terms.md",
    "references/copy-research-basis.md",
    "references/listing-compliance-review.md",
    "references/platform-image-specs.md",
    "references/product-copy-framework.md",
    "references/public-search-policy.md",
    "references/research-evidence-ledger.md",
)
FRONTMATTER_KEYS = {"name", "description"}
MANIFEST_REQUIRED = {
    "name",
    "version",
    "owner",
    "license",
    "status",
    "maturity_tier",
    "review_cadence",
    "target_platforms",
}
SECRET_PATTERNS = (
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._-]{20,}\b"),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[set[str], dict[str, str]]:
    normalized = text.replace("\r\n", "\n")
    lines = normalized.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must close with ---") from exc
    if not any(line.strip() for line in lines[end + 1 :]):
        raise ValueError("SKILL.md must contain instructions after frontmatter")

    keys: set[str] = set()
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        keys.add(key)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return keys, values


def check_required(root: Path, failures: list[str]) -> None:
    for relative in PACKAGE_REQUIRED:
        if not (root / relative).is_file():
            failures.append(f"Missing package file: {relative}")
    references = root / "references"
    if not references.is_dir() or not any(references.glob("*.md")):
        failures.append("Package must include at least one Markdown file under references/")


def validate_skill_metadata(root: Path, failures: list[str]) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return
    try:
        keys, values = parse_frontmatter(read_text(skill_path))
    except ValueError as exc:
        failures.append(str(exc))
        return
    extra = keys - FRONTMATTER_KEYS
    if extra:
        failures.append(
            "SKILL.md frontmatter may contain only name and description; "
            f"unexpected keys: {', '.join(sorted(extra))}"
        )
    if values.get("name") != PACKAGE_NAME:
        failures.append(f"SKILL.md name must be {PACKAGE_NAME}")
    description = values.get("description", "")
    if not description or len(description) > 1024:
        failures.append("SKILL.md description must be present and at most 1024 characters")


def validate_manifest(root: Path, failures: list[str]) -> dict[str, object] | None:
    path = root / "manifest.json"
    if not path.is_file():
        return None
    try:
        manifest = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        failures.append(f"Invalid {path.relative_to(root)}: {exc}")
        return None
    if not isinstance(manifest, dict):
        failures.append("manifest.json must contain a JSON object")
        return None
    missing = MANIFEST_REQUIRED - manifest.keys()
    if missing:
        failures.append(f"manifest.json missing fields: {', '.join(sorted(missing))}")
    if manifest.get("name") != PACKAGE_NAME:
        failures.append("manifest.name must match the Skill name")
    version_path = root / "VERSION"
    if version_path.is_file() and manifest.get("version") != read_text(version_path).strip():
        failures.append("manifest.version and VERSION must match")
    return manifest


def validate_links(root: Path, failures: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for source in root.rglob("*.md"):
        for target in pattern.findall(read_text(source)):
            target = target.strip("<>").split("#", 1)[0].strip()
            if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I):
                continue
            if not (source.parent / target).resolve().exists():
                failures.append(
                    f"Broken local Markdown link in {source.relative_to(root)}: {target}"
                )


def scan_secrets(root: Path, failures: list[str]) -> None:
    extensions = {".md", ".json", ".yaml", ".yml", ".txt", ".py", ".sh"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        text = read_text(path)
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            failures.append(f"Possible secret pattern found in {path.relative_to(root)}")


def validate_package_contents(root: Path, failures: list[str], *, strict: bool) -> None:
    if not strict:
        return
    allowed_exact = set(PACKAGE_ARCHIVE_FILES)
    for path in root.rglob("*"):
        if path.is_symlink():
            failures.append(f"Symbolic links are not allowed in installable Skill package: {path.relative_to(root)}")
            continue
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative in allowed_exact:
            continue
        failures.append(f"Unexpected file in installable Skill package: {relative}")


def validate_package(
    root: Path,
    failures: list[str],
    *,
    strict_contents: bool = True,
) -> dict[str, object] | None:
    check_required(root, failures)
    validate_skill_metadata(root, failures)
    version_path = root / "VERSION"
    if version_path.is_file() and not read_text(version_path).strip():
        failures.append("VERSION must not be empty")
    manifest = validate_manifest(root, failures)
    validate_links(root, failures)
    scan_secrets(root, failures)
    validate_package_contents(root, failures, strict=strict_contents)
    return manifest


def validate_source(root: Path, failures: list[str]) -> None:
    expected_entry = Path("skills") / PACKAGE_NAME / "SKILL.md"
    candidates = [root / "SKILL.md", root / "skill" / "SKILL.md"]
    skills_root = root / "skills"
    if skills_root.is_dir():
        candidates.extend(skills_root.glob("*/SKILL.md"))
    entries = sorted(path.relative_to(root) for path in candidates if path.is_file())
    if entries != [expected_entry]:
        visible = ", ".join(path.as_posix() for path in entries) or "none"
        failures.append(
            "GitHub Skill discovery must expose exactly "
            f"{expected_entry.as_posix()}; found: {visible}"
        )
    for relative in ("VERSION", "manifest.json"):
        if not (root / relative).is_file():
            failures.append(f"Missing source metadata: {relative}")
    if not PACKAGE_ROOT.is_dir():
        failures.append("Missing GitHub CLI discovery entry: skills/ai-ecommerce-workflow")
        return

    # GitHub CLI installs the complete skills/<name>/ directory, so the source
    # tree must obey the same allowlist as the release archive.
    package_manifest = validate_package(PACKAGE_ROOT, failures, strict_contents=True)
    root_version = read_text(root / "VERSION").strip() if (root / "VERSION").is_file() else ""
    package_version = read_text(PACKAGE_ROOT / "VERSION").strip() if (PACKAGE_ROOT / "VERSION").is_file() else ""
    if root_version != package_version:
        failures.append("Repository VERSION and package VERSION must match")

    root_manifest = validate_manifest(root, failures)
    if root_manifest is not None and package_manifest is not None:
        if root_manifest != package_manifest:
            failures.append("Repository and package manifest.json files must match")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, help="validate an extracted package")
    args = parser.parse_args()

    failures: list[str] = []
    target = args.package_root.resolve() if args.package_root else ROOT
    if args.package_root:
        validate_package(target, failures)
    else:
        validate_source(target, failures)

    print(json.dumps({"ok": not failures, "failures": failures}, ensure_ascii=False, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    sys.exit(main())
