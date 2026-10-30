---
id: "src-b162bcec7dc8"
type: "source"
title: "Security of Multi-chip ICs & Security Chiplets with Caliptra: Building a Hardware Root of Trust"
aliases: ["Security of Multi-chip ICs & Security Chiplets with Caliptra: Building a Hardware Root of Trust"]
speakers: "Matt Holdrege — Fellow, Microchip Technology"
source_path: "Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf"
source_git_blob_sha: "aabbe7362df549f4e9fe4572e8056ea8ae50a3c5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [10]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-federated-model-contract]]", "[[knowledge/concepts/compute-memory-cxl-failure-domain]]"]
---

# Security of Multi-chip ICs & Security Chiplets with Caliptra: Building a Hardware Root of Trust

## 核心结论
多供应商 chiplet 的 trust boundary 跨越 die、封装和生命周期。**Caliptra/UDS/DICE 提供 identity、measurement 与密钥根基础，但不能替代整个 package 的授权、保护传输、监测与恢复设计。** 本材料是架构/安全需求讲解，不是已完成的产品安全评测。

## 关键证据
- 需求覆盖 provenance、secure/measured boot、D2D channel protection、provisioning/key management、update/lifecycle、telemetry、traceability 与 IP protection。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=2|PDF p.2]]
- Measured boot 用密码学 hash 记录并证明装载的 firmware/configuration；UDS 建立 silicon root，DICE 用 secret 与下一启动组件 measurement 分层派生 identity/chain。**身份是谁与当前运行什么状态是不同问题**。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=3|PDF p.3]] [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=7|PDF p.7]]
- efuse/shadow register 用于配置、die ID、生命周期/security flags 和 anti-rollback；这不是把明文密钥暴露给所有 chiplet 的建议。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=4|PDF p.4]]
- D2D 保护目标包括 confidentiality、integrity、freshness、availability，并要求定义 initialization/reset/power transition/retry/error 的安全行为。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=5|PDF p.5]]
- 讲者提醒：UCIe 的安全能力需正确配置与验证；BoW 主要定义 PHY，encryption/authentication/access-control/lifecycle 仍需上层或实现机制。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=6|PDF p.6]]
- 两 chiplet 启动示例：primary 管全局启动策略与健康状态；secondary 仍有 local security boundary；双方 RoT/sub-RoT 相互认证身份与固件完整性后继续。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=11|PDF p.11]]

## 指标与条件
没有 crypto throughput、link protection latency、面积/功耗或 boot-time 开销。p.12 提及 UCIe 3.0 的 security/management 特性，p.13 引用 FCSA 1.1 chapter 9；仅记录讲者引用，不把此演讲当规范细节或合规证明。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=12|PDF p.12]] [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=13|PDF p.13]]

## 图表与架构
已视觉核对 p.10：hub-and-spoke、shared bus、daisy-chain 三种 topology 下显示 bound inter-chiplet security domain。拓扑决定通信路径，不自动决定信任边界；经过中间 die 的连接仍需定义端点/中间节点权限。后一条为基于图的系统设计推论。[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=10|PDF p.10]]

## 关联与比较
- [[knowledge/concepts/compute-memory-federated-model-contract|联邦模型契约]] 讨论模型服务身份与保密；本材料讨论硅/固件身份。两者可复用 attestation 思路，但不可将软件容器 identity 等同于 silicon RoT。
- [[knowledge/concepts/compute-memory-cxl-failure-domain|故障域与观测]]：可用性与恢复也是安全生命周期的一部分；独立的带外观测路径应纳入信任和访问控制分析。

## 不确定性与待验证
材料没有给出 threat model 的攻击者能力边界、互认证消息序列、key provisioning/rotation/revocation 细节、fault injection 或 penetration test。对架构成本分析还需 secure transport 的额外字节、pipeline latency、能耗和异常恢复行为，不能假设安全是零成本。


## 原始页码导航
[[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=2|p.2]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/Security of Multi-chip ICs & Security Chiplets with Caliptra- Building a Hardware Root of Trust.pdf#page=13|p.13]]
