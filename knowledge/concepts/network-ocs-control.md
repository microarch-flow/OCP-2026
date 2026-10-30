---
id: "network-ocs-control"
type: "concept"
title: "OCS控制：光路意图、完成状态与预测误差预算"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# OCS控制：光路意图、完成状态与预测误差预算

## 定义
OCS重构纯光连接；交换机数据路径没有packet buffer，不代表切换控制无停顿。端到端闭环需intent→connect→settle→link-ready→traffic→drain→rollback，并明确fallback。

## 标准接口与调度是不同层
OpenConfig/gNMI草案区分connection intent与port实际状态，支持capability/reboot恢复策略；不同robotic/beam-steering/SiPh技术的速度与维护不同。[[knowledge/sources/src-8fba6503c4b7]] [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=9|PDF p.9]][[knowledge/sources/src-8fba6503c4b7]] [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=10|PDF p.10]][[knowledge/sources/src-8fba6503c4b7]] [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=12|PDF p.12]][[knowledge/sources/src-8fba6503c4b7]] [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=13|PDF p.13]]
GPUland实验展示早结束一轮电路会将event-triggered后续round推到trickle路径；绝对time-triggered rounds能消除该实验的级联cliff。但使用7×T4、veth/tc模拟、单kernel clock，不是真实光机。[[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=4|PDF p.4]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=8|PDF p.8]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=10|PDF p.10]]

## 综合设计判断
先用profile筛掉已被compute overlap隐藏或只留在NVLink域内的流量；剩余必须exposed、contended且可预测，才有机会偿还切换与guard band。更快OCS器件不能自动解决predictor误差、round耦合和fallback容量。[[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=2|PDF p.2]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=7|PDF p.7]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=14|PDF p.14]]

## 推理/商业边界
MoE all-to-all看似适合full-bisection需求，但来源明确MoE未测。在线推理请求到达、专家路由和短流更不规则，因此此处只能提出试验计划，不能承诺tokens/s、p99或成本回报。[[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=11|PDF p.11]]

OCS<5%电交换功耗缺同口径系统边界，须补端点光模块、laser、controller、fallback以及capacity slack后再算TCO。[[knowledge/sources/src-8fba6503c4b7]] [[networking/Standardizing OCS Interfaces for Seamless Integration.pdf#page=2|PDF p.2]]

## 未决问题
绝对时钟接口如何暴露给collective？Set到光路settle再到PCS/FEC link-ready多久？失败时怎样撤销schedule而不丢并发intent？共享连接器或laser的blast radius如何影响恢复？

## 关联
[[knowledge/concepts/network-clock-evidence]] · [[knowledge/concepts/network-multipath-behavior]] · [[knowledge/concepts/network-optical-integration]]
