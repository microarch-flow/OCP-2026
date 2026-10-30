---
id: "src-ba3d7c6e0541"
type: "source"
title: "Accelerate your AI journey with QCT：从系统到 AI Factory"
source_path: "executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf"
source_git_blob_sha: "5b2c34d7bdff2b427fe63f8d554e62bfa5b029c9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 23
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 21]
text_reviewed: true
key_pages_visual_checked: [1, 11, 14]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-power-control-boundaries]]", "[[knowledge/concepts/executive-expo-manufacturing-service-chain]]"]
---

# Accelerate your AI journey with QCT：从系统到 AI Factory

## 核心结论
- QCT 将优化分成 POD 级工作负载匹配和设施级电力/冷却优化；token 效率不应只以 GPU 芯片能效衡量。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=6|PDF p.6]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=21|PDF p.21]]
- 材料提出以数字孪生连接设计、施工、交付和运行反馈；它提供工作流架构而非误差已验证的设施预测模型。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=13|PDF p.13]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=14|PDF p.14]]
## 关键证据
- Vera CPU rack 面向 agent 执行，STX 面向上下文/KV cache，另列 GPU、低延迟推理与网络平台；这些是厂商组合定位，不能视为同等成熟度的独立基准。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=7|PDF p.7]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=9|PDF p.9]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=10|PDF p.10]]
- 同时提供 NVIDIA 全栈 AI Factory 与异构系统路线；后者按推理、微调、训练选择 POD。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=16|PDF p.16]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=17|PDF p.17]]
## 指标与条件
- GB200 NVL72 峰值运行示意的设施电力分配：GPU 41%、其他服务器部件 22%、网络及其他 IT 8%、冷却/设施 29%；图源标为 Epoch AI，不是 QCT 现场测量。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=11|PDF p.11]]
- Vera CPU rack 标称支持 22,500+ 并行 CPU 环境，缺少环境资源配额、负载和延迟条件，不能解释为并行模型请求吞吐量。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=9|PDF p.9]]
- 全球电力缺口和 token 总量为引用数据/预测，未在本笔记作为真实可售算力推导依据。[[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=4|PDF p.4]][[executive-sessions/04_Accelerate your AI journey with QCT From system-level to AI Factory pr.pdf#page=5|PDF p.5]]
## 图表与架构
已视觉核对 p.1、11、14：实际封面标题与数字孪生双向数据流确认；没有把“持续改善”箭头解读为已上线自治控制。
## 关联与比较
本源补充设施端分母，推理 accelerator 选型则需同时看上下文缓存、CPU 工具执行、网络和 SLO；在固定 MW 下优化可交付服务，而非单器件峰值。
## 不确定性与待验证
没有具名客户配置、部署规模、每 token 成本或数字孪生与实测误差。产品支持和生态合作不能充当已验收市场部署证据。

## 知识网络
[[knowledge/concepts/executive-expo-power-control-boundaries]] · [[knowledge/concepts/executive-expo-manufacturing-service-chain]]
