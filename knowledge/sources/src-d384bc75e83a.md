---
id: "src-d384bc75e83a"
type: "source"
title: "Sumitomo四芯光纤：线缆密度提升与FIFO迁移代价"
source_path: "expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf"
source_git_blob_sha: "42ecc1cd000d543ffd491bd687ac0de3fafcb27d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 5, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [3, 7, 8, 9, 10, 11]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Sumitomo四芯光纤：线缆密度提升与FIFO迁移代价

## 核心结论
四芯MCF把空间复用放进单根光纤，可在不立即更换端点收发器的情况下，通过两端fan-in/fan-out（FIFO）升级主干；真正收益须扣除FIFO空间、插损、连接器对准与维护成本。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=7|PDF p.7]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=10|PDF p.10]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=12|PDF p.12]]

## 关键证据、指标与条件
- p8同为6912个光学core的示例：SCF缆外径37mm、截面积1075mm²，4-core MCF为13mm、133mm²。按给定数字计算面积减少87.6%、直径减少64.9%；不能与“duct space减60–80%”混成同一分母或完整安装系统保证。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=8|PDF p.8]]
- MPO24采用24根四芯纤得到96个core，MMC16对应64个core；不是96/64根物理光纤。更高芯数路线图不能视作四芯产品当前能力。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=11|PDF p.11]]
- 文档自列劣势：每根纤及连接器更贵、维修成本更高、未标准化、core对准及洁净度要求、更复杂互操作/FIFO。没有给出实际报价或完整TCO模型。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=12|PDF p.12]]
- p3密度压力图存在代际/算术混杂：Feynman栏18×4×4应为288，与写出的576不符；因此不将该页GPU数/纤数预测用于容量规划。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=3|PDF p.3]]

## 图表与架构
已核p3/7/8/9/10/11。p7是四芯到四根单芯的两层波导FIFO概念；p10区分传统SCF、MCF主干加FIFO、端到端原生MCF三条路径。p9采用归一化直径/重量坐标，不据此推导绝对缆重。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=7|PDF p.7]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=9|PDF p.9]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]] 与 [[knowledge/comparisons/network-laser-fault-domain]]。多芯密度改变物理故障相关性：同一纤/连接器上的多个core不能默认是独立失效通道（本库归纳）。本讲认为短距WDM成本/功耗不理想，是厂商路线判断，不是对全部WDM方案的实测否定。[[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=5|PDF p.5]]

## 不确定性与待验证
需芯间串扰、FIFO及连接器累计插损、弯曲损耗、温度/波长范围、极性与core映射、维修工具和现场失败统计。面积优势不直接推出网络p99或每bit成本优势。


跨源比较：[[knowledge/comparisons/network-channel-interface-budget]]。
