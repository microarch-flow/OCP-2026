---
type: "comparison"
title: "AI 基础设施性能证据：哪些数字可以比较，哪些不可以"
tags: ["ai-infra", "inference-architecture"]
---

# AI 基础设施性能证据：哪些数字可以比较，哪些不可以

## 比较问题与口径
用户关心的是**给定模型/质量/请求分布/SLO的可售吞吐与成本**。本页不做跨vendor排名，而是把“指标是什么、比较对象变了什么、证据缺什么”放在同一框架。

## 代表性数字及不可跨越的边界
- **AISBench：397→420 QPM**是选择更稳定时间窗后的统计变化，不是硬件加速；250K requests也不是250K并发。其有用贡献是L0/L1/L2与QoS-compliant throughput分层。[[knowledge/sources/src-72f3f34519b5]] [[ai-clusters/01_AI Cluster Benchmarks – Establishing a standardized evaluation system .pdf#page=6|PDF p.6]] [[ai-clusters/01_AI Cluster Benchmarks – Establishing a standardized evaluation system .pdf#page=16|PDF p.16]]
- **NVIDIA tokenomics：2×/10×/30×及45×**对应不同SLO/宣传口径，缺完整模型、上下文、并发与TCO边界，不组成一条可统一折算的性能曲线。[[knowledge/sources/src-e7760c5d3559]] [[ai-clusters/02_AI Tokenomics Explained.pdf#page=13|PDF p.13]]
- **Astera PCIe：约+50%TPS/+90%prefill-heavy**使用Qwen3.5-122B，一大switch全8GPU P2P对两小switch分4GPU island；topology同时改变，不能归因于单一lane数，也缺请求p99。[[knowledge/sources/src-5b5f8a5b557e]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=13|PDF p.13]]
- **Meta/Keysight workload overlap：EP约1.3×、DP约1.8×变慢**是在固定DUT/collective下真实DAG争用对隔离测试，解释为什么单算子带宽不等于应用表现，不是跨芯片排名。[[knowledge/sources/src-b4e79b188a6e]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=9|PDF p.9]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=10|PDF p.10]] [[ai-clusters/Cluster-less Validation of AI Accelerator Silicon Under Real Workloads.pdf#page=11|PDF p.11]]
- **Arista/AMD 504GPU validation cluster**不同于16K GPU示例与129K理论工程容量；文件给配置但未给性能结果，不能写“已验证129K”。[[knowledge/sources/src-48f9c6b8e63f]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=14|PDF p.14]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=16|PDF p.16]]
- **Arm/Furiosa：Qwen3-32B FP8、4卡、1K/1K、30tok/s用户SLO下约31.6users/kW**来自x86 host；TTFT0.35s未标p99，不能当Arm联合系统实测。[[knowledge/sources/src-57961bbe4020]] [[ai-clusters/Node-to-Rack Efficiency for Real-World AI Inference Arm & FuriosaAI for Scalable Open Infrastructure.pdf#page=12|PDF p.12]]
- **Arm/Rebellions：约2×TPS/W**未给模型、卡数、context、SLO或功耗边界；CPU rack比较混合测量和projection且服务器数量不同，不具备跨vendor公平排序条件。[[knowledge/sources/src-8a1494e40a6b]] [[ai-clusters/Scaling AI Inference with Arm AGI CPU, Rebellions RebelCard, and OCP ORv3 Rack Design.pdf#page=8|PDF p.8]] [[ai-clusters/Scaling AI Inference with Arm AGI CPU, Rebellions RebelCard, and OCP ORv3 Rack Design.pdf#page=9|PDF p.9]]

## 成熟度必须有两个维度
**实现成熟度**：概念→模拟→单组件→集成prototype→多rack→生产fleet。
**证据成熟度**：缺配置宣传→可复现基线→尾延迟/故障→长期稳定→成本与业务利用率。
两轴不可互代：产品已量产不代表本页benchmark充分；模拟方法很严谨也不代表硬件已交付。

## 统一验收表（知识库建议）
1. 模型版本、参数、精度/量化、质量门槛与speculative acceptance。
2. 输入/输出长度分布、prefix reuse、并发与arrival过程。
3. 实际host/accelerator数量、HBM、NIC、拓扑、firmware/runtime版本。
4. p99 TTFT/TPOT、错误/重试、SLO内goodput，固定warm-up与测量窗口。
5. card/server/rack/设施墙上功率边界，peak与平均分开。
6. BOM、折旧、能源、运维、降级容量、租户利用率与服务价格假设。
7. 故障注入、共享争用及长期稳定；ESUN方法明确分四级。[[knowledge/sources/src-6d378c7e79f1]] [[ai-clusters/Validation-methodologies-for-ESUN-ecosystem.pdf#page=14|PDF p.14]]

## 推荐阅读路径
先读[[knowledge/concepts/ai-infra-inference-serving-shapes]]选最简单满足SLO的拓扑，再读[[knowledge/concepts/ai-infra-scaleup-acceptance]]验证，最后把电网与冷却约束接到[[knowledge/concepts/ai-infra-power-to-sla-contract]]。
