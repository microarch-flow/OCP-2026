---
id: power-cooling-protection-coordination
type: comparison
title: "800 V 保护方案如何比较：速度、供能、隔离与服务连续性"
tags: ["ocp2026", "power-cooling", "cross-source"]
---

# 800 V 保护方案如何比较：速度、供能、隔离与服务连续性

## 比较问题与结论

不是“SSCB 是否一定优于 MCCB”，而是**在明确电源、储能、接地和故障位置后，哪套系统能控制能量并保住未受影响的负载**。以下为已读资料的综合判断，不是设备选型认证、PPE 指引或现场操作规程。

## 并列证据

| 证据路径 | 已显示的内容 | 不能推出的结论 | 原始证据 |
| --- | --- | --- | --- |
| Siemens 的 zone/sector/circuit | 危险分区、连续性分组、多源电路是不同维度；快速保护与反灌阻断改变故障包络 | 某个支路有 SSCB 就使整区安全；所有隔离源都天然限流 | [[knowledge/sources/src-4533ea913815\|来源卡]] [[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=4\|PDF p.4]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=5\|PDF p.5]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=11\|PDF p.11]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=14\|PDF p.14]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=16\|PDF p.16]] |
| Schneider 的协调方案 | 器件与电源共同设计；受控源下机械保护仍有适用条件，固态器件自身保护也需严格协调 | 只按 µs 排名即可选定系统；所有快速动作都保持下游选择性 | [[knowledge/sources/src-accd3169319b\|来源卡]] [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=11\|PDF p.11]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=12\|PDF p.12]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=13\|PDF p.13]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=14\|PDF p.14]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=15\|PDF p.15]] |
| NVIDIA/Microsoft 的故障链 | 检测→定位→隔离→稳定；IMD 与 RCM 互补，上下级速度不协调可能扩大断电域 | 过流保护覆盖所有串联电弧；安装检测器就证明误报/漏报满足要求 | [[knowledge/sources/src-89d7f5135019\|来源卡]] [[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=4\|PDF p.4]]、[[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=9\|PDF p.9]]、[[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=11\|PDF p.11]] |
| UL bolted-fault 仿真 | 电容、导线和超级电容改变峰值、di/dt、I²t；低初始电阻和持续储能馈入均重要 | 模型即硬件型式试验；bolted fault 等同电弧入射能试验 | [[knowledge/sources/src-7bb5ed28d115\|来源卡]] [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4\|PDF p.4]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=5\|PDF p.5]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=12\|PDF p.12]] |
| 实际 DC 电弧/开断试验 | 试验中出现无 OCP 长时持续、快速开断和二次电弧等不同结果，条件必须逐例保留 | 某次 250 A MCCB 快速切断代表所有 MCCB；测试占比就是现场故障概率 | [[knowledge/sources/src-3ad922e148cf\|来源卡]] [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=8\|PDF p.8]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=9\|PDF p.9]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=11\|PDF p.11]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=12\|PDF p.12]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=13\|PDF p.13]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=14\|PDF p.14]] |

## 看似矛盾，实则边界不同

- **“限流源安全”不等于峰值低。** Siemens 示例中限流与馈电源都有约 129 kA 初始峰值，后续曲线才分开；上游控制动作前，已充电的母线/机架电容仍可放电。[[knowledge/sources/src-4533ea913815|来源卡]] [[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=14|PDF p.14]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=15|PDF p.15]]
- **典型慢不排除特定工况快。** 技术类别的“数十 ms”与特定试验的亚毫秒结果不是同一对象。应比较同型号、同电流方向、同电压、同时间常数和同动作定义的曲线，而非挑各家的最好数字。[[knowledge/sources/src-89d7f5135019|来源卡]] [[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=8|PDF p.8]]、[[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=9|PDF p.9]] [[knowledge/sources/src-3ad922e148cf|来源卡]] [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=12|PDF p.12]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=13|PDF p.13]]
- **反向阻断、开断和隔离不是同义词。** 防止机架反灌可缩小某一故障贡献，但不消除源侧供能；电子开断也不自动给出可维护的物理隔离。[[knowledge/sources/src-4533ea913815|来源卡]] [[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/LVDC-Architecture-Fundamentals-How-Topology-Protection-and-Standardization-Define-DC-Power-Systems.pdf#page=16|PDF p.16]]
- **I²t 与电弧入射能不同。** UL 模型 1 表用 A²s、模型 2 汇总用 kA²s；即使单位统一，仍不能直接当 cal/cm²，也不能据此免除实际安全评估。[[knowledge/sources/src-7bb5ed28d115|来源卡]] [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=10|PDF p.10]]

## 共同的系统验收清单（综合归纳）

1. **列出全部源。** 电网/整流器、SST、并联电池/超级电容、母线电容、机架反灌及其失效模式。
2. **覆盖状态。** 正常、失去冗余、储能高 SOC、最短/最长线路、冷热电阻、启动、通信/控制电源丢失。
3. **声明方向性。** 正向/反向持续电流、双向故障能力、器件失效短路后的上级后备、物理隔离责任。
4. **先定义保留服务，再协调动作。** 谁必须断开、谁应穿越、冷却与网络是否仍有电、重合/再上电由谁授权。
5. **证据分层。** 模拟→校准→台架→整链故障注入→投运记录；单次演示不是系统寿命/可用性。

这一清单由上述证据归纳，需由设备厂商及具备资格的工程团队按适用规则落实。没有任何一份已读资料给出一个可无条件套用到所有 800 V AI 机房的保护组合。

## CAPEX/OPEX 与未决问题

SSCB 的导通损耗和冷却、混合方案复杂度、熔断器更换、备件与维修时间都影响系统成本，但当前资料缺少统一币种/采购年份、容量与冗余边界、负载率、寿命和停机成本，不能形成可信价格排名。[[knowledge/sources/src-89d7f5135019|来源卡]] [[ai-open-dc-power-distribution/Designing-Safe-800-VDC-Systems-Protection-Fault-Management-and-Operations.pdf#page=8|PDF p.8]]

- 是否可取得同一故障矩阵下的清除能量、未受影响负载掉电概率和恢复时间？
- 模型与试验是否覆盖串弧、高阻故障和接地故障，而不只是金属性短路？
- 保护域与计算作业、网络和冷却分区不一致时，实际 blast radius 是谁决定的？

关联：[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]] · [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

