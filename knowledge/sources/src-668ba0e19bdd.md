---
id: "src-668ba0e19bdd"
type: "source"
title: "Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads"
source_path: "ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf"
source_git_blob_sha: "5fa7db6fb5ea6e0f534b60070ddfb0ad01613f74"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9]
text_reviewed: true
key_pages_visual_checked: [6]
tags: ["ocp2026", "source", "power-cooling", "grid", "power-quality", "ride-through"]
concepts: []
---

# 电网接口扰动规范：电压穿越、故障后恢复与AI负载波动

> 原始题名：Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads。阅读范围：完整可提取文字（物理 PDF 共 10 页），关键引用图表另做视觉核对。

## 核心结论

- 讲者把数据中心并网问题拆成容量、故障穿越/恢复、爬坡、分钟内波动和强迫振荡；AI功率动态约束跨越软件、固件、硬件及冷却设施。 [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=3|PDF p.3]]、[[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=4|PDF p.4]]、[[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=9|PDF p.9]]
- 提案要求在一定电压下继续从电网取有功、恢复后快速回到故障前负载；“切到UPS即可保护IT”并不等于满足电网侧扰动性能。 [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=6|PDF p.6]]
- 方案比较涵盖PSU固件、MVUPS与电网侧无功支撑；既有设施改造受OEM、空间和成本限制，不能承诺统一固件即可解决。 [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=8|PDF p.8]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 约1500 MW北弗吉尼亚负载脱落事件作为动机 | 讲者对2024年事件的转述，本笔记未把它作为独立事故调查 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=2\|PDF p.2]] |
| p.6明确标为Proposed VRT/PFAPR | 统一提案不同于任何地区现行法规；地区例子仅是演讲快照 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=5\|PDF p.5]]、[[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=6\|PDF p.6]] |
| 既有设施grandfathering、增量增长与新设施要求分开 | 这是hyperscaler实施建议，不是已批准法律豁免 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=8\|PDF p.8]] |
| 需要PSU/LV-MV UPS、冷却供应商、grid stability伙伴共同参与 | 架构推论：机柜电源验证用例须包含设施和电网边界，而不仅ASIC负载阶跃 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=9\|PDF p.9]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 提案电压/最短穿越 | 0.80≤V<0.90：2 s；0.50≤V<0.80：0.5 s；0.35≤V<0.50：0.25 s；V<0.35：0.15 s | V为POI线-中性或线-线电压标幺值；低两档允许功率降至任意值，高两档继续取有功且可随V降功率 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=6\|PDF p.6]] |
| 提案恢复 | POI回到0.90–1.10 p.u.后2 s内恢复到故障前90%负载 | 该提案的欠压各档要求；不代表全球统一法定值 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=6\|PDF p.6]] |
| 议程时间 | VRT/PFAPR v1.0：2026年10月发布目标；爬坡/波动v1.0：Q1 2027目标 | 演讲计划，不据此断言版本已发布 | [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=9\|PDF p.9]] |

## 图表与架构

已核对 p.6 提案表，尤其各电压区间边界、最短时间和允许的有功行为。未复原未核对的曲线，也未将p.5区域示例当作当前并网法律建议。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 真实项目应向当地电网取得当前有效并网协议和测试验收口径；本条只解释演讲提案。
- 储能容量、母线电压跌落、负载恢复策略与机械冷却ride-through需联合仿真和验证。
- 未提供电网侧设备或改造CAPEX、停机损失、运行成本，不能做经济排序。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf)
- 来源身份 `src-668ba0e19bdd`；Git blob `5fa7db6fb5ea6e0f534b60070ddfb0ad01613f74`；原始物理页数 `10`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
