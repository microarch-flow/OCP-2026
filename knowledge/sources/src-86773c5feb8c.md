---
id: "src-86773c5feb8c"
type: "source"
title: "Oracle／Vertiv：超越 WUE 的水账本与冷却选型边界"
source_path: "Sustainability/Sustainability and best practices for water efficiency.pdf"
source_git_blob_sha: "0cfb6a2e5575a90f0b6bc6e48de85b561ce14494"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7]
text_reviewed: true
key_pages_visual_checked: [1, 2, 3, 4, 5, 6, 7, 8, 9]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-water-energy-heat-tradeoffs]]"]
---

# Oracle／Vertiv：超越 WUE 的水账本与冷却选型边界

## 核心结论
水效率不能只报告现场WUE：应区分取水、消耗、排放、再用、施工一次性用水和供电上游水负担，再加入流域压力、季节、来源及水质。本PDF主要信息在图像内，已逐页视觉/OCR阅读。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=3|PDF p.3]][[Sustainability/Sustainability and best practices for water efficiency.pdf#page=4|PDF p.4]][[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]]

## 关键证据
- p.4建议先定边界→计量入出流→核对水量平衡→再发布KPI，报告withdrawal与consumption的年度m³、WUE的L/kWh-IT以及流域/上游背景。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=4|PDF p.4]]
- p.6区分蒸发/漂水/排污损失、回收水和隐藏的电力上游水足迹；“neutral”被写为减少淡水取水/增加再用的目标，不能据此认定净零耗水。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]]
- p.7把水压力与free-cooling窗口联合选型，并考虑水质、排放、供电水强度和余热市场；高水压力可限制冷却塔，浓密AI与余热需求又偏向液冷/换热路径。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=7|PDF p.7]]

## 指标与条件
p.5含“典型Microsoft年度用水范围”和多技术模拟PUE/WUE箱线图，但未在本页给统一IT负载/场地样本/气象条件，不能拿绝对升数作跨设施排名。循环流量L/min降低也不等于现场消耗量同比下降。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=5|PDF p.5]][[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]]

## 图表与架构
p.4平衡式是简化示意；工程账本仍须说明是否稳态、初次注水/储量变化和复用水是否跨边界，避免循环流被重复计为取水。p.6各技术条形图明确illustrative，不从其长度提取精确节水百分比。[[Sustainability/Sustainability and best practices for water efficiency.pdf#page=4|PDF p.4]][[Sustainability/Sustainability and best practices for water efficiency.pdf#page=6|PDF p.6]]

## 关联与比较
与Daikin WESI模型合读：费用交叉点不包含缺水约束，现场零蒸发也不等于全生命周期零水。与两相技术对读时应将冷板循环流量、设施补水和上游电力水分开。

## 不确定性与待验证
本文件为最佳实践框架，没有具名部署的计量闭合误差、年度基线或同SLA节水结果；还需水表校准、月度核对、处理药剂/排污及干旱期情景。

## 知识网络
[[knowledge/concepts/sustainability-water-energy-heat-tradeoffs]]
