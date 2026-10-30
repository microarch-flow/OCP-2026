---
id: "src-99abff7266fc"
type: "source"
title: "LITEON／Cambridge：800 V 到芯片的转换级数与负载效率"
source_path: "executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf"
source_git_blob_sha: "c0f23a3e3fd27ed580d54929fb5b2707d14e698e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [4, 5, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [4, 5, 7, 8, 9, 10, 11, 12]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-power-control-boundaries]]", "[[knowledge/concepts/sustainability-thermal-validation-ladder]]"]
---

# LITEON／Cambridge：800 V 到芯片的转换级数与负载效率

## 核心结论
本资料比单个“峰值效率”更有价值的是同时给出不同模块的负载曲线，并提出从三段供电到两段乃至集成 IVR 的路径。级数减少不自动等于总损耗减少，必须统一边界及工作点。[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=4|PDF p.4]][[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=7|PDF p.7]][[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=9|PDF p.9]][[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=10|PDF p.10]]

## 关键证据
| 模块 | 条件与厂商数据 | 证据 |
|---|---|---|
|800→50 V、10 kW full-brick|峰值98.7%@90 A；满载98.1%；2027年12 kW为目标|[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=4\|PDF p.4]]|
|800→50 V、6 kW half-brick|峰值98.2%@55 A；满载97.8%|[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=5\|PDF p.5]]|
|54→12 V、1,500 W IBC|Ta=55°C；峰值97.9%@500 W，满载96.9%|[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=7\|PDF p.7]]|
|54→6 V、1,000 W IBC|Ta=55°C；峰值97.9%@300 W，满载96.6%|[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=8\|PDF p.8]]|
|54→0.8 V 单级VRM|单模块240 A、四并800 A；峰值91.4%、满载87%|[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=9\|PDF p.9]]|

## 指标与条件
不能用各级**不同负载点**的峰值相乘预测整机效率。p.9 标题写 50 V、功能与曲线写 54 V；比较图引述 Google/Meta 双级方案，但相同热条件与系统寄生条件未完整给出。四个240 A模块的800 A并联额定也不能擅自改成960 A。[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=9|PDF p.9]]

## 图表与架构
p.10 的“单级”路径指外部 800 V→12/6/3.3 V，核心内仍有 IVR，因此不能称 800 V 直接无损到核心。p.12 金刚石微通道封装宣称单面/双面热阻0.16/0.1°C/W、绝缘>3 kV（测试仪上限）；热源与流量条件不足，不能直接横比GPU冷板。[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=10|PDF p.10]][[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=12|PDF p.12]]

## 关联与比较
与800 V液冷电源架比较时，把AC/DC、隔离DC/DC、IBC、VRM/IVR、母排损耗逐项列出，加入部分负载、瞬态及冷却功耗再评估tokens/J。

## 不确定性与待验证
AI辅助磁性元件设计给出2,137参数、6.50%磁芯损耗误差，但未充分披露样本及外推条件；它是设计建模结果而非整机节能验证。[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=11|PDF p.11]]

## 知识网络
[[knowledge/concepts/executive-expo-power-control-boundaries]] · [[knowledge/concepts/sustainability-thermal-validation-ladder]]
