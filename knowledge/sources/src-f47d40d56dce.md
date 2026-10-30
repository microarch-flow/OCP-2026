---
id: "src-f47d40d56dce"
type: "source"
title: "Scaling AI：设计到部署的连续验证"
source_path: "executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf"
source_git_blob_sha: "6bbed5cdaa971c8c1b9bed53ab8a4567e2de319e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-text"
evidence_pages: [3, 6, 8, 9, 10, 11, 12, 13]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-inference-sla]]", "[[knowledge/concepts/executive-expo-system-control-evidence]]"]
---

# Scaling AI：设计到部署的连续验证

## 核心结论
- Keysight 认为同步 AI fabric 受最弱链路与尾延迟支配，因此应从 reference model/RTL 到 rack 一直用系统剩余部分的仿真或仿真器来验证局部组件。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=3|PDF p.3]][[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=6|PDF p.6]][[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=13|PDF p.13]]
- 对推理加速器商业化，早期系统验证可用于暴露真实通信/内存/SLO 瓶颈；这是方法论建议，不是证明某工具能准确预测生产性能。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=8|PDF p.8]][[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=12|PDF p.12]]
## 关键证据
- 三个连续性要求：上游结果复用、共同模型、统一合规/benchmark；集成后不是重新定义通过标准。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=6|PDF p.6]][[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=11|PDF p.11]]
- KAI 将 protocols、transport、collectives、workloads 放入 emulation，列示 400G/800G scale-up 连接。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=9|PDF p.9]][[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=10|PDF p.10]]
## 指标与条件
- 本文没有给模型准确度、验证耗时下降、漏检率或客户收益的量化实验。
- 医疗/法律/金融分别强调内存、上下文、低延迟是讲者的概括；实际工作负载不能直接按行业名称固定归类。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=12|PDF p.12]]
## 图表与架构
全文文字已阅读；未对 p.8-13 架构图做视觉核对，不依赖箭头空间关系写拓扑结论。文字层支持 reference model→RTL→ASIC→blade→rack 的阶段划分。[[executive-sessions/06_AI Infrastructure validation at scale presented by Keysight.pdf#page=8|PDF p.8]]
## 关联与比较
验证应沿 workload→服务指标→协议行为→物理链路逐层收敛；同一模型和 workload trace 能帮助比较不同 accelerator/rack 方案，而非仅比 FLOPS。
## 不确定性与待验证
需获得 emulation 与真机结果误差、拥塞/故障注入覆盖、随机种子及尾延迟置信区间；共用 pass/fail 不自动保证覆盖完整。

## 知识网络
[[knowledge/concepts/executive-expo-inference-sla]] · [[knowledge/concepts/executive-expo-system-control-evidence]]
