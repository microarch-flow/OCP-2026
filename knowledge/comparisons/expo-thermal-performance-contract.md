---
id: "expo-thermal-performance-contract"
type: "comparison"
title: "液冷验收合同：热容量、温度收益与推理服务效率不可互换"
tags: ["ocp2026", "expo-hall"]
review_status: "synthesized"
---

# 液冷验收合同：热容量、温度收益与推理服务效率不可互换

## 核心综合
冷板W、热点W/cm²、CDU MW、GPU结温、捕热率、tokens/J分别描述不同层。把它们串成完整热路径有价值，把它们相互替代没有证据。

## 已有证据各能回答什么
- **冷板极限：** CoolIT15kW是TTV、45°C设施水、80°C case、18L/min算术流量；不是15kW GPU，更不是结温80°C。[[knowledge/sources/src-9e459d39cae8]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=14|PDF p.14]] HFH给800–3500W、热点>500W/cm²等能力范围，但没有证明每个温度/流量/功率组合都达标。[[knowledge/sources/src-d70b63b16f7b]] [[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=11|PDF p.11]]
- **业务收益：** Frore的+35%与+43%是两种组合相对共同93°C基线，不能相加；缺GPU/模型/功率策略和设施冷却能耗。[[knowledge/sources/src-f46544da55e0]] [[expo-hall-sessions/Burning Cash- The Hidden Cost of Ignoring Thermal in Your AI Strategy presented by Frore.pdf#page=14|PDF p.14]] MiTAC/Akash的FLOPs/W+22%与token throughput+15%在不同环境，且温差单位存在错误，不能与Frore跨源合成收益曲线。[[knowledge/sources/src-e3c54df076ca]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=18|PDF p.18]]
- **残余热：** CoolIT的70/30算例说明即使GPU液冷，250kW柜仍可能有75kW风冷；SSD、NIC、DIMM和VRM热路径不可忽略。但“必须100%”是设计选择而非该算例证明的物理定律。[[knowledge/sources/src-9e459d39cae8]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=5|PDF p.5]] KIOXIA的E1.S液冷30W预算也没有直接提供p99 IO改善。[[knowledge/sources/src-204a0ecdba21]] [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=3|PDF p.3]] [[knowledge/sources/src-204a0ecdba21]] [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=4|PDF p.4]]
- **回路输运：** Nidec3.2MW在3°C approach的CDU指标与泵冗余/前维护有关，不能倒推某芯片热点温度。[[knowledge/sources/src-e84fa2f73a45]] [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=13|PDF p.13]] MiTAC“压降44%降低”图却用kW纵轴和不同温度simulation，需先获得修正图再纳入泵功模型。[[knowledge/sources/src-e3c54df076ca]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=16|PDF p.16]]
- **化学寿命：** Ecolab50°C物性支持水有导热/黏度优势，但维护和材料条件决定长期可用性。[[knowledge/sources/src-48ba6ea6361c]] [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=7|PDF p.7]] MiTAC第二来源PG25混配ΔT相近仅证明该实验热行为，不能替代弹性体/腐蚀/生物长测。[[knowledge/sources/src-e3c54df076ca]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=17|PDF p.17]] [[knowledge/sources/src-48ba6ea6361c]] [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=16|PDF p.16]]

## 建议统一的五层验收（跨源归纳）
1. 固定芯片/封装/TIM/热源地图，分别报Tjunction、Tcase、液体入口和ambient；禁止只写“温度”。
2. 在声明冷却液、流量、压降、装配公差和寿命阶段下测热阻；同时记录泵/风扇/冷源能量。
3. 整机测GPU及外围残余热，报告捕热率的能量平衡与计量误差；不以“一块15kW冷板”证明整柜无风扇。
4. 固定模型质量、上下文、batch/concurrency、频率/功率限制，比较满足TTFT/TPOT/p99的有效tokens/J或成功任务/kWh，不只裸吞吐。
5. 在失泵、流量不均、滤网/冷板污染和维护更换后重复；维护收益要有MTTR与故障域数据。HFH的30W TIM插拔200/500次差异与CoolIT模块化/单体板权衡正是这层问题。[[knowledge/sources/src-d70b63b16f7b]] [[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf#page=16|PDF p.16]] [[knowledge/sources/src-9e459d39cae8]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=22|PDF p.22]]

## 分歧不是结论
CoolIT偏单相，MiTAC同时展示单相/两相/diamond，Ecolab强调水化学维护；这些不是同负载盲测。两相annualized pPUE1.03也不是全设施PUE，不能跨天气与计量边界排名。[[knowledge/sources/src-9e459d39cae8]] [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf#page=12|PDF p.12]] [[knowledge/sources/src-e3c54df076ca]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=19|PDF p.19]]

关联：[[knowledge/concepts/expo-evidence-to-deployment]]、[[knowledge/comparisons/expo-power-conversion-boundaries]]。当前资料足够生成验收清单，不足以承诺某冷却路线必然降低推理成本。

