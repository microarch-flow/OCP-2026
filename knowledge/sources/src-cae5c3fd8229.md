---
id: "src-cae5c3fd8229"
type: "source"
title: "Nokia／Lightstorm：跨域推理网络的 KV 传输预算与开放试验计划"
source_path: "executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf"
source_git_blob_sha: "602550739a0491877e1e2629c506e7110caae891"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [8, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [10, 11, 12]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-inference-sla]]", "[[knowledge/concepts/executive-expo-kv-data-plane]]"]
---

# Nokia／Lightstorm：跨域推理网络的 KV 传输预算与开放试验计划

## 核心结论
资料把 scale-beyond 定义为跨域分布式推理，最有价值的是把网络需求与 KV 体积、TTFT 预算相连；它展示的是**解析模型和计划试验**，不是“推理永远比训练需要 429 倍带宽”的实测定律。[[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=8|PDF p.8]][[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=11|PDF p.11]][[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=12|PDF p.12]]

## 关键证据
- CIR 定义为每 FLOP 可搬运的字节，以 mB/F 表示。表中 H100 使用 989 TFLOPS dense BF16 基线：HBM 3.39、NVLink 0.910、scale-out 0.006–0.050、传统 1–10 GbE WAN 0.0000158–0.000158。它依赖链路类别及超售，不是所有现网的固有比例。[[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=10|PDF p.10]]
- 70B、MHA、4K 上下文示例在 40 ms 内移动 10.74 GB KV，推得 2,147 Gbps；训练侧 5 Gbps 明确是**假设而非测量**，429× 是两者比值。模型排除了传播时延。[[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=11|PDF p.11]]
- 同页 GQA 仅 1/8 KV heads 时变为 268 Gbps，latent attention 约 58 Gbps，说明注意力结构改变网络瓶颈。[[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=11|PDF p.11]]

## 指标与条件
40 ms 若同时作为端到端 TTFT 目标，就不能全部分配给搬运；计算、排队、传播和协议开销必须另留预算。不能把该示例外推为所有推理场景的强制链路规格。

## 图表与架构
p.12 计划在印度三站点、真实波长与 RDMA 类流量下测量开通时间、保护切换时延分位、多租户隔离、单位成本、TTFT/GPU 利用率以及 transfer-versus-recompute 临界点，试验窗口为演讲所述 2026 年末，尚未给结果。[[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=12|PDF p.12]]

## 关联与比较
应与机柜内 CXL/RDMA KV 池和区域 scale-across 联读：共同问题不是带宽越大越好，而是在同一 SLA 下选择 KV 复用、传输还是重算。

## 不确定性与待验证
缺少公开试验结果、故障情景、尾时延与成本曲线；所引外部论文尚未在本卡独立复核。

## 知识网络
[[knowledge/concepts/executive-expo-inference-sla]] · [[knowledge/concepts/executive-expo-kv-data-plane]]
