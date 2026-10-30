---
id: "src-3c6dee4db3ee"
type: "source"
title: "TeraHop：XPO、Open CPX 与四芯光纤的并行演进"
source_path: "executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf"
source_git_blob_sha: "52f0c2c7c5449b721528fc8d6a33788365d6d98c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [4, 7, 9, 13, 14, 15, 17, 19]
text_reviewed: true
key_pages_visual_checked: [7, 8, 9, 13, 14, 15, 17, 19]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]"]
---

# TeraHop：XPO、Open CPX 与四芯光纤的并行演进

## 核心结论
XPO、NPO/CPO 和多芯光纤分别改变面板密度、光电转换位置与布线密度，并不是同一层面的互斥路线。本文提供早期链路测量，也含明确的厂商偏好与概念图，需区别证据等级。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=4|PDF p.4]][[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=9|PDF p.9]][[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=17|PDF p.17]]

## 关键证据
- 12.8T XPO 页展示 64 发射器、8×1.6T DR8 的 pre-FEC BER 曲线；同时测进液 25/35/45°C、0.3 LPM 的激光温度，以及不同流量的模块功耗。不能只引用 12.8T 而忽略热条件。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=7|PDF p.7]]
- Diablo-1 6.4T NPO **初步**测试展示 32 通道，ER=3 dB、TECQ=2.1 dB，ASIC 至 NPO 插入损耗约 12 dB；这不是规模化系统故障率数据。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=13|PDF p.13]]
- 集成激光 NPO 声称含激光约 5.5 pJ/bit，并采用与 ASIC 分开的冷板。对 ELSFP 的 >3 dB 额外损耗、约 4 倍激光功耗等为该厂商特定比较，不能当成所有外置激光架构必然结论。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=14|PDF p.14]]

## 指标与条件
p.15 声称历史硅光模块出货 >2,500 万、PIC 累计 >1,000 亿器件小时、FIT<0.01；图中 PIC、激光器、模块与新 NPO/XPO 的统计边界不同，不能将成熟 PIC FIT 直接迁移为新系统 FIT。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=15|PDF p.15]]

## 图表与架构
p.9 截面清楚区分主板上 NPO、ASIC 基板上 CPO，以及通过弹性高密连接器连接 HDI 板的 IOA。p.17 四芯光纤通过四个物理分离的芯减少纤维/端接数量，并非单芯速率提升四倍。p.19 右侧“减少光纤”图明确为 **Google Gemini 生成的概念图**，不是部署照片。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=9|PDF p.9]][[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=17|PDF p.17]][[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=19|PDF p.19]]

## 关联与比较
评估开放光接口时，应分别检查电气插损预算、激光/冷板热边界、可更换单元、连接器污染与现场工序；不能仅按 pJ/bit 选择集成或外置激光。

## 不确定性与待验证
需完整 BER 样本、FEC 配置、运行时长、失效统计置信区间及同条件 ELS 对照；MSA 版本和展示支持不等于量产互操作验证。

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]]
