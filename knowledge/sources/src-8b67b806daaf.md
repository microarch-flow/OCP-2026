---
id: "src-8b67b806daaf"
type: "source"
title: "Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers"
source_path: "ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf"
source_git_blob_sha: "9308fdb00907099691f3ad7bcb149875dfea1147"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8, 9, 12, 14]
text_reviewed: true
key_pages_visual_checked: [5, 6, 7]
tags: ["ocp2026", "source", "power-cooling", "lvdc", "voltage", "grounding"]
concepts: []
---

# 从800V到700／1400V：线对地电压比名义母线电压更关键

> 原始题名：Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers。阅读范围：完整可提取文字（物理 PDF 共 14 页），关键引用图表另做视觉核对。

## 核心结论

- DC Opportunities提出800V产品若拓宽低端工作范围，可参与700/1400V TN-S生态；要同时考虑极性、接地、对地绝缘和保护极数，不能只比较800与1500两个数。 [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=3|PDF p.3]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=8|PDF p.8]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=12|PDF p.12]]
- 作者比较显示提高配电电压可能降低平衡负载下电流及线材，但绝缘间距、耐冲击和半导体保护代价随拓扑不同；没有“越高越好”的单轴结论。 [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=6|PDF p.6]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=14|PDF p.14]]
- 表格的FoM是电压×电流×保护极数的简化相对量，不是采购成本；其标准注释含正在修订/讨论条款。 [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=14|PDF p.14]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 相同总母线电压的TN-S/IT可有不同最大线对地应力 | 已核p.7兼容性图；设备需按故障状态而非仅正常对地电压核定 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=6\|PDF p.6]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=14\|PDF p.14]] |
| 建议700V工作能力和源电压限制到750V | 作者兼容路线建议，不意味着所有标称800V器件已兼容 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=8\|PDF p.8]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=12\|PDF p.12]] |
| 700V/800V固定变比对中间母线电压有影响 | p.9列算术例子；未给实际转换器宽压效率和负载动态测试 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=9\|PDF p.9]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 相对电流/线损 | 高压组在相同平衡功率下电流0.5、表列线损0.5 | 作者同时调整线材的比较模型；不能误用成固定线径下I²R损耗推导 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=5\|PDF p.5]] |
| 比较绝缘的共同约束 | 基本绝缘、OVC与污染等级/材料组分别列示 | p.6数字适用于p.14限定假设；不直接转成PCB安全设计规则 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=6\|PDF p.6]]、[[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=14\|PDF p.14]] |
| 半导体FoM | 相对电压×相对电流×受保护极数 | 平衡双极负载假设；没有货币、供应价格或寿命数据 | [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=14\|PDF p.14]] |

## 图表与架构

已核对p.5极性/接地合并列、p.6绝缘表和p.7电压到地兼容性图；未省略p.14标准版本、基本绝缘与平衡负载等脚注。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 这份演讲不能替代现行IEC/UL/NEC设计审查；特别是尚在修订/讨论的部分。
- 真实收益需要同功率、长度、线径温升、接地故障策略、隔离等级、效率和冗余条件。
- 不提供实际高压接线或间距实施建议。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf)
- 来源身份 `src-8b67b806daaf`；Git blob `9308fdb00907099691f3ad7bcb149875dfea1147`；原始物理页数 `14`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
