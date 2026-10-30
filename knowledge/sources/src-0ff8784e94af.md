---
id: "src-0ff8784e94af"
type: "source"
title: "CPO+OCS+SDN：多厂商光加速集群与共享备件池"
source_path: "networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf"
source_git_blob_sha: "083f02c2240be395aaa73cff74fb5f3ca3e2e33a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [3, 6, 8, 9, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [8, 12]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-ocs-control]]"]
---

# CPO+OCS+SDN：多厂商光加速集群与共享备件池

## 核心结论
这里提出的是 EPS 细粒度包路由与 OCS 粗粒度物理重连的混合架构；1:N 共享备用交换机/加速器有潜在资本效率，但光路重接不能自动迁移计算状态或无损恢复 collective。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=6|PDF p.6]][[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=8|PDF p.8]][[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=10|PDF p.10]]

## 关键证据、指标与条件
- 通过中间 OCS 层把失败 leaf 或 XPU 换接到共享 spare pool，目标从 1:1 保护走向 1:N；未给 N、并发故障分布、备件可达矩阵或恢复时长。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=8|PDF p.8]]
- 按 collective 通信模式绕过 spine/leaf 是第二用例，作者承认需要 AI 阶段可见性、NCCL 等软件协同，因为重构期间光路中断会影响 RoCEv2。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=9|PDF p.9]][[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=10|PDF p.10]]
- 标准 YANG/gNMI 可避免每家私有模型 translator，但不意味着各 OCS 切换时延、光损和生命周期一致。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=11|PDF p.11]]
- OFC2027 互操作演示为规划中的 PoC；图示 8 家 OCS、6 active xPU+2 spare、2 packet switch，是目标拓扑不是已经完成的跨厂商生产证据。控制器当时仍为 proprietary，开源为后续诉求。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=12|PDF p.12]][[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=13|PDF p.13]][[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=14|PDF p.14]]

## 图表与架构
已核共享备用路径与 demo 结构。正文 p.3 的 131072 GPU→15分钟 MTBF 没给可核的器件失效率/独立性推导，不能作为采购故障率。[[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=3|PDF p.3]]

## 关联与比较
[[knowledge/concepts/network-ocs-control]]：与时隙电路预测误差、OpenConfig intent/state、零接触验证共同说明“有控制接口”离“安全重构 AI 作业”还有多个环节。

## 不确定性与待验证
需要故障检测→决策→重连→链路训练→路由更新→作业恢复的端到端分布，并计 OCS 本身、共享激光/连接器的共同失效及光预算；未展示吞吐、p99 或净 CapEx 降幅。

