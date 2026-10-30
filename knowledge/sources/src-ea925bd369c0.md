---
id: "src-ea925bd369c0"
type: "source"
title: "Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance"
source_path: "cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf"
source_git_blob_sha: "975aa362a2cdec83d9b22d87c84a3e08e3683f76"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10]
text_reviewed: true
key_pages_visual_checked: [7]
tags: ["ocp2026", "source", "power-cooling", "immersion", "qualification", "safety"]
concepts: []
---

# 浸没液安全资格与系统合规：认证不等于长期材料兼容

> 原始题名：Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance。阅读范围：完整可提取文字（物理 PDF 共 12 页），关键引用图表另做视觉核对。

## 核心结论

- UL Solutions区分液体性质资格、UL2417、系统设计审查和IEC62368-1终产品认证；单独液体通过不能代替系统合规。 [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=4|PDF p.4]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=5|PDF p.5]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=6|PDF p.6]]
- 演讲认为现有框架对长期材料兼容指导不足，UL2417本身也不覆盖兼容性；新的兼容性OOI仍在开发。 [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=4|PDF p.4]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=6|PDF p.6]]
- DTC冷却液UL2417B当时是拟议范围/测试，软管UL4303则另覆盖机械、压力、老化、流体兼容等对象，不能互相替代。 [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=9|PDF p.9]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=10|PDF p.10]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 传统标准多年共识与新兴技术OOI快速路径 | 帮助辨别规范成熟度；OOI不是同等成熟度的长期共识标准 | [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=3\|PDF p.3]] |
| 必测自燃、闪点、击穿、红外身份；可选水分、黏度、酸值、氧化等 | 区分必测与可选；未做可选测试不等于这些风险已合格 | [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=7\|PDF p.7]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=8\|PDF p.8]] |
| IEC62368-1安全与长期材料相容性是不同证据层 | 架构推论：流体资质、材料组合、电子设备和整系统四层证据应分别归档 | [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=4\|PDF p.4]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=5\|PDF p.5]]、[[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=6\|PDF p.6]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| UL2417演讲列门限 | 自燃≥300°C（ASTM E659）；闪点≥135°C（ASTM D93 A）；击穿≥6kV/mm（ASTM D1816） | 资格测试值而非推荐液体工作温度/电场；按演讲快照记录，项目须核对现行正式文本 | [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=7\|PDF p.7]] |
| 系统兼容性时长提及 | 60天 | 讲者对现有IEC要求的说明；不等于验证整个设备寿命 | [[cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf#page=4\|PDF p.4]] |

## 图表与架构

已核p.7完整必测表，保留试验方法及数值用途；没有将闪点/自燃点改写为允许操作温度。

## 关联与比较

- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 实际采购需核验产品iQ认证条目、适用配方/批次和终产品证书。
- 认证最小测试与长期热氧化、材料萃取、污染和电气劣化仍存在差距。
- 本条不是现行标准法律意见；版本变化必须回到正式规范。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/cooling-immersion/Advancing-Immersion-Cooling-Safety-From-Fluid-Qualification-to-System-Compliance.pdf)
- 来源身份 `src-ea925bd369c0`；Git blob `975aa362a2cdec83d9b22d87c84a3e08e3683f76`；原始物理页数 `12`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
