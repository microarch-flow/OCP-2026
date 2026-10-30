---
id: "src-cc9852e7b81d"
type: "source"
title: "Increasing Rigor in Data Center Carbon Disclosure"
source_path: "Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf"
source_git_blob_sha: "ead94afafbf51a85c2e4ad2ff96c45b5aed5a0d6"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [4, 5, 7, 8, 13]
text_reviewed: true
key_pages_visual_checked: [8]
tags: ["ocp2026", "source", "power-cooling", "sustainability", "carbon", "pcr"]
concepts: []
---

# 碳披露可信度：有PCF数字不等于可比较，更不等于已减碳

> 原始题名：Increasing Rigor in Data Center Carbon Disclosure。阅读范围：完整可提取文字（物理 PDF 共 14 页），关键引用图表另做视觉核对。

## 核心结论

- panel材料区分最低披露字段、可比第三方验证披露与真正减碳路径；Disclosure≠Decarbonization，采购阈值需要PCR和证据支持。 [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=4|PDF p.4]]、[[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=5|PDF p.5]]
- 初步landscape显示ICT组件级规则显著不足，MEP较成熟但液冷基础设施仍有缺口；不能把server PCR直接套到所有组件。 [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=7|PDF p.7]]、[[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=8|PDF p.8]]
- 文件提出试点采购字段、共享EPD目录和补齐组件/液冷PCR，未给某产品碳足迹排名。 [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=13|PDF p.13]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| OCP embodied carbon disclosure基础字段：产品、方法、足迹、respondent | 最小数据字段规范；本身不保证方法、边界或数据质量一致 | [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=4\|PDF p.4]] |
| ICT产品功能单位/能源profile不同，组件不能直接复用服务器PCR | 比较架构应先统一功能单位和生命周期边界 | [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=8\|PDF p.8]] |
| 建议要求EPD并逐步淘汰spend-based数据 | landscape建议，不是现行强制采购条款 | [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=8\|PDF p.8]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| ICT初步盘点 | 27类；active PSR/c-PCR覆盖2类、另3类开发 | 演讲扫描快照，generic PCR与category-specific PCR需区分 | [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=8\|PDF p.8]] |
| MEP初步盘点 | 21类；active PCR覆盖20类；PSR/c-PCR覆盖12类 | 另各有1类开发；范围含新兴类别，不能换算为整个行业覆盖率 | [[Sustainability/Increasing Rigor in Data Center Carbon Disclosure.pdf#page=8\|PDF p.8]] |

## 图表与架构

已核p.8左右ICT/MEP两列，避免文字提取顺序把27类与21类错配。

## 关联与比较

- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 文件是panel背景与行动页，不包含现场讨论实录。
- 需要产品级EPD、PCR版本、数据质量、第三方验证范围及同功能单位后才做比较。
- 没有成本或性能归一化结果，不据披露数量推导产品好坏。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Sustainability/Increasing%20Rigor%20in%20Data%20Center%20Carbon%20Disclosure.pdf)
- 来源身份 `src-cc9852e7b81d`；Git blob `ead94afafbf51a85c2e4ad2ff96c45b5aed5a0d6`；原始物理页数 `14`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
