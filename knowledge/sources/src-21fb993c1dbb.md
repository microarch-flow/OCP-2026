---
id: "src-21fb993c1dbb"
type: "source"
title: "Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers"
source_path: "ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf"
source_git_blob_sha: "531d12eb03e6be31fb8577dff7547156ca8f5c86"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [6, 8, 9, 10, 11, 12]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 高温超导配电 RAM：模型可用性依赖冷源、备用链与维修架构

> 原始题名：Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers。阅读范围：完整可提取文字（物理 PDF 共 16 页），关键引用图表另做视觉核对。

## 核心结论

- VEIR/RED 的核心贡献是把液氮系统、终端、超导导体和控制放入可维护的 RAM 架构，而不是只凭导体低损耗宣称整站可用性。液氮冷源本身也依赖电力和备用系统。 [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=4|PDF p.4]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=6|PDF p.6]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=7|PDF p.7]]
- 报告使用故障树和功能黑盒建模，输入来自 IEEE 493、OEM 与内部数据，并随设计迭代；不是多年运行暴露量及置信区间支持的现场可靠性结果。 [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=4|PDF p.4]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=5|PDF p.5]]
- Block redundancy 与 distributed redundancy 比较同时改变容量、共享备用和故障域；不能将两组可用性直接归因于 HTS 材料，或把 AC/DC 数字当作同等站点的路线胜负。 [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=8|PDF p.8]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=9|PDF p.9]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=10|PDF p.10]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=11|PDF p.11]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=12|PDF p.12]]
- DC 方案部分设备尚未成熟，模型包含 DC STS 等设备达到 AC 等效可靠性的假设；模型数字与 Tier 认证不是同一件事。 [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=11|PDF p.11]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=13|PDF p.13]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=14|PDF p.14]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 四个功能子系统 | 液氮供应/冷却、终端单元、导体和控制；需要联合处理冷源失电、维修、冗余切换与共因故障。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=6\|PDF p.6]] |
| 集中与分布式冗余 | 分布式方案可减小单次受影响范围，但作者仅定性描述较高 CAPEX/隐含碳，未给币种、清单边界、运行利用率或寿命。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=9\|PDF p.9]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=12\|PDF p.12]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=13\|PDF p.13]] |
| “近零损耗”边界 | 导体优势的营销描述不等于系统净能耗接近零；液氮制冷、管路热漏、终端及 AC 损耗须计入。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=2\|PDF p.2]]、[[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=7\|PDF p.7]] |
| Tier 名称 | 作者在模型表中将部分结果旁注为 Tier III/IV；本卡不据此认定任何设施已认证，也不把 uptime 百分比直接等同 Tier 等级。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=11\|PDF p.11]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| Block redundancy 模型规模 | AC 21 MW、7+1；DC 20 MW、2+1 | AC 按 7 个 3×1 MW GPU 机架行描述；DC 为两个 10 MW pod。共享备用的覆盖范围不同。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=9\|PDF p.9]] |
| Distributed redundancy 模型规模 | AC 24.3 MW 标题但 6×4 MW = 24 MW；DC 60 MW | AC 容量存在未解释的口径差；DC 为 6×10 MW HAC，4-makes-3 正常 75%、故障 100% 的设计。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=10\|PDF p.10]] |
| Block redundancy 模型可用性 | LIN 99.999%；AC 99.9%；DC 99.99% | 模型输出/假设；LIN 冗余和 UPS/发电机/BESS 供电路径必须保留，不是器件固有可用性。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=11\|PDF p.11]] |
| Distributed redundancy 模型可用性 | 集中式 LIN 99.999%；LIN+AC 设施 99.999%；LIN+DC 设施 99.99% | 图中不同组合边界；不得省略集中式 LIN 条件，且没有现场实测统计或统一设备假设下的敏感性区间。 | [[ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf#page=12\|PDF p.12]] |

## 图表与架构

已核对 p.6、8–12 的功能分解、AC/DC 物理布局与可用性表。不同方案的负荷规模、备用拓扑和设备成熟度不一致。作者关于“部分负荷不浪费制冷”的描述缺少系统基载/效率曲线，不能据此计算电费收益。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 故障率、维修时间、共因比例和模型独立性假设是否可审计，并覆盖冷源/控制共享依赖？
- 失超、液氮供给中断与检修如何影响 IT、接地保护和恢复时间？
- 相同容量、冗余等级和利用率下，净能耗、占地、安装成本及生命周期排放分别是多少？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Reliability-Availability-and-Maintainability-of-High-Temperature-Superconducting-Power-Distribution-for-High-Density-AI-Data-Centers.pdf)
- 来源身份 `src-21fb993c1dbb`；Git blob `531d12eb03e6be31fb8577dff7547156ca8f5c86`；原始物理页数 `16`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
