---
id: "src-8779c0d1fef0"
type: "source"
title: "Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis"
source_path: "ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf"
source_git_blob_sha: "cf93b5c057949d9ce5e1f69de4fdf4398906da94"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [2, 7, 13, 14, 15, 16, 18, 19, 20]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [7, 8, 13, 14, 15, 16, 17, 18]
concepts: ["[[knowledge/concepts/ai-infra-deployment-readiness]]"]
---

# Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis

## 核心结论
NVIDIA以250MW AI factory比较不同城市、高温TCS与heat-rejection架构，说明释放cooling电力有机会增加IT容量；但“更高温→更多tokens/revenue”还需要芯片热性能、SLO与需求验证，不是设施PUE自动给出的收入。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=2|PDF p.2]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=7|PDF p.7]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=15|PDF p.15]]

## 关键证据
D1专用loop+air-cooled chiller；D2专用loop+water-cooled chiller/dry cooler；D3共用高温loop并用CRAC替换CRAH/fanwall。D2/D3改变设备与水路，不能把收益全归于温度一个变量。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=7|PDF p.7]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=14|PDF p.14]]

## 指标与条件
D2从S30到S45模型中额外compute power Seattle20.5MW、Chicago23.9MW、Albuquerque22.6MW、Dallas16MW、Phoenix5.5MW；为既定站点/模型的供电容量余量，不是实际GPU吞吐。p.15另称16MW(37%)/14MW(33%)，百分比分母不清且非250MW总容量比例，不沿用为算力增长率。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=13|PDF p.13]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=15|PDF p.15]]
p.16 Seattle S45 D1/D2/D3 annual PUE1.13/1.09/1.12，15年TCO每MW$23.6M/$22.3M/$22.8M。成本仅纳入mechanical plant差异及能源OpEx，假设$0.12/kWh、3%inflation，非全数据中心TCO。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=16|PDF p.16]]

## 图表与架构
已看全部关键比较页。peak与annual PUE必须分开；S45范围下“zero water”是现场热排放用水口径，不含上游发电或建设。p.18按温度比较也保持同一模型成本边界。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=13|PDF p.13]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=16|PDF p.16]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=18|PDF p.18]]

## 关联与比较
[[knowledge/concepts/ai-infra-deployment-readiness]]；推理架构应联测junction temperature、时钟、errors、TTFT/TPOT与整站墙上功耗，避免把facility节能转成芯片降频。

## 不确定性与待验证
缺详细设备选型/气象年份/部分负载控制、模型验证与失效工况；作者“all regions/climates”应限本研究的五城。S45安全运行仍取决于具体IT与冷板规范。[[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=19|PDF p.19]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=20|PDF p.20]]
