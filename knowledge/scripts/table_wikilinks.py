#!/usr/bin/env python3
"""Check/fix alias pipes in ordinary Markdown tables, without reformatting prose.

Only a header followed by a Markdown delimiter row starts a table. Frontmatter,
fenced/indented code, inline code, comments and escaped wikilinks are protected.
This is a conservative syntax check, not an Obsidian UI/rendering test.
Run without --write to check; --write only inserts missing backslashes.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re


LINK = re.compile(r"(?<!\[)\[\[([^\[\]\r\n]+)\]\](?!\])")


@dataclass(frozen=True)
class TableAliasIssue:
    offset: int
    line: int
    column: int
    link: str


def _escaped(text: str, position: int) -> bool:
    count = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        count += 1
        position -= 1
    return bool(count % 2)


def _mask(text: str) -> str:
    return "".join(c if c in "\r\n" else " " for c in text)


def _inline_code_mask(line: str) -> str:
    runs = list(re.finditer(r"`+", line))
    chars = list(line)
    i = 0
    while i < len(runs):
        start = runs[i]
        if _escaped(line, start.start()):
            i += 1
            continue
        end = next((j for j in range(i + 1, len(runs))
                    if len(runs[j].group()) == len(start.group())), None)
        if end is None:
            i += 1
            continue
        a, b = start.start(), runs[end].end()
        chars[a:b] = _mask(line[a:b])
        i = end + 1
    return "".join(chars)


def _visible_lines(text: str) -> list[str]:
    # Masking preserves all character offsets, including CRLF and Unicode.
    text = re.sub(r"<!--[\s\S]*?(?:-->|\Z)", lambda m: _mask(m.group()), text)
    lines = text.splitlines(keepends=True)
    result = []
    frontmatter = bool(lines and lines[0].lstrip("\ufeff").strip() == "---")
    fence = None
    for index, line in enumerate(lines):
        if frontmatter:
            result.append(_mask(line))
            if index and line.strip() in {"---", "..."}:
                frontmatter = False
            continue
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})([^\r\n]*)", line)
        if fence:
            result.append(_mask(line))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker and (marker[1][0] == "~" or "`" not in marker[2]):
            fence = (marker[1][0], len(marker[1]))
            result.append(_mask(line))
            continue
        if line.startswith(("    ", "\t")):
            result.append(_mask(line))
            continue
        result.append(_inline_code_mask(line))
    return result


def _delimiter(line: str) -> bool:
    line = line.strip()
    if "|" not in line:
        return False
    cells = line.removeprefix("|").removesuffix("|").split("|")
    return bool(cells) and all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell) for cell in cells)


def _row(line: str) -> bool:
    if not line.strip() or line.lstrip().startswith(("#", ">")):
        return False
    # A pipe inside a wikilink alone does not turn prose into a table row.
    visible = LINK.sub(lambda m: _mask(m.group()), line)
    return any(c == "|" and not _escaped(visible, i) for i, c in enumerate(visible))


def find_unescaped_table_aliases(text: str) -> list[TableAliasIssue]:
    visible = _visible_lines(text)
    rows = set()
    for index in range(1, len(visible)):
        if _delimiter(visible[index]) and _row(visible[index - 1]):
            rows.update((index - 1, index))
            following = index + 1
            while following < len(visible) and _row(visible[following]):
                rows.add(following)
                following += 1
    issues = []
    offset = 0
    for index, line in enumerate(visible):
        if index in rows:
            for match in LINK.finditer(line):
                if _escaped(line, match.start()):
                    continue
                inner = match.group(1)
                pipes = [i for i, c in enumerate(inner) if c == "|" and not _escaped(inner, i)]
                if pipes and inner[:pipes[0]].strip():
                    for pipe in pipes:
                        position = match.start(1) + pipe
                        issues.append(TableAliasIssue(offset + position, index + 1, position + 1, match.group()))
        offset += len(line)
    return issues


def normalize_table_aliases(text: str) -> str:
    for issue in reversed(find_unescaped_table_aliases(text)):
        text = text[:issue.offset] + "\\" + text[issue.offset:]
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Markdown file or knowledge directory")
    parser.add_argument("--write", action="store_true", help="insert missing escapes (default: check only)")
    args = parser.parse_args()
    if not args.path.exists() or (args.path.is_file() and args.path.suffix != ".md"):
        parser.error("path must be an existing Markdown file or directory")
    files = [args.path] if args.path.is_file() else sorted(args.path.rglob("*.md"))
    records = []
    for path in files:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        issues = find_unescaped_table_aliases(text)
        if not issues:
            continue
        records.append({"path": str(path.relative_to(args.path)) if args.path.is_dir() else path.name,
                        "count": len(issues), "lines": sorted({i.line for i in issues})})
        if args.write:
            updated = normalize_table_aliases(text)
            if find_unescaped_table_aliases(updated):
                raise RuntimeError(f"normalization left invalid aliases: {path.name}")
            if path.read_bytes() != raw:
                raise RuntimeError(f"file changed during processing; not written: {path.name}")
            path.write_bytes(updated.encode("utf-8"))
    count = sum(r["count"] for r in records)
    print(json.dumps({"mode": "write" if args.write else "check", "files_checked": len(files),
                      "affected_files": len(records), "alias_pipes": count, "files": records},
                     ensure_ascii=False, indent=2))
    return 0 if args.write or not count else 1


if __name__ == "__main__":
    raise SystemExit(main())
