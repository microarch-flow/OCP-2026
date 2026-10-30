---
id: "src-8be3bec59f09"
type: "source"
title: "Advancing Open AI Infrastructure Management through Community and Ecosystem Collaboration"
source_path: "executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf"
source_git_blob_sha: "e4e63fd97435eb6cd6f63af1c5fc1b360cfc187f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 6, 7, 8, 9, 11]
text_reviewed: true
key_pages_visual_checked: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-system-control-evidence]]"]
extraction_note: "全文图像文字经 OCR 辅助阅读并视觉复核"
---

# Advancing Open AI Infrastructure Management through Community and Ecosystem Collaboration

## 核心结论
- MiTAC 展示从 OpenBMC/OPF 到 MiRMC rack manager，再到 MiCoreView POD manager 的分层管理路线；开放固件是硬件交付之后可观测性、补丁和多厂商运营的基础之一。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=2|PDF p.2]][[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=7|PDF p.7]][[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=8|PDF p.8]]
- 这是一份生态/产品架构材料，不是开源固件自动更安全或更便宜的实验。p.3 的开源/闭源二分比较含厂商立场，不可当作所有实现的事实。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=3|PDF p.3]]
## 关键证据
- p.6 明确指出 Intel/AMD 固件栈没有统一接口，希望通过 openSFI/UPCI 减少平台碎片化；因此“开源”不等于已经可直接跨 silicon 互换。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=6|PDF p.6]]
- MiRMC 在 OpenBMC 服务上扩展资源聚合、拓扑/库存、事件和 rack power/cooling；POD 层再接 Redfish、IPMI、SNMP、PLDM。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=8|PDF p.8]][[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=9|PDF p.9]]
- AMD MI355/EPYC 示例包含 ROCm、AMD Enterprise AI Suite、Rafay、DDN、Ubuntu；p.11 对 MiRMC FW 仍标 Coming Soon。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=11|PDF p.11]]
## 指标与条件
材料没有给管理规模上限、遥测频率、固件升级成功率、故障恢复时间或节省的人时。OpenRMC 1.3 是架构版本，不能作为性能数字。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=7|PDF p.7]]
## 图表与架构
原始文字几乎只有页眉；已对全部 13 页 OCR 并逐页视觉检查，实际分析以图中文字为准。p.7 注明架构图来自 OCP Global Summit 2025，但这不是本次整份演讲日期证明。
## 关联与比较
对 accelerator 交付，应把 CPU/GPU 软件栈与独立的管理平面一同验收：接入统一 API、上游补丁、产品分支 LTS 和 rack 事件关联，都是规模运营能力。[[executive-sessions/05_Advancing Open AI Infrastructure Management through Community and Ecos.pdf#page=4|PDF p.4]]
## 不确定性与待验证
需核实开放仓库的实际许可证、代码覆盖范围、上游合入状态、版本兼容矩阵及可审计更新流程；生态 logo 和演示界面不等于生产客户验证。

## 知识网络
[[knowledge/concepts/executive-expo-system-control-evidence]]
