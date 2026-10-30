---
type: concept
title: "浸没资格的证据链：材料兼容、功能验证与服役可靠性不是一回事"
tags: [ocp2026, concept, immersion]
---

# 浸没资格的证据链：材料兼容、功能验证与服役可靠性不是一回事

## 核心命题
“兼容”“通过”“长期稳定”必须带上对象、fluid/BOM、工艺、条件和统计定义。资格不能从coupon直接跳到整机寿命；提高温度也不能在没有机制与加速模型时自动换算多年服役。

## 来自材料的分层比较
|证据层|具体案例|能支持什么|不能支持什么|
|---|---|---|---|
|材料筛查|Samsung Opteon2P50，49°C Soxhlet72h；80°C soak2/4周，所测质量变化<2%。[[cooling-immersion/Material-Compatibility-and-Long-Term-Hardware-Integrity-of-Enterprise-SSDs-in-Two-Phase-Immersion-Cooling.pdf#page=6\|PDF p.6]] [[cooling-immersion/Material-Compatibility-and-Long-Term-Hardware-Integrity-of-Enterprise-SSDs-in-Two-Phase-Immersion-Cooling.pdf#page=7\|PDF p.7]]|所测材料/工艺在给定暴露下的外观/质量与功能|全BOM、所有fluid或多年的可靠性|
|隔离器件平台|Solidigm48位SSD-only架构，高温powered-on idle、30–40°C周期读出。[[cooling-immersion/A-Practical-Infrastructure-Solution-for-Component-and-Device-Level-SSD-Qualification-in-Single-Phase-Immersion-Cooling.pdf#page=3\|PDF p.3]] [[cooling-immersion/A-Practical-Infrastructure-Solution-for-Component-and-Device-Level-SSD-Qualification-in-Single-Phase-Immersion-Cooling.pdf#page=7\|PDF p.7]]|隔离SSD来源的热化学影响、控制污染|已完成48个样品的寿命资格；满载I/O长期稳定|
|板表面电学|多fluid、80°C/500h/5V bias，四package geometry。[[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=6\|PDF p.6]] [[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=7\|PDF p.7]]|电阻与fluid aging/field-history关联|直接映射服务器失效率或BER|
|产品运行|Samsung Gen4/5 SSD，JESD219，>15000h ongoing无观察失败。[[cooling-immersion/Material-Compatibility-and-Long-Term-Hardware-Integrity-of-Enterprise-SSDs-in-Two-Phase-Immersion-Cooling.pdf#page=3\|PDF p.3]]|该组合的运行经验|未知样本量下的MTBF、置信界或零真实失效率|
|机柜与统计|Intel联合方案24服务器/63548 server-hours，性能、SI、化学与95%MTBF下界。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=14\|PDF p.14]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16\|PDF p.16]]|具名系统在模型假设下的demonstrated reliability|全行业通用MTBF，或所有enveloped配置等量验证|
|fleet/经济模型|项目overview转引3000+server/30月、up to12×，另有3.4–5×机制模型。[[cooling-immersion/OCP-Immersion-Project-Scaling-Open-Collaboration-for-Immersion-Cooling-Adoption.pdf#page=13\|PDF p.13]]|提出值得进一步核实的系统收益假设|没有基线/失效定义/混杂控制时的因果证明|

## 三种时间不能混为一谈
1. **经过时长**：一套系统运行了多少小时。
2. **unit-hours**：所有受测单位的暴露累计；server/CPU/DIMM不能相加当独立服务器样本。
3. **等效服役时间**：需指定主导失效机制、应力、加速因子与校准；化学steady-state只是状态条件，不自动等于service lifetime。

Intel案例将封闭/恒容/充分混合反应器作为近似，并用升温加快反应；讲义没有完整Ea/AF，因此不能由该试验导出未经给出的寿命倍数。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=6|PDF p.6]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=7|PDF p.7]]

## 如何读置信界
该案例95% lower confidence limit MTBF为server21218h、CPU42436h、DIMM339488h。原页用恒定失效率/指数生存模型得到一年生存下界66%/81%/97%。这是**统计下界与模型输出**，不是样品中实际观察到对应比例失效，也不是个体保证寿命。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=15|PDF p.15]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16|PDF p.16]]

原表90%server值与其他行比例有疑点，故不复用该列建立新计算模型；完整failure counts、共同原因/独立性与计算脚本仍待公开。公式排版疑点详见来源笔记。

## 资格是有版本的配置，不只是fluid品牌
案例中PSU绝缘材料曾FAIL后更换，CPU材料HIGH RISK后补做封装可靠性，custom hanger避免fluid bypass。任一BOM/机械/工艺改变都可能改变原资格边界。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=4|PDF p.4]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=11|PDF p.11]]

本库建议资格记录保留：具体fluid/批次、完整wetted BOM、cleaning/rinse/dry历史、工作负载、温度与流量、污染与补液/维护、样本数/时长/删失/失效定义、前后功能/性能、统计模型及版本。

## 关联
[[knowledge/concepts/power-cooling-fluid-assurance|流体保证]] · [[knowledge/concepts/immersion-cleanliness-fluid-state|清洁度与流体状态]] · [[knowledge/concepts/immersion-thermal-to-inference-slo|热资格到推理SLO]] · [[knowledge/concepts/compute-memory-modular-platform-contract|有版本的平台契约]]
