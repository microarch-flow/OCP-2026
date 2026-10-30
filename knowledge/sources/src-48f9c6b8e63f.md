---
id: "src-48f9c6b8e63f"
type: "source"
title: "Multi-planar-AI-Scale-Out-Fabrics"
source_path: "ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf"
source_git_blob_sha: "9c8082d4d5a96c51172899c58f7857a6ba02b176"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [4, 5, 8, 9, 10, 11, 12, 13, 14, 16]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [5, 13, 14, 16]
concepts: ["[[knowledge/concepts/ai-infra-multipath-failure-domains]]"]
---

# Multi-planar-AI-Scale-Out-Fabrics

## 核心结论
Arista/AMD的multiplanar设计用端点跨所有独立planes承担喷洒、OOO处理与故障绕行，减少fabric层数；难点从交换网络部分转移到NIC的路径状态、物理fanout和失效检测。[[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=4|PDF p.4]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=8|PDF p.8]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=9|PDF p.9]]

## 关键证据
MRC entropy value可映射固定plane并标记GOOD/SKIP，SRv6显式路径模式不必再依赖ECMP；OOO direct placement不同于把所有包先缓存重排。[[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=12|PDF p.12]]

## 指标与条件
p.5两层1:1理论容量k²/2：102.4T交换机800G radix128→8192 client ports，200G radix512→131072；这不是实装GPU规模。p.13示例6912GPU/96racks/2×800G/2planes，p.14示例16128GPU/224racks/8×200G、两层上限129024；工程布局上限与理想公式不同。[[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=5|PDF p.5]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=13|PDF p.13]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=14|PDF p.14]]
真正列出的validation cluster是504GPU、7Helios racks、8×200G planes、4rails，Arista7060XE7/TH6/EOS、1.6T DR8和8×8 shuffler；支持测试MRC native IPv6与SRv6 uSID/ECMP配置，但未报告测试结果。[[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=16|PDF p.16]]

## 图表与架构
已看理论规模表、两种设计图和validation cluster。Helios参考机架18×4GPU compute trays与6switch trays；每GPU一/两800G NIC，1.6T cage可共享两GPU，不能把cage速率直接当每GPU带宽。[[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=10|PDF p.10]] [[ai-clusters/Multi-planar-AI-Scale-Out-Fabrics.pdf#page=11|PDF p.11]]

## 关联与比较
[[knowledge/concepts/ai-infra-multipath-failure-domains]]；[[knowledge/comparisons/ai-infra-mrc-uet-and-fabric-layers]]。

## 不确定性与待验证
缺plane慢而不死、远端partial failure、探测开销、吞吐公平性、恢复时间及p99数据；不能把504GPU validation配置称为16K GPU已验证结果。
