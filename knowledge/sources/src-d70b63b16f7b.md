---
id: "src-d70b63b16f7b"
type: "source"
title: "HFH微射流冷板与光模块TIM：热阻、压降和可插拔寿命的权衡"
source_path: "expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf"
source_git_blob_sha: "28b427a844ebdcfce1bbbd80b41c72cf132dcb95"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [5, 8, 9, 11, 12, 13, 15, 16]
text_reviewed: true
key_pages_visual_checked: [11, 13, 16]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# HFH微射流冷板与光模块TIM：热阻、压降和可插拔寿命的权衡

## 核心结论
HFH用manifold微射流把冷液优先分配热点，以缩短流路并降低压降；VC与fin一体化减少中间焊接层；光模块用浮动冷板保证接触。这三类设计分别解决流体分配、固体热阻和插拔机械问题，不能只看总冷却W。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=9|PDF p.9]] [[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=12|PDF p.12]] [[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=15|PDF p.15]]

## 关键证据、指标与条件
- 供应商声称每冷板五项100%检查、氦漏率<1×10⁻⁶mbar·L/s、测流阻热阻、钎焊接头逐个C-scan。检查覆盖率不是服役故障率。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=5|PDF p.5]]
- 路线：2025 MCCP量产、2026 mJet/VC量产，P2P两相仍研发、芯片级测试计划2027Q1，diamond-copper/thermosyphon更远期。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=8|PDF p.8]]
- mJet范围800–3500W、热点>500W/cm²、1.35–4.5L/min、入口25–45°C，是能力范围，未证明每个组合皆通过。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=11|PDF p.11]]
- TH7示例Cu fin高1.2mm/厚0.1mm/距0.12mm，计算场标平面最高85°C、Tcase限制90°C余量5°C、压差约2.16psi；热图色标顶却约82.5°C，与85°C标注不完全一致。未给本页总功率、供水温/流量及实测校准，应视设计/仿真展示，不是量产TH7温度认证。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=13|PDF p.13]]
- p16视觉补全：30W界面温差，thermal tape3–4°C、skateboard4–6°C、coating4–6°C；厚度0.1–1.6/0.26/0.03mm，插拔≤200/>500/≥200次，材料PCM+PI/SUS301+PCM/silicone composite。相同温差不代表相同寿命或成本，循环后的判据未给。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=16|PDF p.16]]

## 图表与架构
已核p11/13/16。浮动冷板选1×16共享、2×8或1×1，模块相互影响、接头数量与接触一致性互有代价；“最低压降/最佳接触”缺对照曲线。[[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=15|PDF p.15]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]；可与Frore比较结构机制，不可把HFH热点500W/cm²与Frore35%tokens/W直接排序。光学系统还需接触/插拔与信号故障联合测试。

## 不确定性与待验证
需冷液种类、热源地图、TIM/装配压力、泵功与冷板寿命分布。高热点能力不等于整die均匀承受该热流，也不保证GPU热点和HBM同时满足限制。


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
