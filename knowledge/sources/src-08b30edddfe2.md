---
id: "src-08b30edddfe2"
type: "source"
title: "BUILDING AI RACK SYSTEM WITH OPEN STANDARDS"
source_path: "ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf"
source_git_blob_sha: "45921aa1256afa3946e92a9dc286fb91e8838da3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 11]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [2, 3, 6]
concepts: ["[[knowledge/concepts/ai-infra-multipath-failure-domains]]"]
---

# BUILDING AI RACK SYSTEM WITH OPEN STANDARDS

## 核心结论
HPE/AMD Helios以72GPU、UALoE shared ld/st scale-up、可编程Pensando NIC和rack级fabric manager组合开放机架。关键不只是带宽，还包括vPod分区/故障域、LLR和可演进transport。[[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=3|PDF p.3]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=4|PDF p.4]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=5|PDF p.5]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=6|PDF p.6]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=7|PDF p.7]]

## 关键证据
vPod概念可组合GPU，但FCS allocation限定compute-tray粒度；同vPod recovery影响其中所有jobs，VLAN隔离不等于每GPU独立失败域。[[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=6|PDF p.6]]
AINIC面向front-end、RDMA、NVMeoF等角色；支持协议列表/programmable datapath不证明每个模式已同等量产验证。[[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=7|PDF p.7]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=8|PDF p.8]]

## 指标与条件
p.2 rack汇总72GPU/31TB HBM4/260TB/s scale-up/1.7PB/s HBM/43TB/s scale-out/2.9Exaflops；精度与稀疏口径未给，不用于模型吞吐比较。
p.3每GPU scale-up1.8TB/s/**direction**、scale-out up to2.4Tb/s/**direction**；单位TB与Tb不同。72×1.8×2≈259.2TB/s，提示p.2可能汇总双向，但原页未标，不擅自统一比较。12TH6switches、18compute trays为该参考配置。[[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=2|PDF p.2]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=3|PDF p.3]]

## 图表与架构
已看p.2–3与p.6，确认ld/st跨pod与vPod实际约束；不把架构峰值当effective collective bandwidth。

## 关联与比较
[[knowledge/concepts/ai-infra-multipath-failure-domains]]；[[knowledge/concepts/ai-infra-observability-contract]]：管理、partitioning、fault containment和counter支持共同影响推理可售SLA。

## 不确定性与待验证
无实测模型/p99/功耗/成本、FCS日期或protocol互通矩阵；MRC microsecond recovery为性能方向，无本页原始测试。[[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=9|PDF p.9]] [[ai-clusters/BUILDING AI RACK SYSTEM WITH OPEN STANDARDS.pdf#page=11|PDF p.11]]
