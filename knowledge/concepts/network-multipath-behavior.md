---
id: "network-multipath-behavior"
type: "concept"
title: "多路径传输：选择路径、控制在途量与时序互通"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 多路径传输：选择路径、控制在途量与时序互通

## 定义
“哪里发”与“发多少”耦合。ECMP、packet spray、ReSS、source route不是同义词；拥塞/故障恢复取决于信号采样、RTT/RTO、重传和路径切换行为。

## 来源与差异
MRC ReSS保留少量active subflows并替换最拥塞者，SMaRTT结合ECN/RTT/optional trim；规格若不约定测RTT的位置、reserved bits和重传规则，仅格式一致仍不足。[[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=8|PDF p.8]][[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=9|PDF p.9]][[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=13|PDF p.13]]
SRv6把选定uSID path交给source NIC，switch strict route，提供确定路径表达，而不是自动实现CC。[[knowledge/sources/src-badf54452e3e]] [[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=11|PDF p.11]]
MetaRoCE把多路径封进QP，以SACK精确重传和per-tag streams避免连接内阻塞，依赖best-effort+ECN而非PFC losslessness。[[knowledge/sources/src-f76571507532]] [[networking/MetaRoCE in Software.pdf#page=2|PDF p.2]]

## 跨源归纳
故障时“吞吐恢复”至少拆为detect→feedback→path remove→retransmit→queue drain→应用恢复。75K job案例显示MRC移路早于switch reboot，但时间线无刻度，因此无法给恢复ms SLA。[[knowledge/sources/src-badf54452e3e]] [[networking/SRv6 Deployments in Scale-Out and Scale-Across Networks.pdf#page=13|PDF p.13]] MRC Cluster B吞吐图是单独20-link-failure实验，不可合并成生产75K的p99证据。[[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=10|PDF p.10]]

## 互通验收
Level1 packet fields、Level2 algorithm、Level3 signal frequency/reaction latency三层分别测试。两NIC都“支持MRC”不代表同一网络下公平收敛；packet parsing通了以后还需拥塞增长/退避速率和loss/RTO组合。[[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=14|PDF p.14]][[knowledge/sources/src-f13077d44cf0]] [[networking/MRC- A Purpose-Built RDMA Transport for AI Training Networks.pdf#page=15|PDF p.15]]

## 未决问题
推理短流、mixed NIC、per-path state资源、乱序buffer、极端incast与频繁flap的尾延迟尚缺统一数据。

## 关联
[[knowledge/concepts/network-executable-validation]] · [[knowledge/comparisons/network-transport-and-buffer-context]] · [[knowledge/concepts/network-ocs-control]]
