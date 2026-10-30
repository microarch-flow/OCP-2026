---
id: "expo-inference-cost-contract"
type: "comparison"
title: "从CPU到异构AFD：先统一推理SLO，再比较成本与通信"
tags: ["ocp2026", "expo-hall"]
review_status: "synthesized"
---

# 从CPU到异构AFD：先统一推理SLO，再比较成本与通信

## 问题与结论
本组展台材料有CPU会话容量、CPU batch吞吐、GPU每美元宣传和异构AFD演示；它们都可能有价值，但不是同一个benchmark。商业问题应是“在指定质量与尾延迟下，每个成功请求/合格token的成本”，不是谁的最大tokens/s数字更大。

## 不可直接比较的四个证据
- Intel router用固定445ms p95下会话数量，并讨论AMX和core scaling；它适合说明控制/路由类任务选择，不等同完整大模型decode每token p99。[[knowledge/sources/src-86e4ca03d02c]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=8|PDF p.8]]
- MONAKA的gpt-oss20B307token/s、batch2、无GPU参考平台，没有说明总吞吐还是单序列，也无墙插功率/上下文长度。[[knowledge/sources/src-7fda851035fa]] [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=8|PDF p.8]]
- MiTAC/AMD MI350P最高4.2×tokens/s/$缺本文件内的测试附注和价格基线；260B FP4“能放下”不证明规定延迟下“能服务”。[[knowledge/sources/src-e3c54df076ca]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=12|PDF p.12]]
- d-Matrix AFD给1H100+8Corsair、GPT-OSS20B、batch1与24次往返/token；845tokens/s/user和64并发总20,145tokens/s不能同时当成845×64，后者均摊约314.8。缺请求长度、p99、功率和量化质量。[[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=17|PDF p.17]]

## 异构分解的决策契约
Attention/FFN、draft/verify、prefill/decode分解应分别建立：驻留权重/KV容量、跨边界字节数、每token往返次数、batch形状、EP skew、传输队列/拥塞和重试。d-Matrix图明确不同拆分，并把TP留节点内、跨节点PP/EP；它是具体映射约束，不是“所有并行随意跨任何传输”。[[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=11|PDF p.11]] [[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=16|PDF p.16]]

一个粗略规划式是 `通信项 ≈ N_roundtrip × L_effective + serialized_bytes / B_effective`，这里只是忽略重叠的粗略建模模板，并非严格上界，不能直接代替有overlap、并行rail与调度的实测。JetStream2µs未给单程/往返及测量边界，不能直接乘24宣布总AFD耗时。[[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=6|PDF p.6]] [[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=17|PDF p.17]]

“统一Push Mode”尚未公开completion/fence/ordering/credit/retry契约；端点发送完成、远端可见、graph可推进是不同条件。PCIe semantics over Ethernet也不能自动推导全局coherence。应把跨rail同步和故障后幂等测试纳入软件验收，而不是只测链路线速。[[knowledge/sources/src-92d1f86e9495]] [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf#page=7|PDF p.7]]

## 缓存让成本边界更大，而非更简单
FADU提议可重算KV层避免RAID/EC以减通路/容量成本；但缓存丢失会改变GPU利用率与TTFT，并可能同时影响许多请求。应将重算风暴与恢复p99计入成本，而不只算usableGB/year。[[knowledge/sources/src-62274aac9546]] [[expo-hall-sessions/The-Changing-Course-of-Storage-in-an-AI-World-presented-by-FADU.pdf#page=9|PDF p.9]] [[knowledge/sources/src-62274aac9546]] [[expo-hall-sessions/The-Changing-Course-of-Storage-in-an-AI-World-presented-by-FADU.pdf#page=11|PDF p.11]]

## 可执行的对照实验（本库归纳）
锁定模型/质量门槛、软件版本、上下文及输出长度分布和到达过程；在一系列并发下同时报成功请求/s、有效输出token/s、TTFT/TPOT的p50/p95/p99、拒绝率、墙插与冷却能量。然后加入故障/恢复、缓存冷热、长上下文与EP倾斜。分别列CAPEX摊销、能耗、网络/存储、软件运维，不将芯片TDP当整机耗电。

关联：[[knowledge/concepts/network-inference-acceptance]]、[[knowledge/concepts/network-scaleup-ethernet]]、[[knowledge/comparisons/expo-thermal-performance-contract]]。目前不能从这些演讲得出CPU、GPU或专用加速器的通用成本赢家。

