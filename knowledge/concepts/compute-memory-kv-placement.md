---
type: concept
title: "KV placement：复用缓存、活动注意力与近存计算的不同路径"
tags: [ocp2026, concept, compute-memory]
---

# KV placement：复用缓存、活动注意力与近存计算的不同路径

## 核心判断
“KV offload”不是一个统一访问模式。**可复用prefix的bulk检索、decode时的活动KV随机读取、共享KV的元数据管理、PNM上的partial attention**，各自的带宽、时延、容量和一致性需求不同。不能只给每种介质一个GB/s数字就预测性能。

## 三类主要数据路径
| 路径 | 搬什么/谁算 | 关键条件 | 来源 |
|---|---|---|---|
| Cached-prefix恢复 | 外部KV块回到GPU，省prefill重算 | reuse、工作集、批量传输、TTFT | [[knowledge/sources/src-7961ff4d5709|Micron]]、[[knowledge/sources/src-f667d06e3a4e|Astera]] |
| 活动稀疏attention | indexer/TopK选择后按需gather少量KV | 小访问粒度、IOPS、串行critical path；prefetch可能很弱 | [[knowledge/sources/src-de2863526a98|Alibaba]] p.9/12 |
| Hybrid GPU+PNM | GPU算hit pages、PNM算miss pages，回传partial attention结果后merge | PNM算力、结果缩减比、batch并行、merge数值语义 | [[knowledge/sources/src-c5ad8983371c|PNM实验]] p.28/29 |

另一个正交维度是 **共享与管理服务**：Maru用shared pool减少跨worker副本；Marvell把hash/lookup/serde/compression等服务放到near-memory Arm。它们不自动等于“attention在内存里算”。

## 预取为何在一些材料有效、另一些无效
- XCENA讨论调度时已知道大KV blocks的long-doc QA；pin共享prefix，提前把SSD数据搬进DRAM。inflight1 lookahead526ms接近DRAM509ms；inflight8则2564ms对1484ms，接近程度下降。[[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=17|PDF p.17]] [[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=18|PDF p.18]]
- Alibaba的稀疏attention示例按layer串行indexer→TopK→gather，约584B/token/layer、低空间局部性，并假设0%prefetch收益。[[Server：Composable Memory Systems/Beyond DRAM- Byte-Addressable Persistent Memory via Compute Interconnects for AI.pdf#page=9|PDF p.9]]
- 两者并不矛盾：**工作负载揭示未来地址的时点不同**。预取可用性应是workload/operator属性，而不是SSD/CXL器件固有属性。

## GPU-direct需要写清协议
Astera与Marvell的P2P DMA可绕过host DRAM；Marvell明确GPU端不需要CXL。Alibaba下一代UALink图是native load/store/atomics。Maru共享memory语义的“zero-copy”减少staging/副本，不代表不消耗链路带宽。把它们都称为“GPU直接访问远端内存”会隐藏实际实现限制。

## 一个可执行的分解模型（分析建议）
1. **占用**：weights、active KV、reusable KV、metadata分别计容量，留runtime workspace余量。
2. **访问**：每token/每request多少字节、读写比例、粒度、稀疏性、地址提前可知时间。
3. **传输**：路径跳数、带宽、queue/credit、DMA setup、并发争用、read amplification。
4. **计算**：重prefill、dequant/serde、PNM partial attention、merge分别计时与能耗。
5. **策略**：admission、evict、pin、prefetch、compress、dynamic resize显式建模。
6. **SLO**：先判断容量/链路是否可行，再输出TTFT/TPOT/throughput及分位数，不用单一roofline掩盖capacity cliff。

## 选择PNM的条件
当必须扫描的大输入留在内存侧而返回结果很小，且PNM算力足够时，计算搬迁可换取有效带宽。PNM hybrid attention的batch1仅5.28→5.50tok/s，而batch5到17.7tok/s，说明offload收益依赖并发和可隐藏开销。[[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=29|PDF p.29]] 不能只以“内存带宽高”决定所有算子下沉。

## 关联
[[knowledge/concepts/compute-memory-capacity-vs-datapath|收益归因]] · [[knowledge/concepts/compute-memory-federated-model-contract|多保真模型契约]] · [[knowledge/concepts/compute-memory-cxl-failure-domain|可观测故障与恢复]]。
