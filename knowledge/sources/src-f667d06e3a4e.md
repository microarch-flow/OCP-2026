---
id: "src-f667d06e3a4e"
type: "source"
title: "Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath"
aliases: ["Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath"]
speakers: "Moshe Twitto — Fellow; Amit Golander — Associate VP, Astera Labs"
source_path: "Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf"
source_git_blob_sha: "7caf83063506df99e2f5912debd5ea10532ce513"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 6, 7, 8]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-capacity-vs-datapath]]", "[[knowledge/concepts/compute-memory-kv-placement]]"]
---

# Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath

## 核心结论
用 PCIe fabric 将 GPU KV-offload 流量直接送到 memory controller，避免所有流量绕行 CPU DRAM。**该实验最强的结果是低成本可扩容路径；2×/3× 并不是等容量条件下隔离出的纯 P2P 加速。** 相同128GB容量、短prompt时，讲者反而报告与host memory基本相同。[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=3|PDF p.3]] [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=6|PDF p.6]]

## 关键证据
- 目的包括分散带宽瓶颈、扩展容量、把 CPU 内存带宽留给 agent 工具负载，以及可能避免第二CPU socket。最后一项是潜在系统优化，不是本文完成的双socket等价对照。[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=3|PDF p.3]]
- LMCache 加入多region virtual allocator：host pinned DRAM 与各 Leo PCIe BAR region 具有独立地址空间/leaf allocator，上层通过 allocate/free/batched_allocate 和可插拔策略选择目标。不是把所有异构介质假定成同延迟统一内存。[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=5|PDF p.5]]
- 4×RTX6000 Pro、1×Xeon Platinum8468、4×Leo控制器（每个256GB DDR5-5600）、320-lane Scorpio switch；4个Qwen3-14B实例，vLLM0.19、修改版LMCache0.4.3、DMA、128-token chunk。输出100–150 tokens、3–8 turns、每turn120–180 tokens、batch10–60。[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=4|PDF p.4]]

## 指标与条件
| 图 | prompt | host baseline | fabric方案 | 可以归因什么 |
|---|---|---|---|---|
| p.6 | 1–2K | 每实例128GB | 每实例128GB | 同容量短prompt基本等性能 |
| p.7 | 2–3.5K | 4×128GB | 4×256GB | 图中约2×为容量+路径共同改变 |
| p.8 | 5–6.5K | 4×128GB | 4×(256+128)GB | 图中约3×为混合扩容，非纯P2P |
[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=6|PDF p.6]] [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=7|PDF p.7]] [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=8|PDF p.8]]

图纵轴 **RPS/GPU**，横轴 **output tokens/sec/user**：是吞吐与单用户速度的tradeoff，不是总output tokens/s，更不是p99。未提供实际DIMM/控制器/CPU价格、功耗或总TCO。p.4把96GB GPU memory写为“HBM”，本库保留GPU型号但不据该标签确认其物理内存类型；应在复现实验时核对BOM。

## 图表与架构
已核对 p.3 P2P 流量绕过CPU上行的示意和p.6–8完整性能图。p.6脚注中的CPU可扩至3TB、controller可扩至4TB是更大规模/更长运行的设想，**不是本组已测配置**。

## 关联与比较
[[knowledge/concepts/compute-memory-capacity-vs-datapath|容量收益与数据路径收益的归因]]；[[knowledge/concepts/compute-memory-kv-placement|KV placement 的三种数据路径]]。与Micron模型一致：容量可改变reuse，不能把收益全部归到raw bandwidth。

## 不确定性与待验证
等容量、等DIMM代际、等预算三种实验应分开；还需要CPU background workload、PCIe拓扑/ACS/IOMMU要求、chunk大小敏感性、TTFT/TPOT分位数与多租户干扰。p.9说明LMCache增强已完成，standalone vLLM fabric支持仍进行中，SGLang/Dynamo为合作方向，不代表所有框架已原生支持。


## 原始页码导航
[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=2|p.2]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=3|p.3]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=4|p.4]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=5|p.5]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=6|p.6]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=7|p.7]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=8|p.8]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=9|p.9]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=10|p.10]]
