---
id: "src-c19fabdbe95d"
type: "source"
title: "From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across"
source_path: "ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf"
source_git_blob_sha: "f7660d4552a68982af7c6ff332b5ef4b946af51f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 7, 9, 10, 12, 14, 15, 16]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [5, 10, 12]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across

## 核心结论
Ciena的scale-across方案把广域AI流量问题拆成packet congestion control与coherent optical容量两层：主机协议优化不能创造缺失的光纤容量，光层升级也不能消除长RTT反馈。[[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=2|PDF p.2]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=4|PDF p.4]]

## 关键证据
p.5按技术类别对比O-band IMDD约10km内与C+L coherent长距、多波容量；这是通用类别示意，不是所有模块的采购规格。p.7将near划为<150km、far为>150km并带ILA，是作者讨论边界，非通用标准定义。[[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=5|PDF p.5]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=7|PDF p.7]]

## 指标与条件
p.9以20Pb/s为假设，描述大量fiber pairs与C+L每fiber pair 64×800G。p.10将4→128 rails/rack称32×density，20Pb/s场景从22个huts→1个hut；这些是特定传输部署密度，不是整个数据中心功耗/成本下降32倍。[[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=9|PDF p.9]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=10|PDF p.10]]

## 图表与架构
已看p.5、10、12。p.12的51.2T C+L full-spectrum transponder以“could look like”呈现4×8×1.6T结构，是概念方向而非已交付模块。[[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]。长距离调度与网络设计应一起预算RTT、BDP、光层容量与站点故障域。

## 不确定性与待验证
p.14含2027未来方向；p.15“provably lossless”及1e-24 post-FEC BER是目标表述，不是实验已证明的绝对无丢包。推理复用相似光层组件不等于具备跨区TP/PD的SLA。[[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=14|PDF p.14]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=15|PDF p.15]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=16|PDF p.16]]
