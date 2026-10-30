---
id: "src-2807cd66d1aa"
type: "source"
title: "高容量 QLC：DRAM 节省取决于映射粒度、缓存与工作负载"
source_path: "storage/High-Capacity-QLC-Innovation.pdf"
source_git_blob_sha: "e660727faaaef7d8af9cad8e1ce5b0e1bb95fa5e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 25
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 8, 10, 11, 12, 15, 16, 17, 22, 23, 24]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [5, 10, 23, 24]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-storage-workload-contract]]"]
---

# 高容量 QLC：DRAM 节省取决于映射粒度、缓存与工作负载

> 阅读范围：已阅读本文件全部可提取文字（25页）。关键页已视觉核对：5, 10, 23, 24；不代表逐页视觉审核。

## 核心结论

四家厂商讨论不同的 DRAM 缩减路径，不能合并成一个通用结论：扩大 IU、缓存 L2P、extent/B+ tree FTL、把 FTL 放到 NAND，各自改变读延迟、写放大和元数据局部性。大块或限速 AI 工作负载上的结果不证明小随机写也适用。[[storage/High-Capacity-QLC-Innovation.pdf#page=3|PDF p.3]][[storage/High-Capacity-QLC-Innovation.pdf#page=8|PDF p.8]][[storage/High-Capacity-QLC-Innovation.pdf#page=15|PDF p.15]][[storage/High-Capacity-QLC-Innovation.pdf#page=22|PDF p.22]][[storage/High-Capacity-QLC-Innovation.pdf#page=23|PDF p.23]]

## 关键证据

- Phison 比较减少 L2P 缓存与增大 IU：前者可能每次 miss 增加 NAND 读；后者在小于 IU 的写入上可能出现读改写放大。[[storage/High-Capacity-QLC-Innovation.pdf#page=4|PDF p.4]][[storage/High-Capacity-QLC-Innovation.pdf#page=5|PDF p.5]]
- Kioxia 明确是 hypothetical QLC drive 的模拟/计算、理论性能上限；4K 随机写时缓存 LUT 比采用大 IU 更有利，16K/128K 写下优劣会改变。[[storage/High-Capacity-QLC-Innovation.pdf#page=8|PDF p.8]][[storage/High-Capacity-QLC-Innovation.pdf#page=10|PDF p.10]][[storage/High-Capacity-QLC-Innovation.pdf#page=11|PDF p.11]][[storage/High-Capacity-QLC-Innovation.pdf#page=12|PDF p.12]]
- ScaleFlux 提出热元数据 DRAM、extent 映射和 NAND 持久化；1 MB 顺序区间可一个 entry，而碎片化 4K 随机写可能回退到细粒度。压缩使 WAF<1 的说法以可压缩数据为前提。[[storage/High-Capacity-QLC-Innovation.pdf#page=15|PDF p.15]][[storage/High-Capacity-QLC-Innovation.pdf#page=16|PDF p.16]]
- Sandisk 给出 NAND FTL 与 DRAM FTL 在三种限速负载上的接近结果，并给出部署容量/DRAM 的说明性模型。[[storage/High-Capacity-QLC-Innovation.pdf#page=23|PDF p.23]][[storage/High-Capacity-QLC-Innovation.pdf#page=24|PDF p.24]]

## 指标与条件

Phison 表中九阶段加权 WAF：4K IU 2.449、64K IU 2.628、128K IU 2.980；64K 相比 4K 仍约增加 7.3%，不能把页上“无显著影响”读成零代价。VectorDB run 被排除在该加权行之外；具体权重与测试平台未给出。[[storage/High-Capacity-QLC-Innovation.pdf#page=5|PDF p.5]]

Kioxia 4K 随机写图列 WAF 4.8/19/38/76，分别对应 4K/16K/32K/64K IU；这不是硬件实测结果。[[storage/High-Capacity-QLC-Innovation.pdf#page=8|PDF p.8]][[storage/High-Capacity-QLC-Innovation.pdf#page=10|PDF p.10]]

Sandisk 1 EB 模型：每系统 24×122.88 TB 可用容量、host DRAM 96 GB；SSD DRAM 从 32 降到 4 GB（16K IU），系统 DRAM 从 864 降到 192 GB，340 系统合计 293,760→65,280 GB，约减少 78%。这是包含 host DRAM 的说明性算例，不是已部署项目节省量。[[storage/High-Capacity-QLC-Innovation.pdf#page=24|PDF p.24]]

## 图表与架构

已视觉核对 p.5 工作负载/WAF 表、p.10 等 DRAM 预算对比、p.23 的限速工作负载图与 p.24 部署算例。p.23 图只表明指定负载达到相近速率，不代表无速率限制下随机 IOPS 或 p99 相同。[[storage/High-Capacity-QLC-Innovation.pdf#page=5|PDF p.5]][[storage/High-Capacity-QLC-Innovation.pdf#page=10|PDF p.10]][[storage/High-Capacity-QLC-Innovation.pdf#page=23|PDF p.23]][[storage/High-Capacity-QLC-Innovation.pdf#page=24|PDF p.24]]

## 关联与比较

本材料内部就存在有价值的条件差异：Phison 的 AI 写入轨迹支持更大 IU，Kioxia 的小随机写模型更支持小 IU 加部分缓存；二者不是直接矛盾。选型应先量化 I/O 粒度、局部性、压缩率、随机写比例，再比较 TCO。[[storage/High-Capacity-QLC-Innovation.pdf#page=5|PDF p.5]][[storage/High-Capacity-QLC-Innovation.pdf#page=10|PDF p.10]][[storage/High-Capacity-QLC-Innovation.pdf#page=15|PDF p.15]]

## 不确定性与待验证

p.3/p.6 的 SSD、DDR 价格及 20 EB 节省数字只是所列单价下的商业算例，不是当前市场报价。ScaleFlux 的故障容忍/UBER 主张未提供故障注入、寿命或置信区间；NAND FTL 结果缺少尾延迟与稳态 details。[[storage/High-Capacity-QLC-Innovation.pdf#page=3|PDF p.3]][[storage/High-Capacity-QLC-Innovation.pdf#page=6|PDF p.6]][[storage/High-Capacity-QLC-Innovation.pdf#page=17|PDF p.17]][[storage/High-Capacity-QLC-Innovation.pdf#page=23|PDF p.23]]

