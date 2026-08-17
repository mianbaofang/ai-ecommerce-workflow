#!/usr/bin/env python3
"""Build and clean-install-test the canonical Skill archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from validate_package import PACKAGE_ARCHIVE_FILES


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "ai-ecommerce-workflow"
PACKAGE_ROOT = ROOT / "skills" / PACKAGE_NAME
# Keep the install archive limited to the runtime file contract. Evaluations,
# reports, source-only docs, and release media stay in the repository.
PACKAGE_FILES = PACKAGE_ARCHIVE_FILES


def package_version() -> str:
    return (PACKAGE_ROOT / "VERSION").read_text(encoding="utf-8").strip()


def run_validator(target: Path, package: bool = False) -> None:
    command = [sys.executable, str(ROOT / "scripts" / "validate_package.py")]
    if package:
        command.extend(("--package-root", str(target)))
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(result.stdout or result.stderr)


def run_official_validator(target: Path) -> bool:
    executable = shutil.which("agentskills")
    if not executable:
        return False
    result = subprocess.run(
        [executable, "validate", str(target)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode:
        raise RuntimeError(result.stdout or result.stderr)
    return True


def write_archive(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative_name in PACKAGE_FILES:
            source = PACKAGE_ROOT / relative_name
            if not source.is_file():
                raise FileNotFoundError(f"Missing discoverable package file: {relative_name}")
            if source.is_symlink():
                raise RuntimeError(f"Symbolic links are not allowed in package sources: {relative_name}")
            relative = PurePosixPath(PACKAGE_NAME) / PurePosixPath(relative_name)
            info = zipfile.ZipInfo(str(relative), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def validate_archive(archive_path: Path) -> str:
    """Check the release archive before extracting it into a test directory."""
    with zipfile.ZipFile(archive_path) as archive:
        bad_crc = archive.testzip()
        if bad_crc is not None:
            raise RuntimeError(f"CRC check failed for archive member: {bad_crc}")

        names = [info.filename for info in archive.infolist()]
        if len(names) != len(set(names)):
            raise RuntimeError("Archive contains duplicate member paths")
        folded = [name.casefold() for name in names]
        if len(folded) != len(set(folded)):
            raise RuntimeError("Archive contains case-insensitive duplicate paths")
        if not names:
            raise RuntimeError("Archive is empty")

        top_levels = {PurePosixPath(name).parts[0] for name in names if PurePosixPath(name).parts}
        if top_levels != {PACKAGE_NAME}:
            raise RuntimeError(
                f"Archive must have one top-level directory {PACKAGE_NAME!r}; found: {sorted(top_levels)}"
            )

        skill_entries = []
        for info in archive.infolist():
            member = PurePosixPath(info.filename)
            if "\\" in info.filename:
                raise RuntimeError(f"Archive member must use POSIX separators: {info.filename}")
            if member.is_absolute() or ".." in member.parts or not member.parts:
                raise RuntimeError(f"Unsafe archive member: {info.filename}")
            if info.is_dir():
                continue
            # ZIP symlinks can escape the install boundary after extraction.
            mode = (info.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                raise RuntimeError(f"Archive contains a symbolic link: {info.filename}")
            if member.name.casefold() == "skill.md":
                skill_entries.append(member)

        expected_entry = PurePosixPath(PACKAGE_NAME) / "SKILL.md"
        if skill_entries != [expected_entry]:
            rendered = ", ".join(str(entry) for entry in skill_entries) or "none"
            raise RuntimeError(f"Archive must contain exactly one top-level SKILL.md; found: {rendered}")
        return PACKAGE_NAME


def install_test(archive_path: Path) -> bool:
    with tempfile.TemporaryDirectory(prefix=f"{PACKAGE_NAME}-install-") as temp:
        validate_archive(archive_path)
        target = Path(temp) / PACKAGE_NAME
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(Path(temp))
        if not target.is_dir():
            raise RuntimeError("Archive did not extract to its declared top-level directory")
        run_validator(target, package=True)
        return run_official_validator(target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output.resolve() if args.output else None

    run_validator(ROOT)
    output = output or (ROOT / "dist" / f"{PACKAGE_NAME}-v{package_version()}.zip").resolve()
    write_archive(output)
    official = install_test(output)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    checksum = output.with_suffix(output.suffix + ".sha256")
    checksum.write_text(f"{digest}  {output.name}\n", encoding="ascii")
    print(json.dumps({
        "ok": True,
        "archive": str(output),
        "bytes": output.stat().st_size,
        "sha256": digest,
        "install_test": "passed",
        "official_validation": "passed" if official else "not available",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
