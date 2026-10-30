---
id: "src-badf54452e3e"
type: "source"
title: "SRv6 Deployments in Scale-Out Networks"
source_path: "networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf"
source_git_blob_sha: "4ec6c733ef4e31820eea3f111ba2aa89f6d3cbdc"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [4, 7, 8, 9, 10, 11, 12, 13, 15]
text_reviewed: true
key_pages_visual_checked: [13]
tags: ["ocp-2026", "networking"]
concepts: ["[[knowledge/concepts/network-multipath-behavior]]"]
---

# SRv6 Deployments in Scale-Out Networks

## 核心结论
SRv6为传输层提供确定路径表达；MRC负责利用反馈避开坏路径。两者互补，不应把“路径可编程”本身当成拥塞控制或可靠交付。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=10|PDF p.10]][[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=11|PDF p.11]][[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=13|PDF p.13]]

## 关键证据
- uSID把IPv6 DA用于有序instructions，演讲称DA可放6个uSID；source NIC封装、switch按列表strict source route、destination NIC解封装。拥塞drop可配packet trimming。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=4|PDF p.4]][[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=11|PDF p.11]]
- 低entropy的少量大流与同步burst使静态ECMP不均衡，故障会影响同步collective与checkpoint浪费。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=7|PDF p.7]][[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=8|PDF p.8]]
- SONiC示例通过SRV6_MY_LOCATORS/SRV6_MY_SIDS与FRR/Config DB编程，但这只是配置架构，不是所有ASIC功能等价的证明。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=12|PDF p.12]]

## 指标与条件
- 75K GPUs生产job一次T1停止转发：约25% QPs受影响、约580K packets dropped；MRC移除路径后throughput恢复早于switch reboot。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=13|PDF p.13]]
- 时间线**没有时间刻度**，不能给微秒/毫秒恢复保证。524,288 GPU是另一页multi-plane design可支持规模陈述，不是p.13该job实际规模。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=9|PDF p.9]][[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=13|PDF p.13]]
- Scale-up诉求包括32/64/128B小包效率、single-header、native strict source route、two-tier与radix>576；是需求列表，不是已交付性能结果。[[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=15|PDF p.15]]

## 图表与架构
已核p.13事件序列与三个统计框，避免把均匀排布的timeline读为等时间间隔。全文标题页说Scale-Out，文件名带Scale-Across，后半另讨论Scale-Up需求；以页内范围为准。

## 关联与比较
[[knowledge/concepts/network-multipath-behavior]]；[[knowledge/sources/src-f13077d44cf0]]；[[knowledge/sources/src-e41f8d86b57e]]把SRv6用于区域backbone而不是同一后端job。

## 不确定性与待验证
没有路径状态下发scale、NIC缓存、uSID处理额外latency、故障检测/重传时间分布，也未证明应用p99。商用选择要把source-route capabilities与transport behavior分开验收。
