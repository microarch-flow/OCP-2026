---
type: concept
title: "Chiplet 链路：有效带宽、粒度与尾延迟"
tags: [ocp2026, concept, compute-memory]
---

# Chiplet 链路：有效带宽、粒度与尾延迟

## 核心判断
不要只用 PHY 的 bits/s 衡量 chiplet 间数据流。TLP 结构、LLP 粒度、packing、credit round-trip 与 QoS 会共同决定小消息、bulk tensor、控制流的实际成本。

## 来源与成熟度
主要证据：[[knowledge/sources/src-67f753f38451|OCE TLL 2.0 规格更新]]。生态背景：[[knowledge/sources/src-bf15b5b79b9c|OCE 2026 进展]]。这里没有硅后测量数据，下面是协议结构模型。

## 分解模型（本库推导）
`有效带宽 = PHY raw rate × 编码效率 × 帧/包载荷比例 × 有效利用率`。

必须避免重复计算：BoW.FLEXI binding 使用自己的 header/ECC，不能再叠加普通 LLP 开销。对于传统 24-granule LLP，仅 header 的理想载荷比例为 23/24；16-granule 为 15/16。这两个比例尚未包含 transaction header、ECC、padding、空闲和拥塞。

| 参数 | 为什么必须显式化 |
|---|---|
| Variant + Profile + PHY binding | 同一个“支持 UCIe/BoW”不定义完整事务语义 |
| Packet/granule bytes、packing | 小消息的 header 比例与大块 tensor 不同 |
| LLP 长度 | 长包摊薄 header，但串行化/凑包可能增加尾延迟 |
| Credit 返回延迟、buffer 深度 | 影响可维持的在途字节数和反压 |
| Traffic classes、arbitration | Control/KV metadata 不能默认与 bulk DMA 公平共享 |
| Error/retry model | 低 BER 下均值好看不代表错误恢复时 p99 可接受 |

## 面向 架构探索 DSL/IR 的实验建议
将同一数据流分别映射为 bulk、细粒度 load/store、控制消息，保持 raw rate 不变，只改变 packetization/credit/QoS；报告有效 GB/s、排队与传输分项、p50/p99、buffer 占用。先验证 profile-level 模型，再讨论跨 chiplet 数据流切分。

## 尚不能回答
哪种 PHY 的 pJ/bit 或端到端 ns 最优；材料不足，不能从 2.0 header 缩小推导整机能效提升百分比。
