---
id: "src-bb504cebac57"
type: "source"
title: "Hardware Mitigations for AI-ML Workloads Power Fluctuation"
source_path: "ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf"
source_git_blob_sha: "b8bc721a7f5abda809699bcdc7a4364712ae88e7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 11]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [6, 8]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# Hardware Mitigations for AI-ML Workloads Power Fluctuation

## 核心结论
Google 提出 chip/rack、row/sidecar、facility 三层储能，分别吸收快速负载、bridging/peak shaving 和较长 backup/grid support。设计难点在 PSU/CBU/BBU 共 DC bus 下的控制协同与循环寿命，不只是增加电池容量。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=6|PDF p.6]] [[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=7|PDF p.7]] [[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=8|PDF p.8]]

## 关键证据
同步 AI 负载造成机架和设施 di/dt；软件 smoothing/power cap 是互补工具，硬件缓冲意图避免直接限制 compute。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=3|PDF p.3]] [[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=5|PDF p.5]] CBU 处理动态、BBU 通常留到 AC failure，统一 I-share 控制应避免回路振荡。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=7|PDF p.7]]

## 指标与条件
- 约百万次/年 ML cycles、LFP 约3k–10k cycles、hybrid supercap 4–5× EDLC 能量密度是演讲级概括，未定义 DoD、温度、寿命失效标准或具体电芯。不能据此作供应商合格判定。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=9|PDF p.9]]
- 10年、100M+ cycles 是“industry product concepts”的目标，非已验证寿命。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=10|PDF p.10]]
- “zero performance penalty”是硬件 smoothing 的价值主张，缺实际 workload/BW/p99/功耗对照，不能当测得零开销。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=5|PDF p.5]]
- 20MW/min 是 utility ramp-rate **示例**；不当成普遍适用限值或法规结论。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=4|PDF p.4]]

## 图表与架构
已看 p.6 三层及 p.8 seconds/minutes/hours+。这些是功能/时间尺度分类，并不给出电容、电池、变流器的 sizing equation 或跨层稳定性证明。

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]；[[knowledge/concepts/ai-infra-deployment-readiness]]。推理 SLA/TCO 应把软限功率的 tail penalty 与硬储能的资本/损耗/寿命一起评估，不把“不限频”误当整体系统零成本。

## 不确定性与待验证
HV hybrid battery/supercap 标准贡献计划为未来2–3季度；无明确提交日期、能量/功率配置、效率、热设计、控制稳定裕量、价格与安全认证。[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=11|PDF p.11]]
