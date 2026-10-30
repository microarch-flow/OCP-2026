---
type: concept
title: "从数据语义到分区、放置与异构执行 IR"
tags: [ocp2026, concept, compute-memory]
---

# 从数据语义到分区、放置与异构执行 IR

## 核心命题
描述“算什么”与“在哪儿、何时、以什么数据契约执行”应分开，但不能互相失联。统一 graph IR 不自动带来统一 memory model，更不自动实现多设备最优放置。

## 材料中的三条互补路径
|路径|解决问题|不能替代的部分|
|---|---|---|
|Reffine Field/Operator + 稀疏 lowering|把关系/图/stream 表成稀疏坐标空间，符号边界支持并行化|硬件拓扑、传输成本、多租户调度。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=20\|PDF p.20]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=24\|PDF p.24]]|
|Nacho expression+format+distribution cost|按实际稀疏工作量分区，避免只按坐标等分|数据变化后的重分区成本和跨设备通信。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=31\|PDF p.31]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=44\|PDF p.44]]|
|PJRT/SPEL/PXL backend|接入 buffer、executable、event、compiler/runtime|自动选择 GPU/CPU/NDP、维护 locality 和语义正确性。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=9\|PDF p.9]] [[fti-workshop-data-centric-computing/Bringing-General-Purpose-Parallel-Programming-to-Near-Data-Processing.pdf#page=16\|PDF p.16]]|

## 面向架构探索的最小表达建议（本库推论）
1. **DataObject**：逻辑 ID、format、shape/stride、size、immutable/mutable、alias、权限、生命周期。
2. **Region/Operation**：函数与质量约束、读写集合、稀疏分布/工作量估计、可允许的执行单元。
3. **Placement**：每对象和算子所在层级、memory residency、replication/sharding、local/remote 一致性方案。
4. **ExecutionPlan**：依赖 DAG、DMA/doorbell/event、允许的 overlap、fallback、故障传播。
5. **CostObservation**：实测/模拟/假设标记，条件、误差及适用范围；避免把 peak BW 填成 effective BW。

对象语义可使 allocation hint 或不可变共享成为优化依据，而不是把所有数据压成无结构 byte array。[[fti-workshop-data-centric-computing/Open-Object-Formats-for-Near-Data-Processing.pdf#page=9|PDF p.9]] [[fti-workshop-data-centric-computing/Open-Object-Formats-for-Near-Data-Processing.pdf#page=23|PDF p.23]]

## 必须保留的两种非均匀性
- **空间非均匀性**：CXL、host DRAM、HBM、SSD 的访问与容量不同；shared virtual address 不意味着等成本、等 coherence。
- **工作量非均匀性**：相同 shape/nnz 的算子也可能因 format、nonzero distribution、分区边界和缓存复用不同而耗时不同。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=31|PDF p.31]]

## 评估顺序
先证明语义和功能路径正确，再同容量/同质量比较 placement，然后加入并发/SLO 和故障。用 p99 时必须测联合请求分布，不能把各阶段 p99 相加。SFC-CA 的 GEMM 通信下界也只能在其假设内使用，不能据此保证所有图任务的最优网络扩展。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=16|PDF p.16]]

## 关联
[[knowledge/concepts/compute-memory-ndp-contract|近数据卸载四类契约]] · [[knowledge/concepts/compute-memory-kv-placement|KV 放置]] · [[knowledge/concepts/compute-memory-federated-model-contract|联邦仿真模型契约]]
