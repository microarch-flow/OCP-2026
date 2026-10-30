---
id: "src-9e4b624fe6f8"
type: "source"
title: "d-Matrix：SRAM／3D DRAM 推理与三种异构解耦边界"
source_path: "executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf"
source_git_blob_sha: "3d966787d3433129a34a79fd929d20dac540ec0d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 25
review_status: "analyzed-visual"
evidence_pages: [8, 9, 11, 12, 14, 15, 17, 19, 20, 22, 23, 24]
text_reviewed: true
key_pages_visual_checked: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-inference-sla]]"]
---

# d-Matrix：SRAM／3D DRAM 推理与三种异构解耦边界

## 核心结论
d-Matrix展示三种不同异构分工：draft/verify、attention/FFN、prefill/decode；它们的网络往返频率、传输状态和收益条件不同。公司宣称Corsair GA，但Raptor/Lightning相关段落属于下一代路线，不能合并为当前部署性能。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=9|PDF p.9]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=12|PDF p.12]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=17|PDF p.17]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=20|PDF p.20]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=23|PDF p.23]]

## 关键证据
- Corsair示意每chiplet4个quad、256 MB SRAM；Squadron宣称最多16个SquadRack/1,024个XPU，首套在Arizona用于内部研发，不能据此认定大规模客户量产。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=11|PDF p.11]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=14|PDF p.14]]
- AFD把attention留GPU、FFN/MoE移至Corsair，逐token经低延迟Ethernet/JetStream交换中间activation。页面列845 token/s/user及64并发20,145 token/s。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=15|PDF p.15]]
- Raptor示意N4计算die与定制3D DRAM面对面互连；NVLink Fusion机柜规格144 XPU、2.3 TB容量、7.2 PB/s内存带宽、18计算托盘/9交换托盘。128 XPU ESUN机柜明确“under development”。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=17|PDF p.17]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=19|PDF p.19]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=20|PDF p.20]]
- Lightning图示四层3D DRAM，100B/3T/20T模型级别为路线图分类，未给精度、总/激活参数或实际部署结果。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=22|PDF p.22]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=23|PDF p.23]]

## 指标与条件
**845×64=54,080，并非20,145。** 同页没有解释是否不同负载点；64并发总吞吐平均约315 token/s/user。因此不应写成“64用户每个845”。p.9的3×/7×/10×交互性也无模型、精度、上下文、基线与SLA，属于未充分限定的厂商主张。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=15|PDF p.15]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=9|PDF p.9]]

## 图表与架构
已逐页视觉核查：p.8吞吐/kW—交互性曲线没有数值刻度，是定位示意；p.13为装饰图，不作为技术证据。p.17显示N4，而p.24“6 nm、无HBM/CoWoS”的供应链口号不可无差别外推所有下一代产品。[[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=8|PDF p.8]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=17|PDF p.17]][[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=24|PDF p.24]]

## 关联与比较
与OpenAI负载拆解、网络模拟和内存分层联读：能否在真实SLA下降低总成本，取决于跨设备activation/KV搬运、负载均衡、精度支持、编译迁移和故障恢复，而非局部SRAM带宽。

## 不确定性与待验证
需要AFD模型与并发曲线、端到端TTFT/TPOT分位、功率计量边界、算子覆盖和失败恢复。GA/合作公告不等于独立验证的商业部署；“No Latency”是宣传语而非物理零延迟。

## 知识网络
[[knowledge/concepts/executive-expo-inference-sla]]
