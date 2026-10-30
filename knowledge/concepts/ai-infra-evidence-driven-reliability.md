---
type: "concept"
title: "证据驱动可靠性：恢复、归因、修复三个闭环"
tags: ["ai-infra", "inference-architecture"]
---

# 证据驱动可靠性：恢复、归因、修复三个闭环

## 定义
恢复使任务继续，归因解释故障，修复使它不再重复。三者不能混为一谈。Meta 的训练中断流程保留 timeline、排除项、confidence，并使用故障目录约束 AI 输出。[[knowledge/sources/src-2661a6b57700]]，[[ai-clusters/Achieving AI Cluster Reliability at Scale- Lessons in Reducing Workload Interruptions.pdf#page=3|PDF p.3]] [[ai-clusters/Achieving AI Cluster Reliability at Scale- Lessons in Reducing Workload Interruptions.pdf#page=5|PDF p.5]] [[ai-clusters/Achieving AI Cluster Reliability at Scale- Lessons in Reducing Workload Interruptions.pdf#page=6|PDF p.6]]

## 从 benchmark 到生产的共性
Intel 多代理 DCPerf 工作流使用既有工具、保存配置与遥测、有限重试、逐次实验；FeedSim 调参不增益后把 memory bandwidth 留作假设，而非强行得出 root cause。[[knowledge/sources/src-ad22974e70aa]]，[[ai-clusters/07_From Benchmark to Bottleneck Agentic AI for Datacenter Workload Analys.pdf#page=6|PDF p.6]] [[ai-clusters/07_From Benchmark to Bottleneck Agentic AI for Datacenter Workload Analys.pdf#page=14|PDF p.14]] [[ai-clusters/07_From Benchmark to Bottleneck Agentic AI for Datacenter Workload Analys.pdf#page=20|PDF p.20]]
生产故障还须识别 source vs co-victim；高频监控自身可能造成 backpressure，且看到 PFC 的网络可能只是 HBM 写拥塞的受害者。[[knowledge/sources/src-02fd0252e899]]，[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=6|PDF p.6]] [[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=19|PDF p.19]]

## 可以量化什么，不能量化什么
Meta p.10 图显示 2026 窗口内 A/B 相对起始每周中断率下降 75%/87%，但无绝对 rate、平台身份或等价成熟度；不能据此推算某款推理加速器的 SLA/MTBF。[[ai-clusters/Achieving AI Cluster Reliability at Scale- Lessons in Reducing Workload Interruptions.pdf#page=10|PDF p.10]]
Intel p.20 明确不公开性能成绩与硬件配置；流程成功不等于吞吐提升。[[ai-clusters/07_From Benchmark to Bottleneck Agentic AI for Datacenter Workload Analys.pdf#page=20|PDF p.20]]

## 适用到推理的检查表（本知识库推论）
以 request/SLO breach 为事件单位，连结请求 trace、调度放置、模型版本、host/accelerator counters、network telemetry；记录 retry/cold-start/迁移损失；单独统计未归因与低置信度事件；对自动 remediation 设容量底线、断路器和 anti-flap。
后者调度安全栏有 Helios 演讲例证：warning soft-avoid、critical drain、恢复需 N passes+preflight。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=12|PDF p.12]]

## 未决问题
谁维护故障目录、unknown 不被错误“归零”的机制、人工审计误归因率、跨供应商责任归属及发布节奏，是商业部署而非模型演示的关键。
