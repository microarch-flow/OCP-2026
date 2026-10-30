---
id: "src-b4e79b188a6e"
type: "source"
title: "Cluster-less Validation of AI Accelerator Silicon Under Real Workloads"
source_path: "ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf"
source_git_blob_sha: "f66bc91ec58a733c8ddf77d7565e40ed089e0b35"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [5, 9, 10, 11]
concepts: ["[[knowledge/concepts/ai-infra-scaleup-acceptance]]"]
---

# Cluster-less Validation of AI Accelerator Silicon Under Real Workloads

## 核心结论
Meta/Keysight用真实MTIA DUT加仿真fabric/ranks和Chakra DAG，把真实collective重叠压力提前到单芯片bring-up；核心区别是**bandwidth truth**与**state truth**：一rank一port保真带宽但限port数，多rank共port保连接/QP规模却共享带宽。[[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=2|PDF p.2]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=4|PDF p.4]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=5|PDF p.5]]

## 关键证据
训练骨架混合TP all-gather/reduce-scatter、EPall-to-all、PPp2p和DPgradient all-reduce，单算子测试不覆盖overlap造成的排队/straggler。[[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=3|PDF p.3]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=6|PDF p.6]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=12|PDF p.12]]
32rank实验为4racks×8、每rank1scale-up NIC和1scale-out NIC、2layers/stage、2microbatches，8TPgroups×4；孤立collective100iterations，与一段repeatable workload对比。[[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=8|PDF p.8]]

## 指标与条件
p.9 EPall-to-all4ranks/8MB在workload最慢2957µs vs isolation最慢2177µs，图约1.3×；p.10 DPall-reduce4ranks/64MB约55,974–60,120µs vs32,933–32,937µs，约1.8×。这些是特定重叠负载下的completion-time退化，不是不同硬件优劣。p.11CDF约90%flows slower，但未给样本量/置信区间和请求级p99。[[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=9|PDF p.9]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=10|PDF p.10]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=11|PDF p.11]]

## 图表与架构
已看p.5双模式与p.9–11图，确认min/max、µs与collective size/rank，避免把独立算子带宽当真实系统性能。

## 关联与比较
[[knowledge/concepts/ai-infra-scaleup-acceptance]]；[[knowledge/concepts/ai-infra-deployment-readiness]]。推理MoE/PD也需trace级重叠，迁移后仍须用实际推理DAG验证。

## 不确定性与待验证
1K–10Kranks、更全面多NIC/多tier latency/oversubscription/reordering为下一步；state-mode达到大rank不等于线速仿真万卡。[[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=13|PDF p.13]]
