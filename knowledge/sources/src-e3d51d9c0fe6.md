---
id: "src-e3d51d9c0fe6"
type: "source"
title: "Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics"
source_path: "ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf"
source_git_blob_sha: "c64f8f63fdb93f510e482887c920f7bf629f094f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [3, 9, 10]
concepts: ["[[knowledge/concepts/ai-infra-inference-serving-shapes]]"]
---

# Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics

## 核心结论
Hedgehog/Celestica 给出的原则是：选择满足 SLO 的最简单 serving shape，而非默认跨主机或 prefill/decode 分离。一旦 tensor、expert 或 KV state 跨主机，网络完成时间分布就成为 token 延迟分布的一部分。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=2|PDF p.2]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=4|PDF p.4]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=5|PDF p.5]]

## 关键证据
- Standalone：模型+KV 本地可容纳；Replicated：独立请求横向扩容；Distributed：一个请求跨系统；Disaggregated：角色/阶段分离。它们是部署形态，不是成熟度阶梯。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=3|PDF p.3]]
- 先测最小 serving unit，再判断复制、分布、分离是否必要；最终在 burst、故障、多租户争用下验证。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=4|PDF p.4]]
- scale-out、storage/model、front-end、management 各有不同传输和失败/延迟目标，不能一份通用 PFC/ECN/MTU 配方覆盖全部。共网时还需隔离、QoS、拥塞相互作用测试。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=7|PDF p.7]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=8|PDF p.8]]
- scheduler/router 向 fabric control plane 给出 placement/policy intent，网络回拓扑/health；快速 CC 仍在 NIC、switch、transport，不能把 SDN controller 放到每包快速环。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=11|PDF p.11]]

## 指标与条件
800G/1.6T-class 是参考接口等级，不是实测业务吞吐。p.9 柱状图明确写 illustrative、not benchmark results，不能读出均衡带来的提升倍数。p.13 要求 p99 behavior，但全篇无 p99 数字、模型、batch、上下文或硬件 BOM。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=6|PDF p.6]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=9|PDF p.9]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=13|PDF p.13]]

## 图表与架构
已看 p.3 四形态图、p.9 ECMP 示意与 p.10 router→prefill→KV→decode。p.10 强调 locality 影响但不单独决定传输成本：数据量、usable bandwidth、端点及争用都需测。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/ai-infra-inference-serving-shapes]] 提供面向推理加速器架构的决策与证据表；[[knowledge/concepts/ai-infra-multipath-failure-domains]] 解释路径分布为何影响 tail。

## 不确定性与待验证
Distributed Inference Fabric Profile 仍为 proposed contribution；不应称已批准 OCP 标准或通用商用品。分离是否提升吞吐/成本依赖 phase imbalance 与 KV 搬移代价，需用户真实模型与 SLA。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=10|PDF p.10]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=13|PDF p.13]]
