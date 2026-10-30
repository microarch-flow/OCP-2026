---
type: "concept"
title: "推理部署形态：以最小可行单元满足 SLA"
tags: ["ai-infra", "inference-architecture"]
---

# 推理部署形态：以最小可行单元满足 SLA

## 定义与证据
部署形态不等于技术成熟度。Standalone 要求模型与 KV 本地容纳；Replicated 通过独立副本承接更多请求；Distributed 把一个请求跨加速器域；Disaggregated 拆分 prefill/decode 等角色。来源 [[knowledge/sources/src-e3d51d9c0fe6]]，[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=3|PDF p.3]]。

## 架构决策顺序
1. 固定目标模型/量化、输入输出 token 分布、并发与 p99 TTFT/TPOT，然后测最小单元。
2. 独立请求可扩展时优先复制；模型容量或延迟确实要求时才分布。
3. 只有阶段不平衡收益覆盖 KV 搬移与调度复杂度时才分离。
4. 在突发、故障、多租户争用下验收，而非只测稳态平均 tokens/s。第 2–4 项依据 [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=4|PDF p.4]]；第 1 项具体指标为面向推理架构的本知识库操作化建议，不是原文已做的测试。

## 网络进入关键路径后发生什么
Tensor/expert/pipeline/KV 通信把网络方差传播成 token completion 方差。ECMP 有多条路不代表实际流量利用均匀；p.9 图仅说明热点机制，没有基准分数。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=5|PDF p.5]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=9|PDF p.9]]
Prefill/decode 分离不能自动提高吞吐；同 host/leaf/pod 的 locality 只是传输成本因素，还要量化 KV 字节数、usable BW、端点能力及争用。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=10|PDF p.10]]

## 共识、适用边界与未决问题
- 与 [[knowledge/concepts/ai-infra-multipath-failure-domains]] 的路径分布/故障隔离互补，但 MRC 训练 failover 结果不能替代推理 p99。
- 与 [[knowledge/concepts/ai-infra-observability-contract]] 结合：token tail 异常需追到 HBM/PCIe/scale-up 边界，而不是看“GPU util 低”即加网络。
- 源材料没有实际模型、TTFT/TPOT、p99、批量、功率、成本或每机 GPU 数。没有足够数据判定哪种形态最便宜。

## 应向供应商索取的最小证据
完整硬件 BOM/软件版本；固定 SLA 下可持续并发与 goodput；p50/p99 TTFT、TPOT 和失败率；prefill/decode 利用率与 KV 流量；链路故障/尾部拥塞下恢复；整机与网络功率；相同租期/利用率/折旧口径的成本。这是由来源原则导出的验收建议，不是本批材料已交付的结果。

## 从形态选择进入实证
[[knowledge/comparisons/ai-infra-performance-claim-evidence-matrix]]提供同SLO比较的配置检查表；跨站点PD需另读[[knowledge/concepts/ai-infra-scale-across-bdp-and-deadlines]]。
