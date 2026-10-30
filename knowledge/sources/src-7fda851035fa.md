---
id: "src-7fda851035fa"
type: "source"
title: "Fujitsu MONAKA：CPU推理数值、3D芯粒与上市路线的口径"
source_path: "expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf"
source_git_blob_sha: "608e6bcfd4496f594d95b6c4f4942e655fa088aa"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8, 9, 11]
text_reviewed: true
key_pages_visual_checked: [5, 8, 11]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# Fujitsu MONAKA：CPU推理数值、3D芯粒与上市路线的口径

## 核心结论
MONAKA面向通用AI/cloud/HPC，把2nm计算die与5nm SRAM/IO die做3D集成，主张超低压能效；提供无GPU参考平台推理吞吐，但没有功率与尾延迟，不能仅凭token/s证明能效优于GPU或其他CPU。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=5|PDF p.5]] [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=6|PDF p.6]] [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=8|PDF p.8]]

## 关键证据、指标与条件
- Armv9.3-A、SVE2-256，144核/socket、双路288核，DDR5 12ch 8800MT/s、96lane PCIe6/CXL3.0，风冷/液冷可选。规范subject to change，未给cache容量及实测内存带宽。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=5|PDF p.5]]
- 安全称每VM内存密钥、CPU RoT、remote attestation及4096个保密VM支持；没有证明4096并发实例在该推理吞吐下运行。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=7|PDF p.7]]
- p8明确gpt-oss-20B **307.0 token/s**、Gemma4-31B **55.2 token/s**，均batch2、MONAKA reference platform无GPU；213.8TOPS是INT8峰值。没有说明token/s为合计还是每序列、prefill还是decode，也缺模型量化/上下文/输出长度和测量socket数，不能直接与INT8峰值相除求利用率。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=8|PDF p.8]]
- p9说参考平台现可评估、全球处理器销售2026年11月开始；p11路线又把MONAKA放2027，后续MONAKA-X 1.4nm/SME2/NVLink Fusion在2029。保留时间口径差异，不能直接写已量产上市。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=9|PDF p.9]] [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=11|PDF p.11]]

## 图表与架构
已看p5/8/11。p6半导体功耗趋势明确Fujitsu estimation，未给数轴；A64FX/Fugaku数百万核历史证明既有系统经验，不是MONAKA同规模可靠性记录。[[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=3|PDF p.3]] [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf#page=6|PDF p.6]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：Intel router固定p95会话与MONAKA batch2 token/s、Arm参考设计2×宣传三者测量对象不同，不作简单CPU排名。

## 不确定性与待验证
需模型/软件版本、实际功率、内存容量、TTFT/TPOT p99、精度与成本、上市料号及固件生态验证；材料中的模型/产品状态仅按来源记录，未外部验证。


跨源比较：[[knowledge/comparisons/expo-inference-cost-contract]]。
