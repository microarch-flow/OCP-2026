---
type: comparison
title: "先进冷却证据并列表：比较对象、温度端点与成熟度"
tags: [ocp2026, sustainability]
---

# 先进冷却证据并列表：比较对象、温度端点与成熟度

## 比较问题与口径
问题不是“哪项热阻最小”，而是每份材料实际证明了哪一层。只有同面积、发热分布、介质、入口温度、流量/压降、测点和可靠性要求下才能直接比较。下表保留不相容的单位与边界，不作排名。

| 路线 | 文件内结果/对象 | 基线与工况 | 不能推出的结论 |
| --- | --- | --- | --- |
| Wiwynn 金刚石直接键合 | 3 kW 硅 TTV；R结到入口 0.0254→0.0157 °C/W，38.2% | 铜＋PCM 对金刚石＋铟键合；PG25，30°C，2 LPM/kW，32.2×25.7 mm² | 不能隔离材料收益；不是设施节能率或量产良率 |
| SemiValley 两相水射流 | 液侧 Rth 0.0098 K/W；325 W/cm² @0.14 L/min | 没有统一列出面积、入口温度及全部指标是否同一测试点；另有 V100 300 W 点 | 不能与结到入口热阻直接比；PUE1.05是目标 |
| MHS 膜辅助热沉 | 出口蒸汽质量1；约75°C高品位余热示意 | 换热器直供热与低温热源＋热泵的系统概念对比 | ~10 kW/MW泵功、97%图示不构成完整实测设施节能 |
| Lotus 多孔铜＋Galden HT-55 | 实验曲线接近93 W/cm²；>100标target | 壁面过热度横轴；同时区分光滑/结构化表面和DF1/Galden | 不能把目标当实测，也不能把全部改善归给冷却液 |
| CreAlien 低蒸汽质量水冷 | 2.5 kW、0.5 L/min、Tcase59.5°C；两节点扰动温差约2°C | 50×50mm冷板设计、0.2mm鳍间距优化；非结温 | 不等于完整机柜故障容错或长期水质验证 |
| xFusion 金刚石铜冷板 | 导热率/4 kW 支持主张 | 未列足够流量、入口温度与同基线测量条件 | 不能排在完整TTV实验之前或之后 |

## 页级证据
- Wiwynn：[[knowledge/sources/src-da79a48fdf16]] [[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=3|PDF p.3]] [[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=5|PDF p.5]] [[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=9|PDF p.9]] [[fts-data-center-sustainability/Investigation-of-Diamond-Based-Materials-for-Direct-Liquid-Cooling-of-Next-Generation-AI-Chips.pdf#page=10|PDF p.10]]
- SemiValley：[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=12|PDF p.12]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=13|PDF p.13]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=14|PDF p.14]]
- MHS：[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=18|PDF p.18]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=19|PDF p.19]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=20|PDF p.20]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=21|PDF p.21]]
- Lotus：[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=25|PDF p.25]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=26|PDF p.26]]
- CreAlien：[[knowledge/sources/src-935c06105968]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=29|PDF p.29]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=30|PDF p.30]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=31|PDF p.31]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=32|PDF p.32]] [[fts-data-center-sustainability/Sustainability-Lightning-Talks.pdf#page=33|PDF p.33]]
- xFusion：[[knowledge/sources/src-f8b63b9cf196]] [[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=8|PDF p.8]]

## 冲突与决策边界
- 同称“两相”，MHS 的蒸汽质量1与CreAlien的<0.06不同；把一种支路稳定结果转借给另一种不成立。
- 循环流量下降只支持水力变化；消费水量还需补水/排污/蒸发账本。
- 现场试点正在进行、展台演示、研究原型、量产出货和机房长期部署是不同成熟度；这些资料主要覆盖前几层。

## 下一份应索取的证据
要求统一 TTV 对比和压降/泵功，继而提供异步机柜负载与故障注入、长时材料/水质、设施总电量和净补水。缺一层就保留该层不确定性。

[[knowledge/concepts/sustainability-thermal-validation-ladder]] · [[knowledge/concepts/executive-expo-liquid-cooling-evidence]]
