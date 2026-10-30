---
id: "src-273c2c87ddf0"
type: "source"
title: "Arm与Meta：AGI CPU双节点参考设计的复用边界"
source_path: "expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf"
source_git_blob_sha: "102cd8549e05bf2a1a30b59fa2f867c45d0d7f0e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 10, 11]
text_reviewed: true
key_pages_visual_checked: [4, 7, 11]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# Arm与Meta：AGI CPU双节点参考设计的复用边界

## 核心结论
资料的确定价值是从单CPU到ORv3、DC-MHS、DC-SCM及固件的参考设计复用，帮助Yosemite V5与Rainier HPM两条平台少改板；不是可复现的“Arm比x86快2倍”实验。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=4|PDF p.4]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=6|PDF p.6]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=11|PDF p.11]]

## 关键证据、指标与条件
- 参考服务器1OU双节点，列136 Neoverse V3AE核、12DDR5 DIMM最高8400MT/s、96lane PCIe6/CXL3.0。本文按CPU/节点规格理解，不把双节点机箱总数与单芯片混算；材料没有整机功率/带宽实测。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=4|PDF p.4]]
- Yosemite V5是半宽1OU节点、12通道DDR5-8000、9.5mm和25mm E1.S各1、每机箱6服务器；不能把“每机箱6”误读成每1OU六节点。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=7|PDF p.7]]
- Rainier使用DC-MHS SDNO B305、PICPWR2×3、OCP NIC/DC-SCM及innovation area两E1.S，称PVT后贡献OCP，属于未完成交付条件。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=8|PDF p.8]]
- p3列DC-SCM2.0、p4又列2.1，需锁定实际版本。设计/用户手册、原理图、布局、BOM、参考BIOS/BMC在NDA下提供；“open alignment”并不意味着全部工程资料已公开许可。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=3|PDF p.3]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=4|PDF p.4]]

## 图表与架构
已看p4/7实物及p11宣传页。2× performance at scale带星号/二维码，文件没有基线、工作负载、功率或统计方法，不能用作采购ROI输入。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=11|PDF p.11]] p10又明确部分标准贡献进行中、服务器规格为未来贡献，需与可取得参考设计区分。[[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]；与Intel agentic rack可比较设计目标和资源分工，不能用Intel EMR router会话数与本文件2×宣传作CPU性能横评。

## 不确定性与待验证
补齐每节点/每机箱供电、风量、内存容量、NUMA/IO拓扑、固件版本、开源许可及Arm软件迁移成本；测试真实工具链和p99，避免仅凭核数与空气冷却宣称TCO改善。


跨源比较：[[knowledge/comparisons/expo-inference-cost-contract]]。
