---
id: "src-37ae5f901b3d"
type: "source"
title: "Astera 混合 scale-up：铜保留在何处，光从何处进入"
source_path: "ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf"
source_git_blob_sha: "2db7b72a232d7af0b480b0c6fa179abe86f6d867"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [4, 5, 7, 8, 9, 10, 11, 12, 14]
text_reviewed: true
key_pages_visual_checked: [8, 14]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Astera 混合 scale-up：铜保留在何处，光从何处进入

## 核心结论
对推理架构最有用的是五维决策框架：功率、成本、交付速度、可靠性/服务、性能。铜与光可共存，NPO/CPO的选型应由实际距离、拓扑和维修边界驱动，而非按GPU数量硬切换。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=4|PDF p.4]][[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=12|PDF p.12]]

## 关键证据、指标与条件
- 演讲把训练概括为长持续collective/更大距离，推理为短burst/时延敏感/每美元带宽；这是场景简化，不覆盖跨机柜MoE、PD分离或大KV流量等所有推理。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=5|PDF p.5]]
- 图示DAC≤3m、ACC≤4m、AEC≤7m，LPO/NPO/CPO>50m，没有数据率/损耗/FEC统一条件，因此不是技术硬reach上限。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=8|PDF p.8]]
- NPO强调现有模块制造生态、电可拆、板上纤维与较小FRU；CPO强调高radix/短电通道，但封装yield、测试和供应链尚在演进。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=9|PDF p.9]][[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=10|PDF p.10]][[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=11|PDF p.11]]
- 72–576 accelerator的hybrid pod示意为柜内铜背板、柜间NPO；>576为独立compute/switch racks的全光pod。是目标布局，不是实测最优分界或产品可扩展上限。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=14|PDF p.14]]

## 图表与架构
已核介质位置示意及两种pod图。p.7“Lowest bandwidth per dollar”与正文低成本主张字面相反，可能想表达lowest cost per bandwidth；本卡不擅改成定量收益。[[ocp-special-focus-photonics/Light-on-the-Horizon-Architecting-Scale-Up-Fabrics-with-NPO-CPO-for-the-Next-Gen-Data-Center.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]、[[knowledge/concepts/network-inference-acceptance]]：先把TP/EP/KV在机柜平面上的实际通信图画出，再决定哪些边需要optical reach与哪些边保留铜的成本优势。

## 不确定性与待验证
没有每bit功耗、延迟、实际距离测试、价格或MFU数据。“超过144GPU需光”依赖密度/拓扑，不是物理定律。需同时评估增大scale-up域后的同步尾部、故障影响和软件可用性。

