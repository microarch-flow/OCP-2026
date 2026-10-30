---
id: "src-9e459d39cae8"
type: "source"
title: "CoolIT无风扇服务器：15kW热测试与外围100%热捕获分开验收"
source_path: "expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf"
source_git_blob_sha: "446d04eb48e20be34be940e69f6cd5dd492b457f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 27
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 8, 12, 14, 15, 17, 18, 19, 21, 22, 25, 26]
text_reviewed: true
key_pages_visual_checked: [5, 14, 18, 22, 25]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# CoolIT无风扇服务器：15kW热测试与外围100%热捕获分开验收

## 核心结论
当主芯片已液冷，DIMM、VRM、NIC、OSFP、SSD及板级器件残余热仍可主导机房风冷负担。CoolIT用模块化冷板环路/导热板/整体冷板三种组合提高热捕获率；“无风扇”需整机热平衡而非仅验证一块GPU冷板。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=7|PDF p.7]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=8|PDF p.8]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=22|PDF p.22]]

## 关键证据、指标与条件
- 固定70%液/30%风的算例：250kW机柜残留75kW风冷、500kW残留150kW。“>250kW必须100%热捕获”和“150kW不可能风冷”是该供应商设计主张，不是由这张比例图证明的普适物理阈值。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=5|PDF p.5]]
- 15kW冷板/TTV验证：1.2LPM/kW即总18L/min（本笔记算术），45°C设施水、80°C case、Δ35°C；是冷板与thermal test vehicle，不是15kW量产GPU或芯片结温80°C。无die地图/面积/压降，不能说已验证未来五代全部热点与HBM约束。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=14|PDF p.14]]
- DIMM路径：<20W单侧tube+clip，20–40W以上双侧VC或tube；网络/存储模块<15W固定冷板、>15W riding coldplate，选择还受TIM耐磨与安装空间制约，15W仅此产品划分。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=17|PDF p.17]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=18|PDF p.18]]
- 导热板覆盖SSD/SOCAMM/VRM/NIC，并可board-referenced+gap pad、die-referenced+PCM、双面或板下散热；覆盖全部器件并不自动量化100%的测量误差。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=19|PDF p.19]]
- p25把CIT today(300W/cm²+、4kW+冷板、500kW+柜)与tomorrow(500W/cm²+、15kW+冷板、1MW+柜)并列。p14单项15kW验证不能把全部tomorrow系统规模晋升为当前量产。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=25|PDF p.25]]

## 图表与架构
已核p5/14/18/22/25。模块环路可维修独立部件；单体板减少部分连接但改变拆装故障域，mixed折中。未给三者接头数量/MTTR统计，不能预设哪种最可靠。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=21|PDF p.21]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=22|PDF p.22]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]。与HFH floating冷板相通的是热接触和可维护性共设计；Frore温差/token收益与本讲TTV热容量不是相同基准。

## 不确定性与待验证
部分页标Confidential、p15标NDA ONLY，原件标识保留。缺整机热捕获量测、长期腐蚀/侵蚀曲线、泵功、冷却液和故障降额；“单相赢所有层级”是厂商立场，不是对两相/浸没的等条件比较。[[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=12|PDF p.12]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=15|PDF p.15]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=26|PDF p.26]]


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
