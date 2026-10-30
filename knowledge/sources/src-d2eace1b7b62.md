---
id: "src-d2eace1b7b62"
type: "source"
title: "Fio Sprandom：快速构造稳态，但 OP 与后续验证不能省略"
source_path: "storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf"
source_git_blob_sha: "fd0bfffe7ce4f8284bdcd86919bd946dfd11d4e5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [12, 13, 14]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# Fio Sprandom：快速构造稳态，但 OP 与后续验证不能省略

> 阅读范围：已阅读本文件全部可提取文字（16页）。关键页已视觉核对：12, 13, 14；不代表逐页视觉审核。

## 核心结论

Sprandom 利用 greedy GC 下稳态有效/无效页分布的模型，设计写入/覆盖顺序，以较少预处理写入接近稳态。它不是把持续随机写性能“提高到峰值”，也不应跳过后续随机写稳态检查。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=4|PDF p.4]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=6|PDF p.6]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=14|PDF p.14]]

## 关键证据

- 参数至少依赖 device OP 和 region 数；演讲称对 OP 敏感、对 regions 较不敏感，blocksize 应对齐 IU 避免 read-modify-write。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=7|PDF p.7]]
- spr_cs 延迟失效写，避免原写与覆盖同时留在设备 cache；大容量设备的后续随机测试要注意 random generator。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=7|PDF p.7]]
- NAND page 为 ECC/CRC/metadata 保留的不可访问空间不必然是 GC 可使用的 OP；PI format 改变逻辑 LBA 数时需要重新估计有效 OP。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=9|PDF p.9]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=10|PDF p.10]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=11|PDF p.11]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=12|PDF p.12]]

## 指标与条件

示例传统随机写约 60 h，Sprandom 约 18 h，之后随机写下降到约 600 MiB/s 稳态；预处理阶段 2+ GiB/s 不是稳态随机写能力。来源建议 Sprandom 后继续随机写以初始化控制器状态，因此 60→18 h 不应直接当作整个 qualification suite 的节省。未披露设备型号与全部 job 配置。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=5|PDF p.5]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=6|PDF p.6]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=14|PDF p.14]]

重要勘误待核实：p.12 同时写 `Phy_Sectors=LBAs_orig*(1+spr_op_orig)` 和 `spr_op_new=1-(Phy_Sectors/LBAs_new)`；p.13 也写 `1-((1+spr_op_orig)/utilization)`。在其前式所暗示的正 OP 定义下，后式符号会给出负值且不符合“低 utilization 增加 OP”的文字。不可直接复制执行；应核对 Fio 定义/实现，不能默默修正成正式公式。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=12|PDF p.12]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=13|PDF p.13]]

## 图表与架构

已核对 p.12–13 原文公式，确认不是纯文字提取的正负号错误；p.14 曲线也区分 traditional、standard、70% utilization 与 PI 情形。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=12|PDF p.12]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=13|PDF p.13]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=14|PDF p.14]]

## 关联与比较

与测试计划中的 Factory Mode 一样，加速预处理的价值必须以“最终状态等价”验证；应记录介质容量、nsze、IU、PI、TRIM 和 cache 参数，而非只有运行时长。

## 不确定性与待验证

分析模型对 GC 策略的假设、厂商 OP 信息及 PI 是否落在同一 NAND page 都影响适用性。该例不能证明所有 SSD、FDP 布局和混合负载均可用同一参数。[[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=4|PDF p.4]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=7|PDF p.7]][[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=12|PDF p.12]]

