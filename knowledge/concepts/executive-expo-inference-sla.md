---
type: concept
title: "推理系统的目标函数：满足体验约束的有效任务吞吐"
tags: [ocp2026, executive-expo]
---

# 推理系统的目标函数：满足体验约束的有效任务吞吐

## 定义
**跨源归纳**：推理系统的价值不是峰值FLOPS、独立token/s或机柜瓦数，而是给定质量、模型、请求分布与SLA下可完成的有效工作。推荐同时报告：TTFT、TPOT/完整响应时间、尾分位、成功任务/s、系统能量/成功任务及总成本。不同应用的质量约束不可省略。

## 来源与页级证据
- OpenAI部分明确以相同用户体验/SLA约束下TTLT—energy/token的Pareto前沿评价系统，而非只追求chip数量或单chip吞吐。[[knowledge/sources/src-6a803e49a956]] [[executive-sessions/17_Designing the next AI fabric When compute meets optics presented by Ce.pdf#page=3|PDF p.3]]
- Arm把单agent进度与tasks/s@SLA分开，冻结真实工具轨迹来隔离CPU硬件差异。[[knowledge/sources/src-2f507783aa88]] [[executive-sessions/45_Rethinking CPU Performance for the Agentic AI Era presented by Arm.pdf#page=7|PDF p.7]] [[executive-sessions/45_Rethinking CPU Performance for the Agentic AI Era presented by Arm.pdf#page=8|PDF p.8]]
- NVIDIA MaxLPS在Kimi-K2.5 FP4、8K/1K下称TGP1200→800 W仍维持吞吐，得到更多可部署机架；没有请求尾延迟，故不能直接认作同SLA收益。[[knowledge/sources/src-41b73a819a65]] [[executive-sessions/21_Every Megawatt Counts The Path to Building AI Factories with DSX MaxLP.pdf#page=4|PDF p.4]]
- d-Matrix把speculative、AFD、PDD对应不同异构边界；各自传输数据和同步频率不同，不能只比较宣传倍数。[[knowledge/sources/src-9e4b624fe6f8]] [[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=9|PDF p.9]]

## 共识与分歧
共识是应按工作负载协同设计；分歧在于实际优化对象：MaxLPS优化电力配额利用，Arm优化CPU任务容量，d-Matrix侧重交互性，SSD方案减少重算。它们可能同时有价值，却不是同一指标的可相加增益。

特别区分：**provisioned W是容量约束，consumed J是能耗，成功任务是服务产出**。更多机架不必然降低每任务能耗；更低平均功率可能伴随排队和完成时间上升。

## 适用条件与评估流程
1. 固定模型/精度、输出质量和输入输出长度分布；把缓存命中、batch、并发写入条件。
2. 给出负载曲线而非单点：每个点同时记录TTFT/TPOT尾分位、吞吐、功耗与成功率。
3. 把CPU工具、KV搬运、GPU计算和网络故障恢复纳入服务关键路径；不能只取GPU局部功耗。
4. 再把供电/冷却/网络/BOM与利用率换算成同一服务成本。本文提出的流程是综合分析方法，不是这些讲稿共同完成的实验。

## 未决问题
目前材料没有一套横跨CPU、GPU、专用XPU、CXL/SSD与功率控制的同质量同SLA公开对照。优先索取原始请求级日志、系统功耗时间序列和计费边界。

## 继续阅读
[[knowledge/concepts/executive-expo-kv-data-plane]] · [[knowledge/comparisons/executive-expo-inference-evidence-matrix]] · [[knowledge/concepts/executive-expo-power-control-boundaries]]

## 可持续性边界延伸
[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]
