---
type: concept
title: "可持续指标先固定功能单位：PUE、功率、能量、碳强度不能互代"
tags: [ocp2026, sustainability]
---

# 可持续指标先固定功能单位：PUE、功率、能量、碳强度不能互代

## 定义
比较推理系统时，最小可复用边界应是：**同任务/质量、同延迟 SLA、同到达负载下的有效完成量**，同时报告 IT 与设施电量、碳和资源绝对量。PUE 仅是设施电量/IT 电量；W 是功率，J 或 kWh 是能量；每 core/FP8 TOPS 的隐含碳不是每成功任务的全生命周期碳。这是下列资料的跨源归纳，不是一份新标准。

## 来源与页级证据
- DCEM 的风冷→DLC 示例将总功率 497→485 W，但 PUE 1.28→1.37；低功率 ASIC 的 SNN 任务能量也未优于其 CPU 比较项。[[knowledge/sources/src-a5fa26b34893]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=9|PDF p.9]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=12|PDF p.12]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=13|PDF p.13]]
- Lenovo 的 3.14 MWh 总量与 2.14 MWh IT 对应 PUE 约 1.47，而图标 0.66。先做单位/边界/算术检查，再讨论预测和调度。[[knowledge/sources/src-1b8ab113ff06]] [[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=5|PDF p.5]] [[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=6|PDF p.6]] [[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=7|PDF p.7]]
- 性能归一化隐含碳刻意只覆盖 IT 硬件供应链，分母可为 core、TB、FP8 TOPS；总排放仍可能上升。[[knowledge/sources/src-4001ade000fc]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=2|PDF p.2]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=3|PDF p.3]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=4|PDF p.4]]
- Green Tokens 要把服务时间、地点与资源影响交给用户；等功能单位是关键，示例仪表盘不是已有减排实绩。[[knowledge/sources/src-f328490907a5]] [[Sustainability/The Green Tokens- From Green Computing to Sustainably Intelligent.pdf#page=12|PDF p.12]] [[Sustainability/The Green Tokens- From Green Computing to Sustainably Intelligent.pdf#page=13|PDF p.13]] [[Sustainability/The Green Tokens- From Green Computing to Sustainably Intelligent.pdf#page=14|PDF p.14]]
- OpenAI/Broadcom 将相同 UX/SLA 的时延—能量曲线作为取舍；Arm 区分 tasks/s@SLA 与单 agent 前进速度。[[knowledge/sources/src-6a803e49a956]] [[executive-sessions/17_Designing the next AI fabric When compute meets optics presented by Ce.pdf#page=3|PDF p.3]] [[knowledge/sources/src-2f507783aa88]] [[executive-sessions/45_Rethinking CPU Performance for the Agentic AI Era presented by Arm.pdf#page=7|PDF p.7]] [[executive-sessions/45_Rethinking CPU Performance for the Agentic AI Era presented by Arm.pdf#page=8|PDF p.8]]

## 共识与分歧
共同点是不能用单个“更小”的数字概括系统价值。分歧主要来自测量边界：PUE 把服务器风扇放入 IT 分母；硬件隐含强度不包括运行能量；按 token 归一化还受模型质量、推理长度影响。它们回答不同问题，不应强行收敛成同一个排行榜。

## 适用条件与操作清单
1. 固定服务：模型、精度、输入/输出长度、质量门槛、并发/到达过程、TTFT/TPOT/成功率。
2. 固定时间与电表：全测试窗口积分 `ΣPΔt`，明确包含 CPU、网络、存储、冷却与空闲能耗的层级。
3. 固定归因：共享基础设施的分摊、负载迁移开销、电网因子地点与时间。
4. 同时报绝对量与单位量；PUE、吞吐和可部署容量分别保留。MaxLPS 的电力预算释放允许增容，不等于同幅度节能。[[knowledge/sources/src-41b73a819a65]] [[executive-sessions/21_Every Megawatt Counts The Path to Building AI Factories with DSX MaxLP.pdf#page=4|PDF p.4]] [[executive-sessions/21_Every Megawatt Counts The Path to Building AI Factories with DSX MaxLP.pdf#page=5|PDF p.5]]
5. 节能开关进入 NPI 检查，验证唤醒与尾延迟，不能把 silicon/platform/rack 百分比直接相加。[[knowledge/sources/src-8cf188b85e4d]] [[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=2|PDF p.2]] [[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=5|PDF p.5]] [[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=6|PDF p.6]]

## 未决问题
任务质量与失败重试如何进入功能单位？缓存复用跨请求如何摊销？低负载与峰值时的结论是否反转？采购时应索取原始时序与任务输出，而非只有平均 W 或最大 TOPS。

## 关联
[[knowledge/concepts/executive-expo-inference-sla]] · [[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]] · [[knowledge/comparisons/sustainability-metric-reversal-and-accounting]]
