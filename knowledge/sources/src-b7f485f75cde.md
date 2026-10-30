---
id: "src-b7f485f75cde"
type: "source"
title: "Meta GW 级 AI：跨地域集群与可靠性爬坡比名义容量更重要"
source_path: "keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf"
source_git_blob_sha: "8556151e9db0bc4bf31aa353ee1391e23a3ff330"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [9, 11, 12, 15, 18, 19]
updated: "2026-10-30"
---

# Meta GW 级 AI：跨地域集群与可靠性爬坡比名义容量更重要

> 阅读范围：已阅读本文件全部可提取文字（21页）。关键页已视觉核对：9, 11, 12, 15, 18, 19；不代表逐页视觉审核。

## 核心结论

主旨逐个挑战“集群只在一栋楼”“建完就能工作”“软件容易”等假设。可直接支持的技术结论是跨区域网络与长期可靠性治理已成为系统设计的一部分；图片和口号不能补成未记录的施工/软件细节。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=2|PDF p.2]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=6|PDF p.6]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=8|PDF p.8]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=13|PDF p.13]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=17|PDF p.17]]

## 关键证据

- 图中文字以多个 region 与 backend aggregation 表示多区域 GPU 集群，而 MetaRoCE 的说明强调 per-path signals、绕过拥塞与只重传丢失部分。没有给对照延迟/吞吐曲线。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=6|PDF p.6]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=7|PDF p.7]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=8|PDF p.8]]
- 可靠性图按 interruptions per 8K GPUs/day 归一化，并区分 actual 与 dotted projection；这是运行有效性比总 GPU 数更重要的证据。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=15|PDF p.15]]
- Prometheus 1 GW+ cluster、Hyperion future 5 GW 属规模描述/未来规划，不能等同当前可用算力或已接电容量。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=20|PDF p.20]]

## 指标与条件

p.15 target 为 2.0 interruptions/8K GPUs/day。GPU-1、GPU-2 trend 分别标 5.5%/week、5.9%/week；实际末端点仍高于目标，跨过目标的是投影线。没有横轴日期、事件定义或置信区间，因此不能声称“已达标”、计算真实到达日期或作器件 AFR。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=15|PDF p.15]]

## 图表与架构

已核对 p.9、11–12 工程照片，p.15 可靠性图，p.18 可靠系统示意与 p.19 装饰画。空文字页并非含可提取实验数据；照片不证明工期、成本或施工方案。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=9|PDF p.9]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=11|PDF p.11]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=12|PDF p.12]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=15|PDF p.15]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=18|PDF p.18]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=19|PDF p.19]]

## 关联与比较

与 RAS/测试材料联读：故障中断频率、隔离范围、诊断有效率、恢复时间需共同构成 useful compute 预算；单项优化不能直接变成 tokens/s 可用性。

## 不确定性与待验证

无法由资料确定 region 实际距离分布、算法通信容忍度、光网/冗余配置、GPU-1/2具体型号或中断根因。未记录的现场讲解与视频不作已读内容。[[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=3|PDF p.3]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=4|PDF p.4]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=5|PDF p.5]][[keynotes/03_Concrete to Code Engineering AI Infrastructure at Gigawatt Scale.pdf#page=15|PDF p.15]]

