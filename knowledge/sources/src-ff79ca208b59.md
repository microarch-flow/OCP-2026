---
id: "src-ff79ca208b59"
type: "source"
title: "NVMe 2.4 更新：已批准能力与规划路线分开看"
source_path: "storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf"
source_git_blob_sha: "862184dcb48cb7fc1c865751d005b92eff6fa3e9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [5, 7, 8, 9, 12, 13, 14, 15]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [14]
updated: "2026-10-30"
---

# NVMe 2.4 更新：已批准能力与规划路线分开看

> 阅读范围：已阅读本文件全部可提取文字（17页）。关键页已视觉核对：14；不代表逐页视觉审核。

## 核心结论

该更新以 2026 年 8 月的 NVMe 2.4 规格集合为快照，覆盖安全、能耗、管理和迁移。规格批准、路线图计划与某款 SSD 已实现是三件不同的事。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=5|PDF p.5]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=7|PDF p.7]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=14|PDF p.14]]

## 关键证据

- 安全方向包括 TDISP information package、virtualization lockdown、跨掉电的 lockdown persistence 与 PQC；作用分别不同，不能概括成一个“NVMe 已安全”标签。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=7|PDF p.7]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=8|PDF p.8]]
- QoS rate limiting 用于 migration load 与业务竞争时的公平性；host-addressable SLM 提供 memory addresses。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=12|PDF p.12]]
- NVMe-MI 增加状态报告、持久数据区域、E2 form factor 等；与数据平面的命令集演进分开。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=13|PDF p.13]]

## 指标与条件

材料报告自 2.3 以来授权 17 个新 work items、批准 15 个 technical proposals、11 个 ECNs；这是标准活动计数，不是设备功能覆盖率。Voltage Monitoring 支持监控最多 4 路 rail，是能力上限而非测量精度承诺。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=5|PDF p.5]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=9|PDF p.9]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=15|PDF p.15]]

## 图表与架构

已视觉核对 p.14：绿色为 ratified、蓝色为 planned、橙色为 new specification，横条左端表示批准或计划批准季度；不是设备上市区间或完成百分比。IO Prioritization、distributed namespaces、LBA range access control 等在此图仍属计划项。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=14|PDF p.14]]

## 关联与比较

与 TP4221 I/O prioritization 材料联读：rate limiting 与延迟优先级不是同一机制。与 OCP DC NVMe 2.8 联读：基础标准允许某能力，不代表某 profile 尚未/已经将它设为必选。

## 不确定性与待验证

此卡记录演讲中的版本状态，没有独立核实当下最新规范或厂商实现。路线图和功能清单也可能存在更新节奏差异，应以正式 TP/ECN 及目标产品声明为落地依据。[[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=14|PDF p.14]][[storage/NVM-Express-State-of-the-Union-NVMe-Technology-Roadmap-for-Hyperscale-Infrastructure.pdf#page=15|PDF p.15]]

