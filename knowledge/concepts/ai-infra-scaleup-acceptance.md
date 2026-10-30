---
type: "concept"
title: "Scale-up 验收：从 SI 合格到 collective 与业务 SLA"
tags: ["ai-infra", "inference-architecture"]
---

# Scale-up 验收：从 SI 合格到 collective 与业务 SLA

## 定义与来源
Scale-up 验收需要四个不同证据层：电气信道 → sustained traffic → collectives → 业务 SLA。[[knowledge/sources/src-79e676213ada]]，[[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=3|PDF p.3]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=5|PDF p.5]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=6|PDF p.6]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=7|PDF p.7]]；最后一层的推理 SLA 是本知识库结合 [[knowledge/sources/src-e3d51d9c0fe6]] 的扩展，不是铜互连演讲已完成的测试。

## 为什么线速和 PRBS 都不够
低 BER 的 PRBS 不覆盖运行时 PI、串扰、热漂移、重传与拥塞。失效边缘链路继续承载流量，会在 ring all-reduce 中放大为 straggler；明确 down 的 plane 反而可能更容易隔离。[[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=4|PDF p.4]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=5|PDF p.5]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=7|PDF p.7]]
需要每 lane 向量与 FEC histogram，不只一个 BER；需要 operation×message-size×scale×algorithm 矩阵，不只最大包的一个带宽点。

## 以 Tahan 为例划清指标边界
[[knowledge/sources/src-d29c84030e6a]] 当前 16 accelerator 域给出 6.4Tbps/accelerator/**direction**，4 switches、一跳；<1µs 是 switch hop 的 fabric-path 指标，排除 NIC/PCIe/software。[[ai-clusters/Tahan-An-Open-Ethernet-Based-Scale-Up-Switch-for-Meta-s-MTIA-Accelerators.pdf#page=10|PDF p.10]] [[ai-clusters/Tahan-An-Open-Ethernet-Based-Scale-Up-Switch-for-Meta-s-MTIA-Accelerators.pdf#page=11|PDF p.11]]
下一代 72 accelerator、9.6Tbps/direction 属 roadmap；cut-through -25% 仍 under exploration。不得把它们合成为当前产品已经交付的端到端延迟。[[ai-clusters/Tahan-An-Open-Ethernet-Based-Scale-Up-Switch-for-Meta-s-MTIA-Accelerators.pdf#page=14|PDF p.14]]

## 推荐验收矩阵（综合推论）
- SI：lane 位置、温度、老化/插拔、pre/post-FEC BER、burst error histogram。
- Traffic：满载多源多目的、真实消息大小、flow control 与拥塞、telemetry on/off。
- 故障：黑洞/断链/flap、检测和恢复时间、保留带宽、错误归因。
- CCL：all-reduce/all-gather/all-to-all 等实际算子与算法拐点。
- 推理：固定模型/上下文/batch/并发下 p99 TTFT/TPOT、失败率和功率成本。

## 证据成熟度与缺口
铜验证文档 p.11 保留 `[to be populated]`，不可当成完整 root-cause case study；conformance suite 仍为倡议，阈值尚未统一。[[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=8|PDF p.8]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=11|PDF p.11]]
[[knowledge/concepts/ai-infra-observability-contract]] 是诊断和自动验收的必要输入，不等于已经给出业务 SLA 保证。
