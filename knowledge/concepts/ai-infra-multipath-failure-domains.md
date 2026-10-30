---
type: "concept"
title: "多路径与多平面：吞吐利用率和故障域不是同一件事"
tags: ["ai-infra", "inference-architecture"]
---

# 多路径与多平面：吞吐利用率和故障域不是同一件事

## 定义
Multipath 是路由多样性；multiplane 是端口和故障域多样性。单 QP packet spraying 让应用不必自己建立多条独立连接，但 NIC 必须管理乱序、有序完成、选择性重传和拥塞反馈。[[knowledge/sources/src-76146cb07840]]，[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=3|PDF p.3]] [[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=5|PDF p.5]]

## 跨层证据
- MRC：Entropy Value 标识/选择路径；故障后排除 EV，保留连接；SRv6 去除对网络路由收敛的端点依赖。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=6|PDF p.6]] [[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=10|PDF p.10]]
- Virgo：两层独立 planes 与 skinny links，单 plane down 时名义带宽留 (N-1)/N。[[knowledge/sources/src-3783a6289a84]]，[[ai-clusters/Co-Designing-AI-Fabrics-Inside-Google-s-Virgo-Network-and-the-Campus-as-a-Computer.pdf#page=6|PDF p.6]] [[ai-clusters/Co-Designing-AI-Fabrics-Inside-Google-s-Virgo-Network-and-the-Campus-as-a-Computer.pdf#page=7|PDF p.7]]
- 推理：可用路径没有被真实流量使用时，热点仍会放大同步完成时间尾部。[[knowledge/sources/src-e3d51d9c0fe6]]，[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=9|PDF p.9]]

## 必须守住的比较口径
(N-1)/N 是等容量 plane 的理论残余容量，不是 SLA goodput；MRC 的 75K GPU 训练案例展示 switch failure 下不中止训练，不提供推理请求 p99。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=12|PDF p.12]] [[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=13|PDF p.13]]
MPR=8 packets 是协议示意；实际窗口应结合 RTT/BDP、重排跨度与 NIC 资源评估，材料不披露具体产品配置。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=7|PDF p.7]]

## 协议与实现边界
MRC 标准化反馈，不强制唯一 CC；NSCC 是所展示实现。把可选 trimming/probe 当 mandatory 会高估跨产品共同能力。[[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=8|PDF p.8]] [[ai-clusters/Enabling-AI-Networking-Scale-with-Multi-path-Reliable-Connections-MRC.pdf#page=9|PDF p.9]]
参见 [[knowledge/comparisons/ai-infra-mrc-uet-and-fabric-layers]]。

## 对推理加速器的验收建议（综合推论）
把真实请求/collective 流量映射到 per-plane/per-path 利用率；分别注入 link down、link flap、switch blackhole、plane loss；记录 p99、goodput、重传、收敛和 NIC memory pressure，避免只看链路恢复。

## 未决问题
等价 multipath 是否共享电源/冷却/控制器？失效 detector 假阳性是否导致路径抖动？剩余 plane 是否被跨租户流量挤占？这些问题不能由 topology 图本身回答。
