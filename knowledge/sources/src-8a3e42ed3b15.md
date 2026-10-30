---
id: "src-8a3e42ed3b15"
type: "source"
title: "A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments"
source_path: "ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf"
source_git_blob_sha: "ace2a612f743c302d5f764b6dc67d97f668f858b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
evidence_pages: [4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [9, 15]
concepts: ["[[knowledge/concepts/ai-infra-multipath-failure-domains]]"]
duplicate_content_of: "src-912af8761fc2"
---

# A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments

## 核心结论
Broadcom将MRC描述为RoCEv2 RC增量扩展、UEC为涵盖transport/link/security的clean-slate体系。选择取决部署时间、现有API/硬件和迁移复杂性，不是一个“更先进即更快”的结论。[[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=4|PDF p.4]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=16|PDF p.16]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=17|PDF p.17]]

## 关键证据
MRC wire format不与legacy RC互通，但复用verbs/QP；当前write/write-with-immediate，controller与applicationAPI分离。UEC/UET提供更广操作/ordered-unordered modes、sender/receiver CC及LLR/CBFC/CSIG等跨层工作。[[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=7|PDF p.7]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=9|PDF p.9]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=10|PDF p.10]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=11|PDF p.11]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=12|PDF p.12]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=13|PDF p.13]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=15|PDF p.15]]

## 指标与条件
无同配置吞吐/latency测试；p.8 EV128–256和“microseconds reroute”为作者实现概述，无硬件、负载或恢复分布。不能拿来覆盖专门MRC材料对optional primitives与可选CC的精确说明。[[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=8|PDF p.8]]

## 图表与架构
已看p.9API图及p.15比较表。“UEC更durable foundation”属于作者判断，非实验结果；表中production/maturing状态只对应演讲时点，未独立核验。

## 关联与比较
[[knowledge/comparisons/ai-infra-mrc-uet-and-fabric-layers]]。与另一源路径UEC-vs-MRC…为**完全相同Git blob内容**；本卡与对应源卡仅保留两个路径身份，不算两份独立证据。

## 不确定性与待验证
需直接规范/实现interop测试才能判mandatory/optional/security支持；p.5标准CC保证互通的概括不能解释为MRC只允许一个CC算法。[[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=5|PDF p.5]] [[ai-clusters/A Comparative Analysis of Next-Generation Networking Standards for Large-Scale DC Deployments.pdf#page=18|PDF p.18]]

重复路径源卡：[[knowledge/sources/src-912af8761fc2]]。同一Git blob，不独立计证。
