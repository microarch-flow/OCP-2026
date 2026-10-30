---
id: "network-inference-acceptance"
type: "concept"
title: "推理网络验收：按通信图、尾延迟和可观测性采购"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 推理网络验收：按通信图、尾延迟和可观测性采购

## 问题
加速器线速和AllReduce峰值不是推理SLO。TP/EP小消息、KV迁移、慢CPU/接收NIC以及多租户负载会产生不同瓶颈。本页建议由演讲证据推导，来源并未提供完整推理p99基准。

## 已有直接证据
Meta按workload拆解：预训练并发ring冲突调LB；后训练trainer→sampler incast调buffer；推理remote KV经CPU进入RDMA NIC慢接收导致PFC上游扩散，需CC与通信库限速。[[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=10|PDF p.10]]
同演讲32 rings×16 GPUs，flowlet+CC调优将NCCL peak bus BW从58.4升到75.5GB/s，波动收窄；**这是吞吐+run variation，不是p99/ITL结果**。[[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=11|PDF p.11]]
CSP交换机遥测必须在合同明确metric、格式、频率；host access不等于fabric可观测。[[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=12|PDF p.12]]

## 建议的验收矩阵
- 工作负载：实际TP/EP/KV图、消息size分布、并发数、prefill/decode阶段、CPU/NIC回压；不要只复用training ring。
- 性能：业务TTFT/ITL/p99、collective完成p99、timeout/retry、GPU有效利用率与吞吐并列。
- 故障：中断、退化、flap、warm reboot、线路维修；衡量恢复窗口与剩余路径公平性。
- 证据：远端计数器、queue/PFC/ECN/FEC、配置与clock map；缺失capability不可写0。[[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=6|PDF p.6]][[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=8|PDF p.8]]
- 商业：performance guarantees与test artifacts交付、保留原始trace、维护余量、备件和故障归责；暂无价格证据，不做采购报价。

## 读数防错
Fungible FCP p99 10.5µs不是MRC生产推理p99。[[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=6|PDF p.6]] CPO省60%指光学下一代产品目标，不是整机TCO。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=7|PDF p.7]] ESUN小头节省24–44B不等于端到端collective同倍提升。[[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=7|PDF p.7]]

## 关联
[[knowledge/concepts/network-multipath-behavior]] · [[knowledge/concepts/network-buffer-workload-placement]] · [[knowledge/concepts/network-optics-reliability]]
