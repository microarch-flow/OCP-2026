---
id: "src-0c1cca733ec2"
type: "source"
title: "Broadcom 主旨：Ethernet scale-up 的开放协议与铜光物理约束"
source_path: "keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf"
source_git_blob_sha: "971d6f9410863331c8c76817f1709e8850f8747d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 25
review_status: "analyzed-visual"
evidence_pages: [4, 9, 10, 11, 12, 13, 16, 18, 19, 21, 22, 23]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [16, 22]
updated: "2026-10-30"
---

# Broadcom 主旨：Ethernet scale-up 的开放协议与铜光物理约束

> 阅读范围：已阅读本文件全部可提取文字（25页）。关键页已视觉核对：16, 22；不代表逐页视觉审核。

## 核心结论

主旨把 scale-up、scale-out、scale-across 放在共同 Ethernet 运维基础上，但其物理约束仍不同。单机架铜连接受到背板密度、功率与距离约束；多机架光连接增加成本/传播延迟，OCI 是试图改善这个折衷的方向。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=4|PDF p.4]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=9|PDF p.9]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=16|PDF p.16]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=18|PDF p.18]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=19|PDF p.19]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=21|PDF p.21]]

## 关键证据

- ESUN 与 SUE-T 分层：前者强调可靠/小消息/多跳链路基础，后者讨论 push/pull、ordering、packing、load balancing、scheduling。材料列 v1.0 published 与 SUE-T 2H2026 target，不应混成同一规范均已发布。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=10|PDF p.10]]
- 厂商自报 5+ hyperscalers 在生产用 Ethernet scale-up、10+ partners 构建 racks，未提供部署规模或互操作矩阵。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=11|PDF p.11]]
- Open Cluster Designs 从 XPU pod 到 XOC-N，blueprints v1.0 published 与第二代开发是设计交付，不是所有组合都已资格认证。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=23|PDF p.23]]

## 指标与条件

p.16 current gen 示例 72 XPUs、14.4 Tb/s/XPU、1.04 Pb/s 总带宽、约 250 kW/rack、铜 reach ~2 m；possible next gen 28.8 Tb/s/XPU、2.08 Pb/s、~500 kW 是可能方案，不是同功耗翻倍或已交付。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=16|PDF p.16]]

p.22 200G link 对照：DAC 7 pJ/bit@2m、integrated OCI 7 pJ/bit@500m、DR LRO front-panel 23 pJ/bit@500m。未给测量平台/温度/激光功耗口径；应视为厂商链路模型/主张，不能直接作全机架节电量。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=22|PDF p.22]]

## 图表与架构

已核对 p.16 current/possible-next 区分及 p.22 XPU↔switch total-link 边界。250 ns switching 等不包含端点、排队、collective 与多跳总延迟。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=12|PDF p.12]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=16|PDF p.16]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=22|PDF p.22]]

## 关联与比较

与工作负载契约相连：混合铜光把 scale-up domain 分成不同延迟域，调度/collective topology 需要感知这种非均匀性。开放 Ethernet 运维工具有复用价值，不代表 scale-up 的内存语义自动等同普通网络。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=19|PDF p.19]]

## 不确定性与待验证

缺少实际应用 scaling efficiency、p99、误码/重试、可靠性和成本对照；OCI “approach copper KPI”是设计目标。图上标称带宽的方向/有效负载口径需向供应商确认。[[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=13|PDF p.13]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=21|PDF p.21]][[keynotes/05_Scaling AI Infrastructure Through Open Innovation.pdf#page=22|PDF p.22]]

