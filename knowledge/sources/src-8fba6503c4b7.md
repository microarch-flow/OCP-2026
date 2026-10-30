---
id: "src-8fba6503c4b7"
type: "source"
title: "Standardizing OCS Interfaces for Seamless Integration"
source_path: "networking/Standardizing OCS Interfaces for Seamless Integration.pdf"
source_git_blob_sha: "d5cdfeee57ababaf2796ed5fe7a75d8a066a05f1"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-text"
evidence_pages: [2, 6, 7, 8, 9, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp-2026", "networking"]
concepts: ["[[knowledge/concepts/network-ocs-control]]"]
---

# Standardizing OCS Interfaces for Seamless Integration

## 核心结论
OCS的标准化重点是把“连接意图”和“当前光路状态”分开建模，并复用OpenConfig/gNMI管理生态；共同API不意味着不同光开关技术具有相同reconfiguration时间、维护方式或断电恢复语义。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=6|PDF p.6]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=8|PDF p.8]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=9|PDF p.9]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=13|PDF p.13]]

## 关键证据
- OCS建立纯光input-output paths，不做O-E-O/packet queuing；因此对bit rate/protocol较透明，但并不代替端点transceiver和整网调度。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=2|PDF p.2]]
- OpenConfig YANG + gNMI Get/Set/Subscribe复用配置/streaming telemetry；forwarding control、capability discovery、restoration与port health需OCS扩展。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=6|PDF p.6]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=7|PDF p.7]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=8|PDF p.8]]
- any-any与some-some、fast beam steering/SiPh与slow robotic、active/passive maintenance、reboot的maintain/remake/remove必须显式发现。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=9|PDF p.9]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=10|PDF p.10]]
- port state含OFF/BLOCKED/FAILED/TUNING/TUNED/UNKNOWN；connection intent另含CONNECTED/CONNECTING/DELETING/FAILED/INVALID，不能把Set成功当光路已经可用。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=11|PDF p.11]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=12|PDF p.12]]

## 指标与条件
p.2宣称OCS功耗低于传统electrical packet switch的5%，但没有给radix、port speed、laser/transceiver计入范围或实验平台；仅保留为作者概括，不作为系统TCO定量输入。v0.8在演讲时为draft，multicast/unidirectional等niche features尚未完整覆盖。[[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=9|PDF p.9]][[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=14|PDF p.14]]

## 图表与架构
全文文字已读，未视觉核图；schema文本可核到配置与状态分离。p.11将input/output-optical-power-dbm字段写成uint32，负dBm/精度的表达需回到正式schema核实，不擅自修正为另一类型。

## 关联与比较
[[knowledge/concepts/network-ocs-control]]；[[knowledge/concepts/network-multipath-behavior]]。OCS重构拓扑与MRC/SRv6在既定路径上重路由是不同控制层，需共同定义drain、settle、link retrain与rollback。

## 不确定性与待验证
没有reconfiguration/settling distribution、光预算、损耗、故障恢复p99或流量迁移算法。纯光数据路径无packet queue不代表控制操作零停顿，也不代表网络无需security controls。
