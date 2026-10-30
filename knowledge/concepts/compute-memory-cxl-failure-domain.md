---
type: concept
title: "CXL 扩容：把故障域与可观测性计入容量成本"
tags: [ocp2026, concept, compute-memory]
---

# CXL 扩容：把故障域与可观测性计入容量成本

## 结论
CXL 不只是“在 CPU/GPU 外接更便宜的 GB”。要比较可用的容量成本，应同时描述访问路径、故障传播边界、可观测性和恢复行为。

## 本库证据
- [[knowledge/sources/src-38d499006926|Meta fleet 经验]]：设备内部多种故障会坍缩成相同 read timeout；主机看到 MCE 不足以定位 DIMM、控制器或固件。设备协议合规与 fleet 可诊断性是两种属性。
- [[knowledge/sources/src-fcfa27796971|Physical AI FCSA 提案]]：跨 chiplet safety 要在 package 层组合，D2D 既传播故障也承载诊断信号。它提供跨域对照，但不表示 CXL 数据中心必须采用 Physical AI 认证。

## 架构比较应列出的字段
| 层 | 要问的问题 | 对推理系统的意义（分析推论） |
|---|---|---|
| 数据路径 | host staging、P2P、load/store、DMA？共享哪条链路？ | 决定搬运、排队和反压 |
| 故障域 | DIMM、expander、host、pool 谁会失效？ | 决定单次失效损失多少会话/KV |
| 可观测性 | 带外 heartbeat、持久错误日志、每端口/每 media 计数器？ | 避免故障后只剩主机 timeout |
| 隔离恢复 | poison/隔离/热替换/进程重试/整机重启？ | TTFT、TPOT 与 p99 恢复尾部不同 |
| 调度契约 | 故障资源可否撤回？数据能否重建？ | KV 迁移、重预填充与 admission control |

## 用于成本模型的假设，非演讲测量
可把单位有效 token 成本表示为总成本除以 **满足 SLO 的成功 token**，而非标称 tokens/s。故障重试、重预填充和在途任务损失均计入分母减少/额外计算。当前源文件没有足够数据估计这些项，不应填入猜测的 failure rate。

## 给 架构探索 DSL/IR 的可实现问题
给 memory-tier/link/resource 定义 `failure_domain_id`、`observable_events`、`recovery_policy`，在仿真中注入失效事件；比较平稳吞吐和恢复窗口内的分位延迟。此为本库建议，不是材料中已实现的 架构探索 DSL/IR 功能。

## 待验证
真实错误率、MTTR、错误分类准确率、带外路径存活性，以及“低成本容量扩容”是否保持相同服务可靠性。
