---
id: "src-8d543d42bc2d"
type: "source"
title: "Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute"
source_path: "cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf"
source_git_blob_sha: "d470465612090a3e5878e6b4e1fadd8ebbd2f41e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10]
text_reviewed: true
key_pages_visual_checked: [5, 8]
tags: ["ocp2026", "source", "power-cooling", "air-cooling", "rack-width", "general-compute"]
concepts: []
---

# 通用计算的900mm宽风冷机架：早期收益与尚未验证的热边界

> 原始题名：Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute。阅读范围：完整可提取文字（物理 PDF 共 11 页），关键引用图表另做视觉核对。

## 核心结论

- Microsoft/Lenovo讨论900mm宽风冷机架，以气流面积、散热器体积与DDR6布局余量延长通用计算风冷生命周期；不是对高热通量AI训练机柜液冷的否定。 [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=4|PDF p.4]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=5|PDF p.5]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=7|PDF p.7]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=9|PDF p.9]]
- 作者报告1.5OU系统更宽机箱约20–30%风扇W/kW下降，但650–1000W+ CPU热范围在对比表仍标“pending rack test”。 [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=5|PDF p.5]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=8|PDF p.8]]
- 材料明确是早期数据供社区讨论，不是规范贡献或新工作组；全液冷更高基础设施成本的百分比缺完整成本口径。 [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=4|PDF p.4]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=10|PDF p.10]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 600→900mm机架，气流面积约+50%，等体积流量下降低流速 | 几何/流动机理说明与早期风扇曲线，缺入口温度、风扇型号和热裕量 | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=5\|PDF p.5]] |
| CPU/DIMM/VRM并排布局可降低thermal shadowing | p.7是DDR6概念布局；未来32通道路线含推测，不能当作产品定案 | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=3\|PDF p.3]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=7\|PDF p.7]] |
| Hybrid与full liquid须计入泵/CDU负载、液体/泄漏/腐蚀管理 | 比较的是架构维度，不是端到端能耗的定量排名 | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=8\|PDF p.8]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 风扇功耗收益 | 约20–30%低fan W/kW | 1.5OU参考；900mm rack/750mm chassis对600mm rack/520mm chassis等曲线；不是整机/数据中心省电20–30% | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=5\|PDF p.5]] |
| CPU热能力目标 | 650–1000W+，pending rack test | 热通量、进风温度、海拔、噪声和量产裕量未给，不作为风冷普适上限 | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=6\|PDF p.6]]、[[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=8\|PDF p.8]] |
| 全液冷基础设施成本陈述 | 比Hybrid高50% | 未给货币、设备清单、负载密度、利用率和年限；不可用于采购预算或TCO计算 | [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=4\|PDF p.4]] |

## 图表与架构

已核p.5 TDP-风扇功耗曲线和1.5OU条件，以及p.8 pending rack test限定。图中不同宽度不止是标签，还对应不同机箱宽度。

## 关联与比较

- [[knowledge/concepts/power-cooling-capacity-evidence-ladder]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 需要row-level有效算力/面积而非仅每rack密度，同时计入900mm占地。
- 风扇W/kW和整站PUE不是同一边界；液冷泵/CDU与热回收也未统一比较。
- 需真实工作负载和环境条件下的thermal margin测试。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf)
- 来源身份 `src-8d543d42bc2d`；Git blob `d470465612090a3e5878e6b4e1fadd8ebbd2f41e`；原始物理页数 `11`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
