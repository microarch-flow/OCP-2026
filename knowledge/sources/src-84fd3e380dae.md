---
id: "src-84fd3e380dae"
type: "source"
title: "Meta与AMD MetaRoCE：逐路径可靠性、接收端提示与64GPU集合通信"
source_path: "expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf"
source_git_blob_sha: "281888ba8dcd79951b8e7ac07feea4e87affcea8"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [8, 9, 10, 12, 13]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-multipath-behavior]]"]
---

# Meta与AMD MetaRoCE：逐路径可靠性、接收端提示与64GPU集合通信

## 核心结论
MetaRoCE将一个QP拆为多路径流，每路径可靠性/拥塞窗口，QP窗口为各PWND之和；接收端经任一路ACK反馈速率提示，以SACK容忍丢包/乱序，并保持completion顺序而非数据到达顺序。要求交换机ECN+ECMP，不要求trim、自适应路由或交换机遥测。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=4|PDF p.4]] [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=5|PDF p.5]] [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=6|PDF p.6]] [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=7|PDF p.7]]

## 关键证据、指标与条件
- p3目标/主张>90%网络效率，未定义负载和分母，不能当所有拓扑上限。明确反对按BDP增长的reorder buffer，但仍需ACK/SACK和completion状态，不能理解为无NIC内存开销。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=3|PDF p.3]] [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=5|PDF p.5]]
- AMD可编程NIC图分P4DMA TX/RX内存引擎、P4NET parser/deparser、packet buffer和800Gbps MAC。可编程架构支持协议迭代，不证明任意程序同时线速。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=8|PDF p.8]]
- 本地5–15µs RTT示例最大Cwnd约75、path约12；跨站1.5ms示意，Cwnd3500–7000、path30–50，以4K MTU packets表示并声称线速。图未给每路径/总窗口口径的完整解释及实际带宽时间序列，不将其乘积当精确SRAM需求。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=9|PDF p.9]]
- incast页仅画多sender→receiver并给每sender200Gbps rate hint，没有收敛时间、队列峰值或p99，不能证明远距离incast已经稳定。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=10|PDF p.10]]
- 关键p12图是**64GPU collective completion time相对RoCEv2的百分比差值**，不是绝对µs也不是p99。AllReduce多尺寸约降低数%–近30%；AllToAll既有约-30%改善，也有0B近+20%、1MB附近+15%等回退，大消息接近零且若干正值。故不能写成“MetaRoCE所有collective快30%”。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=12|PDF p.12]]

## 图表与架构
已核p8/9/10/12/13；开放规范、参考软件、compliance suite与vendor hardware形成反馈闭环。图展示期望生态组成，不等于所有供应商已经互通。[[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=13|PDF p.13]] [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf#page=14|PDF p.14]]

## 关联与比较
[[knowledge/concepts/network-multipath-behavior]] 与 [[knowledge/concepts/network-executable-validation]]。本文件补充AMD硬件和64GPU性能；与原MetaRoCE软件deck同项目数据，不当独立第三方验证。

## 不确定性与待验证
图没有消息大小对应的重复次数、统计量、RoCEv2 CC参数、PFC状态、GPU/NIC/拓扑配置。推理验收应覆盖MoE AllToAll大小分布、prefill/decode混合、慢接收者、链路失效后的完成尾部，而不是只挑最好柱子。

