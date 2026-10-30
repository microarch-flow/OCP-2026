---
id: "src-ba3c0b3882c6"
type: "source"
title: "Demystifying MRC and UET- A Panel of Experts"
source_path: "ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf"
source_git_blob_sha: "870071993516e0fce3342d0202163d5e0eeb49f8"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 6
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [3]
concepts: ["[[knowledge/concepts/ai-infra-multipath-failure-domains]]"]
---

# Demystifying MRC and UET- A Panel of Experts

## 核心结论
这是六页圆桌材料，唯一实质技术比较集中在 p.3；它不是完整 MRC/UET 规范，也不包含问答实录。[[ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf#page=2|PDF p.2]] [[ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf#page=3|PDF p.3]]

## 关键证据
p.3 表述：UET 1.0 为 2025、MRC 1.0 为 2026；UET 从 clean slate 出发，MRC 以 RoCE 为起点；UET libfabric（libibverbs soon），MRC libibverbs；二者共同列 packet spraying、乱序交付、traffic steering 与 SACK/NACK/timeout/trimming。此为演讲时点的对照。[[ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf#page=3|PDF p.3]]

## 指标与条件
表无吞吐/延迟/扩展效率基准，不能据此判断哪个协议更快。API 路线与发布时间不是量产生态成熟度指标。

## 图表与架构
已看原表，确认“Core Technologies”与“Loss Detection”是跨两列的共同项；避免文字提取把共享项误分给一个协议。

## 关联与比较
[[knowledge/comparisons/ai-infra-mrc-uet-and-fabric-layers]] 记录关键细节：本表把 MRC CC 简写为 NSCC，而 MRC 专门演讲说它标准化反馈信号、不强制某个 CC 算法。优先以更细粒度来源理解，不能用表格简写覆盖规范语义。

## 不确定性与待验证
“libibverbs soon”属于路线表述；需原始规范/实现测试验证 API 支持和互通。p.5 提供规范入口，但本卡不宣称已外部复核。[[ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf#page=5|PDF p.5]]
