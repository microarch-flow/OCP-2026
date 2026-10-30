---
id: "src-9d2ab7f25f7f"
type: "source"
title: "LVDC-Building-an-Open-and-Evolving-Ecosystem"
source_path: "ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf"
source_git_blob_sha: "b5b5c014cdc624c6573f6927bb09688ae12adee0"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [7, 11]
tags: ["ocp2026", "source", "power-cooling", "lvdc", "ecosystem"]
concepts: []
---

# LVDC开放生态：从高功率机柜扩展到全部IT与设施负载

> 原始题名：LVDC-Building-an-Open-and-Evolving-Ecosystem。阅读范围：完整可提取文字（物理 PDF 共 13 页），关键引用图表另做视觉核对。

## 核心结论

- Google/NVIDIA主张将LVDC统一到IT行级，避免AC/DC分区限制机架摆放、网络线长与容量利用；并非所有托盘都必须直接接800V。 [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=3|PDF p.3]]、[[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7|PDF p.7]]
- 低功率机架仍可保留48–54V母排，通过新DC/DC power shelf适配；CDU、风机和少量AC辅助负载也是生态迁移范围。 [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=8|PDF p.8]]、[[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=9|PDF p.9]]
- 完整生态在演讲时尚未形成：2026单lineup验证、2027–2028数据中心验证、2029+ GW级部署属于路线图。 [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=11|PDF p.11]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 高密度下机内AC/DC及备份占据有价值的IT空间 | 讲者以≥100kW为讨论起点、>600kW机内AC/DC不可行为主张；未给完整样机布局和普遍适用证明 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=4\|PDF p.4]] |
| 互通tapbox/busway、limited connector set决定交付同步和机柜可替换性 | 容量扩展受机械/电气接口和供应链约束，不只是转换器效率 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=12\|PDF p.12]] |
| 新power shelf桥接800V设施和54V机内生态 | 已核架构图；旧AC与新DC两路都向54V母排供电 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7\|PDF p.7]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 供电架密度陈述 | 55→95 kW/RU | p.7同时称“doubling”；按数字仅约1.73倍。未给冗余、温升、输入/输出条件及测试报告，不写成精确2倍 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7\|PDF p.7]] |
| 机内空间占用陈述 | AC/DC约10–15%；BBU另10–15%；N+N增加转换配置 | 讲者估计、配置依赖；不是机房面积或TCO节省比例 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=4\|PDF p.4]] |
| 建议分界 | <100 kW优先48–54V母排 | 架构建议而非电压或热安全硬上限 | [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7\|PDF p.7]] |

## 图表与架构

已核对p.7电源架适配示意和数值、p.11阶段路线图；特别保留55→95与“doubling”措辞间的精度差异。

## 关联与比较

- [[knowledge/concepts/power-cooling-time-scales-and-control-authority]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 需要同冗余等级、工作负载、冷却条件下的机内空间与效率对比。
- Sidecar tax是架构空间/成本负担的表达，文中没有货币值、利用率或年限。
- 生态里程碑不是采购可用性保证。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf)
- 来源身份 `src-9d2ab7f25f7f`；Git blob `b5b5c014cdc624c6573f6927bb09688ae12adee0`；原始物理页数 `13`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
