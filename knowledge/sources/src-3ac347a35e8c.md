---
id: "src-3ac347a35e8c"
type: "source"
title: "Meta QLC 实践：块级修复、数据放置与缓存感知分配"
source_path: "storage/QLC-Storage-in-Hyperscalefleet.pdf"
source_git_blob_sha: "60a5baf7d1b758d93f58f967dc78fbc7d67c738c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 23
review_status: "analyzed-visual"
evidence_pages: [4, 7, 9, 10, 11, 12, 14, 15, 16, 19, 20, 22, 23]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [7, 12, 20]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# Meta QLC 实践：块级修复、数据放置与缓存感知分配

> 阅读范围：已阅读本文件全部可提取文字（23页）。关键页已视觉核对：7, 12, 20；不代表逐页视觉审核。

## 核心结论

QLC 商用化需要应用与设备协作，而不仅是容量替换：块级错误尽量原位修复，按数据寿命放置以减少 WAF，按缓存恢复状态分配 burst 写入。三条路径分别影响可用容量、寿命与写入尾延迟。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=10|PDF p.10]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=12|PDF p.12]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=14|PDF p.14]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=22|PDF p.22]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=23|PDF p.23]]

## 关键证据

- 单块问题导致整盘退役会浪费大容量设备；建议应用可从 block-level failure 恢复。p.12 流程包含 healthy、可疑块隔离、修复/验证和最终迁移，而不是无限重试。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=9|PDF p.9]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=11|PDF p.11]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=12|PDF p.12]]
- host-directed placement 保留 hot/warm/cold 寿命信息到 reclaim unit；drive-managed 模式可能在堆栈中丢失这些信息。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=14|PDF p.14]]
- cache-aware allocator 使用 ready/in-use/cooling-off 分类；材料承认 host 不知道真实内部 GC 状态，先用最近写入历史和性能 cliff 来估计。要求新增 buffer fill、GC progress、live WAF 等 telemetry 正是为弥补这个盲区。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=16|PDF p.16]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=23|PDF p.23]]

## 指标与条件

材料称有效 DWPD 从 0.17 到 0.96，但未给计算寿命、负载与 WAF 前后测量方法，不能外推 5.6× 所有设备寿命。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=15|PDF p.15]]

p.7 onboarding failure 表合计为 supplier A 2.9、B 11.7、all 3.7；视觉核对仍没有单位、分母或观察窗口。因此本卡不称其为 AFR/百分比，也不把供应商差异当普遍质量排名。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=7|PDF p.7]]

持续写在 SLC/pSLC 满后可能下降 3–10× 是来源主张；p.20 示例为 1 MiB sequential write、QD32 的 cache cliff，而非 4K random 或应用 p99。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=19|PDF p.19]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=20|PDF p.20]]

## 图表与架构

已核对 p.7 无单位表、p.12 block recovery 状态流、p.20 写入 cliff 图。p.4 跨 TLC/QLC/HDD 的范围表未提供型号统一测试条件，未拿来作横向产品排名。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=4|PDF p.4]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=7|PDF p.7]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=12|PDF p.12]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=20|PDF p.20]]

## 关联与比较

与 Micron FIP 共同主张不要把局部介质退化立刻升级为整盘损失；与 Sandisk Direct Write 则是不同层策略：后者试图移除 SLC 缓存原因，Meta 方案管理现有缓存行为。不能将两者视为同一实现。

## 不确定性与待验证

cache timer 不是实时 GC 真值；冷热误分类、跨租户公平、剩余寿命和重建流量可能抵消收益。缺少降级期间数据完整性证明、错误阈值和线上 A/B 的 SLA 数据。[[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=12|PDF p.12]][[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=23|PDF p.23]]

