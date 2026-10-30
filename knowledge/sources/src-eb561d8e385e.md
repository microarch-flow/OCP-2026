---
id: "src-eb561d8e385e"
type: "source"
title: "NVIDIA 主旨：机架、供电、运行软件共同决定每 MW 有效吞吐"
source_path: "keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf"
source_git_blob_sha: "fc3f020a9b2c45341d984dd81e8aa62ab0383202"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 9, 12, 13, 14, 16, 17]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [5, 9, 13]
updated: "2026-10-30"
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# NVIDIA 主旨：机架、供电、运行软件共同决定每 MW 有效吞吐

> 阅读范围：已阅读本文件全部可提取文字（21页）。关键页已视觉核对：5, 9, 13；不代表逐页视觉审核。

## 核心结论

主旨将 MGX 机械/液冷设计、800 VDC 供电、CPU agent 计算、MaxLPS 和多平面网络放入同一 AI factory 设计。材料的应用收益是全栈结果，不能拆成某单个器件或协议的独立贡献。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=5|PDF p.5]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=6|PDF p.6]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=8|PDF p.8]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=12|PDF p.12]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=14|PDF p.14]]

## 关键证据

- MGX1.2 将 compute/switch tray、blind mate、manifold、busbar 与机架承力一体考虑；cableless/hoseless 指 tray service 接口，不是整个数据中心无需线缆管路。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=6|PDF p.6]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=7|PDF p.7]]
- 800 VDC 架构图用 16 MW deployment unit、4 MW scalable units、集中 end-of-row conversion；这些是设计单元，不是此材料证明的已带载总容量。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=8|PDF p.8]]
- networking 支持多 transport（Falcon/MetaRoCE/MRC/adaptive RDMA）是生态范围，不能由支持名单断言不同端点间透明互通。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=16|PDF p.16]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=17|PDF p.17]]

## 指标与条件

p.5 “up to30×”来自 DeepSeek-V4-Pro / SemiAnalysis AgentX、Vera Rubin NVL72 与 GB300 NVL72 的全栈比较；包含 disaggregation、KV caching/routing、rate matching、kernels 等，且曲线随 interactivity 改变。未给完整工作负载/测量设置，不作统一性能倍率。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=5|PDF p.5]]

p.13 具体案例自报 Iceland、Kimi K2.5、8K/1K、同 provisioned power budget 下多部署 37% GB300 GPUs、throughput +49%；“同预算”不等于实际耗电量/冷却能耗相同，也不是每 GPU +49%。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=13|PDF p.13]]

p.9 原稿把 1.2 TB/s 写为 memory bandwidth **per core**，未解释口径；不能据此算单芯片总带宽，需厂商澄清。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=9|PDF p.9]]

## 图表与架构

已核对 p.5 token/MW–interactivity 与 cost 曲线、p.9 带宽措辞、p.13 案例条件。4×/30× 等图中文字不能脱离所在轴和服务交互条件。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=5|PDF p.5]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=9|PDF p.9]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=13|PDF p.13]]

## 关联与比较

与 Meta 可靠性爬坡、SSD KV、开放 management 材料联读：商业指标必须把功率额度、可部署 GPU 数、稳定利用率、服务质量和停机窗口同时计入，而不能只比标称 FLOPS。

## 不确定性与待验证

“durable/fungible/appreciating value”、长期售卖年限和厂商排名为定位主张；没有统一 TCO、故障率、客户端 tail latency 或资本成本数据。MaxLPS、光网与 rack 优化是否同一配置需另行确认。[[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=4|PDF p.4]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=12|PDF p.12]][[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=14|PDF p.14]]

