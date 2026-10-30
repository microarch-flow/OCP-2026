---
id: "src-ef44afab3769"
type: "source"
title: "800V direct-to-server and power shelf solutions"
source_path: "Rack & Power/800V direct-to-server and power shelf solutions.pdf"
source_git_blob_sha: "9f012c9dacf2acc185a6c303ee8557e8cde343f3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
text_reviewed: true
key_pages_visual_checked: [3, 9, 16]
tags: ["ocp2026", "source", "power-cooling", "pdb", "power-shelf", "800v"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]"]
---

# 800 V 直达服务器与电源架：PDB 把模块变成可集成子系统

> 原始题名：800V direct-to-server and power shelf solutions。阅读范围：完整可提取文字（物理 PDF 共 18 页），关键引用图表另做视觉核对。

## 核心结论

- Advanced Energy 将机架电源架和服务器内 PDB 作为两条落地路径；高压越深入可缩短低压大电流距离，但把安全隔离、EMI、热管理和维护责任带入 IT 设备。 [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=3|PDF p.3]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=4|PDF p.4]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=5|PDF p.5]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=6|PDF p.6]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=7|PDF p.7]]
- PDB 价值不只是多个 DC/DC 的组合，还包括保持电容、预充/放电、熔断、数字控制及传导/辐射 EMI；这些功能会稀释裸转换器功率密度。 [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=10|PDF p.10]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=11|PDF p.11]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=12|PDF p.12]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=15|PDF p.15]]
- 100/160 kW 电源架及主要模块在产品状态页标为 Sampling，不能从“Prototype and Production”标题推断全部已量产或已通过系统认证。 [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=9|PDF p.9]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=16|PDF p.16]]
- 演讲建议标准化 OCP PDB，但以问题形式征求需求；没有已批准的统一 PDB 规格。 [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=17|PDF p.17]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| HSC 管理插入浪涌与拔出放电 | 半砖模块、隔离 12 V 辅助输出及 V/I 监测；需冷板热管理，不能把“热插拔”当可任意带电操作 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=12\|PDF p.12]] |
| LVDC→50 V 隔离非稳压与 50→12 V 非隔离稳压分工 | 前者依赖受控母线且要求加强绝缘；后者复用低压平台。各块效率不等于总链效率 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=13\|PDF p.13]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=14\|PDF p.14]] |
| 电源架温度感知 | 输出连接器热敏电阻和外部母排温度测量属于设计功能；没有展示过热故障注入结果 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=9\|PDF p.9]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 电源架规格 | 100 / 160 kW，均采用 18 kW PSU | 100 kW：537×46×867 mm；160 kW：855×46×1086 mm。产品处于 Sampling；输入/冗余需按方案核对 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=9\|PDF p.9]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=16\|PDF p.16]] |
| 隔离模块效率要求 | >98% | 作者 must-have 要求/产品主张；未给完整输入、负载与温度条件 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=10\|PDF p.10]]、[[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=13\|PDF p.13]] |
| 板上隔离模块送样 | 4/6 kW、50 V；3 kW、12 V | p.16 列为 Sampling；不代表所有型号相同效率或相同热包络 | [[Rack & Power/800V direct-to-server and power shelf solutions.pdf#page=16\|PDF p.16]] |

## 图表与架构

p.3 图中可选 800 V BBU/CBU 位于 HVDC 母线，降压可发生在 shelf 或服务器入口。p.9 160 kW 采用 4 个 HVDC 六针接口，100 kW 为 2 个；额外 sense/earth/return 管脚是接口组成而非简单两根功率线。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]

## 不确定性与待验证

- p.5 把 LV 与 ELV/SELV、60 V 阈值混用；本文不将该页术语直接当法规结论，正式安全设计需按适用标准版本、场景与认证机构确认。
- PDB 的 EMI、保持时间、放电到安全状态所需时间和漏液故障策略需整机验证；演讲没有足够数据核算 TCO。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/800V%20direct-to-server%20and%20power%20shelf%20solutions.pdf)
- 来源身份 `src-ef44afab3769`；Git blob `9f012c9dacf2acc185a6c303ee8557e8cde343f3`；原始物理页数 `18`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
