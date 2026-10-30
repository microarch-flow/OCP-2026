---
id: "src-e67fbded1ca5"
type: "source"
title: "高容量 HDD：SAS4、NVMe 与每 TB 性能预算"
source_path: "storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf"
source_git_blob_sha: "58235006c6a64731073735913a3540d887274cbb"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 8, 9, 10, 11]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [6, 7, 8]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# 高容量 HDD：SAS4、NVMe 与每 TB 性能预算

> 阅读范围：已阅读本文件全部可提取文字（12页）。关键页已视觉核对：6, 7, 8；不代表逐页视觉审核。

## 核心结论

容量扩张不能只看单盘 TB；必须同时给出 MB/s/TB、IOPS/TB、共享上行和功耗预算。SAS4/NVMe 的选择取决于盘数与介质吞吐倍数，接口升级本身不增加机械随机 IOPS。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=5|PDF p.5]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=6|PDF p.6]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=8|PDF p.8]]

## 关键证据

- 架构模型为 head node 经 HBA/PCIe root 与 switch 到 JBOD，所有盘共享上行；因此单盘链路带宽不是机箱可实现带宽。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=6|PDF p.6]]
- 演讲建议标准化吞吐/IOPS multiplier 的发现与报告，并建立共同 benchmark；这是生态行动建议而非既有统一测试结果。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=11|PDF p.11]]
- 容量、吞吐、IOPS、功耗之外还列出振动等系统约束；盘级优点需要重新在完整机箱中验证。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=9|PDF p.9]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=10|PDF p.10]]

## 指标与条件

p.6 明示 aggregate-link 模型：单盘基线 275 MB/s、JBOD 上行 8 lanes。32 盘时最高吞吐倍率分别为 SAS3 1×、SAS4 2×、PCIe5 3×、PCIe6 6×；64 盘时变成 <1×、1×、1×、3×。这些是给定拓扑的模型边界，不是实测盘速。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=6|PDF p.6]]

9 MB/s/TB 目标模型采用 275 MB/s、70% fill 与每增量倍率 70% efficiency，表中 1×/4× 对应约 44/135 TB；5 IOPS/TB 的另一模型使用 140 IOPS、相同填充/效率假设，1×/4× 对应 40/124 TB。这里容量是模型可支撑点，不是已交付 HDD 规格。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=7|PDF p.7]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=8|PDF p.8]]

## 图表与架构

已核对 p.6 上行瓶颈图及 p.7–8 曲线、表格和脚注。曲线描述随容量增长的单位容量性能下降；不能把整盘容量、填充率和可用容量混用。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=6|PDF p.6]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=7|PDF p.7]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=8|PDF p.8]]

## 关联与比较

与高容量 QLC 的“少 DRAM”问题相似：削减某项单位容量成本可能把瓶颈推给其他层。采购应把容量价格、正常工作负载性能和降级/重建窗口一起建模，而不是只比较接口代际。

## 不确定性与待验证

模型没有给出具体盘型、寻道分布、队列深度、混合读写、机箱振动测试、尾延迟或功耗测量；无法据此推算端到端存储 SLA。接口标称 Gb/s 与用户有效 GB/s 也不是同一指标。[[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=5|PDF p.5]][[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=10|PDF p.10]]

