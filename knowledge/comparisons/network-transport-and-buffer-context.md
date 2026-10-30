---
id: "network-transport-and-buffer-context"
type: "comparison"
title: "看似矛盾的AI网络建议：无损、尽力而为、深缓冲与浅缓冲"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 看似矛盾的AI网络建议：无损、尽力而为、深缓冲与浅缓冲

## 比较原则
同一厂商在不同fabric上选择相反机制不必是矛盾：先固定workload、placement、transport、distance、feedback和成熟度，再评估。**本页为跨源解释，不是同平台A/B实验。**

## 四种语境
1. **BAG跨L2训练**：replica在L2，DP ring跨BAG，5:1 oversub；长距RoCE+credit+deep buffer，按距离切headroom。[[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=6|PDF p.6]][[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=9|PDF p.9]][[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=12|PDF p.12]]
2. **RBB区域共享数据**：DC-class每W密度，shallow buffer+GLIDE/ECN，5ms单向70%link与常态7%buffer；4.5:1 incast仍能填满buffer。[[knowledge/sources/src-e41f8d86b57e]] [[networking/Srv6 powered backbone networks.pdf#page=5|PDF p.5]][[knowledge/sources/src-e41f8d86b57e]] [[networking/Srv6 powered backbone networks.pdf#page=6|PDF p.6]]
3. **某CSP与Meta历史栈对齐**：由lossy/aggressive retrans/custom CC变为PFC/two classes/relaxed retrans，目的on-prem parity；不能推广为“关闭CC最佳”。同演讲推理slow receiver要求CC/库限速。[[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=7|PDF p.7]][[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=10|PDF p.10]]
4. **新transport演进**：MetaRoCE best-effort+ECN+QP内多路径+SACK；MRC关注ReSS/SMaRTT和mixed-NIC行为；ESUN则在固定scale-up fabric用LLR/CBFC简化端点。[[knowledge/sources/src-f76571507532]] [[networking/MetaRoCE in Software.pdf#page=2|PDF p.2]][[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=7|PDF p.7]][[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=9|PDF p.9]]

## 共识与真正分歧
共识：静态平均线速不足，必须处理hotspot、incast、failure和应用放置。分歧：恢复可靠性放在link、fabric还是endpoint；代价分别表现为credit/headroom、switch buffer、reorder/retransmission状态与control complexity。

## 推理选择规则（综合建议）
- 不用训练DP ring证明EP all-to-all或KV迁移的可用oversub。
- 不用GLIDE特定测量证明没有配套CC的浅buffer也安全。
- 不用无损标签证明无拥塞、无HOL或无p99放大。
- 不用“支持标准”替代behavior compatibility：采样节奏、RTO、流/路径CC边界要进测试。

## 待解
缺少相同trace下不同transport/buffer方案的queue+p99+CPU/NIC状态+成本比较。下一步是构建可复用验收fixture而非从宣传页挑最大数字。

## 关联
[[knowledge/concepts/network-buffer-workload-placement]] · [[knowledge/concepts/network-inference-acceptance]] · [[knowledge/concepts/network-multipath-behavior]]
