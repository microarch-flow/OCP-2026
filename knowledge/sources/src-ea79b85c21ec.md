---
id: "src-ea79b85c21ec"
type: "source"
title: "Scaling up AI Compute, Memory and Connectivity"
aliases: ["Scaling up AI Compute, Memory and Connectivity"]
speakers: "Igor Elkanovich — CTO, GUC"
source_path: "Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf"
source_git_blob_sha: "1c5f8ec705b5dcac4641a10286104f7faa374bb8"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 7, 8, 9, 11, 12, 13]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-package-memory-wall]]", "[[knowledge/concepts/compute-memory-federated-model-contract]]"]
---

# Scaling up AI Compute, Memory and Connectivity

## 核心结论
GUC给出从2.5D/3D compute、DRAM-on-logic、CPO到vertical power/wafer-scale的共同设计视角。高密度互连和低pJ/bit需要以 **短距离、密集bond、定制接口与制造/热约束**为代价；不能不带条件地宣称custom D2D全面优于标准UCIe。

## 关键证据
- GLink-LL表采用4–8Gb/s、0.4–1.0mm trace、定制pitch，宣称0.05–0.10pJ/bit与1–3ns含CDC；对照UCIe-S/A的速率、距离和封装均不同，非等条件器件bench。BER<1e−30/no CRC-retry属于vendor保证主张，材料无测试时长和统计置信度。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=4|PDF p.4]]
- GLink-3D每项目自定义bond map、DDR/SDR、signal-clock ratio、redundancy、power domains；p.5表中1.0/2.0/2.1标silicon proven，但**80Tb/s/mm²的3.0标Execution**。全双工密度不能当单向external bandwidth。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=5|PDF p.5]]
- 3D设计需优化TSV分布、SRAM间routing、power delivery、warpage与thermal；p.6以7.5W/mm² average TDP为高密度目标条件。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=6|PDF p.6]]
- DRAM-on-compute用5–8µm hybrid bonding、每bank更宽专用bus；controller负责interleave/reorder/redundancy/repair。source宣称顺序~100%、随机70–80%utilization及AXI read-to-data<30ns，但没有完整访问分布和队列参数。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=8|PDF p.8]] [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=9|PDF p.9]]

## 指标与条件
| 演讲比较 | DRAM-on-compute | HBM4E | 条件/限制 |
|---|---|---|---|
| BW | 32TB/s | 24TB/s | 前者full-reticle 4layer；后者6stacks×16G，不等stack/面积 |
| Density | 110MB/mm² | 310MB/mm² | 分别4layer和12layer，容量密度取舍不能隐藏 |
| Latency/pJ per bit | 30ns/0.5 | 200ns/2.5 | 都声称含PHY/controller，未给全测试条件 |
| Max temperature | 125°C | 95°C | 方案规格，不是生产系统应持续运行的建议 |
[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=8|PDF p.8]]

HBM5 24–32Gb/s、~90W、2029生产为路线目标，HBM4E16Gb/s/controller ready为讲者状态声明。IVR示例TSMC16nm、1.8V入、0.5–1.0V出、high/low current效率85%/75%、3W/mm²；没有完整电流曲线。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=7|PDF p.7]] [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=12|PDF p.12]]

## 图表与架构
已核对各比较表、3D风险图、memory controller、COUPE四阶段测试插入、vertical-power和SoW图。SoW>40reticles、up to64HBM4E、20kW TDP/30kW peak是scale目标/挑战，不是已交付系统的推理benchmark。[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=11|PDF p.11]] [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=13|PDF p.13]]

## 关联与比较
[[knowledge/concepts/compute-memory-package-memory-wall|封装内存墙]]；[[knowledge/concepts/compute-memory-federated-model-contract|多物理场模型契约]]。此材料显示“更低互连能耗”可能伴随更高功率密度与更复杂制造，应同时比较thermal/PDN/yield成本。

## 不确定性与待验证
没有应用级TTFT/TPOT/p99，缺少system yield、成本、repair和生命周期数据。表格数值均保留供应商语境，不能把“silicon proven”扩展为本文每个下一代参数已硅后验证。


## 原始页码导航
[[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=2|p.2]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=13|p.13]] · [[Server：Open Chiplet Economy/Scaling up AI Compute, Memory and Connectivity.pdf#page=14|p.14]]
