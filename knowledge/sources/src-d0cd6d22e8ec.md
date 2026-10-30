---
id: "src-d0cd6d22e8ec"
type: "source"
title: "02_AI Computing Continuum Extending the Open Data Center Ecosystem Across"
source_path: "ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf"
source_git_blob_sha: "8dd8c0a32cfaaaf6f765b2d1df81d4a27aa69a32"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 16, 17]
tags: ["ai-infra", "ai-computing-continuum"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [6, 16]
concepts: ["[[knowledge/concepts/ai-infra-deployment-readiness]]"]
---

# 02_AI Computing Continuum Extending the Open Data Center Ecosystem Across

## 核心结论
AICC聚焦hyperscale-adjacent：colo、enterprise、telco PoP、工业/本地场景，用开放模块降低分散站点的部署差异，而非把完整高密度机架按比例缩小。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=4|PDF p.4]] [[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=5|PDF p.5]] [[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=9|PDF p.9]]

## 关键证据
约束包括旧19英寸机柜、空间、功率/散热限制、远程管理、规模渐增；MHS/DC-SCM/Open Rack是可复用building blocks，不代表所有站点采用相同scale-up规模。wired与wireless接入也应按SLO分层。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=3|PDF p.3]] [[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=6|PDF p.6]] [[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=7|PDF p.7]] [[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=8|PDF p.8]]

## 指标与条件
p.6给1GPU约0.8–2kW短深度、8GPU scale-up约8–15kW等场景区间，属于架构示意，不是产品统一额定值或实测整机功耗。不能以其反推cost/token。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=6|PDF p.6]]

## 图表与架构
已看p.6部署谱系与p.16规格目标。后者明确未来12个月预期贡献：hyperscale-adjacent rack/server、APN NIC/SmartNIC、Edge-MHS修订、无线AuRU/bridge board等；不是全部已发布规范。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=16|PDF p.16]]

## 关联与比较
[[knowledge/concepts/ai-infra-deployment-readiness]]；[[knowledge/concepts/ai-infra-locality-and-control-timescales]]。页内议程明确2026-10-13，不仅依仓库名判年。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=4|PDF p.4]]

## 不确定性与待验证
该讲是initiative与路线图，无benchmark/BOM/SLA。需把具体用例配对到硬件规格、管理/安全接口和可复现case study，原文也以此作为下一年优先事项。[[ai-computing-continuum/02_AI Computing Continuum Extending the Open Data Center Ecosystem Across.pdf#page=17|PDF p.17]]
