---
id: "src-8d1efe38d717"
type: "source"
title: "Intel 主旨：按请求选模型与按阶段选计算，而非统一加速器"
source_path: "keynotes/13_Put Every Prompt in Its Place.pdf"
source_git_blob_sha: "fa555d9d6bbbfff2dcd65158e75ef52f1977d396"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 23
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 8, 10, 13, 15, 18]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [5, 6, 8, 13, 18]
updated: "2026-10-30"
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# Intel 主旨：按请求选模型与按阶段选计算，而非统一加速器

> 阅读范围：已阅读本文件全部可提取文字（23页）。关键页已视觉核对：5, 6, 8, 13, 18；不代表逐页视觉审核。

## 核心结论

“Put Every Prompt in Its Place”的可操作含义是两层路由：先按任务质量/成本选择模型，再按 prefill/decode/CPU-native agent 操作选择计算。开放接口与 OAC 用于保留组合空间，但具体效率仍需以相同服务质量和真实请求分布比较。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=4|PDF p.4]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=5|PDF p.5]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=10|PDF p.10]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=18|PDF p.18]]

## 关键证据

p.18 示意 Xeon 负责 classify/route/coordinate，GPU D-series 支持 throughput，低延迟路径分 D-series prefill 与 SambaNova RDU decode，CPU执行 agent native operations。是任务分工架构，不是已经给出通用混合部署 benchmark。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=18|PDF p.18]]

p.8 产品名 Crescent Island；p.15 将 dense E-core 与高单线程 P-core 需求区分。核数、FLOPS 与 agent 完成任务数不能直接等价。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=8|PDF p.8]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=15|PDF p.15]]

## 指标与条件

p.5 引述多份外部 routing 研究，汇总 ~60% lower cost、>80% lower per-query energy、<1% performance drop；没有同一实验完整条件，不可当作 D-series 产品实测或同一负载必然同时达到。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=5|PDF p.5]]

p.8 标称 1.5 TB/s、350 W air-cooled PCIe、1311/2622 TFLOPS FP8/MxFP4。**480 GB 是设计支持 partner ODM cards 的上限；脚注 Intel-branded card 为160 GB LPDDR5x。** 不能把480 GB写成默认Intel卡规格。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=8|PDF p.8]]

## 图表与架构

已核对 p.5 引用/质量边界、p.6 open-weight usage 图、p.8 规格脚注、p.13 agent增长图与p.18异构流程。使用量图不代表开源模型质量或市场全部流量，agent增长未用来推导硬件销量。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=5|PDF p.5]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=6|PDF p.6]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=8|PDF p.8]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=13|PDF p.13]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=18|PDF p.18]]

## 关联与比较

与 KV cache/IO prioritization 相接：路由改变请求分布、缓存命中率、数据移动与排队，因此模型选择收益不能与硬件标称倍率简单相乘。商业化应按 quality-constrained cost/task 或 energy/task 而非仅cost/token比较。

## 不确定性与待验证

没有统一在线 p99/TTFT/TPOT、模型精度、batch、量化、价格和功耗实测。多个外部研究的引用在此未独立复核；只说明源页如何陈述，不能延伸成最新通用结论。[[keynotes/13_Put Every Prompt in Its Place.pdf#page=5|PDF p.5]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=8|PDF p.8]][[keynotes/13_Put Every Prompt in Its Place.pdf#page=18|PDF p.18]]

