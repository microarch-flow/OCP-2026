---
id: "network-time-budget-contract"
type: "concept"
title: "AI网络的时间预算：时钟准确度、抖动、编程与预测误差"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# AI网络的时间预算：时钟准确度、抖动、编程与预测误差

## 定义
“需要更准的时钟”常混合五种不同问题：绝对时间可信度、节点间同步、timestamp采集路径、控制面编程延迟、未来流量预测误差。一个ns数字无法代替其余四项。本页为跨源分解。

## 证据与误差归属
- **信任**：多参考源/holdover要检测并隔离异常；多GNSS receiver未必独立，因为可共享干扰/欺骗环境。Timecard带保护能力不等于已获某个认证。[[knowledge/sources/src-fef1d5b111ed]] [[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=16|PDF p.16]][[knowledge/sources/src-fef1d5b111ed]] [[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=17|PDF p.17]]
- **局部相对同步**：Intel提出rack-local≤2hop辅助时间与global UTC并存，避免为了跨全网统一absolute time牺牲局部性能；<50ns是能力方向，不是整机房实测。[[knowledge/sources/src-aba4b9355d9b]] [[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=4|PDF p.4]][[knowledge/sources/src-aba4b9355d9b]] [[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=6|PDF p.6]]
- **采集路径**：ePPS方案NIC输出和host输出有ns级p-p数据，但host表min/max与列出的p-p不一致；OTS-C虽称±1µs，图有越界点，且Chrony估计offset不是外部绝对测量。必须保留测量仪器、参考源与统计量。[[knowledge/sources/src-25482e5ef2a3]] [[Time Appliances/Timing Recovery Using PTP within NIC and Distribution by ePPS to Computing Modules.pdf#page=10|PDF p.10]][[knowledge/sources/src-a9eed6924fac]] [[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=6|PDF p.6]]
- **尾部概率**：SiTime TTU把确定项+Q倍RMS组预算，fleet PE公式还需时间机会数与相关性。RMS、peak和年失败概率不可互换。[[knowledge/sources/src-a1c813b65c00]] [[Time Appliances/Bounding Time Uncertainty in Distributed Systems.pdf#page=5|PDF p.5]][[knowledge/sources/src-a1c813b65c00]] [[Time Appliances/Bounding Time Uncertainty in Distributed Systems.pdf#page=7|PDF p.7]]
- **配置与执行**：SAI PerfMon只测SDK边界逐对象API成本，排除了IPC/排队，也不保证硬件何时生效；不能用它当OCS或路由切换端到端时间。[[knowledge/sources/src-f96b2b46b138]] [[networking/02_Closing the Observability Loop in SAI From Performance Telemetry to Pl.pdf#page=11|PDF p.11]][[knowledge/sources/src-f96b2b46b138]] [[networking/02_Closing the Observability Loop in SAI From Performance Telemetry to Pl.pdf#page=12|PDF p.12]]
- **预测窗口**：时隙电路实验用共享kernel clock、tc/veth而非真实OCS/PTP；在预测σ60ms时slack10→180ms，完成时间7.5→1.16s。主要损失是schedule误配，不是ns同步不足。[[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=4|PDF p.4]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=7|PDF p.7]]

## 怎样写可执行合同
每次动作记录：intent版本、预计生效时刻、允许误差窗、实际设备状态、端点观测和rollback条件。每条telemetry记录身份、时间基准、WOU、freshness、support/quality，缺失不可填零。需要跨设备因果顺序时，两个WOU重叠就不宣称确定先后。[[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=5|PDF p.5]][[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=6|PDF p.6]]

## 适用边界与未决问题
高radix交换仿真中按精确到达时间调度可降p99.99，但该结果是特定1000port/负载下Monte Carlo，不是网络已具备确定性在线推理SLO。[[knowledge/sources/src-2715b9f53773]] [[Time Appliances/High Radix Switches and Precise Time.pdf#page=20|PDF p.20]] 下一步优先测“谁造成哪段不确定度”，再决定预算投向PTP/PTM、事件采集、固件执行或workload预测。[[knowledge/concepts/network-clock-evidence]] · [[knowledge/concepts/network-ocs-control]]

