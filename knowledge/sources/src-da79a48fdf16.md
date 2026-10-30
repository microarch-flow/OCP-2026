---
id: "src-da79a48fdf16"
type: "source"
title: "Wiwynn：直接键合金刚石微通道的 3 kW 热测试证据"
source_path: "fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf"
source_git_blob_sha: "b4af1e52184024f0a3f1437e63d7c34f5caf40d3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text_reviewed: true
key_pages_visual_checked: [2, 3, 4, 5, 6, 7, 8, 9]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-thermal-validation-ladder]]"]
---

# Wiwynn：直接键合金刚石微通道的 3 kW 热测试证据

## 核心结论
Nick Liu、Jake Hsieh（Wiwynn）报告将单晶金刚石微通道直接键合硅热测试载体的实验。在所列 3 kW 工况下，结到入口热阻从 0.0254 降至 0.0157 °C/W，降幅 **38.2%**。这是“材料＋微通道＋键合界面”组合相对铜冷板＋PCM TIM 的结果，不是只换材料的隔离实验，也不是整机柜节能率。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=1|PDF p.1]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]]

## 关键证据
- 材料表给单晶金刚石导热率 >2,000 W/(m·K)、热膨胀系数约 1 ppm/K；铜约 400 W/(m·K)、17 ppm/K。金刚石铜复合材料是另一列，不能与本次单晶样件混为一物。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=3|PDF p.3]]
- 微通道鳍宽与间隙各 0.1 mm、高 1 mm、基底厚 0.5 mm，面积 32.2 × 25.7 mm²；金刚石与硅均采用 Ti/Ni/Au 金属化，再通过铟回流键合，上盖 O 形圈密封并用螺钉固定。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=4|PDF p.4]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=5|PDF p.5]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=6|PDF p.6]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=8|PDF p.8]]
- 240/300/360 W/cm²、即 2,000/2,500/3,000 W 下，铜＋PCM 基线最高结温分别 84.3/95.0/106.2°C，新结构为 64.9/70.8/77.1°C；相应热阻分别 0.0272/0.0260/0.0254 与 0.0175/0.0163/0.0157 °C/W。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]]

## 指标与条件
p.9 明确测试介质 **PG25、入口 30°C、流量 2 LPM/kW**；硅 TTV 有 9 个结温测点，加热区域 32.2 × 25.7 mm²。流量按功率归一化，所以 3 kW 点对应 6 L/min，而不是全曲线固定 2 L/min。冷板泵压、泵功、芯片功能性、生产良率与长期循环寿命未给出。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]]

## 图表与架构
已核对 p.2–9 的热阻拆解、材料表、层间结构、制作步骤及完整对照表。结构减少传统 TIM 接触路径但仍存在金属化/铟键合界面；作者将实测 38.2% 与模拟 59.5% 的差距推测归因于非理想键合的界面热阻，尚非独立故障归因实验。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=4|PDF p.4]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=7|PDF p.7]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]]

## 关联与比较
对高功率加速器，此材料提供比“支持几千瓦”营销口号更完整的比较边界；但与另一方案比较时仍需统一结温/壳温/液侧热阻定义、面积、入口温度、流量与压降。p.2 的冷板＋TIM 占总热阻 65–85% 是该演讲的背景估计，不宜套用所有封装。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=2|PDF p.2]][[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]]

## 不确定性与待验证
仍在改善键合、探索其他金刚石复合材料和扩大制造规模；展台演示与白皮书入口不证明已规模部署。后续应补热循环、腐蚀/兼容性、漏液、键合应力、可返修性及单位成本，否则不能由 TTV 温度降低推断部署 TCO。[[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=10|PDF p.10]]

## 知识网络
[[knowledge/concepts/sustainability-thermal-validation-ladder]]
