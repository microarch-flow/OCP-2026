---
type: topic
title: "networking"
tags: ["ocp2026", "topic"]
---

# networking

返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。

## 阅读路线与主题综合

这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。跨源概念与比较入口见下方；结论的适用条件仍需回查相应笔记。

<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->

<!-- GENERATED:topic-concepts:BEGIN -->
## 关联的跨源概念与比较

以下链接来自本主题源卡的实际引用，按引用它的源卡数量排序；关联不等于独立验证。

- [[knowledge/concepts/network-executable-validation|可执行规范：把协议、平台和网络行为变成验收契约]]（本主题 12 份源卡引用）
- [[knowledge/comparisons/network-transport-and-buffer-context|看似矛盾的AI网络建议：无损、尽力而为、深缓冲与浅缓冲]]（本主题 5 份源卡引用）
- [[knowledge/concepts/network-multipath-behavior|多路径传输：选择路径、控制在途量与时序互通]]（本主题 5 份源卡引用）
- [[knowledge/concepts/network-buffer-workload-placement|缓冲容量不是孤立参数：传播距离、拥塞控制与作业放置]]（本主题 4 份源卡引用）
- [[knowledge/concepts/network-ocs-control|OCS控制：光路意图、完成状态与预测误差预算]]（本主题 3 份源卡引用）
- [[knowledge/concepts/network-inference-acceptance|推理网络验收：按通信图、尾延迟和可观测性采购]]（本主题 2 份源卡引用）
- [[knowledge/concepts/network-optics-reliability|光互连可靠性：从平均 BER 转向中断、故障域与修复时间]]（本主题 2 份源卡引用）
- [[knowledge/concepts/network-scaleup-ethernet|Scale-up Ethernet：紧凑 framing、局部重试与端点边界]]（本主题 2 份源卡引用）
- [[knowledge/concepts/network-clock-evidence|时间对齐的遥测证据：不确定窗口、缺失语义与安全闭环]]（本主题 1 份源卡引用）
- [[knowledge/concepts/network-optical-integration|光学集成边界：LPO、NPO、CPO、XPO 与 Open CPX]]（本主题 1 份源卡引用）
<!-- GENERATED:topic-concepts:END -->

## 来源与分析进度

<!-- GENERATED:topic-sources:BEGIN -->
本主题：27 份 PDF；已分析声明 27；部分分析 0；零字节 0。

