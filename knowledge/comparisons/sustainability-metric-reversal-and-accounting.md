---
type: comparison
title: "当绿色指标方向相反：六种容易误判的边界与基线"
tags: [ocp2026, sustainability]
---

# 当绿色指标方向相反：六种容易误判的边界与基线

## 比较问题
下列例子不做厂商优劣排名，而是展示**指标改善与实际目标可能反向**的原因。每一行都需要保留原始功能单位与基线；说明性场景、模型与实测分开。

| 看起来的改善 | 资料中的反例或限制 | 决策应追加的量 |
| --- | --- | --- |
| PUE越低越好 | DCEM示例DLC使总497→485W但PUE1.28→1.37 | 同任务设施kWh、服务器风扇与CDU归属 |
| 峰值W越低越省能 | SNN示例ASIC2.883W却29.877J，CPU60.2W却18.479J | 任务时长、成功率、总J与测量边界 |
| 每TOPS隐含碳下降就是绝对减碳 | 性能归一化可随硬件进步下降，同时采购增长使绝对Scope3上升 | 总kgCO₂e、实际利用率/寿命、任务性能 |
| 湿冷省电所以总成本更低 | Daikin模型某些区域水/污水费使干冷费用更低；WESI不含水压力 | 小时电价/需量费、水价、CAPEX与缺水约束 |
| 循环L/min减少就是同幅度节水 | 两相原型的低流量不能代替设施补水/消耗与上游水账本 | 取水、消耗、排污、蒸发、储量变化 |
| 回收热比例越高回本越快 | Hitachi说明性方案WHRF0.04→0.06，成本35→50万美元、回本4.5→6.3年 | 热用户年度需求、输送/热泵能耗、真实现金流 |

## 页级证据与类型
- 功率/PUE与任务能量：示例/特定任务数据，不能扩展所有平台。[[knowledge/sources/src-a5fa26b34893]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=9|PDF p.9]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=12|PDF p.12]] [[Sustainability/DCEM workstream update- Case studies of metric measurements from servers to data centers.pdf#page=13|PDF p.13]]
- 隐含碳归一化：方法与假设情景，非微软实际绝对减排曲线。[[knowledge/sources/src-4001ade000fc]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=2|PDF p.2]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=4|PDF p.4]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=5|PDF p.5]]
- 干湿冷却：18区域小时模型，非18个现场实测。[[knowledge/sources/src-865e0a58fa77]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=7|PDF p.7]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=8|PDF p.8]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=9|PDF p.9]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=10|PDF p.10]]
- 水边界：工作组框架＋原型的设施外推需要补证。[[knowledge/sources/src-86773c5feb8c]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=4|PDF p.4]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=5|PDF p.5]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]] [[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=12|PDF p.12]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=13|PDF p.13]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=14|PDF p.14]]
- 余热经济性：明确illustrative，回收期缺完整现金流。[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=7|PDF p.7]]

## 算术与口径先于优化
Lenovo示意屏总/IT电量3.14/2.14 MWh却显示PUE0.66，按其定义约为1.47；它首先是数据一致性错误，不能被当成行业领先成绩。ABB“400%误差”缺可复算基线，也不能成为所有EPD的通用误差率。[[knowledge/sources/src-1b8ab113ff06]] [[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=5|PDF p.5]] [[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=7|PDF p.7]] [[knowledge/sources/src-63c5f8637ac9]] [[Sustainability/Standardizing Data Center Operational Carbon Tracking- Supplier Metrics vs. Operator Needs.pdf#page=13|PDF p.13]] [[Sustainability/Standardizing Data Center Operational Carbon Tracking- Supplier Metrics vs. Operator Needs.pdf#page=15|PDF p.15]]

## 使用方法
先确定目标（同质量同SLA完成任务、成本、水压力或碳），再列硬约束及绝对资源预算，最后用多指标看可行解；不把不同边界的百分比相加。给未知项留下空白，比给一张貌似统一的排行榜更可靠。

[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]] · [[knowledge/concepts/sustainability-water-energy-heat-tradeoffs]] · [[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]]
