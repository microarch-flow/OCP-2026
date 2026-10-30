---
id: "src-8cf188b85e4d"
type: "source"
title: "Microsoft／Intel：把节能功能前移到 NPI 设计门槛"
source_path: "Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf"
source_git_blob_sha: "c8353df0d066b2e14f5022f65162737cde0955ae"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [2, 3, 5, 6, 7]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]"]
---

# Microsoft／Intel：把节能功能前移到 NPI 设计门槛

## 核心结论
节能不能等到交付末期才启用BIOS/OS开关；芯片、平台和机架各层应有预算、负责人、默认设置、例外理由及SLA验证。本材料提出共同规范方向，不是已完成的跨厂商合规标准。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=2|PDF p.2]][[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=5|PDF p.5]][[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=8|PDF p.8]]

## 关键证据
- 层次潜力写作silicon15–25%、平台10–20%、rack5–15%；没有同一基线的分层实验，不能相加宣称总节能30–60%。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=2|PDF p.2]]
- CPU checklist要求DVFS、core/package C-state、turbo和energy-performance bias写明状态、BIOS/BMC/OS控制、默认值及例外；C6唤醒时延必须在SLA内。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=5|PDF p.5]]
- NPI图以目标1250 W，对照concept1455、architecture1430、EVT1530、DVT1430、PVT1220 W，明确为**示例且混合模拟/测量**，不是具名平台实测节能轨迹。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=6|PDF p.6]]

## 指标与条件
CPU50%、内存19%、VR损耗8%等是示例平台预算，accelerator+NIC只有7%，不适用于GPU密集AI机架的默认分解。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=3|PDF p.3]]

## 图表与架构
p.7把CPU、memory、storage、NIC/accelerator和platform放在共同定义、开关、测量/报告框架之下；统一接口的作用是减少重复验证，并不保证各层节能独立可乘。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=7|PDF p.7]]

## 关联与比较
与MaxLPS动态机架预算、Arm任务SLA及DCEM功耗分解互补：feature enabled只是起点，必须测试低负载收益、唤醒尾延迟、设备状态兼容与故障恢复。

## 不确定性与待验证
未提供开关组合矩阵、工作负载、真实功耗曲线或已批准规范；草案与CPU清单计划两个季度内供评审，不能解释为当前完成状态。[[Sustainability/From Silicon to System- Embedding Power Efficiency as a Core Design Principle for Scalable AI.pdf#page=8|PDF p.8]]

## 知识网络
[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]
