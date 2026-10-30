---
id: "src-accd3169319b"
type: "source"
title: "800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety"
source_path: "ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf"
source_git_blob_sha: "f52d3f4a2c6d15eb696c4abc6df27be57c228f67"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 20
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18]
text_reviewed: true
key_pages_visual_checked: [10, 11, 12, 13, 14, 15]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 800 V 保护协调：目标是可预测系统，不是单器件速度排名

> 原始题名：800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety。阅读范围：完整可提取文字（物理 PDF 共 20 页），关键引用图表另做视觉核对。

## 核心结论

- Schneider 主张把源限流、储能、接地、冗余和分断装置共同设计；受控故障源可能给传统机电保护留出足够时间，而自保护迅速关断的源可能需要更快隔离。 [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=6|PDF p.6]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=9|PDF p.9]]
- 要区分负载连续性和故障电源链连续性：冗余路径可能保持 IT 运行，即使故障源先关机；但必须隔离、验证并恢复故障电源链，不能把剩余冗余耗尽当作无影响。 [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=12|PDF p.12]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=13|PDF p.13]]
- 无机架冗余、依赖转供的结构受故障清除/转供/保持窗口约束；图中时间关系是设计要求，不是已通过的现场结果。 [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=12|PDF p.12]]
- 该材料与 Siemens 更强调 SSCB 的演讲形成有用对照：选择应由波形、故障边界、成本与成熟度决定，而不是按厂商表格直接宣布胜负。 [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=10|PDF p.10]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=11|PDF p.11]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=18|PDF p.18]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 电容初始放电 + 上游持续馈入 | 800 V 本身不能定义故障波形；测试波形必须覆盖源控制和储能，不仅使用传统 L/R 上升曲线。 | [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=10\|PDF p.10]] |
| 接地和保护极数矩阵 | 作者矩阵有条件项；例如浮地两线单保护极需要监测与互操作验证，浮地三线不能仅用表中两极器件覆盖全部导线。不是现场合规意见。 | [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=14\|PDF p.14]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=15\|PDF p.15]] |
| 系统认证缺口 | 要求共同故障波形、声明响应契约、HIL/硬件验证和开放接口；当前缺口属于讲者报告，不能代替最新版标准核查。 | [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=17\|PDF p.17]]、[[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=18\|PDF p.18]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 分支保护典型分断时间 | Fuse 0.5–5 ms；EMCB 1–20 ms；HCB 0.2–1 ms；SSCB <10 µs | 作者概括，不是各技术所有产品的承诺；电流、源限流、温度、极数、线路电感及夹持能量均会改变结果。 | [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=11\|PDF p.11]] |
| 成本与集成代价 | Low 至 High 的定性分级 | 没有价格、币种、寿命、损耗电费或利用率，不能计算采购或生命周期最优方案。 | [[ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf#page=11\|PDF p.11]] |

## 图表与架构

已核对 p.10–15 的故障波形、保护技术表、冗余/转供拓扑和接地极数矩阵。p.12 的“冗余保证在线”仅在剩余路径容量充分、故障不共因传播且控制正常等假设下成立。

## 关联与比较

- [[knowledge/comparisons/power-cooling-protection-coordination]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 必须保持在线的最小故障域与可接受恢复时间是多少？
- 源先关断后，保护装置还是否能定位和完成隔离，控制供电从哪里来？
- 同一真实 R/L/C、反灌和负载窗口下，机电、混合及固态方案如何比较损耗、可维护性及总成本？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/800VDC-Power-Systems-Redefining-Protection-Coordination-System-Safety.pdf)
- 来源身份 `src-accd3169319b`；Git blob `f52d3f4a2c6d15eb696c4abc6df27be57c228f67`；原始物理页数 `20`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
