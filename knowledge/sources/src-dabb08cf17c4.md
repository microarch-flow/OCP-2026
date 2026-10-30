---
id: "src-dabb08cf17c4"
type: "source"
title: "Cold plate subproject update"
source_path: "Cooling：Cold Plate/Cold plate subproject update.pdf"
source_git_blob_sha: "65e70bd632894ea51f8e61814c44f36dcc9063c0"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 60
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 12, 13, 16, 17, 22, 23, 24, 26, 29, 30, 31, 32, 33, 35, 38, 39, 40, 41, 44, 49, 50, 51, 52, 53, 54, 55, 57]
text_reviewed: true
key_pages_visual_checked: [14, 15, 17, 31, 39, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
tags: ["ocp2026", "source", "power-cooling", "cold-plate", "interoperability", "ssd", "qd"]
concepts: []
---

# 冷板子项目合集：SSD集成冷板、冷却液与接液材料、PBMC及UQD互操作

> 原始题名：Cold plate subproject update。阅读范围：完整可提取文字（物理 PDF 共 60 页），关键引用图表另做视觉核对。

## 核心结论

- 此60页PDF是六段工作流合集：总体p.1–10、DLC E1.S p.11–18、流体p.19–27、接液材料p.28–36、PBMC p.37–46、UQDv2 p.47–60；不能只把它当项目更新封面。 [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=2|PDF p.2]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=4|PDF p.4]]
- SSD内置冷板需兼顾手工热插拔、两面器件高度/温限及TIM压力；所示双面集成冷板仍是conceptual reference方向。 [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=12|PDF p.12]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=13|PDF p.13]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=16|PDF p.16]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=17|PDF p.17]]
- 接液材料兼容必须针对具体配方与具体材料组合；相同PG25或PA名称不能证明跨供应商兼容。 [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=29|PDF p.29]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=30|PDF p.30]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=32|PDF p.32]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=33|PDF p.33]]
- UQDv2互操作试点显示流失量、连接力、压降和seal washout都需统一测法；形状互配不等于完整运行互操作。 [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=49|PDF p.49]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=50|PDF p.50]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=51|PDF p.51]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=52|PDF p.52]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=53|PDF p.53]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=54|PDF p.54]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=55|PDF p.55]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=57|PDF p.57]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 已批准单相冷板测试、UQD2、PG25/水/两相介电液base spec、PBMC等；部分guidelines仍在过程 | 工作组快照。水基guideline p.23明确计划2026年11月，不能把目录全称已发布 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=5\|PDF p.5]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=6\|PDF p.6]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=7\|PDF p.7]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=23\|PDF p.23]] |
| guideline面向使用部署运维，base spec面向供应商质量性能 | PG25、水、两相介电三类分开，避免把不同液体要求混成一个通用配方 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=22\|PDF p.22]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=24\|PDF p.24]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=26\|PDF p.26]] |
| 接液验证从应用/材料→失效模式→方法/条件/判据→资格→证据清单 | 流程围绕组件力学性能与液体污染/抑制剂流失双向退化 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=30\|PDF p.30]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=31\|PDF p.31]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=33\|PDF p.33]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=35\|PDF p.35]] |
| PBMC支撑高流量、误差容纳与1RU/OU服务性，Rev1.1补ORB接口和机械测试 | 接口标准与实际多供应商完整互测仍需配套证据 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=38\|PDF p.38]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=39\|PDF p.39]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=40\|PDF p.40]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=41\|PDF p.41]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=44\|PDF p.44]] |
| UQD试点强调tare fixture一致；seal washout跨站点有方向性差异 | 说明测量方法本身影响互操作结论，不是宣称所有组合完成寿命保证 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=53\|PDF p.53]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=54\|PDF p.54]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=55\|PDF p.55]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| PBMC设计参数 | 5mm径向偏移；5mm区内组合2.5°；配合距离工作范围6.5mm | 该接口的设计陈述，不推广到其他QD | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=39\|PDF p.39]] |
| PBMC压力/流量 | 36LPM压降目标<4psi；最大工作压力75PSIG | p.40表平均2.50、上界4.00、下界1.00psid；工质温度未给 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=40\|PDF p.40]] |
| 接液材料示例 | PP-R/PP-RCT/PP-H，ASTM D543，60/80°C、1008h | 示例判据：质量/尺寸变动<5%，拉伸/断裂伸长变化<10%；不是材料已经通过的结果 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=31\|PDF p.31]] |
| UQD08互操作试点 | 流失图n=60、USL0.07mL/cycle；连接力图n=200；PQ图n=420 | 为图示样本/数据点标签，未说明统计独立性；不能当420个长期无故障系统 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=51\|PDF p.51]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=52\|PDF p.52]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=53\|PDF p.53]] |
| UQD08压降 | 额定流量18L/min处约1.0±0.2psi | 试点跨供应商/流向一致性陈述；需要同tare校正方法 | [[Cooling：Cold Plate/Cold plate subproject update.pdf#page=53\|PDF p.53]]、[[Cooling：Cold Plate/Cold plate subproject update.pdf#page=54\|PDF p.54]] |

## 图表与架构

全文可提取文字已读；另核p.14–15、17、31、39–40及48–58，补回UQD图像页。UQD流失/力/PQ图有统计标签，但没有据图推导未给的可靠性置信寿命。

## 关联与比较

- [[knowledge/concepts/power-cooling-fluid-assurance]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 本文件含多个作者和成熟度，合并PDF不是全部内容共同背书。
- PBMC Rev1.1文字把torque用N表示，单位疑点需回正式规范，不在本笔记纠正成N·m。
- E1.S双面冷板是概念；UQD seal washout方法和统一verification文件仍WIP。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Cooling%EF%BC%9ACold%20Plate/Cold%20plate%20subproject%20update.pdf)
- 来源身份 `src-dabb08cf17c4`；Git blob `65e70bd632894ea51f8e61814c44f36dcc9063c0`；原始物理页数 `60`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
