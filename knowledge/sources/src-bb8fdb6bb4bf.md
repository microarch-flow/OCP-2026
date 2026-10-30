---
id: "src-bb8fdb6bb4bf"
type: "source"
title: "跨传统与 AI 机房的功率管理：分层闭环、事件和恢复顺序"
source_path: "market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf"
source_git_blob_sha: "bb265c109813789505bc02017418fab13e5673d7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 4, 8, 9, 10, 11, 13, 14, 15, 16]
tags: ["ocp", "source", "platform", "market-impact-adoption"]
text_reviewed: true
key_pages_visual_checked: [9, 10, 15]
updated: "2026-10-30"
---

# 跨传统与 AI 机房的功率管理：分层闭环、事件和恢复顺序

> 阅读范围：已阅读本文件全部可提取文字（18页）。关键页已视觉核对：9, 10, 15；不代表逐页视觉审核。

## 核心结论

统一功率管理需要同时覆盖传统 PDU/AC 与 power shelf/DC、CDU、eFuse、supercapacitor；新增接口只是第一步，还需分层采样、硬约束优先、应急策略和分阶段上电。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=3|PDF p.3]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=4|PDF p.4]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=8|PDF p.8]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=10|PDF p.10]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=16|PDF p.16]]

## 关键证据

- 低层采样应比高层更快，秒级 burst 不能只由分钟级聚合判断；材料未给通用采样率。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=8|PDF p.8]]
- tiered capping 从 component→system→rack→cluster→DC，执行点取 hard constraints 与上层policy的约束，形成反馈；ML预测只是策略输入。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=10|PDF p.10]]
- 事件词表新增 shelf redundancy lost、DC droop、supercapacitor短路、OAM eFuse latch-off等；reset与full power-cycle是不同恢复动作。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=13|PDF p.13]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=14|PDF p.14]]
- 分阶段上电与存储/网络依赖需要rack manager执行，不能仅在所有电源打开后期待业务自动恢复。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=16|PDF p.16]]

## 指标与条件

p.9 引述 A100 MILC 特定任务在约50%TDP cap下性能损失<15%，另一个 CPU/LAMMPS 配置示意15%功率降低而性能影响小；两者负载与平台不同，不能合并成AI推理普遍节能曲线。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=9|PDF p.9]]

品牌样本中11家 power shelf约27.3% Redfish/72.7% SNMP，23家PDU约21.7% SNMP+Redfish/78.3% SNMP；这是品牌口径，不是出货或fleet设备占比。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=15|PDF p.15]]

## 图表与架构

已核对 p.9 平台条件、p.10 分层回路和 p.15 样本分母；没有从图中估计通用cap最优点。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=9|PDF p.9]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=10|PDF p.10]][[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=15|PDF p.15]]

## 关联与比较

与 SCMP 和平台可运营性契约相连：统一外部行为可保留legacy SNMP，而不必把“统一”理解为全部设备立刻替换Redfish。需要权限、事件顺序、失联fallback和恢复验证。

## 不确定性与待验证

p.11 的事故时间线与soft/hard EPR是案例/方案讨论，不是可直接执行的应急操作规程；风扇、冷却和断电动作必须由现场安全设计与设备要求决定。材料没有证明预测模型、闭环稳定性或SLA影响。[[market-impact-adoption/01_A unified power management solution for AI data centers and legacy dat.pdf#page=11|PDF p.11]]