| 原始资料 | 源卡 / 状态 |
| --- | --- |
| [[networking/01_Bridging the Gap Accelerating Open-Source Agility on Cisco Silicon One.pdf\|01_Bridging the Gap Accelerating Open-Source Agility on Cisco Silicon One]] | [[knowledge/sources/src-1553798ef474\|Cisco Silicon One：跨 SONiC/FBOSS 的分层验证复用 · analyzed-text]] |
| [[networking/02_Closing the Observability Loop in SAI From Performance Telemetry to Pl.pdf\|02_Closing the Observability Loop in SAI From Performance Telemetry to Pl]] | [[knowledge/sources/src-f96b2b46b138\|SAI 观测闭环：平台约束查询与 SDK 边界 PerfMon · analyzed-text]] |
| [[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf\|03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD]] | [[knowledge/sources/src-a348d96bbbf5\|Cisco/AMD 模块化 SmartSwitch：DPU sled 标准化边界 · analyzed-visual]] |
| [[networking/04_Meta 102.4T Ethernet Switch.pdf\|04_Meta 102.4T Ethernet Switch]] | [[knowledge/sources/src-699968f5fe65\|Meta IceCube 102.4T：铜飞线、混合液冷与机柜纤维管理 · analyzed-visual]] |
| [[networking/05_More Signal, Less Noise Improving AI Cluster Returns Through Standardi.pdf\|05_More Signal, Less Noise Improving AI Cluster Returns Through Standardi]] | [[knowledge/sources/src-5356709581c5\|Credo 增强光模块遥测：远端分段诊断与持久事件证据 · analyzed-visual]] |
| [[networking/06_NVIDIA SDK + FBOSS Building Production-Ready AI Network Fabrics.pdf\|06_NVIDIA SDK + FBOSS Building Production-Ready AI Network Fabrics]] | [[knowledge/sources/src-55e14ad184e2\|NVIDIA SDK + FBOSS: Building Production-Ready AI Network Fabrics · analyzed-visual]] |
| [[networking/07_Open, AI-Ready FBOSS From Platform Bring-up to Solution Qualification .pdf\|07_Open, AI-Ready FBOSS From Platform Bring-up to Solution Qualification ]] | [[knowledge/sources/src-983fb0686005\|Config-Driven FBOSS: From Board Bring-up to Qualified Platform · analyzed-visual]] |
| [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf\|08_Operating Linear Pluggable Optics at Hyperscale From Link Management t]] | [[knowledge/sources/src-6ce06488969f\|Operating Linear Pluggable Optics at Hyperscale: From Link Management to Production Reliability · analyzed-visual]] |
| [[networking/09_SONiC for OTN Expanding SONiC and OCP SAI into Optical Transport Netwo.pdf\|09_SONiC for OTN Expanding SONiC and OCP SAI into Optical Transport Netwo]] | [[knowledge/sources/src-2884b339ab4a\|SONiC for OTN：将开放 NOS 延伸至光传送设备 · analyzed-text]] |
| [[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf\|10_Switch Platform Architecture A Unified Network Switch Platform Referen]] | [[knowledge/sources/src-4cb1cfbea778\|Open Switch Platform Architecture (OSPA): A Unified Network Switch Platform Reference Design · analyzed-visual]] |
| [[networking/Beyond Traditional BGP- Decoupling Route Distribution for Large-Scale AI Clusters at Alibaba.pdf\|Beyond Traditional BGP- Decoupling Route Distribution for Large-Scale AI Clusters at Alibaba]] | [[knowledge/sources/src-bac5a3ea76a0\|Alibaba HPN Pivot：基础路由与业务路由解耦 · analyzed-visual]] |
| [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf\|Bridging On-prem and Cloud - GPU Networking at Meta Scale]] | [[knowledge/sources/src-b704f1f146e0\|Bridging On-Prem and Cloud — GPU Networking at Meta Scale · analyzed-visual]] |
| [[networking/Deep Buffers- The Essential Foundation for Scalable AI Training and Inference Infrastructure.pdf\|Deep Buffers- The Essential Foundation for Scalable AI Training and Inference Infrastructure]] | [[knowledge/sources/src-5d08f4927b78\|Arista/Broadcom Scale-Across：分层深缓冲与 BDP 仿真边界 · analyzed-visual]] |
| [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf\|ESUN- Open Ethernet for the AI Scale-Up Era]] | [[knowledge/sources/src-6415268b7f70\|ESUN: Open Ethernet for the AI Scale-Up Era · analyzed-visual]] |
| [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf\|MRC- A Purpose-Built RDMA Transport for AI Training Networks]] | [[knowledge/sources/src-f13077d44cf0\|MRC: A Purpose-Built RDMA Transport for AI Training Networks · analyzed-visual]] |
| [[networking/MetaRoCE in Software.pdf\|MetaRoCE in Software]] | [[knowledge/sources/src-f76571507532\|MetaRoCE in Software · analyzed-text]] |
| [[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf\|Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case]] | [[knowledge/sources/src-58ce2a4bef6e\|IREN 端到端自动化：可执行设计意图比单独配网更重要 · analyzed-text]] |
| [[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf\|Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases]] | [[knowledge/sources/src-0ff8784e94af\|CPO+OCS+SDN：多厂商光加速集群与共享备件池 · analyzed-visual]] |
| [[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf\|SRv6 Deployments in Scale-Out and Scale-Across Networks]] | [[knowledge/sources/src-badf54452e3e\|SRv6 Deployments in Scale-Out Networks · analyzed-visual]] |
| [[networking/Scaling AI Beyond the Cloud Boundary- High-Capacity Interconnects Between Hyperscalers and GPUaaS.pdf\|Scaling AI Beyond the Cloud Boundary- High-Capacity Interconnects Between Hyperscalers and GPUaaS]] | [[knowledge/sources/src-418a431c7736\|Hyperscaler 到 GPUaaS：服务感知 T0 边界网关 · analyzed-visual]] |
| [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf\|Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG]] | [[knowledge/sources/src-c4cafad20442\|Scaling AI Infrastructure: Meta’s Journey with BAG · analyzed-text]] |
| [[networking/Srv6 powered backbone networks.pdf\|Srv6 powered backbone networks]] | [[knowledge/sources/src-e41f8d86b57e\|SRv6 Powered Backbone Networks · analyzed-visual]] |
| [[networking/Standardizing Ethernet Scale-Up Validation- Test Strategy and Current Progress on LLR-CBFC.pdf\|Standardizing Ethernet Scale-Up Validation- Test Strategy and Current Progress on LLR-CBFC]] | [[knowledge/sources/src-9912ba7e02b4\|LLR/CBFC 测试：交换机全通过不等于端点全通过 · analyzed-visual]] |
| [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf\|Standardizing OCS Interfaces for Seamless Integration]] | [[knowledge/sources/src-8fba6503c4b7\|Standardizing OCS Interfaces for Seamless Integration · analyzed-text]] |
| [[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf\|The UALink Switch API - A Common Abstraction for Scale-Up AI Switches]] | [[knowledge/sources/src-33ffd49678ca\|UALink Switch API：面向 scale-up 的对象管理与租户隔离 · analyzed-text]] |
| [[networking/Traffic Engineering in AI DCI-WAN for AI Traffic.pdf\|Traffic Engineering in AI DCI-WAN for AI Traffic]] | [[knowledge/sources/src-5f5b68866e25\|Alibaba/Cisco SRv6 AI WAN：按作业 TE 与光层降级反馈 · analyzed-visual]] |
| [[networking/Zero-Touch OCS Fabrics for AI Scale-Out Infrastructure at Hyperscale.pdf\|Zero-Touch OCS Fabrics for AI Scale-Out Infrastructure at Hyperscale]] | [[knowledge/sources/src-9a76a7b2552d\|Oracle/Lumentum 零接触 OCS：行为合同与端到端光路验真 · analyzed-visual]] |
<!-- GENERATED:topic-sources:END -->
