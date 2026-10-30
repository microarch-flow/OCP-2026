#!/usr/bin/env python3
"""Rebuild manifests and marked navigation regions without writing analysis cards.

Usage: python knowledge/scripts/refresh.py [--extraction-log PATH]
No network requests; unknown page counts stay null; extraction != analysis.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

from common import ANALYZED, KNOWLEDGE, cards, generated, load_manifest, wikilink


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extraction-log", type=Path)
    args = parser.parse_args()
    manifest = load_manifest()
    rows = manifest["sources"]
    by_path = {row["source_path"]: row for row in rows}
    if args.extraction_log:
        for number, line in enumerate(args.extraction_log.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                print(f"WARNING: ignored incomplete extraction-log line {number}")
                continue
            row = by_path.get(item.get("path"))
            if row is None or item.get("sha") != row["source_git_blob_sha"]:
                print(f"WARNING: ignored unmatched extraction record at line {number}")
                continue
            if item.get("source_commit") not in {None, row["source_commit"]}:
                print(f"WARNING: ignored different-commit extraction record at line {number}")
                continue
            if row["source_bytes"] == 0:
                row["extraction_status"] = "blocked-empty"
                continue
            row["extraction_status"] = item.get("status", row["extraction_status"])
            if isinstance(item.get("pages"), int) and item["pages"] > 0:
                row["source_pages"] = item["pages"]
            for field in ("text_characters", "low_text_pages"):
                if field in item:
                    row[field] = item[field]
    found = cards()
    for row in rows:
        card = found.get(row["id"])
        row["analysis_card"] = "knowledge/sources/" + row["id"] if card else None
        row["review_status"] = card[1].get("review_status", "partial") if card else ("blocked" if row["source_bytes"] == 0 else "pending")
        # A page count declared in a note is not silently promoted to verified extraction metadata.
    (KNOWLEDGE / "source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (KNOWLEDGE / "id-map.json").write_text(json.dumps({r["source_path"]: r["id"] for r in rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    topics = defaultdict(list)
    for row in rows:
        topics[row["topic"]].append(row)
    review = Counter(r["review_status"] for r in rows)
    extraction = Counter(r["extraction_status"] for r in rows)
    count = sum(review[s] for s in ANALYZED)
    coverage = {
        "source_commit": manifest["source_commit"], "pdf_total": len(rows), "topic_total": len(topics),
        "zero_byte_sources": sum(r["source_bytes"] == 0 for r in rows),
        "analysis_cards": len(found), "analyzed_sources": count,
        "review_status_counts": dict(sorted(review.items())),
        "extraction_status_counts": dict(sorted(extraction.items())),
        "known_page_counts": sum(r["source_pages"] is not None for r in rows),
        "known_pages_total": sum(r["source_pages"] or 0 for r in rows),
        "note": "Analysis states are author declarations checked structurally by validate.py, not independent factual verification. Extraction never counts as analysis.",
    }
    (KNOWLEDGE / "coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = f"- 原始 PDF：**{len(rows)}**；主题：**{len(topics)}**；零字节：**{coverage['zero_byte_sources']}**。\n- 已有源卡：**{len(found)}**；已分析声明：**{count}/{len(rows)}**（文字分析 {review['analyzed-text']}、关键页视觉核对 {review['analyzed-visual']}）；部分分析：{review['partial']}。\n- 待分析：**{review['pending']}**；阻塞：**{review['blocked']}**；已知页数的 PDF 数：{coverage['known_page_counts']}（合计 {coverage['known_pages_total']} 页，不含页数未知文件）。\n- 提取状态：" + "；".join(f"`{key}` {value}" for key, value in sorted(extraction.items())) + "。\n\n> 清单登记、机器提取、部分阅读、文字分析、视觉核对是不同层次；以上分析状态来自源卡声明，不等于独立证实全部主张。统计由脚本从当前文件刷新，不是手工估计。"
    generated(KNOWLEDGE / "coverage.md", "coverage", summary, "# 覆盖率与处理状态\n\n返回 [[knowledge/index|总入口]]。机器可读数据：`coverage.json`。")

    table = ["| ID | 原始 PDF | 主题 | 字节 | PDF 页数 | 提取状态 | 分析 |", "| --- | --- | --- | ---: | ---: | --- | --- |"]
    for row in rows:
        analysis = wikilink(row["analysis_card"], row["review_status"], True) if row["analysis_card"] else ("阻塞：空文件" if row["source_bytes"] == 0 else "待分析")
        table.append(f"| `{row['id']}` | {wikilink(row['source_path'], row['title'], True)} | {wikilink(row['topic_note'], row['topic'], True)} | {row['source_bytes']} | {row['source_pages'] if row['source_pages'] is not None else '未知'} | `{row['extraction_status']}` | {analysis} |")
    generated(KNOWLEDGE / "source-manifest.md", "sources", "\n".join(table), f"# 来源清单\n\n返回 [[knowledge/index|总入口]] · [[knowledge/coverage|覆盖率]]。\n\n来源提交：`{manifest['source_commit']}`。原始路径、Git blob SHA、字节数及状态详见同目录 `source-manifest.json`；路径 ID 不是内容 hash。**这里是 501 项目录，不是 501 篇分析。** 显示名称来自原始文件名，未断言是 PDF 内实际演讲标题；源卡记录核对后的实际标题。原始目录与文件均保留原位。")

    topic_table = ["| 主题 | PDF | 已分析 | 部分分析 | 空文件 |", "| --- | ---: | ---: | ---: | ---: |"]
    for topic, items in sorted(topics.items()):
        note = items[0]["topic_note"]
        complete = sum(r["review_status"] in ANALYZED for r in items)
        partial = sum(r["review_status"] == "partial" for r in items)
        empty = sum(r["source_bytes"] == 0 for r in items)
        topic_table.append(f"| {wikilink(note, topic, True)} | {len(items)} | {complete} | {partial} | {empty} |")
        lines = [f"本主题：{len(items)} 份 PDF；已分析声明 {complete}；部分分析 {partial}；零字节 {empty}。", "", "| 原始资料 | 源卡 / 状态 |", "| --- | --- |"]
        for row in items:
            analysis = wikilink(row["analysis_card"], row["id"] + " · " + row["review_status"], True) if row["analysis_card"] else ("阻塞：原始文件为空" if row["source_bytes"] == 0 else "待分析，不从标题推断内容")
            lines.append(f"| {wikilink(row['source_path'], row['title'], True)} | {analysis} |")
        initial = "---\ntype: topic\ntitle: " + json.dumps(topic, ensure_ascii=False) + "\ntags: [\"ocp2026\", \"topic\"]\n---\n\n# " + topic + "\n\n返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。\n\n## 阅读路线与主题综合\n\n这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。主题综合与跨演讲阅读路线需在实际分析后补写，不能依据标题补造。\n\n<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->\n\n## 来源与分析进度"
        generated(KNOWLEDGE.parent / (note + ".md"), "topic-sources", "\n".join(lines), initial)

    navigation = []
    for folder, title in [("concepts", "跨演讲概念"), ("comparisons", "对比分析"), ("questions", "待验证问题")]:
        notes = sorted(p for p in (KNOWLEDGE / folder).glob("*.md") if p.stem != "index")
        body = []
        for path in notes:
            try:
                title_text = str(metadata_for_index(path).get("title", path.stem))
            except ValueError:
                title_text = path.stem
            body.append("- " + wikilink("knowledge/" + folder + "/" + path.stem, title_text))
        generated(KNOWLEDGE / folder / "index.md", "entries", "\n".join(body) if body else "暂无已写入条目；不把待办清单冒充跨源结论。", "# " + title + "\n\n返回 [[knowledge/index|总入口]]。")
        navigation.append("- " + wikilink("knowledge/" + folder + "/index", title) + f"：{len(notes)} 篇。")
    index_body = summary + "\n\n## 知识入口\n\n" + "\n".join(navigation) + "\n\n## 32 个主题\n\n" + "\n".join(topic_table)
    initial_index = "# OCP-2026 语料集 · 可追溯知识库\n\n**把整个仓库作为 Obsidian vault 打开**，然后打开本页。原始 PDF 留在原目录；所有新增分析与导航都在 `knowledge/`。没有插件或额外服务要求。\n\n## 怎么读\n\n1. 从下方主题进入已经写成的源卡；重要结论可点击原 PDF 页级证据。\n2. 查看概念与比较页理解跨演讲联系；区分原始主张、我们的归纳和未验证问题。\n3. 用 [[knowledge/source-manifest|完整来源清单]] 查未读/空文件，用 [[knowledge/coverage|覆盖率]] 看真实范围。\n4. 维护者先读 [[knowledge/AGENTS|维护约定]]；历史变更见 [[knowledge/log|编译日志]]。\n\n> 本知识库借鉴 [Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)，采用“原始资料 + 互链知识 + 维护规则”，不是单纯给每份 PDF 生成空摘要。\n\n## 当前覆盖"
    generated(KNOWLEDGE / "index.md", "navigation", index_body, initial_index)
    print(json.dumps(coverage, ensure_ascii=False, indent=2))


def metadata_for_index(path):
    from common import metadata
    return metadata(path)


if __name__ == "__main__":
    main()
