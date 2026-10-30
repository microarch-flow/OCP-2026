---
id: "src-a4497dec3bd9"
type: "source"
title: "Architecting Openness: How Switches Enable the Future of Open Adapter Card Platforms"
aliases: ["Architecting Openness: How Switches Enable the Future of Open Adapter Card Platforms"]
speakers: "Chris Blackburn（Astera Labs）"
source_path: "server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf"
source_git_blob_sha: "6e688bef4b45d552188295fb47515a7e27577b4e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 6, 7, 8]
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 12]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-modular-platform-contract]]", "[[knowledge/concepts/compute-memory-kv-placement]]"]
---

# Architecting Openness: How Switches Enable the Future of Open Adapter Card Platforms

## 核心结论
OAC平台至少有两张不同网络：XPU scale-up fabric 与连接CPU/XPU/NIC/SSD的PCIe fabric。机械卡槽统一并不规定唯一拓扑；应同时选择switch radix、设备数、链路宽度、带宽分配和管理边界。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=4|PDF p.4]] [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=5|PDF p.5]]

## 关键证据
p.6展示8/16XPU单switch或多switch方案；p.8展示集中、按CPU分组和分层/分散PCIe交换。不同拓扑可能改变hop、oversubscription、P2P locality与故障域，不能仅按“支持设备数量”选型。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=6|PDF p.6]] [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=8|PDF p.8]]

## 指标与条件
例子1–2CPU、8–16XPU、8NIC、8–16SSD说明host port预算压力，不是实测非阻塞吞吐。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=7|PDF p.7]]
p.3把OAC5000W、112 scale-up lanes列为示意并明确spec仍开发、数字未必被规范写死；与其他OAC演讲合看时需保留版本/条件。没有switch latency、power或端到端训练/推理数据。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=3|PDF p.3]]

## 图表与架构
作者提出高radix、不同port/lane选项、小面积低功率、link health/bandwidth telemetry；“non-blocking/low latency”是feature目标，需给流量矩阵和uplink配置才可验证。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=9|PDF p.9]] [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]]：协议开放不自动使不同switch在任意fabric互通。[[knowledge/concepts/compute-memory-kv-placement|KV放置]]：若存储/内存绕经不同PCIe子树，数据路径不能用统一link BW替代。

## 不确定性与待验证
实际lane mapping、P2P路由、ACS/IOMMU隔离、reset containment、multi-host ownership及热预算未完整列出。p.12仍以“能否达到PCIe AIC式真正互通”提问，不能写成已完成全面跨vendor互换。

## 原始页码导航
[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=3|p.3]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=4|p.4]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=5|p.5]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=6|p.6]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=7|p.7]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=8|p.8]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=9|p.9]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=10|p.10]] · [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=12|p.12]]
