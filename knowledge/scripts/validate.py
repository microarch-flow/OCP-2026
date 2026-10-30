#!/usr/bin/env python3
"""Validate source identity, evidence metadata, navigation and optional raw integrity.

Default mode validates PDF links against the pinned manifest, allowing assembly
workspaces without 501 local originals. --check-source-bytes additionally requires
every original file at the vault root and verifies its Git blob hash and size.
This is a structural check, not factual/semantic review or Obsidian UI testing.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

from common import ANALYZED, KNOWLEDGE, REVIEW_STATES, VAULT, load_manifest, metadata, source_id, wiki_targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-source-bytes", action="store_true")
    parser.add_argument("--json-report", type=Path)
    args = parser.parse_args()
    errors, warnings = [], []
    manifest = load_manifest()
    rows = manifest["sources"]
    ids, paths = {}, {}
    sha_pattern = re.compile(r"^[0-9a-f]{40}$")
    for row in rows:
        sid, path = row.get("id"), row.get("source_path")
        if sid in ids:
            errors.append(f"duplicate source id: {sid}")
        if path in paths:
            errors.append(f"duplicate source path: {path}")
        ids[sid], paths[path] = row, row
        if sid != source_id(path):
            errors.append(f"path-derived ID mismatch: {sid}")
        if Path(path).is_absolute() or ".." in Path(path).parts:
            errors.append(f"unsafe source path: {path}")
        if not sha_pattern.fullmatch(str(row.get("source_git_blob_sha", ""))):
            errors.append(f"invalid Git blob SHA: {sid}")
        if row.get("source_commit") != manifest["source_commit"]:
            errors.append(f"source commit mismatch: {sid}")
        if row.get("source_pages") is not None and (type(row["source_pages"]) is not int or row["source_pages"] < 1):
            errors.append(f"invalid known page count: {sid}")
        if row.get("source_bytes") == 0 and row.get("review_status") in ANALYZED:
            errors.append(f"zero-byte source claimed analyzed: {sid}")
        if args.check_source_bytes:
            source_file = VAULT / path
            if not source_file.is_file():
                errors.append(f"missing original PDF: {path}")
            else:
                raw = source_file.read_bytes()
                actual_sha = hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
                if actual_sha != row["source_git_blob_sha"] or len(raw) != row["source_bytes"]:
                    errors.append(f"original PDF content differs from pinned Git blob: {path}")
    cards, card_page_counts = {}, {}
    required = {"id", "type", "title", "source_path", "source_git_blob_sha", "source_commit", "source_pages", "review_status", "evidence_pages", "tags"}
    for file in sorted((KNOWLEDGE / "sources").glob("*.md")):
        rel = file.relative_to(VAULT).as_posix()
        try:
            data = metadata(file)
        except (ValueError, TypeError) as exc:
            errors.append(f"{rel}: {exc}")
            continue
        cards[file.stem] = data
        missing = required - data.keys()
        if missing:
            errors.append(f"{rel}: missing fields {sorted(missing)}")
        sid = data.get("id")
        if file.stem != sid or sid not in ids:
            errors.append(f"{rel}: card filename/id not in manifest")
            continue
        row = ids[sid]
        for key in ("source_path", "source_git_blob_sha", "source_commit"):
            if data.get(key) != row.get(key):
                errors.append(f"{rel}: {key} differs from manifest")
        if data.get("type") != "source":
            errors.append(f"{rel}: type must be source")
        status = data.get("review_status")
        if status not in REVIEW_STATES:
            errors.append(f"{rel}: unsupported review_status {status}")
        if status == "pending":
            errors.append(f"{rel}: unread placeholder cards belong only in manifest")
        pages = data.get("source_pages")
        if pages is not None and (type(pages) is not int or pages < 1):
            errors.append(f"{rel}: source_pages must be positive integer or null")
            pages = None
        if row.get("source_pages") is not None and pages != row["source_pages"]:
            errors.append(f"{rel}: source_pages differs from actual extraction result")
        if pages is not None:
            card_page_counts[row["source_path"]] = pages
        evidence = data.get("evidence_pages", [])
        if not isinstance(evidence, list) or any(type(p) is not int or p < 1 or (pages is not None and p > pages) for p in evidence):
            errors.append(f"{rel}: invalid evidence_pages")
            evidence = []
        if status in ANALYZED:
            if row["source_bytes"] == 0:
                errors.append(f"{rel}: cannot analyze a zero-byte PDF")
            if not evidence:
                errors.append(f"{rel}: analyzed source needs evidence_pages")
            if pages is None:
                errors.append(f"{rel}: analyzed source needs actual PDF page count")
            body = file.read_text(encoding="utf-8")
            cited = []
            for target in wiki_targets(body):
                match = re.fullmatch(re.escape(row["source_path"]) + r"#page=(\d+)", target)
                if match:
                    cited.append(int(match.group(1)))
            if not cited:
                errors.append(f"{rel}: no direct physical-page PDF evidence links")
            unlisted = set(cited) - set(evidence)
            if unlisted:
                errors.append(f"{rel}: PDF citations absent from evidence_pages: {sorted(unlisted)}")
            uncited = set(evidence) - set(cited)
            if uncited:
                warnings.append(f"{rel}: evidence_pages without direct matching link: {sorted(uncited)}")
            for section in ("核心结论", "关键证据", "指标与条件", "图表与架构", "关联与比较", "不确定性与待验证"):
                if section not in body:
                    warnings.append(f"{rel}: recommended section absent: {section}")
        visual = data.get("key_pages_visual_checked", [])
        if not isinstance(visual, list) or any(type(p) is not int or p < 1 or (pages is not None and p > pages) for p in visual):
            errors.append(f"{rel}: invalid key_pages_visual_checked")
        if status == "analyzed-visual" and not visual:
            errors.append(f"{rel}: analyzed-visual needs key_pages_visual_checked")
        if row.get("review_status") != status or row.get("analysis_card") != f"knowledge/sources/{sid}":
            errors.append(f"{rel}: stale manifest; run refresh.py")
    for row in rows:
        if row.get("analysis_card") and row["id"] not in cards:
            errors.append(f"manifest points to absent source card: {row['id']}")

    link_count, pdf_page_count = 0, 0
    for file in sorted(KNOWLEDGE.rglob("*.md")):
        if "templates" in file.relative_to(KNOWLEDGE).parts:
            continue
        for target in wiki_targets(file.read_text(encoding="utf-8")):
            link_count += 1
            rel = file.relative_to(VAULT).as_posix()
            path, _, fragment = target.partition("#")
            if not path:
                continue
            if path in paths:
                if fragment:
                    match = re.fullmatch(r"page=(\d+)", fragment)
                    if not match:
                        errors.append(f"{rel}: unsupported PDF fragment: {target}")
                    else:
                        pdf_page_count += 1
                        p = int(match.group(1))
                        max_page = paths[path]["source_pages"] or card_page_counts.get(path)
                        if p < 1 or (max_page is not None and p > max_page):
                            errors.append(f"{rel}: PDF page out of range: {target}")
                        if paths[path]["source_bytes"] == 0:
                            errors.append(f"{rel}: page citation points to empty PDF: {target}")
                continue
            if Path(path).is_absolute() or ".." in Path(path).parts:
                errors.append(f"{rel}: unsafe wikilink: {target}")
                continue
            candidate = VAULT / path
            if not candidate.is_file() and not Path(str(candidate) + ".md").is_file():
                errors.append(f"{rel}: broken wikilink: {target}")
    coverage_path = KNOWLEDGE / "coverage.json"
    if coverage_path.exists():
        coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
        expected = {"pdf_total": len(rows), "topic_total": len({r["topic"] for r in rows}), "analysis_cards": len(cards), "analyzed_sources": sum(c.get("review_status") in ANALYZED for c in cards.values()), "zero_byte_sources": sum(r["source_bytes"] == 0 for r in rows)}
        for key, value in expected.items():
            if coverage.get(key) != value:
                errors.append(f"stale coverage.{key}: run refresh.py")
    else:
        errors.append("coverage.json absent: run refresh.py")
    report = {
        "result": "pass" if not errors else "fail", "source_commit": manifest["source_commit"],
        "sources": len(rows), "source_cards": len(cards), "wikilinks_checked": link_count,
        "pdf_page_links_checked": pdf_page_count,
        "raw_byte_integrity": "checked" if args.check_source_bytes else "not-run (manifest-backed source-link validation only)",
        "semantic_claim_review": "not-performed by this structural validator",
        "obsidian_ui_rendering": "not-run", "errors": errors, "warnings": warnings,
    }
    if args.json_report:
        args.json_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
