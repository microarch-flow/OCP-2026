---
id: "src-aa7f850cad5a"
type: "source"
title: "Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture"
source_path: "Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf"
source_git_blob_sha: "87ad3d09f7d55050a72fa3ece91f23326d32a165"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 8
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 6, 8]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 800 V 直流侧柜：模块化方案与必须澄清的额定值

> 原始题名：Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture。阅读范围：完整可提取文字（物理 PDF 共 8 页），关键引用图表另做视觉核对。

## 核心结论

- Rittal/Bosch 提案以高功率转换模块、模块化直流配电及可选 BBU 构成侧柜；其优势主张是减少模块数和保留计算机架空间，不是已经证明的最低 TCO。 [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=3|PDF p.3]]、[[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=5|PDF p.5]]、[[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=7|PDF p.7]]、[[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=8|PDF p.8]]
- 风冷上限来自特定效率、进出风温差及通风截面积模型；不能把幻灯片的 600–700 kW 当作所有侧柜的物理上限。 [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=4|PDF p.4]]
- BBU 页内存在功率与能量标注冲突：21 kW/21 kWh、825 kW 与 3×225 kW；应向作者确认，不能据此计算可靠备电时长。 [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=6|PDF p.6]]、[[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=8|PDF p.8]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 大模块与 PCB 模块比较 | 200 kW 级与约 20 kW 级方案的模块数/密度比较；不是同一散热、冗余、器件寿命下的实测优化。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=3\|PDF p.3]] |
| IP2X 母排与可移动 SSCB 插位 | 提出 60 mm 扁铜母排、盲插容差及控制层次；触电、拉弧、故障选择性仍需完整组件验证。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=5\|PDF p.5]] |
| 前维护与热插拔 | 作者产品架构主张；未给 MTTR、维护事故率或可用性数据。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=7\|PDF p.7]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 示例侧柜整流容量 | 5×200 kW = 1 MW，工作负载示例 800 kW | 可理解为模块配置与负载额定值区分；不能自动把任何失效情形都视作 N+1。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=8\|PDF p.8]] |
| 示例储能 | 6×3.5 kWh = 21 kWh | 同页标 825 kW BBU，但 DC/DC 标 3×225 kW = 675 kW，未消解。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=8\|PDF p.8]] |
| 800 kW 散热模型 | 空气 59.7 m³/min；液体 34.8 L/min | 97% 转换效率；空气 20→40°C，液体 30→40°C；不同单位和温差，不能把“factor 1000”解读成能效提高 1000 倍。 | [[Rack & Power/Powering the AI Rack of the Future- A Scalable 800 V DC Sidecar Architecture.pdf#page=4\|PDF p.4]] |

## 图表与架构

已核对模块比较、风/液冷计算、配电结构、侧柜配置及尺寸布局（p.3–6、8）。p.8 的 2 MW 配置是整流模块扩展，不等于提供 2 MW、同一持续时长的电池备电。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 请确认 BBU 的实际额定功率、能量、持续时间及 p.6/p.8 的冲突。
- 97% 在哪些负载、电压及温度下成立？泵、CDU、风机是否纳入？
- 维护时旁路/隔离、故障域及控制电源冗余如何设计？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/Powering%20the%20AI%20Rack%20of%20the%20Future-%20A%20Scalable%20800%20V%20DC%20Sidecar%20Architecture.pdf)
- 来源身份 `src-aa7f850cad5a`；Git blob `87ad3d09f7d55050a72fa3ece91f23326d32a165`；原始物理页数 `8`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
