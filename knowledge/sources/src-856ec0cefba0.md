---
id: "src-856ec0cefba0"
type: "source"
title: "Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs"
source_path: "ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf"
source_git_blob_sha: "1dde307131c296c53409e7a6ed7bb50d7bf3696a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 20
review_status: "analyzed-visual"
evidence_pages: [2, 6, 8, 9, 11, 12, 14, 15, 16, 19]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [9, 12, 16]
concepts: ["[[knowledge/concepts/ai-infra-scaleup-acceptance]]"]
---

# Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs

## 核心结论
Delos Data/Eridu提出compute与switching分机架、高radix optical连接、单跳数千端点的开放scale-up，以减少小domain placement碎片；是新workstream/reference architecture提案，不是已交付5120GPU产品。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=2|PDF p.2]] [[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=8|PDF p.8]] [[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=19|PDF p.19]]

## 关键证据
p.9布置表为128端点1row/~4m，2048为5rows/~15m，5120为12rows/~30m；p.12有12row布局。长度基于layout示例，光链预算、端点数、radix和端口带宽仍需产品验证。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=9|PDF p.9]] [[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=12|PDF p.12]]
单大域使placement更简单但可能扩大失败域；这是本知识库从架构导出的风险，原文只强调flat domain收益。

## 指标与条件
p.16引用Turbalance训练**simulation**：230Tswitch GPUutil64%→petabit88%，相对约37.5%（图写38%），不是增加38个百分点，也不是实测推理goodput。缺模型、仿真假设与成本/功耗边界，不能证明cost/token降幅。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=16|PDF p.16]]
p.6各厂商announced规模与single-hop规模为作者整理，未外核，不能当当前采购目录。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=6|PDF p.6]]

## 图表与架构
已看p.9、12layout与p.16donut图，确认模拟脚注；p.11仍有“ToDo:Simplify”，不视作冻结设计。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=11|PDF p.11]]

## 关联与比较
[[knowledge/concepts/ai-infra-scaleup-acceptance]]；[[knowledge/concepts/ai-infra-inference-serving-shapes]]。扩大domain须测拓扑、故障、KV/collective关键路径，而不只radix。

## 不确定性与待验证
petabit silicon/system co-design、power/cooling/packaging未给PPA或实硅；新workstreamkickoff计划earlyNovember，日期未定。[[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=14|PDF p.14]] [[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=15|PDF p.15]] [[ai-clusters/Breaking-up-the-Monolith-An-Open-Architecture-for-Multi-rack-Scale-up-Domain-of-5000-GPUs.pdf#page=19|PDF p.19]]
