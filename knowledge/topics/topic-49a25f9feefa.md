---
type: topic
title: "storage"
tags: ["ocp2026", "topic"]
---

# storage

返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。

## 阅读路线与主题综合

这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。跨源概念与比较入口见下方；结论的适用条件仍需回查相应笔记。

<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->

<!-- GENERATED:topic-concepts:BEGIN -->
## 关联的跨源概念与比较

以下链接来自本主题源卡的实际引用，按引用它的源卡数量排序；关联不等于独立验证。

- [[knowledge/concepts/platform-storage-workload-contract|存储是工作负载契约：容量、尾延迟、耐久与故障恢复联合定价]]（本主题 11 份源卡引用）
- [[knowledge/comparisons/platform-inference-metric-boundaries|推理与机房效率指标不可混算：七种证据边界]]（本主题 2 份源卡引用）
<!-- GENERATED:topic-concepts:END -->

## 来源与分析进度

<!-- GENERATED:topic-sources:BEGIN -->
本主题：18 份 PDF；已分析声明 18；部分分析 0；零字节 0。

| 原始资料 | 源卡 / 状态 |
| --- | --- |
| [[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf\|Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud]] | [[knowledge/sources/src-e67fbded1ca5\|高容量 HDD：SAS4、NVMe 与每 TB 性能预算 · analyzed-visual]] |
| [[storage/Comprehensive-Testing-for-OCP-Datacenter-NVMe-SSD-Specification-Compliance.pdf\|Comprehensive-Testing-for-OCP-Datacenter-NVMe-SSD-Specification-Compliance]] | [[knowledge/sources/src-8810594a9907\|Datacenter NVMe SSD 测试计划：覆盖、模式与认证边界 · analyzed-text]] |
| [[storage/High-Capacity-QLC-Innovation.pdf\|High-Capacity-QLC-Innovation]] | [[knowledge/sources/src-2807cd66d1aa\|高容量 QLC：DRAM 节省取决于映射粒度、缓存与工作负载 · analyzed-visual]] |
| [[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf\|IO-Prioritization-for-Optimized-Command-Handling]] | [[knowledge/sources/src-e3d8ea7e9b34\|NVMe I/O 优先级：从队列权重到端到端延迟契约 · analyzed-text]] |
| [[storage/Increasing-Block-Sizing-Changes-Data-Placement-Economics.pdf\|Increasing-Block-Sizing-Changes-Data-Placement-Economics]] | [[knowledge/sources/src-211b41341213\|NAND 大擦除块如何改变 FDP 小 RU 的经济性 · analyzed-visual]] |
| [[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf\|NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure]] | [[knowledge/sources/src-ff79ca208b59\|NVMe 2.4 更新：已批准能力与规划路线分开看 · analyzed-visual]] |
| [[storage/Near-Line-SSD-the-Path-to-the-Future.pdf\|Near-Line-SSD-the-Path-to-the-Future]] | [[knowledge/sources/src-7af780a098ba\|Near-Line QLC 与 Failure-in-Place：用可见容量损失换可管理性能 · analyzed-visual]] |
| [[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf\|OCP-Storage-Specifications-Update-and-What-Customers-Care-About]] | [[knowledge/sources/src-9e8eab9b92b1\|OCP 存储规范与客户诉求：恢复、安全和可观测性的共同基线 · analyzed-text]] |
| [[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf\|Optimizing-SSD-Performance-Testing-using-FIO-Sprandom]] | [[knowledge/sources/src-d2eace1b7b62\|Fio Sprandom：快速构造稳态，但 OP 与后续验证不能省略 · analyzed-visual]] |
| [[storage/QLC-Storage-in-Hyperscalefleet.pdf\|QLC-Storage-in-Hyperscalefleet]] | [[knowledge/sources/src-3ac347a35e8c\|Meta QLC 实践：块级修复、数据放置与缓存感知分配 · analyzed-visual]] |
| [[storage/QLC-Writes-the-end-of-SLC-caching.pdf\|QLC-Writes-the-end-of-SLC-caching]] | [[knowledge/sources/src-f07a528e26fb\|Direct Write QLC：可读首遍编程减少 SLC 保护开销 · analyzed-visual]] |
| [[storage/Recent-Advancements-in-OCP-Telemetry-for-SSDs.pdf\|Recent-Advancements-in-OCP-Telemetry-for-SSDs]] | [[knowledge/sources/src-43a03424124b\|SSD 遥测：从通用解码到基于群体基线的主动处置 · analyzed-visual]] |
| [[storage/SNIA-SFF-spec-updates-to-the-Storage-Form-Factor.pdf\|SNIA-SFF-spec-updates-to-the-Storage-Form-Factor]] | [[knowledge/sources/src-71239ecee484\|EDSFF 更新：液冷接触面、Streaming Boot 与高速/OOB 边界 · analyzed-visual]] |
| [[storage/Storage-Track-Close.pdf\|Storage-Track-Close]] | [[knowledge/sources/src-3020de0b6580\|Storage Track Closing：参与入口而非技术结论 · analyzed-text]] |
| [[storage/Storage-Track-Introduction.pdf\|Storage-Track-Introduction]] | [[knowledge/sources/src-1017a3a8aac9\|Storage Track Introduction：工作流与规范演进索引 · analyzed-text]] |
| [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf\|Storage-as-a-Performance-Tier-for-LLM-Serving]] | [[knowledge/sources/src-3f525f18fc6b\|SSD 作为 LLM KV 性能层：近 DRAM TTFT 与耐久约束并存 · analyzed-visual]] |
| [[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf\|The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace]] | [[knowledge/sources/src-dbfa4e967f8b\|Open Flash Platform：DPU 闪存密度方案，不等于已证实 Serverless SLA · analyzed-visual]] |
| [[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf\|Vertical-Optimizations-for-KV-Infrastructure]] | [[knowledge/sources/src-d4ac456fb37b\|KV$ 垂直优化：寿命分组降低 WAF，大传输降低 CPU 成本 · analyzed-visual]] |
<!-- GENERATED:topic-sources:END -->
