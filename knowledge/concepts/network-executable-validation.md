---
id: "network-executable-validation"
type: "concept"
title: "可执行规范：把协议、平台和网络行为变成验收契约"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 可执行规范：把协议、平台和网络行为变成验收契约

## 定义与归纳
接口PDF、API兼容、模拟器通过与生产合格是四个不同层次。有效开放生态需要可重复image、配置、topology、fault injection与跨实现测试，且在交付合同中写明缺失能力和测量条件。

## 四层证据
- 预硬件功能层：SimX让SAI/FBOSS提前集成，但明确不模拟QoS与L1；90%测试通过不等于p99已验证。[[knowledge/sources/src-55e14ad184e2]] [[networking/06_NVIDIA SDK + FBOSS Building Production-Ready AI Network Fabrics.pdf#page=8|PDF p.8]][[knowledge/sources/src-55e14ad184e2]] [[networking/06_NVIDIA SDK + FBOSS Building Production-Ready AI Network Fabrics.pdf#page=13|PDF p.13]]
- 平台管理层：OSPA涵盖power/sensor/OOB/FW而非routing；配置驱动发现需硬件拓扑/驱动匹配。[[knowledge/sources/src-4cb1cfbea778]] [[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=5|PDF p.5]][[knowledge/sources/src-4cb1cfbea778]] [[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=14|PDF p.14]]
- 多节点服务层：FBOSS TaaC将traffic+disruption+health checks声明为数据；Wedge800仍有50 failing、TH6P multi-DUT尚未建立，必须保留未完状态。[[knowledge/sources/src-983fb0686005]] [[networking/07_Open, AI-Ready FBOSS From Platform Bring-up to Solution Qualification .pdf#page=6|PDF p.6]][[knowledge/sources/src-983fb0686005]] [[networking/07_Open, AI-Ready FBOSS From Platform Bring-up to Solution Qualification .pdf#page=8|PDF p.8]]
- 协议行为层：MetaRoCE双独立实现互测加确定性loss/reorder注入；MRC把互通分格式、算法、时序行为三级。[[knowledge/sources/src-f76571507532]] [[networking/MetaRoCE in Software.pdf#page=12|PDF p.12]][[knowledge/sources/src-f76571507532]] [[networking/MetaRoCE in Software.pdf#page=15|PDF p.15]][[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=14|PDF p.14]]

## 推理网络验收建议（综合推导）
把测试artifact与firmware/NOS/CC/config/topology一起版本化。测试矩阵包含small messages、all-to-all、KV慢接收端、incast、单/多链路损坏、mixed-NIC、warm upgrade、telemetry压力。报告p50/p99/timeout/retry、吞吐和资源占用，失败项不从分母隐藏。

ML运维闭环还需negative controls：容器资源限制不是零影响证明，错误action需要权限、速率上限、回滚与版本审计。[[knowledge/sources/src-e59f410df3c1]] [[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=12|PDF p.12]]

## 未决问题
不同模拟器缺失哪些信号？同一“passed”版本的测试集是否改变？跨厂出现行为分歧时谁是oracle？生产CSP可交付哪些交换机计数器？

## 关联
[[knowledge/concepts/network-inference-acceptance]] · [[knowledge/concepts/network-multipath-behavior]]
