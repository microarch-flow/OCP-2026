---
id: "src-f364f1fe74e8"
type: "source"
title: "Federated Chiplet Design and Simulation: An OCE/CDX Framework for Multi-Vendor Co-Design Without IP Disclosure"
aliases: ["Federated Chiplet Design and Simulation: An OCE/CDX Framework for Multi-Vendor Co-Design Without IP Disclosure"]
speakers: "David Ratchkov; Kevin Cameron"
source_path: "Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf"
source_git_blob_sha: "995b0bbdb3f1902684347b44fd79a896c4e4372c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [7, 8, 9, 15]
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-federated-model-contract]]"]
---

# Federated Chiplet Design and Simulation: An OCE/CDX Framework for Multi-Vendor Co-Design Without IP Disclosure

## 核心结论
本演讲提出让供应商保留私有模型、对外提供受约束的仿真服务，以解决多供应商 chiplet 的系统级协同设计问题。**它是框架/POC 提案，不是已验证的自动化芯粒市场或完成的多物理场仿真产品。**

## 关键证据
- 集成前不仅要验证功能和架构互操作，还需 SI、PI、瞬态功率、热、应力/翘曲、封装装配及 workload-dependent 性能功耗；所需模型往往包含供应商机密。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=3|PDF p.3]] [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=4|PDF p.4]]
- 核心原则是模型所有权与执行分离：integrator 发送允许的边界条件，供应商返回允许的结果。CDXML 关联 Simulation Capability Manifest，模型本体无需放入 CDXML。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=5|PDF p.5]] [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=6|PDF p.6]]
- Manifest 包含模型身份/版本/hash、domain、I/O/单位/端口/范围/timestep、有效范围/误差界限、执行类型、安全授权和商业策略。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=7|PDF p.7]]
- 多物理场环路：workload activity → performance model 的 power profile → PI supply behavior → 电压反馈 → thermal → leakage/performance 反馈 → mechanical constraints → 收敛。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=9|PDF p.9]]
- AI agent 应在可信仿真之上做候选生成、不可行排除及 surrogate-guided exploration，而不是替代可信仿真。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=14|PDF p.14]]

## 指标与条件
“5 chiplets、至少 800 GB/s、封装低于 600 W、结温低于 90°C、最小成本”是 **设计任务示例**，不是已实现方案或测试结果。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=14|PDF p.14]]

POC 第一阶段：两颗独立建模芯粒、一块 substrate/package、两个供应商服务器和一个 orchestrator；**仅 power + thermal，不含 SI、PI、mechanics、functional simulation**。第二阶段才增加 transient PI、workload/performance、functional SystemC 和更多可选芯粒。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=15|PDF p.15]]

## 图表与架构
已核对 p.8：Marketplace/CDXML → System Design Graph → Federated Orchestrator → 各 vendor private model/API → package/system models → system-level result → AI agent。p.7/p.9/p.15 明确 contract、耦合迭代及分阶段范围，避免把愿景图当落地能力。

## 关联与比较
- [[knowledge/concepts/compute-memory-federated-model-contract|面向 架构探索 DSL/IR 的多保真模型契约]]：可借鉴 manifest 把 unit、validity、hash、timesteps 与误差界限作为 IR/model 边界。
- 与 TLL 互连格式的关系：仿真需要消费具体 profile 和 PHY binding，而非仅写“支持 UCIe”。

## 不确定性与待验证
联邦执行不自动保护 IP：演讲明确指出大量精心选择查询可能造成 model extraction，需要 query/result granularity、rate limit、attestation/audit 等控制。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=10|PDF p.10]] 容器化不是已证明安全性。还需验证跨模型收敛、步长协同、结果可复现性、服务可用性与模型版本固定。材料推荐复用 FSS/FMI 等通用机制，OCE 定义 chiplet-specific semantics。[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=12|PDF p.12]]


## 原始页码导航
[[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=13|p.13]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=14|p.14]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=15|p.15]] · [[Server：Open Chiplet Economy/Federated Chiplet Design and Simulation.pdf#page=16|p.16]]
