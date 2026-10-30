---
id: "src-7f631cbf9c52"
type: "source"
title: "CPU/GPU RAS诊断：以安全故障域、诊断有效率与修复时间验收"
source_path: "systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf"
source_git_blob_sha: "1afa12e47cb6a63d951e705c77438d12d5f07d44"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tags: ["ocp", "source", "platform", "systems-management"]
text_reviewed: true
key_pages_visual_checked: [6, 7]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-operability-contract]]"]
---

# CPU/GPU RAS诊断：以安全故障域、诊断有效率与修复时间验收

> 阅读范围：已阅读本文件全部可提取文字（12页）。关键页已视觉核对：6, 7；不代表逐页视觉审核。

## 核心结论

- 作者将运营指标从部署算力转向有效工作/美元/瓦，并强调blast radius、diagnostic efficacy、MTTR；修复结果而非只触发告警才是收益。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=2|PDF p.2]][[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=3|PDF p.3]]
- 先contain，再按故障深度选诊断配方；避免所有异常都跑完整多小时套件或重启整训练job。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=5|PDF p.5]][[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=6|PDF p.6]][[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=9|PDF p.9]]

## 关键证据

- Supplier交付工具、error→repair JSON、recipes与OCPTV日志；hyperscaler结合遥测选择recipe、定位FRU并执行修复。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=5|PDF p.5]]
- rack-level缺口包括时间同步、GPU/fabric/power/cooling跨域关联和诊断流程分裂。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=8|PDF p.8]]
- 恢复需防静默数据损坏、支持逐级scope、可观察退化/机制耗尽，由workload/SLA政策选择recovery或fail-fast。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=10|PDF p.10]][[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=11|PDF p.11]]

## 指标与条件

- 分级时长是建议范围：T0无需诊断周期；T1 5–10分钟；T2 <1小时；T3多小时，不是实测平均MTTR。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=6|PDF p.6]]
- 成熟产品建议diagnostic efficacy≥90%，定义FR/(FR+FU)，仅同时检测、找到可修根因、给行动、恢复正常才计resolved；需按故障域给样本与周期。非本文件已达成90%。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=7|PDF p.7]]
- 作者称CPU诊断0.9/GPU RAS1.9于2026 Summit发布，本文未另核实仓库release。[[systems-management/GPU-CPU-Diagnostics-and-RAS-Standardization-Advances-for-Hyperscale-Infrastructure.pdf#page=4|PDF p.4]]

## 图表与架构

已视觉核对p.6诊断分层与p.7公式/门槛，未把推荐门槛当测试结果。

## 关联与比较

可作为采购验收框架：标准化outcome和observability而非强迫厂商用相同内部恢复机制；结合训练/推理不同SLO定义安全最小scope。

## 不确定性与待验证

需真实故障分布、误报/漏报、修复复发率、部分降级下吞吐与p99影响，不能只用coverage或单次demo替代fleet outcome。

