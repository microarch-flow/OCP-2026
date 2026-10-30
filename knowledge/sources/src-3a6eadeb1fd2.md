---
id: "src-3a6eadeb1fd2"
type: "source"
title: "From Silicon to Services：性能排名必须固定模型、服务约束与 TCO 口径"
source_path: "market-impact-adoption/04_From Silicon to Services.pdf"
source_git_blob_sha: "1b81987cf67583246f7b878eacd340846a659329"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [1, 6, 9, 10, 11, 12, 13, 14, 15]
tags: ["ocp", "source", "platform", "market-impact-adoption"]
text_reviewed: true
key_pages_visual_checked: [10, 11, 12, 13, 14]
updated: "2026-10-30"
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# From Silicon to Services：性能排名必须固定模型、服务约束与 TCO 口径

> 阅读范围：已阅读本文件全部可提取文字（16页）。关键页已视觉核对：10, 11, 12, 13, 14；不代表逐页视觉审核。

## 核心结论

这份研究机构材料最有价值的不是单次厂商排名，而是显示排名随模型、serving engine、精度、TTFT/交互速度和成本口径变化。AgentX重放长上下文工具会话，与固定8K/1K测试回答不同问题。所有结果均为演讲引用的快照，未独立复跑。[[market-impact-adoption/04_From Silicon to Services.pdf#page=9|PDF p.9]][[market-impact-adoption/04_From Silicon to Services.pdf#page=10|PDF p.10]][[market-impact-adoption/04_From Silicon to Services.pdf#page=11|PDF p.11]][[market-impact-adoption/04_From Silicon to Services.pdf#page=13|PDF p.13]][[market-impact-adoption/04_From Silicon to Services.pdf#page=14|PDF p.14]]

## 关键证据

- AgentX v1.0列393匿名coding sessions，选自8300会话；44%用subagents。88K/272K/675K input-token p50/p90/p99来自指定DeepSeek run，不能当所有真实用户分布。[[market-impact-adoption/04_From Silicon to Services.pdf#page=9|PDF p.9]]
- AMD+TileRT示例达到约470tokens/s/user的P90 interactivity，但源页同时警告higher TTFT，因此峰值streaming speed不证明cost-efficiency胜出。[[market-impact-adoption/04_From Silicon to Services.pdf#page=11|PDF p.11]]
- TPUv7结果是aggregated FP8/STP preview；disaggregated prefill/decode、MTP、AgentX仍待比较。未来Trainium3等覆盖没有已给结果。[[market-impact-adoption/04_From Silicon to Services.pdf#page=14|PDF p.14]][[market-impact-adoption/04_From Silicon to Services.pdf#page=15|PDF p.15]]

## 指标与条件

Rubin preview在DeepSeekV4Pro AgentX、匹配P90 interactivity下，相对bestGB300 engine为100tok/s/user时约2.1×、150时约7.2× tokens/MW；all-in utility power/chip采用VR2003.3kW、GB3002.12kW、MI355X2.09kW的模型，且prerelease software。不是任何SLA都7.2×。[[market-impact-adoption/04_From Silicon to Services.pdf#page=12|PDF p.12]]

p.13 internalTCO（TPU$1.03/chip-hour）与p.14 externalTCO不是同口径；后者100tok/s/user、Qwen3.5FP8、8K/1K、STP下列$0.181/M total tokens vsB200$0.222/B300$0.276。total tokens不等于output tokens，也不是零售API报价。[[market-impact-adoption/04_From Silicon to Services.pdf#page=13|PDF p.13]][[market-impact-adoption/04_From Silicon to Services.pdf#page=14|PDF p.14]]

## 图表与架构

已核对p.10–14比较图、preview与条件说明。p.10的20×+、5×、CPU KV offload +81.7%来自不同模型/engine/对照，不能串成一个综合收益。[[market-impact-adoption/04_From Silicon to Services.pdf#page=10|PDF p.10]][[market-impact-adoption/04_From Silicon to Services.pdf#page=11|PDF p.11]][[market-impact-adoption/04_From Silicon to Services.pdf#page=12|PDF p.12]][[market-impact-adoption/04_From Silicon to Services.pdf#page=13|PDF p.13]][[market-impact-adoption/04_From Silicon to Services.pdf#page=14|PDF p.14]]

## 关联与比较

与AMD/NVIDIA/Intel主旨联读能解释看似冲突的最高性能主张：offline吞吐、P90交互、E2E latency、quality与tokens/$是不同目标。应做Pareto曲线而非无条件单一排行榜。

## 不确定性与待验证

页面带Confidential标识，源文件已由用户提供于本语料；本卡仅作必要分析，不复制图表或长段原文。外部CI链接、TCO模型价格和样本代表性未独立验证；残留模板日期不作为演讲日期。报价、收入、投资评价不在此卡结论范围。[[market-impact-adoption/04_From Silicon to Services.pdf#page=1|PDF p.1]][[market-impact-adoption/04_From Silicon to Services.pdf#page=6|PDF p.6]][[market-impact-adoption/04_From Silicon to Services.pdf#page=11|PDF p.11]][[market-impact-adoption/04_From Silicon to Services.pdf#page=14|PDF p.14]]

