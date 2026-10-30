---
id: "src-d4ac456fb37b"
type: "source"
title: "KV$ 垂直优化：寿命分组降低 WAF，大传输降低 CPU 成本"
source_path: "storage/Vertical-Optimizations-for-KV-Infrastructure.pdf"
source_git_blob_sha: "0bb31700b165d53bd613eaccd82d1a2b6335725c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 7]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# KV$ 垂直优化：寿命分组降低 WAF，大传输降低 CPU 成本

> 阅读范围：已阅读本文件全部可提取文字（10页）。关键页已视觉核对：4, 5, 6, 7；不代表逐页视觉审核。

## 核心结论

KV cache 是可重算且短暂的数据，保留策略应比较 DRAM 容量、SSD retrieval 与 recompute 成本。材料展示 FDP 寿命分组与传输粒度的分别优化，但 storage replay 结果不是 serving TTFT 实验。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=3|PDF p.3]][[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]][[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=7|PDF p.7]]

## 关键证据

- 图示把 HBM 保留为 live execution home；L1 在 pinned DRAM、Device-DAX 或 GDS NVMe 中三选一，不是三个同时叠加；P2P 依赖连续 pinned-DRAM L1。此限制属于图中实现，不能泛化所有 cache 框架。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=4|PDF p.4]]
- 软件图分开 control plane 与 data transfer owner，并列 lookup/probe/prefetch/retrieve/release；是否先 probe、由谁传输都影响 CPU 与调度成本。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=5|PDF p.5]]
- FDP 以 workload class/cache_salt 对应 PID/RUH，让相似寿命一起回收，减少跨流搬迁；页面将 chat、long-context、RAG、low-reuse、metadata-heavy 分开。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]]

## 指标与条件

p.6 标为 measured effect：PM9D3a、960 GiB configured、89% utilized、4× capacity writes、9 workers、855 GiB synthetic LMCache trace；每次运行前 sequential fio prefill。WAF 2.600→1.425（−45.2%），p90 object-I/O write/read latency −29.4%/−22.0%。脚注明确这不是 serving TTFT。平均 write 标注 25,364.155→11,249.847 ms，必须保留其 object-level 粒度，不能误作单个块 I/O 延迟。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]]

p.7 的右侧文字声称 CPU 成本从约 473–592 降到 38–57 Mcycles/GiB（10–12×），但同页图在相同 3 GiB/s read rate 下，128 KiB 起点约为 io_uring 330、libaio 365 million CPU cycles/GiB，和文字基线不一致；因此不能把 10–12× 当作图形已验证的倍率。simulation 约 23 Mcycles/GiB 是预测，不是测量。超过 4 MiB 后收益递减，circle 点还使用 contiguous huge-page buffer，故不可把所有差异仅归因于 transfer size。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=7|PDF p.7]]

## 图表与架构

已视觉核对 p.4–7，包括文字提取遗漏的架构、FDP 条件与脚注。p.6 latency reduction 与 p.7 CPU cycle reduction 不可相乘为总体性能提升。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=4|PDF p.4]][[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=5|PDF p.5]][[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]][[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=7|PDF p.7]]

## 关联与比较

与 SK hynix KV serving 实验应分层阅读：这里证实所列 replay 下存储侧与 CPU 路径改善；后者讨论真实多轮 TTFT。下一步应把同一 workload、容量、命中率、耐久和 serving SLA 放进同一试验。

## 不确定性与待验证

未给重复次数、置信区间、完整 trace/commit 与跨 SSD 复现实验。p.8 提议贡献可复现 workload/config，说明社区标准化仍在讨论，不等于已形成统一 benchmark。[[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=8|PDF p.8]]

