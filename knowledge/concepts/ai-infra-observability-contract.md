---
type: "concept"
title: "边界遥测契约：观测开销、故障归因与商用准入"
tags: ["ai-infra", "inference-architecture"]
---

# 边界遥测契约：观测开销、故障归因与商用准入

## 定义
边界遥测契约明确每个 PCIe/C2C/XGMI/scale-up/内存接口需要暴露的 latency、credits、backpressure、bandwidth，以及生产/调试采集档位、API 对齐和开销门限。主证据 [[knowledge/sources/src-02fd0252e899]]，[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=20|PDF p.20]] [[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=21|PDF p.21]]；这是拟议开放标准，而非已批准规范。

## 为什么高集成度反而需要更多设计投入
Helios 移除外部 PCIe switch 后，原诊断探针消失；全部流量汇聚 GPU Data Fabric，新 silicon 必须自己提供可定位计数器。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=5|PDF p.5]] [[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=8|PDF p.8]]
同一演讲报告高频轮询通过 partial-cache-line write 制造 CPU memory backpressure。因此“更多采样总会更准确”不成立。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=6|PDF p.6]]

## 三个相互补足的层
- In-band 提供细粒度；OOB 在启动/拥塞时保存健康状态；低优先级、adaptive polling、core affinity 和 verbosity tier 防止观察者效应。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=7|PDF p.7]]
- 生产约 1s（可至 10s），debug 部分计数器可至十几 ms；这些频率只对应演讲平台，不是跨厂商默认值。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=9|PDF p.9]]
- 提案将生产轮询下 BusBW 降幅 >1% 设为资格失败。不能读作已实现 1% 开销或 OCP 已批准门限。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=21|PDF p.21]]

## 根因与受害者
PFC pause 是症状而不必是网络源故障：p.19 中 NIC DMA 是 aggressor、HBM 写队列是 choke point，UALoE/XGMI 是共同受害者。必须追踪“积压在哪里不再排空”。[[ai-clusters/Unified Telemetry for Next-Generation Rack-Scale Infrastructure.pdf#page=19|PDF p.19]]
此思路与 Meta 中断归因的 source vs co-victim 一致，[[knowledge/sources/src-2661a6b57700]]，[[ai-clusters/Achieving AI Cluster Reliability at Scale- Lessons in Reducing Workload Interruptions.pdf#page=6|PDF p.6]]；但同一组织的多份演讲不是独立统计验证。

## 向光互连延伸
[[knowledge/sources/src-6109035b9a67]] 要求 CPO thermal、optical power、external laser、pre/post-FEC BER 与 packet 层共享健康语义和责任边界。[[ai-clusters/Next Generation Optically Integrated Platform Solution for AI Data Centers.pdf#page=8|PDF p.8]] CPO pJ/bit 优势无法替代维修、故障定位、跨团队运营证据。

## 对推理芯片商业化的综合判断
可定位的接口错误与低扰动遥测可以降低 bring-up/qualification 的诊断摩擦；但材料没有 qualification 周期、RMA 节省额等定量证据，不能估算收入/毛利收益。

## 未决问题
全边界 always-on counter 仍未齐全；不同 clock domain 时间对齐、计数器溢出/清零、采集原子性、租户隔离、debug 访问权限与 production overhead benchmark 仍需规范。[[knowledge/questions/ai-infra-architecture-evidence-gaps]]
