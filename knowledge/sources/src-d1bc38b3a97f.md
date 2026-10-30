---
id: "src-d1bc38b3a97f"
type: "source"
title: "Arm 主旨：Agentic 数据中心的三种 CPU 工作与 DPU 分工"
source_path: "keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf"
source_git_blob_sha: "c858bb1b3281064e441ed9bfa67bb8a153027dcb"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 25
review_status: "analyzed-text"
evidence_pages: [2, 4, 8, 11, 12, 13, 14, 16, 20, 21, 23]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# Arm 主旨：Agentic 数据中心的三种 CPU 工作与 DPU 分工

> 阅读范围：已阅读本文件全部可提取文字（25页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

材料区分 AI head node（供给加速器）、cloud-native services（用户服务）和 agentic virtual users（持续执行环境）。这比笼统“AI 需要更多 CPU”更可操作：三者的吞吐、低延迟、memory/I/O 与隔离目标不一样。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=8|PDF p.8]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=12|PDF p.12]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=20|PDF p.20]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=21|PDF p.21]]

## 关键证据

- Head node 负责 schedule、prepare、move data、coordinate，设计目标是 accelerator 不等待 CPU。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=8|PDF p.8]]
- DPU 分离 networking/storage/security 等 infrastructure services，释放应用 CPU 并强化隔离；材料未证明只要部署 DPU 就有 deterministic performance。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=11|PDF p.11]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=13|PDF p.13]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=14|PDF p.14]]
- 开放路径覆盖 SBSA/SBBR/SBMR、ACS/ADAC、RAS API、reference server、FCSA 与 ORv3/ORW。规范、参考设计和 marketplace product 是不同交付形态。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=4|PDF p.4]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=23|PDF p.23]]

## 指标与条件

旧 cloud schematic 将 75–80% compute 用于应用、20–25% infrastructure services，仅为概括性比例，没有负载/平台测量。CPU market 2026→2030 的 $52B→$300B 是引述预测，不是当前收入或确定容量需求。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=11|PDF p.11]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=21|PDF p.21]]

## 图表与架构

未视觉核对图形；只记录完整文本明确命名的职责，不从重复 CPU 图标推算核数、成本或拓扑。

## 关联与比较

与 AMD Helion 的 performance/balanced/dense 配置共同提示：agent orchestration、sandbox 和推理服务应分别做资源画像。与 SCMP/DPU 管理材料联读时仍需验证控制权、故障恢复与攻击面。

## 不确定性与待验证

新闻、用户增长和市场预测在本卡仅作来源背景，不作外部核实的现状。没有 agent task completion/s、p99、J/task 或每租户隔离开销的实测；不能从核心数或 ISA 推导业务效率。[[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=2|PDF p.2]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=16|PDF p.16]][[keynotes/04_The Agentic Decade Starts with Open Infrastructure.pdf#page=21|PDF p.21]]

