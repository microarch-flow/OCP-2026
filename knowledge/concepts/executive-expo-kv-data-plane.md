---
type: concept
title: "KV 缓存是活动数据通路：容量、复用域与搬运预算"
tags: [ocp2026, executive-expo]
---

# KV 缓存是活动数据通路：容量、复用域与搬运预算

## 定义
KV缓存属于推理中的可复用模型状态，不等同于模型权重或普通冷存储。**跨源归纳**：放置决策应同时考虑容量、热度、复用可见域、搬运时间、精度与版本兼容，而非只按每GB价格排序。

## 来源与页级证据
- Hyve提出HBM热状态→DDR/CXL温状态→NVMe溢出/复用→对象/HDD冷数据，但其约65%三年TCO下降明确为示意模型。[[knowledge/sources/src-73c5e6030f9f]] [[executive-sessions/42_Open, Modular Rack-Scale AI Infrastructure for the Agentic Era present.pdf#page=9|PDF p.9]] [[executive-sessions/42_Open, Modular Rack-Scale AI Infrastructure for the Agentic Era present.pdf#page=14|PDF p.14]]
- MARS使用机柜内CXL、跨机柜RDMA扩展共享域；表中重算、SSD、CXL-DDR与Hybrid的TTFT平均/尾值各不相同，且尾分位未定义。[[knowledge/sources/src-2f5c553a1e78]] [[executive-sessions/33_Introduction to Memory-centric AI Rack Systems (MARS) presented by SK .pdf#page=7|PDF p.7]] [[executive-sessions/33_Introduction to Memory-centric AI Rack Systems (MARS) presented by SK .pdf#page=10|PDF p.10]]
- Solidigm/Metrum共享池实验把四副本中原本需要重算的后续请求变成读KV；99K-token、并发1时p50 TTFT18.38→2.20 s。[[knowledge/sources/src-2d7659491efb]] [[executive-sessions/54_The New Tokenomics How Data Infrastructure Increasingly Sets AI ROI pr.pdf#page=10|PDF p.10]]
- Lightstorm的70B MHA/4K/40 ms搬运示例推得2147 Gbps，但GQA和latent attention分别降至268和约58 Gbps；传播时延被排除。[[knowledge/sources/src-cae5c3fd8229]] [[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=11|PDF p.11]]

## 共识与分歧
1. **介质速度与服务速度不同**：共享SSD比GPU-only方案更早出首token，可能因为避免了重算，并非SSD比HBM访问更快。
2. **共享不是免费**：复用域扩大增加网络负载、缓存索引/一致性、访问控制与失败恢复责任。
3. **容量与活跃并发不同**：Hyve公式若输出字节需乘每元素字节数，80GB预算也未必全部可给KV。[[executive-sessions/42_Open, Modular Rack-Scale AI Infrastructure for the Agentic Era present.pdf#page=7|PDF p.7]]
4. 压缩要考虑精度和CPU：Solidigm4-bit测试恢复延迟+9.6%、host CPU约2.5×；其3-bit预设质量分下降。[[executive-sessions/54_The New Tokenomics How Data Infrastructure Increasingly Sets AI ROI pr.pdf#page=13|PDF p.13]]

## 适用条件：搬运还是重算
一个最低限度的工程判断是：`索引/排队 + 有效字节数/实测带宽 + RTT/协议 + 恢复/反量化`是否小于重算时间，并且均落在剩余TTFT预算内。对于逐token拉取的数据，还须验证TPOT，而不是只验首token。公式为综合推导，不是来源的统一性能模型。

命中率、请求前缀兼容、模型/精度/位置编码版本、租户隔离、缓存逐出策略都应成为测试输入。给每层写入明确责任：谁拥有状态、何时失效、丢失后是重算还是失败。

## 未决问题
跨站点方案最缺真实尾时延/故障结果；机柜内方案最缺相同请求集的高并发比较。还需SSD写入寿命与缓存污染成本，不能只看一次warm-hit演示。

## 继续阅读
[[knowledge/sources/src-f1226a6f9088|PCIe6／CXL KV收益]] · [[knowledge/sources/src-70e790b097b6|存储人格与KV数据]] · [[knowledge/comparisons/executive-expo-inference-evidence-matrix]]
