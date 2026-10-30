---
id: "src-4001ade000fc"
type: "source"
title: "Microsoft：性能归一化隐含碳不能替代绝对排放与完整生命周期"
source_path: "Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf"
source_git_blob_sha: "848ed12faa1cd59d736a7a5ded579cba53a4c400"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [2, 4, 5, 6]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]", "[[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]]"]
---

# Microsoft：性能归一化隐含碳不能替代绝对排放与完整生命周期

## 核心结论
按core、TB或GPU FP8 TOPS归一化的机架隐含碳，可帮助分离供应链减排与硬件性能增长；但单位强度下降仍可能伴随采购总量增长和绝对Scope3上升。该指标应与绝对量并列，而非取代它。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=2|PDF p.2]][[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=3|PDF p.3]][[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=7|PDF p.7]]

## 关键证据
- 研究范围刻意聚焦IT硬件隐含碳，以简化供应链归因；不包括完整软件、运行电力、水或基础设施生命周期。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=3|PDF p.3]]
- 按年度采购功能容量归一化：kgCO₂e/TB、kgCO₂e/core、kgCO₂e/FP8 TOPS；是硬件portfolio指标，不是kgCO₂e/成功推理任务。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=4|PDF p.4]]
- 三种情景分开：参考年强度×当前采购量、已包含通常软硬件效率改善的baseline、再加入供应商清洁电力/低碳材料干预后的actual/projected actual。反事实选择决定avoided emissions。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=5|PDF p.5]]

## 指标与条件
同为FP8 TOPS仍需明确稀疏/稠密、精度、峰值/持续等规格；跨代core也不是相同有效工作。不能用单位理论算力碳强度直接判定同SLA服务更低碳。图中走势和FY30计算均为**假设情景**，不是Microsoft实际减排曲线。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=4|PDF p.4]][[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=5|PDF p.5]]

## 图表与架构
p.6将组件级供应商归因与机架/portfolio级设计归因分开，要求共同taxonomy、functional unit、data quality和attribution。该图明确不聚焦逐SKU代际改善。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=6|PDF p.6]]

## 关联与比较
与LCA at Scale互补：前者提供可信分子和数量，本文选择归一化分母；推理SLA框架还需引入寿命、实际利用率、任务质量和运行能耗。

## 不确定性与待验证
没有具名rack PCF或代际实测性能；需要功能单位一致性、供应商干预归因、防重复记账及全生命周期反事实，不能把隐含强度指标称为完整避免排放核算。[[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=7|PDF p.7]][[Sustainability/Performance-Normalized Embodied Rack Carbon Intensity for Next-Generation Hardware.pdf#page=8|PDF p.8]]

## 知识网络
[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]] · [[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]]
