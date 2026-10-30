---
id: "src-3ad922e148cf"
type: "source"
title: "DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results"
source_path: "ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf"
source_git_blob_sha: "2ec2908eb55cd6279d5233b8f196e986c4680a03"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]
text_reviewed: true
key_pages_visual_checked: [7, 8, 9, 10, 11, 12, 13, 14]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# DC 弧闪实测：不能用自熄多数掩盖持续电弧尾部风险

> 原始题名：DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results。阅读范围：完整可提取文字（物理 PDF 共 18 页），关键引用图表另做视觉核对。

## 核心结论

- Schneider 将侧柜和集中式配电分别建模，并在 2026 年 9 月实验室测试；不同输出电容、反向阻断和源限流会产生不同故障包络，不能给“800 V”一个统一入射能量。 [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=6|PDF p.6]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=8|PDF p.8]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=10|PDF p.10]]
- 39 次试验中作者称约 80% 电弧未持续，但仍有 >4 cal/cm² 情形；样本比例不是实际机房故障概率，也不能据此取消 PPE 或带电作业控制。 [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=12|PDF p.12]]
- 11 次相似配置对照显示自熄、母排间持续电弧及母排—外壳双电弧三种结果；仿真需要解释这些差异，而非只拟合平均能量。 [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=14|PDF p.14]]
- 250 A MCCB 的快速分断例子说明机电装置在特定波形下也可能有效；不能外推全部 MCCB 或所有低电流/高阻故障。 [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=13|PDF p.13]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=15|PDF p.15]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 模型与实验不完全同条件 | p.11 明示侧柜实验能量高于仿真；集中式波形也有振荡差别，因此不能称两者已严格等条件吻合。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=11\|PDF p.11]] |
| 反向阻断与故障源 | 机架电容的故障贡献可能超过上游转换器；模型需明确反灌、限流和关断，不只代入一个稳态电流。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=8\|PDF p.8]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=15\|PDF p.15]] |
| 方法与标准缺口 | 本文报告方法适用性的作者判断及研究计划；不代替当前标准、专业弧闪研究或现场 PPE 选型。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=4\|PDF p.4]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=5\|PDF p.5]]、[[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=16\|PDF p.16]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 全部试验分布 | 39 次：21、7、6、3、2 次分布在图列 <0.1、<0.2、<1.2、<4、>4 cal/cm² 档 | 表内阈值写成嵌套小于号，但次数相加 39，意图为分档；精确区间下界与工况矩阵未提供。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=12\|PDF p.12]] |
| 相似配置子集 | 11 次：7 次 <0.1；2 次约 2；2 次 >4 cal/cm² | 无过流保护；试验站约 130 ms 电流窗口。最后两次涉及母排与外壳之间额外电弧。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=14\|PDF p.14]] |
| MCCB 示例 | 250 A；清除约 0.6 ms；入射能量 0.03 cal/cm² | 图注为 800 VDC、约 90 kA 峰/350 µs、18.5 kA 稳态的测试源描述；不代表任意距离/外壳/间隙的风险。 | [[ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf#page=13\|PDF p.13]] |

## 图表与架构

已核对 p.7–14 的架构、模拟、实验室照片、波形及统计图。p.8 的侧柜模型出现约 0.05 与 0.01 cal/cm² 两种方法估计，p.14 的双电弧结果高于较简单模拟；不能只挑较低算法值作安全结论。PDF 中视频仅有静态帧，本分析未声称观看嵌入视频。

## 关联与比较

- [[knowledge/comparisons/power-cooling-protection-coordination]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 39 次试验各自的间隙、电极材料、外壳、工作距离、传感器布置和源波形是什么？
- 无保护子集与有 MCCB 示例能否提供逐次原始数据及独立复现？
- 低电流长持续、高阻和多点电弧是否纳入最坏情形，而不仅看峰值电流？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/DC-Arc-Flash-Learnings-from-Practical-Study-and-Test-Results.pdf)
- 来源身份 `src-3ad922e148cf`；Git blob `2ec2908eb55cd6279d5233b8f196e986c4680a03`；原始物理页数 `18`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
