"""Shared, dependency-optional helpers for this Markdown knowledge base."""
from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path

KNOWLEDGE = Path(__file__).resolve().parents[1]
VAULT = KNOWLEDGE.parent
ANALYZED = {"analyzed-text", "analyzed-visual"}
REVIEW_STATES = ANALYZED | {"partial", "pending", "blocked"}


def source_id(path: str) -> str:
    return "src-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:12]


def scalar(value: str):
    value = value.strip()
    if value in {"null", "~", ""}:
        return None
    if value in {"true", "false"}:
        return value == "true"
    try:
        return json.loads(value)
    except ValueError:
        pass
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value.startswith("[") and value.endswith("]"):
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return [scalar(v) for v in value[1:-1].split(",") if v.strip()]
    return value


def metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    try:
        import yaml
    except ImportError:
        data, key = {}, None
        for line in match.group(1).splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if re.match(r"\s+- ", line) and key:
                if data[key] is None:
                    data[key] = []
                if not isinstance(data[key], list):
                    raise ValueError("unsupported nested YAML; use flat fields")
                data[key].append(scalar(line.strip()[2:]))
                continue
            item = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
            if not item:
                raise ValueError("unsupported YAML; use documented flat schema or install PyYAML")
            key, value = item.groups()
            data[key] = scalar(value)
    else:
        data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def load_manifest() -> dict:
    return json.loads((KNOWLEDGE / "source-manifest.json").read_text(encoding="utf-8"))


def cards() -> dict:
    found = {}
    for path in sorted((KNOWLEDGE / "sources").glob("*.md")):
        data = metadata(path)
        found[path.stem] = (path, data)
    return found


def label(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def wikilink(target: str, title: str | None = None, table=False) -> str:
    sep = "\\|" if table else "|"
    return "[[" + target + (sep + label(title) if title is not None else "") + "]]"


def generated(path: Path, name: str, body: str, initial: str):
    begin, end = f"<!-- GENERATED:{name}:BEGIN -->", f"<!-- GENERATED:{name}:END -->"
    replacement = begin + "\n" + body.rstrip() + "\n" + end
    if path.exists():
        text = path.read_text(encoding="utf-8")
        pattern = re.escape(begin) + r".*?" + re.escape(end)
        if re.search(pattern, text, re.S):
            text = re.sub(pattern, lambda _: replacement, text, count=1, flags=re.S)
        else:
            raise ValueError(f"refusing to overwrite unmarked author content: {path}")
    else:
        text = initial.rstrip() + "\n\n" + replacement + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def prose(text: str) -> str:
    """Exclude syntax examples in fenced/inline code from link validation."""
    text = re.sub(r"(?m)^```[^\n]*\n.*?^```\s*$", "", text, flags=re.S)
    return re.sub(r"`[^`\n]+`", "", text)


def wiki_targets(text: str):
    for match in re.finditer(r"!?\[\[([^\]\n]+)\]\]", prose(text)):
        target = match.group(1).replace("\\|", "|").split("|", 1)[0]
        yield target
