---
id: "src-58ce2a4bef6e"
type: "source"
title: "IREN 端到端自动化：可执行设计意图比单独配网更重要"
source_path: "networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf"
source_git_blob_sha: "86aeca2253070a7d8dfd80b8f6c5547e5c42310b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-text"
evidence_pages: [4, 7, 8, 9, 10, 12]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-inference-acceptance]]"]
---

# IREN 端到端自动化：可执行设计意图比单独配网更重要

## 核心结论
案例最有用的经验是区分“能根据 JSON 配置网络”与“有可执行 RA 持续发现漂移”。物理布线、光错误与 NIC/交换机 RoCE 参数必须在 Day 0 一起验证，不能等训练异常后逐域排查。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=8|PDF p.8]][[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=9|PDF p.9]][[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=10|PDF p.10]]

## 关键证据、指标与条件
- 首次 AMD/Micas/Broadcom SONiC 部署没有编码 RA，只有端口 spreadsheet；平台发现拓扑后交给 MCP 做模式识别，定位缺失/错接线，但承认不能自动告警所有错线。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=8|PDF p.8]]
- CRC/FEC 相对基线的异常触发检查、清理或更换光纤；向 GPU 与交换机推同一 RoCE profile，包含 queue/ECN/PFC。这里只是这个部署的 lossless 选择，不是所有 AI 网络应启用 PFC 的证明。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=9|PDF p.9]]
- 后续 Childress/MacKenzie 计划采用 NVIDIA NCP RA 2.1.2，设计意图才可用于持续 drift alert。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=10|PDF p.10]]
- “bare metal 到 tokens-ready <2小时”未列节点数量、开始/结束边界、模型及基线；“MTTR 降 95%”和“100% privacy”也未给统计与威胁模型。不能纳入可比较 ROI 指标。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=4|PDF p.4]][[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=12|PDF p.12]]

## 图表与架构
已读全文，未核图。材料明确 on-prem/local LLM、图数据库、遥测时序库，以及变更推送前人工批准；不是已经证明无监督自治安全。[[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=7|PDF p.7]][[networking/Networking In Silo is Not Enough - Building End-to-End Automation for AI Factories the IREN Use Case.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/network-inference-acceptance]]：建议把 time-to-first-token 的交付定义拆成设备发现、拓扑验收、链路质量、RDMA 基线与真实模型 SLO，分别保存证据。

## 不确定性与待验证
营销页的电力/收入/市场叙事不用于本卡技术结论。需固定测试规模、变更回滚与批准审计、异常漏报率、RA 版本差异；本地运行并不自动排除供应链、权限或日志泄漏风险。

