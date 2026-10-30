---
type: concept
title: "近数据卸载：函数、数据、执行与资源的四类契约"
tags: [ocp2026, concept, compute-memory]
---

# 近数据卸载：函数、数据、执行与资源的四类契约

## 核心命题
把计算移到数据附近需要四种契约同时成立。只给统一函数名，或只让 host/device 看到同一 pointer，都不足以建立可移植、可预测的系统。这是本库综合推论，不是某项 OCP 已批准规范。

|契约|必须表达|材料支持|
|---|---|---|
|函数语义|operation、dtype/shape、数值误差、side effects、算法质量/recall|[[knowledge/sources/src-0e22a543f8f9]]；[[knowledge/sources/src-5a74ab1ff3cb]]|
|数据语义|对象身份、地址/offset、layout/stride、所有权、生存期、可变性、coherence、权限|[[knowledge/sources/src-6931b04fc946]]；[[knowledge/sources/src-d3922ae0a378]]|
|执行语义|提交/完成、依赖、同步、fallback、错误、重试/幂等|[[knowledge/sources/src-5a74ab1ff3cb]]；[[knowledge/sources/src-d3922ae0a378]]|
|资源与放置|resident bytes、local/remote path、带宽与 compute、NUMA/拓扑、并发及多租户配额|[[knowledge/sources/src-3ded8c0c80fb]]；[[knowledge/sources/src-cb9ec6c9c6ee]]|

## 卸载的必要记账
用相同算法/质量、相同有效容量做对照，然后分别记：
- host raw-read bytes、device local bytes、result bytes、控制消息数；
- dispatch/queueing/local compute/transfer/sync 及可重叠部分；
- pool occupancy、GPU HBM 被释放的时间、CPU work、端到端 SLO。

例如向量检索的约 60× 数据量减少是带宽机会，不是 60× 服务加速；原页甚至有 96D/768D 标注冲突，应先完成算术和条件核对。[[fti-workshop-data-centric-computing/Bridging-Compute-and-Memory-Fabric-Data-Services-for-Direct-XPU-Access.pdf#page=9|PDF p.9]]

## 三种不同的“零复制”
1. **不复制对象表示**：稳定 offset/object reference 避免序列化，但引用解析与映射仍有成本。[[fti-workshop-data-centric-computing/Open-Object-Formats-for-Near-Data-Processing.pdf#page=24|PDF p.24]] [[fti-workshop-data-centric-computing/Open-Object-Formats-for-Near-Data-Processing.pdf#page=26|PDF p.26]]
2. **不把大状态搬回 host**：近端 GEMV/search 返回小结果，但设备本地 DRAM 仍需读取，控制提交也存在。[[fti-workshop-data-centric-computing/Bringing-General-Purpose-Parallel-Programming-to-Near-Data-Processing.pdf#page=15|PDF p.15]]
3. **不经 host staging**：GPU direct 数据路径仍可能有小 I/O 放大、polling 与 access-control 成本。[[fti-workshop-data-centric-computing/Bridging-Compute-and-Memory-Fabric-Data-Services-for-Direct-XPU-Access.pdf#page=7|PDF p.7]]
三者不能互相替代，也不能推导出“无通信开销”。

## 与推理服务的连接
context→prefill→decode 的 context 阶段可能包括大量不规则检索和 tokenization；只有 profile 确认其在 critical path，近数据硬件才可能改善用户指标。[[knowledge/sources/src-8b394680b55e]]
共享池 tokenization 复用的实际实验与移除 tokenization 的 oracle 消融必须分开；稀疏 KV selection 还必须同时报告质量。[[knowledge/sources/src-462ae941f171]]

## 可操作的验证矩阵（本库建议）
同一 workload 至少比较：CPU 原地；GPU direct 拉原数据；近端固定函数；近端通用 kernel。固定 capacity、batch、precision、recall、并发分布，再测 p50/p99、goodput、J/query 和错误恢复。没有这些条件时，先记录功能可行性，不填写虚构性能常数。

## 关联
[[knowledge/concepts/compute-memory-capacity-vs-datapath|容量与数据路径归因]] · [[knowledge/concepts/compute-memory-partitioning-placement-ir|分区与放置 IR]] · [[knowledge/concepts/compute-memory-cxl-failure-domain|CXL 故障域]]
