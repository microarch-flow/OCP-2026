---
id: "src-e41f8d86b57e"
type: "source"
title: "SRv6 Powered Backbone Networks"
source_path: "networking/Srv6 powered backbone networks.pdf"
source_git_blob_sha: "a23200e5b2af20d8f55f05425ac28babc7b50652"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 11]
text_reviewed: true
key_pages_visual_checked: [6]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-buffer-workload-placement]]"]
---

# SRv6 Powered Backbone Networks

## 核心结论
Meta的RBB选择浅buffer源于高密度/每W带宽约束，并用GLIDE/ECN和SRv6 TE配合；这是“可控制端点+特定流量/距离”的系统设计，不是普遍证明长距网络不需要buffer。[[networking/Srv6 powered backbone networks.pdf#page=4|PDF p.4]][[networking/Srv6 powered backbone networks.pdf#page=5|PDF p.5]][[networking/Srv6 powered backbone networks.pdf#page=6|PDF p.6]]

## 关键证据
- Ring把多region数据副本替换为共享storage pool，释放space/power给compute，却将local reads转成backbone traffic。RBB区域流量与EBB全局深buffer分工。[[networking/Srv6 powered backbone networks.pdf#page=3|PDF p.3]][[networking/Srv6 powered backbone networks.pdf#page=4|PDF p.4]]
- RBB：64 parallel planes，plane内sites full mesh；Ring RTT预算1/5/10ms。800G ZR+跨度650km以上，带宽需求约EBB十倍促使选择DC-class density。[[networking/Srv6 powered backbone networks.pdf#page=4|PDF p.4]][[networking/Srv6 powered backbone networks.pdf#page=5|PDF p.5]]
- SRv6的选择有具体QoS编码需求：作者Olympic QoS需6类strict priority，其MPLS编码只能4类；这是其编码方案限制，不可概括为所有MPLS只能4类。[[networking/Srv6 powered backbone networks.pdf#page=7|PDF p.7]]
- control plane每plane controller每30秒运行五类调用，FRR在controller之下；30秒TE周期不是故障恢复时延。[[networking/Srv6 powered backbone networks.pdf#page=9|PDF p.9]]

## 指标与条件
GLIDE实验单向5ms，达到link 70%目标、common-case约7%buffer；4.5:1 incast会填满32–53MB。既没有证明满线速，也没有证明极端incast不需要缓冲。[[networking/Srv6 powered backbone networks.pdf#page=6|PDF p.6]]

## 图表与架构
已核p.6条形示意与文字，70%和7%分别属于link与buffer分母，不可当成“吞吐提升10倍”。uSID每hop消费16bit，超过6项用End.B6.Encaps.Red拼接；每adjacency一条mySID而非每path一条。[[networking/Srv6 powered backbone networks.pdf#page=8|PDF p.8]]

## 关联与比较
[[knowledge/concepts/network-buffer-workload-placement]]；[[knowledge/comparisons/network-transport-and-buffer-context]]；[[knowledge/sources/src-c4cafad20442]]的BAG则为长距RoCE保留深buffer/credit与距离headroom。

## 不确定性与待验证
缺少ECN threshold、GLIDE状态机、流大小分布、loss/p99和incast恢复曲线；SAI在FRR monitored-object down与class-based forwarding上仍有规范缺口。[[networking/Srv6 powered backbone networks.pdf#page=11|PDF p.11]] 不能把GLIDE结果直接移植到未配套CC的NIC。
