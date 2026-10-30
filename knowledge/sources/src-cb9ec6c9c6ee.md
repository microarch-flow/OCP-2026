---
id: "src-cb9ec6c9c6ee"
type: "source"
title: "Deep Dive into Enabling 1 Million GPUs to Talk to Thousands of Smart Devices — Today’s Focus: Partitioning"
aliases: ["Deep Dive into Enabling 1 Million GPUs to Talk to Thousands of Smart Devices — Today’s Focus: Partitioning"]
speakers: "Pankaj Mehra（主持）；Galen Shipman；Anand Jayarajan；Evangelos Georganas；Atharva Chougule"
source_path: "fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf"
source_git_blob_sha: "1fae7c84728301cdd8dd8e7045e91a0902abb2eb"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 47
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [9, 12, 15, 16, 17, 20, 21, 24, 25, 28, 30, 31, 32, 33, 40, 44, 45, 46]
evidence_pages: [2, 3, 9, 15, 16, 17, 20, 21, 24, 25, 30, 31, 32, 33, 40, 44, 45, 47]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-partitioning-placement-ir]]"]
---

# Deep Dive into Enabling 1 Million GPUs to Talk to Thousands of Smart Devices — Today’s Focus: Partitioning

## 核心结论
标题的百万 GPU 是框架规模愿景，**不是展示了百万 GPU 实测系统**。材料汇集三个可复用思想：空间填充曲线保局部性、统一稀疏关系/张量 IR、依据表达式和稀疏分布生成负载均衡分区。核心不是平均切字节，而是同时考虑计算工作量和跨分区通信。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=2|PDF p.2]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=9|PDF p.9]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=31|PDF p.31]]

## 关键证据
1. HPC 分区目标是负载均衡、减少 ghost/private 比和低成本构造初始划分。Hilbert ordering 将多维空间映成保持一定局部性的 1D 序，不保证任意图都达到最优。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=9|PDF p.9]]
2. SFC-CA GEMM 以 generalized Hilbert/Gilbert 次序遍历 tile，BRGEMM/zero/add-reduce 为基础 primitive；K-layers 调节生成 2D/2.5D/3D 算法族。所谓约 30 行代码不包括底层高性能 microkernel。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=15|PDF p.15]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=16|PDF p.16]]
3. Reffine 把 stream/graph/relational data 表成 sparse unbounded multidimensional Field，以声明式 Operator 描述计算；注入 `s < pk <= e` 边界做并行化，最后把空间交集/过滤降到循环。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=20|PDF p.20]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=21|PDF p.21]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=24|PDF p.24]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=25|PDF p.25]]
4. Nacho 的 cost 取决于 tensor expression、format、nonzero distribution。动画用 `C(x)=区间[0,x)内非零数量`，以 cumulative targets 3/6/9 查找边界 2/5/10；扩展到每维 cost 与层次搜索。它说明按坐标等分并不一定按工作量等分。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=30|PDF p.30]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=31|PDF p.31]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=32|PDF p.32]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=33|PDF p.33]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=40|PDF p.40]] [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=44|PDF p.44]]

## 指标与条件
- SFC-CA GEMM p.17 对照图标 oneDNN：64-core Emerald Rapids 最大 2.6×/加权调和平均 1.45×；128-core Granite Rapids 最大 5.5×/WHM 1.8×；96-core AMD 最大 1.7×/WHM 1.15×；96-core Graviton 最大 2.5×、WHM 持平。最大值和总体均值不能互换，材料也没有据此证明网络级 million-GPU 扩展。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=17|PDF p.17]]
- Nacho p.45 给不同 total nnz 的 runtime 散点，作者报告对 Taco 几何平均 2.4×、cuSPARSE 1.8×。本页未完整给机器、矩阵集合、预处理是否计时及所有算子，因此只保留为作者报告，不直接用于推理加速器选型。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=45|PDF p.45]]

## 图表与架构
p.28–44 多页是分区搜索逐步动画；不应把同一 toy example 的中间帧当多个实验。p.32 有明显排版覆盖/箭线，概念应结合 p.31/33/44 理解。通信下界论断限定 square/rectangular GEMM regimes，不能迁移到所有稀疏算子。[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=16|PDF p.16]]

## 关联与比较
[[knowledge/concepts/compute-memory-partitioning-placement-ir|分区与放置 IR]]：先定义计算/数据语义，再建立 cost model，然后在拓扑上调度。需要把通信、稀疏不均衡和内存占用同 FLOPs 一起表达。

## 不确定性与待验证
p.3/47 提出的 partial gather、collectives、quantized operands 等是开放议题，不是已批准标准。引用论文中完整证明和实验未包含在本仓库材料，本文不以标题替代验证。

## 原始页码导航
[[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=2|p.2]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=3|p.3]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=9|p.9]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=15|p.15]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=16|p.16]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=17|p.17]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=20|p.20]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=21|p.21]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=24|p.24]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=25|p.25]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=30|p.30]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=31|p.31]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=32|p.32]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=33|p.33]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=40|p.40]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=44|p.44]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=45|p.45]] · [[fti-workshop-data-centric-computing/Deep-dive-into-what-allows-1-million-GPUs-talk-to-thousands-of-smart-devices.pdf#page=47|p.47]]
