---
id: "src-3ded8c0c80fb"
type: "source"
title: "Beyond the Monolith: Open Middleware for Heterogeneous AI Infrastructure at Hyperscale"
aliases: ["Beyond the Monolith: Open Middleware for Heterogeneous AI Infrastructure at Hyperscale"]
speakers: "Gaurav Agarwal（主持/Marvell）；Chris Gottbrath；Mayank Saxena（Samsung）；Harry Kim（XCENA）；Youngpyo Joo（SK hynix）"
source_path: "fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf"
source_git_blob_sha: "a1f906ce7588247435926eb7a000dbb1c6509a53"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-text"
text_reviewed: true
key_pages_visual_checked: []
evidence_pages: [2, 4, 6, 7, 8, 10, 12, 14]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-ndp-contract]]"]
---

# Beyond the Monolith: Open Middleware for Heterogeneous AI Infrastructure at Hyperscale

## 核心结论
这是带各方观点页的 panel 材料，不是讨论实录。共同需求是开放数据/函数接口与可维护的软件接入；分歧主要在抽象边界、是否先固定 API，以及谁决定数据和计算放置。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=2|PDF p.2]]

## 关键证据
|观点|具体主张|
|---|---|
|PyTorch 接入与维护|allocator、自定义 operator、PrivateUse1、Dynamo/Inductor/Triton 可接入设备；长期需要硬件可用性、维护者与 CI/regression，而不只是一次 demo。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=6\|PDF p.6]] [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=7\|PDF p.7]]|
|Samsung|“standardize handoff, not vehicle”：先稳定薄的 workload-specific handoff，让硬件 fast path 独立演化。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=10\|PDF p.10]]|
|XCENA|数据优先、先测 workload 再定接口；不存在所有场景都胜出的设备，不同 memory model 应保留表达能力。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=12\|PDF p.12]]|
|SK hynix|先以扩容硬件建立部署，再验证计算收益、迭代公共接口；layout/placement 不能全留给应用开发者手工处理。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=14\|PDF p.14]]|

## 指标与条件
没有可用的端到端性能/功耗基准。Cognos 的开放时间是演讲中的计划，本文未以访问仓库方式验证发布状态。

## 图表与架构
文本提出 AI graph lowering、多层 IR、可插拔 backend，以及数据平面和发现/配置/管理控制平面分离。接口必须容纳非均匀内存和近数据计算，而非仅增加一个 device name。[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=4|PDF p.4]] [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=7|PDF p.7]]

## 关联与比较
与 [[knowledge/concepts/compute-memory-ndp-contract|近数据卸载的四类契约]] 互证：算子签名只是一个层次，所有权、coherence、placement、完成语义及维护责任同样重要。

## 不确定性与待验证
本笔记只归纳书面观点，不声称 panel 达成了共识或正式标准。需要具体可运行 reference path、跨供应商 compatibility tests 和系统级 benchmark 来检验抽象是否过宽/过窄。

## 原始页码导航
[[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=2|p.2]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=4|p.4]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=6|p.6]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=7|p.7]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=8|p.8]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=10|p.10]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=12|p.12]] · [[fti-workshop-data-centric-computing/Beyond-the-Monolith-Open-Middleware-for-Heterogeneous-AI-Infrastructure-at-Hyperscale.pdf#page=14|p.14]]
