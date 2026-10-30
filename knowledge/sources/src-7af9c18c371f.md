---
id: "src-7af9c18c371f"
type: "source"
title: "Moving Beyond Interchangeability: Characterizing Esters among Coolants for Immersion"
aliases: ["Moving Beyond Interchangeability: Characterizing Esters among Coolants for Immersion"]
speakers: "Stefan Maier（Evonik）；Beau Van Vaerenbergh（Oleon）；Valentina Serra-Holm（Perstorp）"
source_path: "cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf"
source_git_blob_sha: "86cbde721451adbfed55fe63c57d28c527ab591d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 6, 7, 8, 9, 10]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tags: ["ocp2026", "source", "immersion"]
concepts: ["[[knowledge/concepts/power-cooling-fluid-assurance]]", "[[knowledge/concepts/compute-memory-channel-evidence]]", "[[knowledge/concepts/immersion-cleanliness-fluid-state]]"]
---

# Moving Beyond Interchangeability: Characterizing Esters among Coolants for Immersion

## 核心结论
流体化学决定热物性、介电、吸湿和材料相互作用；酯也不是单一可互换配方。标准化应规定每种属性的方法、温度和判据，不能只按product name或同一ppm水分比较。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=2|PDF p.2]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=7|PDF p.7]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=11|PDF p.11]]

## 关键证据
GroupIV与EsterA示例flash point155/160°C、40°C黏度5.2/4.5cSt、FOM1为62/65。自然对流实验500W/server、20L/cassette；另一强制循环35L、最高4L/min、server+TTV。两装置/流量不同，不能只从FOM1直接推出任何GPU冷却能力。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=3|PDF p.3]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=4|PDF p.4]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=5|PDF p.5]]

## 指标与条件
- p.6频率约16–49GHz，low-ε ester与GroupIV接近但不相同，reference ester仍更高；液体均显著不同于air εr≈1。不能称“GHz下完全等介电、无需改interconnect”。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=6|PDF p.6]]
- 水分应结合相对饱和度、配方与温度；p.7的ppm区间是类别示例，缺完整温度/配方，不能作为统一运行限值。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=7|PDF p.7]]
- EsterB室温强制湿度暴露6天，water约0.11–0.12wt%；**DBV由38降至约28–29kV**。作者说resistivity/DDF仅小变、酸值不变，不等于所有dielectric指标不变或多年不水解。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=8|PDF p.8]]
- 80°C/336h材料试验：EsterC对PVC1/2体积变化较GroupIV低，但对PUR更高，A2出现dissolution；不能概括所有ester对所有材料更兼容。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=9|PDF p.9]]

## 图表与架构
低黏度/较高density与flash point需要联合比较，thermal figure-of-merit并不含全系统安全或寿命。流量/散热器按fluid属性设计才可能兑现材料性能。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=3|PDF p.3]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=5|PDF p.5]]

## 关联与比较
[[knowledge/concepts/power-cooling-fluid-assurance|流体保证]] · [[knowledge/concepts/compute-memory-channel-evidence|通道证据阶梯]]：bulk物性不是板级信号与长期服役的替代证据。

## 不确定性与待验证
FOM1公式、error bars、热边界和样本数不完整；不从3D柱图提取精确温差。fully miscible只表示混溶，不证明任意混液保持资格；“readily biodegradable/low persistence”缺本讲具体配方测试，不扩展为全生命周期环保结论。

## 原始页码导航
[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=2|p.2]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=3|p.3]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=4|p.4]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=5|p.5]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=6|p.6]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=7|p.7]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=8|p.8]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=9|p.9]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=10|p.10]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=11|p.11]] · [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=12|p.12]]

## 跨源概念
[[knowledge/concepts/immersion-cleanliness-fluid-state]]
