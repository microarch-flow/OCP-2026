---
id: "src-3f525f18fc6b"
type: "source"
title: "SSD 作为 LLM KV 性能层：近 DRAM TTFT 与耐久约束并存"
source_path: "storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf"
source_git_blob_sha: "da7e63597485db79e93aab0b62cc30399adb51a5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [9, 11]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# SSD 作为 LLM KV 性能层：近 DRAM TTFT 与耐久约束并存

> 阅读范围：已阅读本文件全部可提取文字（18页）。关键页已视觉核对：9, 11；不代表逐页视觉审核。

## 核心结论

在 prefix cache 命中时，避免重复 prefill 使数据搬运成为关键路径；SSD 可以成为性能层，但必须同时配置内部/多盘并行、PCIe 带宽、CPU I/O 以及每日写入耐久。近 DRAM 的结果限定于给定软件、负载与 cache capacity，不能推广到任意 serving p99。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=5|PDF p.5]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=6|PDF p.6]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=7|PDF p.7]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=11|PDF p.11]]

## 关键证据

- 测试配置：vLLM 0.9.1、LMCache 0.3.1、Qwen3-14B BF16、H100 PCIe Gen5 x16、Gen5 NVMe、基于 io_uring 的异步多线程 I/O。microbenchmark 为 100% hit，macrobenchmark 为 ShareGPT 多轮 QPS sweep，DRAM/SSD cache capacity 相等。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=7|PDF p.7]]
- 同样大小 chunk 的 SSD retrieval 仍有延迟变化，队列初始积累与不规则 completion 没被吞吐优化消除。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=12|PDF p.12]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=13|PDF p.13]]
- KV-aware interface 与更多 PCIe allocation 是下一步建议，而不是此结果中已经验证的性能收益。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=14|PDF p.14]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=15|PDF p.15]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=17|PDF p.17]]

## 指标与条件

p.9 microbenchmark：未调优的四盘 TTFT 仍约为 memory baseline 1.26–1.92×；调 chunk 与 io_uring 后约 1.07–1.14×，含义是延迟仍高 7–14%，不是“快 7–14%”。macrobenchmark 展示吞吐接近及饱和后的 TTFT 陡升；没有 p99 或 TPOT 数据。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]]

Qwen3-14B 场景 daily KV writes 可达约 57.5 TB/GPU/day。来源定义每盘 endurance-bound capacity = total daily writes/(SSD 数×DWPD)；p.11 的 SLC/TLC/QLC 容量点依赖未完整列出的 endurance 假设，不能作无条件容量推荐。OP/ZNS/FDP 的收益也需具体 workload 验证。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=10|PDF p.10]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=11|PDF p.11]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=16|PDF p.16]]

## 图表与架构

已视觉核对 p.9 的 latency ratio、micro/macro 区别与饱和曲线，p.11 的耐久容量图。长 TTL 的 working-set 图使用指定数据集，不等同所有聊天业务；提供商 TTL 描述只视为来源背景，未验证其当前产品政策。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=3|PDF p.3]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=11|PDF p.11]]

## 关联与比较

与 Samsung KV$ 材料互补：这里测 serving TTFT，后者 FDP 测 storage replay object latency，两者不能横向相减或拼接成一个端到端收益。共同设计问题是“重算、保留和取回”的成本分界。

## 不确定性与待验证

缺少 SSD 型号、容量、固件、精确 IO 配置、请求分布、重复次数、置信区间、功耗和成本。100% hit 是 microbenchmark 上限条件；实际命中率和排队会改变收益。没有已证实的 p99 SLA 或生产 TCO。[[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=7|PDF p.7]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]][[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=12|PDF p.12]]

