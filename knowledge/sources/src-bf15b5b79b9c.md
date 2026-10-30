---
id: "src-bf15b5b79b9c"
type: "source"
title: "The Open Chiplet Economy: Progress, Challenges, and the Road Ahead"
aliases: ["The Open Chiplet Economy: Progress, Challenges, and the Road Ahead"]
speakers: "Jawad Nasrullah (Palo Alto Electron); Anu Ramamurthy (Microchip); Mark Knight (Arm)"
source_path: "Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf"
source_git_blob_sha: "fb0e05608319b87e4db5246a9a9f236129ff2cf0"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 8]
evidence_pages: [2, 3, 4, 5, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]", "[[knowledge/concepts/compute-memory-federated-model-contract]]"]
---

# The Open Chiplet Economy: Progress, Challenges, and the Road Ahead

## 核心结论
OCE 的开放目标跨越接口、系统契约、设计模型、供应链和商业风险；**有各层规范，不等于已有可部署的多供应商互操作系统**。演讲将 2027 的重点定义为从定义标准走向可验证互操作及商业上有吸引力的复用。[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=2|PDF p.2]] [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=8|PDF p.8]]

## 关键证据
- 架构图连起 HPC modularity、FCSA/Physical AI、BoW/FlexI 与光互连、PHY-agnostic link layer、CDX、virtual prototyping 和 marketplace/business workstream。[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=3|PDF p.3]]
- 报告时点：FCSA 1.0.0 于 2026-02 首发；1.1.0 在会期当周获批发布。CMI over I3C 为完成但等待 OCP 批准；CMI over UCIe 在审；CMI over BoW 和 dedicated SCMI API 为 initial draft；LSI 贡献为 draft。必须保留这些不同成熟度。[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=4|PDF p.4]]
- BoW Flexi 1.0 标注 2026-09 发布，目标 MCU、sensors、edge AI、IoT；不能据此假设它面向 HBM 级带宽。[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=5|PDF p.5]]
- 新商业 workstream 提议多供应商 project structure、case studies、model agreements，以降低 early alignment、返工和 CDX 参与成本。[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=9|PDF p.9]]

## 指标与条件
Marketplace 页面浏览/参与数字是生态触达指标，不是 silicon 出货、良率、供应可得性或互操作通过率；这里不将其作为技术成熟度证据。

## 图表与架构
已检查 p.3 分层关系、p.4 状态表、p.5 Flexi 发布/应用范围和 p.8 路线图。本材料 p.10 日期为 Thursday, October 15，会期语境为 2026；所有状态只归属于演讲时点，不宣称已核查到当前最新版。

## 关联与比较
[[knowledge/concepts/compute-memory-chiplet-link-efficiency|TLL/PHY 性能模型]] 解决数据平面的一部分；[[knowledge/concepts/compute-memory-federated-model-contract|联邦模型契约]] 解决 pre-RTL 可评估性。两者都不足以单独证明多供应商产品化成熟。

## 不确定性与待验证
应进一步索取跨供应商 conformance test、参考设计、真实 catalog 的供货条款、模型许可与 validated range。规范、草案、POC、演示和量产采用应分栏，而不是统称“开放生态已成熟”。


## 原始页码导航
[[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=2|p.2]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/The Open Chiplet Economy- Progress, Challenges, and the Road Ahead.pdf#page=10|p.10]]
