---
id: "src-2244c05beeab"
type: "source"
title: "PLDM诊断数据面：统一发现与传输，不统一所有载荷"
source_path: "manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf"
source_git_blob_sha: "116632c4e958065a68a3f2dbb6a2c2b1483f3f96"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
tags: ["ocp", "source", "platform", "manageability-workshop"]
text_reviewed: true
key_pages_visual_checked: [6, 12]
updated: "2026-10-30"
---

# PLDM诊断数据面：统一发现与传输，不统一所有载荷

> 阅读范围：已阅读本文件全部可提取文字（15页）。关键页已视觉核对：6, 12；不代表逐页视觉审核。

## 核心结论

- Bulk telemetry、crash dump、timer/watchdog复用现有PLDM基础/文件传输/监控控制，而非另造transport；标准化重点是发现、控制、传输，载荷语义仍可由厂商或其他标准定义。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=3|PDF p.3]][[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=4|PDF p.4]]
- 参考架构让BMC取走并转发不透明数据，分析放OpenTelemetry collector；BMC无需理解所有厂商内容，但下游仍需对应解析插件/metadata。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=6|PDF p.6]][[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=9|PDF p.9]]

## 关键证据

- bulk数据有file、snapshot、SerialTxFIFO streaming和独立telemetry events四类行为，metadata可选。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=5|PDF p.5]]
- Crash dump可由错误事件或人工触发，单/多文件、多实例皆允许。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=7|PDF p.7]][[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=8|PDF p.8]]
- Timer不需周期刷新，watchdog需agent刷新且超时触发动作；动作仍可厂商定义，包括事件、telemetry或crash dump。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=10|PDF p.10]][[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=11|PDF p.11]]
- Redfish对齐TelemetryService/TelemetryData、LogService、HostWatchdogTimer是informative关联，不替代PMCI要求。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=13|PDF p.13]]

## 指标与条件

没有bulk吞吐、采样率、BMC CPU利用率、crash dump生成时延或watchdog恢复时长数据；“减少定制”是结构收益而非测量。

## 图表与架构

已视觉核对p.6collector数据流与p.12 timer状态/实体示例：状态sensor/effecter与计数/timeout数值接口分开。未声称所有超时动作都强制reset。

## 关联与比较

连接[[knowledge/sources/src-130c021db4d4|GPU可观测性]]的分层证据方案：标准传输解决取数，metadata/解析器与时间关联解决可解释性，两者都必需。

## 不确定性与待验证

文件为WIP；明确要求完善Redfish数据模型和PLDM→Redfish转发。需补背压、丢样、buffer占用、安全权限和敏感dump脱敏。[[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=2|PDF p.2]][[manageability-workshop/PLDM-Modeling-for-Common-Crash-Dump-Bulk-Telemetry-and-Watchdog-Timer-Access.pdf#page=14|PDF p.14]]

