---
id: "network-scaleup-ethernet"
type: "concept"
title: "Scale-up Ethernet：紧凑 framing、局部重试与端点边界"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# Scale-up Ethernet：紧凑 framing、局部重试与端点边界

## 定义
Scale-up fabric强调短消息效率、低时延、高radix与故障可控；开放Ethernet方案可以复用生态，但必须明确fabric和endpoint transport/内存语义的边界。

## 证据
ESUN 1.0的4B EH header替换28–48B IP/UDP区，保留ECN、CoS、16b flow label、TTL；E2E transport/CRC仍在后面。[[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=7|PDF p.7]][[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=8|PDF p.8]] UEC定义LLR/CBFC，前者局部重传、后者防overflow与减小buffer，但本文没有测量recovery latency/credit预算。[[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=9|PDF p.9]]
SRv6演讲列32/64/128B效率、single-header、strict source route、two-tier与>576radix作为scale-up诉求，不能当已交付规格。[[knowledge/sources/src-badf54452e3e]] [[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=15|PDF p.15]]
MetaRoCE软件层可替换wire envelope到ESUN/PSP，说明端点可靠transport与fabric framing可独立演进。[[knowledge/sources/src-f76571507532]] [[networking/MetaRoCE in Software.pdf#page=11|PDF p.11]]

## 共识与适用条件
这里的共识是协议开销与可靠性机制要共同设计，而非“以太网现成芯片即可无成本替代所有scale-up互连”。应单独预算FEC、LLR replay、credit RTT、header/IPG、endpoint processing和queueing。

## 未决问题
无统一p99/energy/endpoint buffer结果；缺少deadlock/virtual channel、load-store/一致性语义、故障降lane行为。1.1许多项在演讲时WIP，不把路线图当现成能力。[[knowledge/sources/src-6415268b7f70]] [[networking/ESUN- Open Ethernet for the AI Scale-Up Era.pdf#page=10|PDF p.10]]

## 关联
[[knowledge/concepts/network-multipath-behavior]] · [[knowledge/concepts/network-executable-validation]]
