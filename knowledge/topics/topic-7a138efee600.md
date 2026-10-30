---
type: topic
title: "systems-management"
tags: ["ocp2026", "topic"]
---

# systems-management

返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。

## 阅读路线与主题综合

这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。跨源概念与比较入口见下方；结论的适用条件仍需回查相应笔记。

<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->

<!-- GENERATED:topic-concepts:BEGIN -->
## 关联的跨源概念与比较

以下链接来自本主题源卡的实际引用，按引用它的源卡数量排序；关联不等于独立验证。

- [[knowledge/concepts/platform-operability-contract|可运营性契约：协议名称不等于可部署行为]]（本主题 6 份源卡引用）
- [[knowledge/concepts/platform-firmware-decoupling|固件解耦的四个维度：调用、配置、组件交付与可信发布]]（本主题 1 份源卡引用）
<!-- GENERATED:topic-concepts:END -->

## 来源与分析进度

<!-- GENERATED:topic-sources:BEGIN -->
本主题：15 份 PDF；已分析声明 15；部分分析 0；零字节 0。

| 原始资料 | 源卡 / 状态 |
| --- | --- |
| [[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf\|Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges]] | [[knowledge/sources/src-1b36f933cf3b\|遥测聚合流水线：时间、空间与上下文必须共同保真 · analyzed-text]] |
| [[systems-management/DMTF-PMCI-Enhancements-for-OCP-Hardware-Management.pdf\|DMTF-PMCI-Enhancements-for-OCP-Hardware-Management]] | [[knowledge/sources/src-819271b48bb1\|PMCI进展：简单MCTP、有界USB侧带与可复用测试 · analyzed-text]] |
| [[systems-management/From-Lab-to-Fleet-A-Secure-Unified-Debug-Framework-for-Cloud-Systems.pdf\|From-Lab-to-Fleet-A-Secure-Unified-Debug-Framework-for-Cloud-Systems]] | [[knowledge/sources/src-91426f6ca943\|BMC本地Debug Gateway：省掉WAN细粒度往返但保留授权边界 · analyzed-visual]] |
| [[systems-management/From-Scale-to-Security-Evolving-GPU-Management-Standards-in-2026.pdf\|From-Scale-to-Security-Evolving-GPU-Management-Standards-in-2026]] | [[knowledge/sources/src-6a15956dd77d\|GPU管理标准2026：遥测二进制数据面、更新Fast Fail与MinSVN拆分 · analyzed-visual]] |
| [[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf\|GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure]] | [[knowledge/sources/src-7f631cbf9c52\|CPU/GPU RAS诊断：以安全故障域、诊断有效率与修复时间验收 · analyzed-visual]] |
| [[systems-management/Graph-Query-Language-APIs-for-OpenBMC-Metrics-OpenRMC-DM-as-a-Proxy-GraphQL-Server.pdf\|Graph-Query-Language-APIs-for-OpenBMC-Metrics-OpenRMC-DM-as-a-Proxy-GraphQL-Server]] | [[knowledge/sources/src-582f9c0de536\|OpenRMC GraphQL代理：北向减少请求，不消除南向Redfish成本 · analyzed-visual]] |
| [[systems-management/Hardware-Management-Project-Journey.pdf\|Hardware-Management-Project-Journey]] | [[knowledge/sources/src-a220bfb9dcfe\|Hardware Management项目地图：从组件到机架及故障闭环 · analyzed-text]] |
| [[systems-management/Hierarchical-Device-Managers-to-manage-complex-Multi-Rack-systems.pdf\|Hierarchical-Device-Managers-to-manage-complex-Multi-Rack-systems]] | [[knowledge/sources/src-13bfd642b536\|递归Device Manager：多机架管理把fan-out分层但不消除 · analyzed-visual]] |
| [[systems-management/OBMF-Specifications-and-Workstream-Status-Update.pdf\|OBMF-Specifications-and-Workstream-Status-Update]] | [[knowledge/sources/src-3332546c9d23\|OBMF-ICP状态：统一通道协议与USB/MCTP绑定的成熟度 · analyzed-visual]] |
| [[systems-management/OCP-Auxiliary-Management-Controller-overview.pdf\|OCP-Auxiliary-Management-Controller-overview]] | [[knowledge/sources/src-16cc579881c4\|AMC2.0：以强制profile收敛辅助设备的管理选择空间 · analyzed-text]] |
| [[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf\|OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship]] | [[knowledge/sources/src-7b5ff256c6ff\|硬件故障生态：CPER→分析器→政策授权→CPAD→结果闭环 · analyzed-visual]] |
| [[systems-management/Operating-OpenBMC-at-Hyperscale-What-Works-What-Breaks-and-What-Needs-to-Change.pdf\|Operating-OpenBMC-at-Hyperscale-What-Works-What-Breaks-and-What-Needs-to-Change]] | [[knowledge/sources/src-37316fad4677\|OpenBMC超大规模运营：开源采用成功之后是行为一致性成本 · analyzed-text]] |
| [[systems-management/Prescribing-remote-manageability-for-IT-OT.pdf\|Prescribing-remote-manageability-for-IT-OT]] | [[knowledge/sources/src-ca1ac0e57929\|IT/OT管理Profile：把Redfish可选能力变成可检验的服务契约 · analyzed-visual]] |
| [[systems-management/Runtime-SBOMs-Extending-DMTF-Redfish-to-Connect-Build-Time-and-Live-Software-State.pdf\|Runtime-SBOMs-Extending-DMTF-Redfish-to-Connect-Build-Time-and-Live-Software-State]] | [[knowledge/sources/src-e7442ca742b5\|Runtime SBOM：把既有SBOM准确关联到active/staged/recovery镜像 · analyzed-visual]] |
| [[systems-management/System-Level-Manageability-for-GPU-Platforms-Progress-in-the-OCP-System-GPU-Management-Workstream.pdf\|System-Level-Manageability-for-GPU-Platforms-Progress-in-the-OCP-System-GPU-Management-Workstream]] | [[knowledge/sources/src-0981434e18fe\|System GPU Management：公开profile、事件与聚合模型的接口收敛 · analyzed-text]] |
<!-- GENERATED:topic-sources:END -->
