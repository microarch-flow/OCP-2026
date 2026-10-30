---
id: "src-0de5a776ae41"
type: "source"
title: "Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question"
source_path: "ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf"
source_git_blob_sha: "79f18e86075e8402df1cd828a1c4787c0dcc8458"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [6]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question

## 核心结论
Broadcom/Arista提出scale-across的Backward-to-Sender通知：在长RTT场景，拥塞点直接向sender返回丰富信息，而不必等待端到端回路。核心收益假设是控制信号更早抵达，不是改变光传播时延。[[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=3|PDF p.3]] [[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=4|PDF p.4]] [[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=5|PDF p.5]]

## 关键证据
通知可含port/traffic-class/device queue信息及截取的原packet，针对阈值、drop、path failure；设计意图是不改原packet header、不要求switch per-flow state。控制流量约1%或更低属于目标。[[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=7|PDF p.7]]

## 指标与条件
p.6图以BTS 10µs对end-to-end 1000µs展示反馈时延，纵轴对数；未给硬件、距离、负载、重复次数，不应称实测100倍应用加速，更不能等同p99降低100倍。[[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=6|PDF p.6]]

## 图表与架构
已看p.6反馈路径与坐标。长RTT、短于RTT的flow和昂贵DCI容量使反馈滞后尤其敏感；但更快反馈仍需与sender算法、buffer、限速协调。[[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=5|PDF p.5]]

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]；[[knowledge/comparisons/ai-infra-mrc-uet-and-fabric-layers]]。

## 不确定性与待验证
多hop重复通知、rate-control、sender接收处理能力、异构CCA协调仍未决；SAIPR/UEC BTS讨论组处于推进阶段，不是已完成标准和跨vendor部署证明。[[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=8|PDF p.8]] [[ai-clusters/Scale-Across-To-Go-Forward-or-To-Go-Backwards-That-is-the-question.pdf#page=9|PDF p.9]]
