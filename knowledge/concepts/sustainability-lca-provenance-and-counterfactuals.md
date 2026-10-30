---
type: concept
title: "从 BOM 到生命周期决策：证据质量、绝对量与反事实分开"
tags: [ocp2026, sustainability]
---

# 从 BOM 到生命周期决策：证据质量、绝对量与反事实分开

## 定义
生命周期决策需要两条链：**物理对象链**（身份、数量、材料、制造、运行、复用/处置）和**证据链**（来源、质量、适用时间/地区、边界、假设）。实际排放、性能归一化强度、相对某情景的避免排放是三个不同结果。

## 来源与页级证据
- Newport 单站直接再用 249 吨钢、约 10% 框架；直接复用约 520 tCO₂e 与包含再生含量策略的约 4,400 tCO₂e 不可互换。逐梁身份、检测、接受与安装追踪构成证据链。[[knowledge/sources/src-95eea63714c4]] [[Sustainability/Closing the Loop- Structural Steel Reuse in Hyperscale Datacenter Construction.pdf#page=6|PDF p.6]] [[Sustainability/Closing the Loop- Structural Steel Reuse in Hyperscale Datacenter Construction.pdf#page=7|PDF p.7]] [[Sustainability/Closing the Loop- Structural Steel Reuse in Hyperscale Datacenter Construction.pdf#page=11|PDF p.11]]
- LCA at Scale 以 DQ 0–10 分层缺失、经济代理、参数模型、代理 PCF 与原始 PCF；BOM 示例聚合需要数量和边界去重，FMD 材料映射明确不含 PCBA 装配/测试。[[knowledge/sources/src-576b1cffe203]] [[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=4|PDF p.4]] [[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=6|PDF p.6]] [[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=9|PDF p.9]]
- 性能归一化方法把参考年强度、正常效率演进 baseline 和供应链干预分开，图是反事实/预测情景，不是绝对实际降幅。[[knowledge/sources/src-4001ade000fc]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=4|PDF p.4]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=5|PDF p.5]] [[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=6|PDF p.6]]
- ABB 要求将多负载点电损耗 kWh 与电力因子拆开，按工况与寿命重算；同一 EPD 的静态使用阶段不能代表所有设施。[[knowledge/sources/src-63c5f8637ac9]] [[Sustainability/Standardizing Data Center Operational Carbon Tracking- Supplier Metrics vs. Operator Needs.pdf#page=9|PDF p.9]] [[Sustainability/Standardizing Data Center Operational Carbon Tracking- Supplier Metrics vs. Operator Needs.pdf#page=11|PDF p.11]] [[Sustainability/Standardizing Data Center Operational Carbon Tracking- Supplier Metrics vs. Operator Needs.pdf#page=16|PDF p.16]]
- 项目更新明确区分 2025 年已发布披露基础规范、2027 年中目标 PCR、已可用循环性指南与尚待发布/启动的碳核算工作。[[knowledge/sources/src-17fd666644b1]] [[Sustainability/Updates from an exciting year with the OCP Sustainability Project, DCF Sustainability Project.pdf#page=7|PDF p.7]] [[Sustainability/Updates from an exciting year with the OCP Sustainability Project, DCF Sustainability Project.pdf#page=8|PDF p.8]] [[Sustainability/Updates from an exciting year with the OCP Sustainability Project, DCF Sustainability Project.pdf#page=9|PDF p.9]] [[Sustainability/Updates from an exciting year with the OCP Sustainability Project, DCF Sustainability Project.pdf#page=14|PDF p.14]]

## 共识与分歧
数据完整性不能靠把缺失值当零；但低质量代理也不能被包装成精确实测。DQ 分数是证据等级，不是概率置信区间。供应商组件 PCF 与运营商 portfolio/使用情景各有边界；相同产品因电力组合、负载和寿命不同可有不同使用碳，不表示制造 PCF 被改写。

## 适用条件：采购包应保存什么
- BOM 版本、数量、declared unit、供应商 PCF/EPD 的边界和年份。
- 原始/代理数据标记、DQ 及人工接受记录；价格代理只能用于所定义的缺口估算。
- 损耗曲线、环境与模式、实际负载时序、寿命/再利用情景。
- 参考情景中的技术演进、采购增长、归因和重复计数规则。
- 实际绝对量与避免排放分别列示；性能强度下降不替代总量约束。

## 未决问题
复用收益分给首次购买者还是接收者？运输、清洗、检测和备件是否完整？为了延长寿命保留旧设备的额外运行能耗何时超过新设备隐含碳？需要一致服务功能单位与地区电网路径才能回答，当前材料没有统一数值阈值。

## 关联
[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]] · [[knowledge/concepts/executive-expo-manufacturing-service-chain]] · [[knowledge/comparisons/sustainability-metric-reversal-and-accounting]]
