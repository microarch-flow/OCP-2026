---
id: "src-740daf8fb736"
type: "source"
title: "OPEN NPO：36通道电连接器与SuperPOD路线"
source_path: "ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf"
source_git_blob_sha: "3cfba5c640b4a2f56a1266aedc3d4287027021d9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17]
text_reviewed: true
key_pages_visual_checked: [12, 15]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# OPEN NPO：36通道电连接器与SuperPOD路线

## 核心结论
此项目首先统一NPO电连接器，而非统一所有光PHY或总线协议。它与OpenCPX同样试图拆开芯片/OE供应链，但材料没有证明二者机械或电气互换。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=5|PDF p.5]][[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=6|PDF p.6]][[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=7|PDF p.7]]

## 关键证据、指标与条件
- Type1 connector与NPO module样品在测试；2026–2027 Type1、2027–2028高密度Type2、2029–2030 OIO为计划，首步向OCP贡献时间标2026-12-30。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=7|PDF p.7]][[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=17|PDF p.17]]
- 72 differential pairs=36双向通道，另96 power/low-speed pins。p.12图是16列×26行，功率低速实际位于两侧各两列；正文“first and last columns”不够精确，不能当pin文件。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=12|PDF p.12]]
- 机械要求：插入力≤150N、初始拔出力≥20N、全行程≤80N、50次耐久，承压瞬时≥380N/长期≥183N；这些是规格要求，不是全部测试通过报告。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=13|PDF p.13]]
- 低速/电源pin额定1A、12VDC，body impedance80–90Ω；IL≤1.5dB@10MHz–56GHz，ERL≥11dB以CEI-224G-Linear计算。不得把额定pin电流乘所有pin当模块可用供电。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=14|PDF p.14]]

## 图表与架构
已核p.15：IL和impedance图**包含test board**；RL/NEXT/FEXT标为去嵌入。IL图在56GHz约数dB损耗，不可直接拿它与connector-only1.5dB规格对比判不合格；反之也不能据图宣布全部满足规范。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=15|PDF p.15]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]：与OpenCPX/XPO共同构成连接器生态，但应分开看formfactor、lane count、SI条件、生命周期及控制接口。

## 不确定性与待验证
“τ scaling law”和NPO首选属于演讲观点，未提供可计算模型或部署数据。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=3|PDF p.3]][[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=4|PDF p.4]] 2027–2028 switch-to-switch、2028–2029 XPU光输出是实施路线，尚非规模交付；需原始S参数、去嵌入方法、温度/寿命与插拔后性能。[[ocp-special-focus-photonics/Open-NPO-Standards-Building-the-Optical-Interconnect-Ecosystem-for-SuperPOD.pdf#page=16|PDF p.16]]

