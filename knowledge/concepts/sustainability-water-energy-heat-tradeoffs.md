---
type: concept
title: "水、电、碳与余热：先画流量边界，再选冷却方案"
tags: [ocp2026, sustainability]
---

# 水、电、碳与余热：先画流量边界，再选冷却方案

## 定义
**循环流量**是闭环输送能力（L/min）；**取水**是跨场地边界的入水；**消耗**是未回到相应水系统的水；现场与供电上游又是不同空间边界。余热价值同时由温度、可供热量、时间、地点及热用户需求决定。低 PUE、低现场 WUE、低成本和低碳不必是同一方案。

## 来源与页级证据
- 水工作组要求从边界、计量、水量平衡走向 KPI，区分现场、上游和施工，并加入流域压力与免费冷却窗口。[[knowledge/sources/src-86773c5feb8c]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=3|PDF p.3]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=4|PDF p.4]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]] [[Sustainability/Sustainability and best practices for water efficiency.pdf#page=7|PDF p.7]]
- Daikin 对 18 个区域的小时模拟，用 WESI=盈亏平衡水价/实际水价比较湿/干成本；它不包含水压力。每额外 Mgal 现场水的碳收益随电网脱碳至 2050 下降 29–99%，不是总设施碳下降幅度。[[knowledge/sources/src-865e0a58fa77]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=7|PDF p.7]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=8|PDF p.8]] [[Sustainability/Cooling the Cloud- Regional Tradeoffs in U.S. Data Center Cooling Architectures.pdf#page=9|PDF p.9]]
- Microsoft 的余热框架按实际运行 IT 而非铭牌容量承诺热源，采用换热器隔离责任并匹配温度、时间、规模、地点。[[knowledge/sources/src-c0b1a4f05c97]] [[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=4|PDF p.4]] [[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=6|PDF p.6]] [[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=10|PDF p.10]] [[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=11|PDF p.11]]
- Lightning Talks 中更高 WHRF 的说明性方案并非更短回本期；两相水冷将循环流量减少外推成同幅度节水，缺少补水与排放账本支撑。[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=7|PDF p.7]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=13|PDF p.13]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=14|PDF p.14]]
- 项目状态表把蒸发冷却的现场水、上游水与总水分别标增、减、待评估，拒绝单一方向结论。[[knowledge/sources/src-17fd666644b1]] [[Sustainability/Updates from an exciting year with the OCP Sustainability Project, DCF Sustainability Project.pdf#page=17|PDF p.17]]

## 共识与分歧
湿式冷却可用更多现场水换更少用电，但电网水强度/碳强度、当地水费与干旱约束会改变选择。直接液冷与直接余热回收并不自动意味着零现场/上游水；“不在芯片旁蒸发”也不能替代设施总账。

## 适用条件：两阶段选择
1. **可行性约束**：峰值热负荷、芯片温度、可靠性、流域供水限制、场地空间和服务 SLA。
2. **可行解比较**：全年小时天气/负载、泵和冷机电量、取水/消耗/排放、当地/时变碳因子、CAPEX/OPEX、热用户需求与备用方案。

余热收入只对实际可交付 MWh 和接收温度计价；提高源温度必须同时检查 IT 性能、材料与热泵/泵功。原材料没有提供可跨站直接套用的回本期。

## 未决问题
冷却改造的补水计量是否闭合？热用户夏季不接热时如何退回可靠主冷却？电网未来路径、干旱和水价如何做敏感性？这些问题优先于按单次最低 PUE 排名。

## 关联
[[knowledge/concepts/sustainability-thermal-validation-ladder]] · [[knowledge/concepts/executive-expo-liquid-cooling-evidence]] · [[knowledge/comparisons/sustainability-metric-reversal-and-accounting]]
