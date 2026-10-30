---
id: power-cooling-single-vs-two-phase
type: comparison
title: "单相与两相冷板：比较的是完整系统，不是单一潜热"
tags: ["ocp2026", "power-cooling", "cross-source"]
---

# 单相与两相冷板：比较的是完整系统，不是单一潜热

## 比较问题与口径

在相同芯片功率图、结温/可靠性目标、设施水边界和冗余要求下，哪种冷却架构能以可接受的泵功、空间、维护和全生命周期成本交付容量？以下是条件化证据，**不建立通用冠军排名**。

## 并列证据

- **单相微流体优化：** H200在同流体、同1LPM和测试架下，供应商报告GPU结到入口温升29.5→23.9°C，HBM42.0→32.4°C；未披露功率/入口温度/压降，不能推算整机节电。[[knowledge/sources/src-b544bc4ee058|Pushing the Single-Phase Cold Plate Limit]] [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=16|PDF p.16]]。
- **负压水沸腾：** 特定2kW试验比较了热阻组成、流量与压力条件；低流量或某层热阻下降不能直接视为设施总电耗下降。[[knowledge/sources/src-d81f4633d93f|A Novel Liquid Cooling Solution- A Negative-Pressure Two-Phase Water-Boiling Cold Plate]] [[Cooling：Cold Plate/A Novel Liquid Cooling Solution- A Negative-Pressure Two-Phase Water-Boiling Cold Plate.pdf#page=6|PDF p.6]] [[Cooling：Cold Plate/A Novel Liquid Cooling Solution- A Negative-Pressure Two-Phase Water-Boiling Cold Plate.pdf#page=7|PDF p.7]]。
- **直接换工质的反例：** AVC/Wiwynn在PG25设计冷板上分别比较PG25与R515B/R1233zd(E)，PG25结温更低。它证明需要两相专用设计，不证明优化后两相必然差。[[knowledge/sources/src-e3364f4601e1|System-level Challenges and Considerations in Transitioning from Single-Phase to Two-Phase Cooling]] [[Cooling：Cold Plate/System-level Challenges and Considerations in Transitioning from Single-Phase to Two-Phase Cooling.pdf#page=9|PDF p.9]]。
- **系统代价：** 两相可能需要限流/调节器、更大回流管与接收罐、低NPSHr泵；这会改变泵扬程、CDU占地和维修。[[knowledge/sources/src-e3364f4601e1|System-level Challenges and Considerations in Transitioning from Single-Phase to Two-Phase Cooling]] [[Cooling：Cold Plate/System-level Challenges and Considerations in Transitioning from Single-Phase to Two-Phase Cooling.pdf#page=10|PDF p.10]] [[Cooling：Cold Plate/System-level Challenges and Considerations in Transitioning from Single-Phase to Two-Phase Cooling.pdf#page=11|PDF p.11]]。
- **标准化成熟度：** 圆桌材料仅给议题与行动项，未给大规模互操作/运维实测。[[knowledge/sources/src-f37354b8183d|Reducing Operational Complexity Through Standardized Two-Phase Liquid Cooling for AI Infrastructure]] [[Cooling：Cold Plate/Reducing Operational Complexity Through Standardized Two-Phase Liquid Cooling for AI Infrastructure.pdf#page=3|PDF p.3]] [[Cooling：Cold Plate/Reducing Operational Complexity Through Standardized Two-Phase Liquid Cooling for AI Infrastructure.pdf#page=4|PDF p.4]]。

## 共同验收清单（综合判断）

1. 芯片：非均匀热图、HBM温限、TIM、翘曲、封装/冷板安装公差，不能只用均匀铜块TTV。
2. 液压：入口温度、全回路压降、流量/质量流量、支路负载变化；两相增加压力—饱和温度、干度、流动不稳定与回流汽体积。
3. 设施：冷凝/换热端温差、设施水温可达性、环境极端温度与失电恢复。
4. 可靠性：材料/工质寿命、颗粒堵塞、密封、泄漏、服务接口、备用件与供应商可替代性。
5. 经济性：在同利用率、币种、建设边界和寿命期内算CAPEX/OPEX，不把百分比温升改善当百分比节电。

## 不可比较项与待补证据

水沸腾、不同冷媒和单相PG25的单个实验，不具备相同冷板/热图/系统边界；“相同LPM”也不等于相同质量流量或泵功。需要面向相同计算任务的系统对照和动态故障测试，才能决定产品路线切换时点。

