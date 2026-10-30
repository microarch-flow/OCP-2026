---
id: "src-883fafcb5701"
type: "source"
title: "Custom HBM as a System: Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI Accelerators"
aliases: ["Custom HBM as a System: Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI Accelerators"]
speakers: "Mark Hsin-wei Tseng — Director, Marvell Technology"
source_path: "Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf"
source_git_blob_sha: "3e441b03ab33806a2f3ca10ae143abafe357e044"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 5, 7, 8, 9, 10, 11, 13]
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-package-memory-wall]]", "[[knowledge/concepts/compute-memory-federated-model-contract]]"]
---

# Custom HBM as a System: Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI Accelerators

## 核心结论
cHBM把PHY/controller移入可定制base die，可以释放compute die的面积/shoreline，但把问题转化为 **base-die接口能耗、堆叠热阻、混合键合良率和跨供应商共同设计**。不能将“移走HBM PHY”直接等同于整颗加速器等比例提高性能。

## 关键证据
- HBM4接口2048bit使PHY、power、die edge压力增加。演讲引用约30%compute-die面积、>50%XPU成本及部分BOM60–80%等估算，来源/分母不同，**不是所有GPU都满足的常数**。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=3|PDF p.3]]
- 定制base die目标是回收up to25%die area并用于up to30%更多compute；这是方案级价值主张，未包含frequency、memory-stall、yield变化后的实测性能。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=4|PDF p.4]] [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=13|PDF p.13]]
- p.7引用某2.5D stackup热阻分解：HBM内部57%、ASIC内部13%，两者是各自热路径组成，不是HBM占整机散热57%。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=7|PDF p.7]]
- p.8援引hybrid bond相对microbump降低die-to-die热阻23–47%，依赖Cu pad coverage≥20%及interface质量；更短热路径不消除3D逻辑堆叠更高footprint热流密度。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=8|PDF p.8]]
- 为D2D PHY热点预留silicon heat path，TIM/lid/cold plate与base die一起设计，而非最后补冷却。p.9的~100W/stack为HBM5 projection，不是本演讲测得样品。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=9|PDF p.9]]

## 指标与条件
p.10 SBD相对“无adaptive power management接口”：normal workload功率25%（−75%）、peak traffic58%（−42%）；**不是整芯片功耗下降75%，也不是峰值流量下降75%**。normal workload的activity分布未给。p.11列64Gb/s/wire、15%PHY area等厂家IP主张，缺统一面积/性能比较边界。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=10|PDF p.10]] [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=11|PDF p.11]]

p.5 HBM4E/next-gen带宽含2027–28E、2028E+预测及不同pin rate区间；不把它们写成当前量产保证。p.6 TDP/logic-area推导的W/mm²也不同于HBM局部hotspot热通量。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=5|PDF p.5]] [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=6|PDF p.6]]

## 图表与架构
已检查p.13最终checklist：跨memory vendor接口、3D volume yield、>100W/stack与>2W/mm² cooling验证、可复用cHBM模块仍未勾选；前页全空checklist是引导页，不能当最终完成状态。[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=12|PDF p.12]] [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=13|PDF p.13]]

## 关联与比较
[[knowledge/concepts/compute-memory-package-memory-wall|封装内存墙：shoreline、热与容量不是同一个问题]]；[[knowledge/concepts/compute-memory-federated-model-contract|共享热/功率模型契约]]。与Weaver外部LPDDR及GUC DRAM-on-compute的取舍在封装范围、容量密度、能耗与制造成熟度上不同。

## 不确定性与待验证
材料混合公开文献、厂商新闻和未来估算，非单一可复现实验。要评估成本收益需base-die面积/工艺、bond yield、test/repair、stack温度、真实流量下pJ/bit和package级供电/散热共同数据。


## 原始页码导航
[[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=13|p.13]] · [[Server：Open Chiplet Economy/Custom HBM as a System- Co-designing the Base Die, Die-to-Die Power, and Package Thermals for AI.pdf#page=14|p.14]]
