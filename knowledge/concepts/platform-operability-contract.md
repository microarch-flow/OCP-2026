---
type: "concept"
title: "可运营性契约：协议名称不等于可部署行为"
review_status: "synthesis"
tags: ["ocp", "concept", "platform"]
sources: ["[[knowledge/sources/src-fb5996cd03af]]", "[[knowledge/sources/src-130c021db4d4]]", "[[knowledge/sources/src-f471e738fe63]]", "[[knowledge/sources/src-2244c05beeab]]", "[[knowledge/sources/src-3bd90d8e4e75]]", "[[knowledge/sources/src-819271b48bb1]]", "[[knowledge/sources/src-6a15956dd77d]]", "[[knowledge/sources/src-7f631cbf9c52]]", "[[knowledge/sources/src-16cc579881c4]]", "[[knowledge/sources/src-37316fad4677]]", "[[knowledge/sources/src-ca1ac0e57929]]"]
updated: "2026-10-30"
---

# 可运营性契约：协议名称不等于可部署行为

## 定义与边界

**跨源归纳：** “支持Redfish/PLDM/SPDM”只限定一个功能族。可交付机群需要版本、mandatory profile、命名/单位/时间、失败语义、权限、生命周期以及可重跑测试共同组成契约。目标不是更多遥测，而是将故障约束在最小安全范围、获得可行动证据并恢复有效工作。

## 来源与页级证据

- Microsoft运营材料自报millions BMC/100+平台，但强调多ODM/代际的event、retry、依赖、更新行为仍分化；互通必须测试而非由协议支持推断。[[knowledge/sources/src-37316fad4677|源卡]] · [[systems-management/Operating-OpenBMC-at-Hyperscale-What-Works-What-Breaks-and-What-Needs-to-Change.pdf#page=4|PDF p.4]] [[knowledge/sources/src-37316fad4677|源卡]] · [[systems-management/Operating-OpenBMC-at-Hyperscale-What-Works-What-Breaks-and-What-Needs-to-Change.pdf#page=7|PDF p.7]]
- AMC把协议选项收敛成辅助设备profile，2.0强制Type7及更完整SPDM要求；Service Baseline统一账户/证书/日志/更新等housekeeping。[[knowledge/sources/src-16cc579881c4|源卡]] · [[systems-management/OCP-Auxiliary-Management-Controller-overview.pdf#page=8|PDF p.8]] [[knowledge/sources/src-ca1ac0e57929|源卡]] · [[systems-management/Prescribing-remote-manageability-for-IT-OT.pdf#page=8|PDF p.8]]
- CTAM试图建立供应商/客户共同验收语言；测试数量并不是安全覆盖率。[[knowledge/sources/src-fb5996cd03af|源卡]] · [[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=4|PDF p.4]]
- Bulk telemetry/crash dump标准化发现/传输而保持载荷可私有，BMC透明转发不等于解析器互通。[[knowledge/sources/src-2244c05beeab|源卡]] · [[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=3|PDF p.3]] [[knowledge/sources/src-2244c05beeab|源卡]] · [[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=6|PDF p.6]]
- Alias已发布功能与ServiceAlias/TelemetryBundle WIP必须分开；同名不等于同样采样。[[knowledge/sources/src-3bd90d8e4e75|源卡]] · [[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=4|PDF p.4]] [[knowledge/sources/src-3bd90d8e4e75|源卡]] · [[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=7|PDF p.7]]
- RAS API需明确CPER读取是否pop、动作队列满如何拒绝、溢出如何报告。[[knowledge/sources/src-f471e738fe63|源卡]] · [[manageability-workshop/OCP RAS API PLDM Modeling.pdf#page=11|PDF p.11]] [[knowledge/sources/src-f471e738fe63|源卡]] · [[manageability-workshop/OCP RAS API PLDM Modeling.pdf#page=12|PDF p.12]]
- GPU更新Fast Fail是optional且目标范围有条件；MinSVN burn与rollout解耦是一项安全/可回滚性政策。[[knowledge/sources/src-6a15956dd77d|源卡]] · [[systems-management/From-Scale-to-Security-Evolving-GPU-Management-Standards-in-2026.pdf#page=13|PDF p.13]] [[knowledge/sources/src-6a15956dd77d|源卡]] · [[systems-management/From-Scale-to-Security-Evolving-GPU-Management-Standards-in-2026.pdf#page=15|PDF p.15]]
- 诊断有效率只有检测→可修根因→动作→恢复全达成才计resolved；90%为成熟产品建议目标，不是已测成效。[[knowledge/sources/src-7f631cbf9c52|源卡]] · [[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=7|PDF p.7]]

## 共识与分歧

共同方向是把厂商差异放在受控扩展/内部机制，将外部行为和证据统一。但材料间的状态不同：已发布profile、WIP数据模型、展台PoC、生产经验不能合并成“标准已完全落地”。CTAM管理合规、内部DV、安全审查、运维SLA分别验证不同性质。

## 适用条件

面向采购验收可用六栏矩阵：**能力/版本 → profile mandatory项 → 异常与恢复行为 → 安全权限 → 实测预算 → 测试与证据**。对瞬态VR故障特别应区分管理遥测（来源称常约1–10Hz）与能捕获子周期瞬态的按需通道。[[knowledge/sources/src-130c021db4d4|源卡]] · [[manageability-workshop/05_Redfish Native Fleet-Scale GPU Observability Assistant for AI Cluster .pdf#page=8|PDF p.8]]

验收应包含固件/设备缺失、接口down、队列满、事件风暴、时间不同步、证书过期、重启中断及部分更新失败；不能只对正常GET返回做happy-path检查。

## 未决问题

- mandatory profile是否覆盖恢复/错误语义还是只覆盖资源存在性？
- 高层聚合是否隐瞒原始source、timestamp、缺失值和故障范围？
- 一次维修后是否复发、误报/漏报有无分故障域样本？
- 需报告有效tokens/s、p99和node-hours恢复等业务结果，不能从“接口统一”直接计算TCO降低。
