---
id: "src-aba39fa610e7"
type: "source"
title: "2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers"
source_path: "ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf"
source_git_blob_sha: "1135a284df57fa1ea99c0fc69903abc4ec9a9a5b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 11]
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 6, 7, 8, 9, 10, 11]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 800 V 两线与三线：接地、储能和全极隔离必须一起选

> 原始题名：2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers。阅读范围：完整可提取文字（物理 PDF 共 13 页），关键引用图表另做视觉核对。

## 核心结论

- Siemens 比较两线 800 V 与三线 ±400 V，并分别分析 IT 浮地和 TN-S 接地；两线不自动等于浮地，三线也不自动消除故障危险。 [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=3|PDF p.3]]、[[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=4|PDF p.4]]
- 增加本地电容可改善穿越与动态负载，但同时提高故障放电贡献；容量与保护时序应联合设计，不能用“更多电容”单独解决稳定性。 [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=5|PDF p.5]]
- 单极断开不等于维修隔离：作者示例包含半母线反向、另一极继续馈电和其他位置故障经接地路径影响已停机机架。 [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=8|PDF p.8]]
- 供方强调 SSCB 的速度价值，但“线长/故障电流不影响 SSCB”及最低 TCO 属于广泛主张；本材料的有限波形不足以证明全部器件和系统都如此。 [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=9|PDF p.9]]、[[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=10|PDF p.10]]、[[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=11|PDF p.11]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 两线/三线权衡 | 三线需平衡并支持半母线负载；复杂度、功率密度和故障能量表是作者定性比较，不能脱离导体总铜量、负载对称性与储能配置。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=4\|PDF p.4]] |
| 寄生电容触电模型 | 作者按标准效果区分类，但未完整公开人体模型/阈值定义；不将表内电容或“无心室颤动风险”作为现场安全限值。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=6\|PDF p.6]] |
| 低故障电流可能更难分断 | 图示 MCCB 燃弧时间随故障电流降低而变长、熔断器可能重燃；仅做最大金属性短路试验不覆盖所有故障。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=10\|PDF p.10]]、[[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=11\|PDF p.11]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 寄生电容示例 | 0.01 µF 对应 0.3 ms；5 µF 对应 151 ms 暴露 | 作者模型结果，电压、人体阻抗、暴露判定需原始研究；不用于个体触电风险计算。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=6\|PDF p.6]] |
| 故障穿越电容比较 | 熔断器 300 mF / 373 V；SSCB 10 mF / 约 400 V | 同页给定架构示例，不是任意熔断器与 SSCB 的通用容量比；没有币种、利用率、期限，不能形成 TCO 数字。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=9\|PDF p.9]] |
| 电容分断波形条件 | 800 VDC、20 mF，电缆 6 ft 与 10 ft | 展示所选器件的重燃/分断差异；器件型号、重复次数及全部回路参数不足，不能外推认证。 | [[ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf#page=10\|PDF p.10]] |

## 图表与架构

已核对 p.3–11 全部关键拓扑、波形及比较表。p.9 对地电压变化强调极间不协调风险；SSCB 关闭状态也不应未经验证就等价于具有规定绝缘隔离的检修断开。

## 关联与比较

- [[knowledge/comparisons/power-cooling-protection-coordination]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 供方能否提供实际器件型号、回路 R/L/C、故障类型及重复性数据？
- IT 第一故障后如何检测、定位和限定修复时间，第二故障时全极断开如何保证？
- 断开后的剩余电荷、反灌路径和无电验证由哪个安全机制负责？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/2-Wire-vs.-3-Wire-at-800VDC-Grounding-Fault-Behavior-and-Protection-for-AI-Data-Centers.pdf)
- 来源身份 `src-aba39fa610e7`；Git blob `1135a284df57fa1ea99c0fc69903abc4ec9a9a5b`；原始物理页数 `13`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
