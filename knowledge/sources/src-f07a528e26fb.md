---
id: "src-f07a528e26fb"
type: "source"
title: "Direct Write QLC：可读首遍编程减少 SLC 保护开销"
source_path: "storage/QLC-Writes-the-end-of-SLC-caching.pdf"
source_git_blob_sha: "2e4666763fd0931678339154d007d75536c1c604"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [7, 8]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# Direct Write QLC：可读首遍编程减少 SLC 保护开销

> 阅读范围：已阅读本文件全部可提取文字（10页）。关键页已视觉核对：7, 8；不代表逐页视觉审核。

## 核心结论

Sandisk 定义的 Direct Write 使 QLC 第一遍 program 就可读，从而不必把 host data 暂存到 SLC 来覆盖不可持久的窗口；它并不是把 QLC 变成 SLC，也不是无条件消除所有 GC、缓存或写放大。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=3|PDF p.3]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=5|PDF p.5]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=9|PDF p.9]]

## 关键证据

- 传统两遍编程示意中第一遍不可持久，掉电可能使大量数据处于风险；SLC copy 提供 durability，同时还可经过 controller 做纠错。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=4|PDF p.4]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=5|PDF p.5]]
- SLC 占用原本可作 OP 的 NAND 容量；需按耐久比例与最坏情形配置，否则 SLC 区域可能先失效。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=6|PDF p.6]]
- 去掉该缓存同时影响容量、数据路径带宽和功耗，属于介质编程、保护策略与控制器设计的联合优化。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=8|PDF p.8]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=9|PDF p.9]]

## 指标与条件

p.7 模型 WAF 从 3.81 到 4.85，约 +27%，对应其选定区域减少 4 个百分点 OP；这不是任意 OP 点都具有同一斜率。p.8 模型称每 1 GB/s host writes 带来约 1 W SLC cache penalty，没有给实际器件/电压/计量方法。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=7|PDF p.7]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=8|PDF p.8]]

“四次数据路径操作/4× bandwidth and power”针对示意中的数据搬运，不是整块 SSD 总功耗提高 4 倍，也不能反推 Direct Write 使整机功耗下降 75%。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=8|PDF p.8]]

## 图表与架构

已核对 p.7 OP/WAF 曲线与 p.8 四步数据路径图。图中的 1× power 是同一抽象数据操作单位，不是各阶段完整器件功率测量。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=7|PDF p.7]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=8|PDF p.8]]

## 关联与比较

与大 RU FDP 经济性讨论互相解释：大 erase block、保护窗口和 SLC pool 的代价会改变数据放置的最优点。与 Meta cache-aware 软件策略不同，这是改变 NAND programming 路径的硬件/固件方案。

## 不确定性与待验证

材料未给 Direct Write 实测读 margin、RBER/UBER、断电注入、保持时间、温度、寿命、延迟或量产设备对照。标题“End of SLC Caching”应按此特定 host-data protection 用途理解，不是所有 SSD 缓存机制的终结。[[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=2|PDF p.2]][[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=9|PDF p.9]]

