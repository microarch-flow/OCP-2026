---
id: "src-e3d8ea7e9b34"
type: "source"
title: "NVMe I/O 优先级：从队列权重到端到端延迟契约"
source_path: "storage/IO-Prioritization-for-Optimized-Command-Handling.pdf"
source_git_blob_sha: "35b28482b8519aa44b53dfa77cb8073d1c83309d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-text"
evidence_pages: [5, 6, 8, 9, 11, 12, 13, 14, 15]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# NVMe I/O 优先级：从队列权重到端到端延迟契约

> 阅读范围：已阅读本文件全部可提取文字（16页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

TP4221 材料讨论按 submission queue 声明优先级及 duration limit，让紧急 I/O 不被后台批量工作阻塞，同时维持低优先级进度。这是提案及厂商经验，不是已统一实现的端到端延迟保证。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=5|PDF p.5]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=6|PDF p.6]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=9|PDF p.9]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=15|PDF p.15]]

## 关键证据

- Google 指出限带宽不等于限延迟，WRR 也不自动考虑 I/O 的资源成本；提出按 NAND media-time 做调度的经验。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=6|PDF p.6]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=8|PDF p.8]]
- NVIDIA 说明小/中请求队列也能阻塞大而高优先级的 I/O，需要考虑完成时限与全链路资源。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=9|PDF p.9]]
- 若临近 deadline 就提升低优先级请求，可能反过来破坏优先级隔离；需要明确 admission、降级和最低进度语义。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=13|PDF p.13]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=14|PDF p.14]]

## 指标与条件

媒体时间 WFQ 页声称 p50 降低 20%、p99 降低 50%，但没有提供设备、请求分布、基线、样本量与测试时长；不能作为通用收益。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=8|PDF p.8]]

示例场景之一：高优先级 QD1 4K random read，与低优先级 QD1024、4K 70/30 read/write 共存；另列 16K 读 burst、后台 10 MB/s 随机写等。500 µs@99.99%、1 ms@99%、10 ms mean 是服务等级目标示例，不是达标实测。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=12|PDF p.12]]

## 图表与架构

未视觉核对架构图；本卡没有推断图中未被文字表达的队列或时序关系。

## 关联与比较

与高容量 QLC 的映射策略应联合分析：更大 IU/元数据 miss 会改变单次 I/O 的介质成本，单纯按请求条数分权未必维持公平或尾延迟。此为跨源推论，不是本提案的实验结论。

## 不确定性与待验证

需要验证 Linux/驱动/控制器实现、队列映射、超载行为、后台 GC、热节流和故障恢复期间的优先级保持。p.11 对 Linux 支持状态是演讲时点描述，不应当作永久事实。[[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=11|PDF p.11]][[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=13|PDF p.13]]

