"""Validate the documentation-only public LUMEN Sieve showcase."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "assets/lumen-sieve-social-preview.png",
    "docs/ARCHITECTURE.md",
    "docs/PRODUCT_FLOW.md",
    "docs/EXAMPLE_OUTPUT.md",
    "docs/ENGINEERING_DECISIONS.md",
    "docs/SECURITY_AND_PRIVACY.md",
)

REQUIRED_README_TEXT = (
    "production source",
    "private",
    "Limitations",
    "Security and privacy",
    "Product media",
)

PROHIBITED_IMPLEMENTATION_SUFFIXES = {".go", ".proto", ".sql", ".tf", ".tsx"}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "Google API key": re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
    "Stripe live key": re.compile(r"sk_live_[0-9A-Za-z]{16,}"),
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def public_files() -> list[Path]:
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_readme_contract(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in REQUIRED_README_TEXT:
        if phrase.casefold() not in readme.casefold():
            errors.append(f"README is missing required boundary text: {phrase}")


def check_relative_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.suffix.casefold() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")


def check_public_boundary(files: list[Path], errors: list[str]) -> None:
    allowed_code = {ROOT / "scripts" / "validate_showcase.py"}
    for path in files:
        if path in allowed_code:
            continue
        if path.suffix.casefold() in PROHIBITED_IMPLEMENTATION_SUFFIXES:
            errors.append(f"private implementation file type is not allowed: {path.relative_to(ROOT)}")


def check_secrets(files: list[Path], errors: list[str]) -> None:
    text_suffixes = {".md", ".py", ".yml", ".yaml", ".txt", ""}
    for path in files:
        if path.suffix.casefold() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    files = public_files()
    check_required_files(errors)
    check_readme_contract(errors)
    check_relative_links(files, errors)
    check_public_boundary(files, errors)
    check_secrets(files, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Showcase validation passed for {len(files)} public files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
