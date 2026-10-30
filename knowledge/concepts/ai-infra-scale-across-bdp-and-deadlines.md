---
type: "concept"
title: "跨站点 AI：从 BDP 到请求关键路径"
tags: ["ai-infra", "inference-architecture"]
---

# 跨站点 AI：从 BDP 到请求关键路径

## 核心定义
Scale-across只说明资源跨站点，不说明一次请求内的交互粒度。先区分可流水化的数据加载、复制一致性、每token KV/collective、任务级调度，再评估距离。以下是本知识库跨源归纳，不是所有厂商共同批准的标准。

## 三层预算，而非一句“低延迟光网”
1. **容量层**：Ciena强调coherent光层增加每fiber pair容量，但transport算法不能创造缺失容量。51.2T full-spectrum模块仍是概念；密度倍数不是应用加速。[[knowledge/sources/src-c19fabdbe95d]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=4|PDF p.4]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=10|PDF p.10]] [[ai-clusters/From-Single-Data-Centers-to-Multi-Region-AI-Clusters-The-Rise-of-Scale-Across.pdf#page=12|PDF p.12]]
2. **在途与buffer层**：Broadcom在800GE、约10µs/km RTT假设下给100km→100MB BDP。其≥1.5BDP near-ideal FCT/零重传只在所列simulation条件成立；必须补拓扑、流到达、incast、失效与buffer带宽。[[knowledge/sources/src-b67d631c7d89]] [[ai-clusters/Scale-across-Networking-Panel-discussion-on-routing-and-transport-equipment-implications.pdf#page=46|PDF p.46]] [[ai-clusters/Scale-across-Networking-Panel-discussion-on-routing-and-transport-equipment-implications.pdf#page=49|PDF p.49]] [[ai-clusters/Scale-across-Networking-Panel-discussion-on-routing-and-transport-equipment-implications.pdf#page=51|PDF p.51]]
3. **deadline层**：反馈早到不等于应用早完成。BTS的10µs对1000µs是illustration；完整控制还含检测、通知处理、CCA响应与排队清空。[[knowledge/sources/src-0de5a776ae41]] [[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=6|PDF p.6]] [[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=8|PDF p.8]]

## 为什么一种远端工作负载近本地，另一种不一定
NTT Unet3D/4×H100/100G APN实验中40km epoch357→364s，关键是加载batch N+1与计算N重叠，前提为加载速度跟得上GPU消费。它没有证明跨区TP all-reduce或每token同步KV访问也只慢1.9%。另一个PD PoC架构没有TTFT/TPOT结果。[[knowledge/sources/src-87903c12792f]] [[ai-computing-continuum/01_AI Computing Continuum Use Cases and Collaboration Items.pdf#page=4|PDF p.4]] [[ai-computing-continuum/01_AI Computing Continuum Use Cases and Collaboration Items.pdf#page=5|PDF p.5]] [[ai-computing-continuum/01_AI Computing Continuum Use Cases and Collaboration Items.pdf#page=6|PDF p.6]] [[ai-computing-continuum/01_AI Computing Continuum Use Cases and Collaboration Items.pdf#page=15|PDF p.15]]

**推论**：当可隐藏的数据搬移耗时小于本地计算窗口，额外RTT可能不成为吞吐瓶颈；当每步依赖远端结果时，必须把每次RTT计入critical path。计算窗口、消息字节量、可用带宽、overlap比例及tail均需测量。

## 控制面统一不能消除物理距离
Celestica以LISP把EID/RLOC、tenant IID与跨domain注册/订阅结合，是管理/寻址提案。其WAN/RAN愿景、250ns目标与sub-µs convergence没有端到端测量，不能覆盖传播成本，也不能由protocol名称推出隔离保证。[[knowledge/sources/src-03c858066777]] [[ai-computing-continuum/04_Breaking the Data Center Walls Unifying AI Fabrics for Agentic AI at t.pdf#page=4|PDF p.4]] [[ai-computing-continuum/04_Breaking the Data Center Walls Unifying AI Fabrics for Agentic AI at t.pdf#page=12|PDF p.12]] [[ai-computing-continuum/04_Breaking the Data Center Walls Unifying AI Fabrics for Agentic AI at t.pdf#page=14|PDF p.14]]

## 对推理系统的可执行证据需求
- 按replica/TP/EP/PD列每请求跨站次数、消息尺寸、KV寿命与失效重试。
- 固定模型/精度/context/concurrency，报告p50/p99 TTFT、TPOT及goodput，而非只链路线速。
- 同时测试短消息、高incast、跨站慢路径、单plane掉线与buffer接近上限。
- 显式标出把数据保存在本地与数据被远端GPU读取的信任边界；没有持久复制不等于数据从不出站。

关联：[[knowledge/concepts/ai-infra-locality-and-control-timescales]]、[[knowledge/concepts/ai-infra-inference-serving-shapes]]、[[knowledge/concepts/ai-infra-multipath-failure-domains]]。
