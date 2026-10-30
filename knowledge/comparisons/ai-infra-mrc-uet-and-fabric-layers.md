---
type: "comparison"
title: "MRC、UET、Virgo 与 Tahan：先分清比较层次"
tags: ["ai-infra", "inference-architecture"]
---

# MRC、UET、Virgo 与 Tahan：先分清比较层次

## 比较问题与口径
这些名词不是可直接按一个“带宽/延迟”榜单排序的产品：MRC/UET 是传输体系，Virgo 是 scale-out fabric 架构，Tahan 是 MTIA scale-up 交换系统。以下只比较来源实际陈述，不假装同负载 benchmark。

## MRC 与 UET 的明确差异
[[knowledge/sources/src-ba3c0b3882c6]] 的表（已视觉核对）称：UET 1.0 2025、libfabric（libibverbs soon）、clean slate、面向 AI/HPC；MRC 1.0 2026、libibverbs、RoCE 起点、面向 AI training。共有 packet spraying、OOO、traffic steering 与 SACK/NACK/timeout/trimming。[[ai-clusters/Demystifying MRC and UET- A Panel of Experts.pdf#page=3|PDF p.3]]
这反映演讲时点/圆桌简表，不替代规范版本与互通测试。

## 一处需要保留的“简表 vs 详细说明”差异
圆桌表把 MRC CC 写作 NSCC；专门 MRC 讲稿说规范标准化反馈信号，CC policy 可由实现选择，NSCC 是展示实现。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=9|PDF p.9]] 应解释为简表压缩上下文，而不是自动推断协议矛盾或唯一强制算法。

## 跨层并列，不作性能排名
- **MRC**：75K GPU 生产训练故障例，约 25% QPs affected；曲线证明一次 switch 故障事件中的短暂吞吐下降与恢复。没有 p99 请求延迟。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=12|PDF p.12]] [[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=13|PDF p.13]]
- **Virgo**：多 plane、两层、skinny links；公式 (N-1)/N 是单 plane 损失后的名义带宽，不是同一次 MRC 测试结果。[[ai-clusters/Co-Designing-AI-Fabrics-Inside-Google-s-Virgo-Network-and-the-Campus-as-a-Computer.pdf#page=7|PDF p.7]]
- **Tahan**：当前 16 加速器单跳 scale-up、6.4Tbps/accelerator/direction，<1µs switch hop 排除 NIC/PCIe/software。不是网络级 failover 或推理 SLA 数字。[[ai-clusters/Tahan-An-Open-Ethernet-Based-Scale-Up-Switch-for-Meta-s-MTIA-Accelerators.pdf#page=10|PDF p.10]] [[ai-clusters/Tahan-An-Open-Ethernet-Based-Scale-Up-Switch-for-Meta-s-MTIA-Accelerators.pdf#page=11|PDF p.11]]
- **Distributed inference profile**：要求 p99、burst/failure/多租户测试，但没有实测结果可加入性能排名。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=4|PDF p.4]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=13|PDF p.13]]

## 选择与下一步证据
先确定 scale-up/scale-out/scale-across 边界、软件 API 与现有 NIC，再比较 mandatory/optional features、拥塞策略、multi-vendor wire interoperability、故障域、生产尾延迟。硬件峰值无法替代 [[knowledge/concepts/ai-infra-inference-serving-shapes]] 的 SLA 选择。
