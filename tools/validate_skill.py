"""Validate this skill's distributable files; does not evaluate model behavior."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {path.name}: {exc}")
        return ""


def load_mapping(text: str, label: str, errors: list[str]) -> dict:
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"Invalid YAML in {label}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a YAML mapping")
        return {}
    return value


def validate(skill: Path) -> list[str]:
    skill = skill.resolve()
    errors: list[str] = []
    entry = skill / "SKILL.md"
    text = read_text(entry, errors)
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)\Z", text, re.S)
    metadata = {}
    if not match:
        errors.append("SKILL.md needs YAML frontmatter delimited by ---")
    else:
        metadata = load_mapping(match.group(1), "SKILL.md", errors)
        if not match.group(2).strip():
            errors.append("SKILL.md has no instructions")

    name = metadata.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append("Skill name must be lowercase kebab-case, at most 64 characters")
    elif name != skill.name:
        errors.append("Skill name must match its directory")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("Skill description must be nonempty text, at most 1024 characters")

    ui_path = skill / "agents" / "openai.yaml"
    ui = load_mapping(read_text(ui_path, errors), "agents/openai.yaml", errors)
    interface = ui.get("interface", {})
    if not isinstance(interface, dict):
        errors.append("UI interface must be a mapping")
        interface = {}
    for field in ("display_name", "short_description", "default_prompt"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"UI {field} is missing or not text")
    short = interface.get("short_description")
    if isinstance(short, str) and not 25 <= len(short) <= 64:
        errors.append("UI short_description must have 25-64 characters")
    prompt = interface.get("default_prompt")
    if isinstance(prompt, str) and isinstance(name, str) and f"${name}" not in prompt:
        errors.append("UI default_prompt must mention the skill invocation")

    files = sorted(skill.rglob("*"))
    documents: dict[Path, str] = {}
    for path in files:
        resolved = path.resolve()
        if not resolved.is_relative_to(skill):
            errors.append(f"Resource escapes the skill directory: {path.relative_to(skill)}")
            continue
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            content = read_text(path, errors)
            if not content.strip():
                errors.append(f"Empty resource: {path.relative_to(skill)}")
            if re.search(r"\[TODO\s*:|\bTODO\b|\bFIXME\b", content):
                errors.append(f"Unfinished scaffold: {path.relative_to(skill)}")
            is_template = path.is_relative_to(skill / "assets" / "templates")
            if not is_template and re.search(r"\{\{[^}]+\}\}", content):
                errors.append(f"Unfilled template outside assets: {path.relative_to(skill)}")
            if path.suffix == ".md":
                documents[resolved] = content

    graph: dict[Path, set[Path]] = {}
    for path, content in documents.items():
        # Our documents use fenced code and inline Markdown links. Links inside
        # examples are not runtime resource dependencies.
        prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", content)
        targets: set[Path] = set()
        for target in LINK.findall(prose):
            parts = urlsplit(target.strip("<>"))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (path.parent / unquote(parts.path)).resolve()
            if not destination.is_relative_to(skill):
                errors.append(f"Link escapes skill: {path.relative_to(skill)} -> {target}")
            elif not destination.is_file():
                errors.append(f"Broken local link: {path.relative_to(skill)} -> {target}")
            else:
                targets.add(destination)
        graph[path] = targets

    reachable: set[Path] = set()
    remaining = [entry.resolve()]
    while remaining:
        path = remaining.pop()
        if path in reachable:
            continue
        reachable.add(path)
        remaining.extend(graph.get(path, set()) - reachable)
    for path in documents:
        if path not in reachable:
            errors.append(f"Resource not discoverable from SKILL.md: {path.relative_to(skill)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=ROOT / "skills" / "project-interview")
    args = parser.parse_args()
    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {args.path.name} metadata, resources, links, and template boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
