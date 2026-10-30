---
id: "src-34bf8c349f5b"
type: "source"
title: "Open Rack-Scale Optical Infrastructure for AI Scale-Up with Co-Packaged Optics"
source_path: "fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf"
source_git_blob_sha: "2f9a4101e44bf98b0a98d226d743209fa7ef9c29"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [2, 8]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Open Rack-Scale Optical Infrastructure for AI Scale-Up with Co-Packaged Optics

## 核心结论
Wiwynn/Ayar从1024ASIC scale-up目标反推rack、tray、fiber、power与package，提醒光IO不是只把铜线换成fiber：front-panel ELS、双热域、PM fiber走线和跨vendor测试边界共同限制系统。[[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=3|PDF p.3]][[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=5|PDF p.5]][[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=6|PDF p.6]]

## 关键证据
单stage ASIC-switch-ASIC；每compute rack32×1OU trays连接各switch rack，in-rack shuffle管理fiber。L10含2CPO ASIC boards、16ELSFP、12V→3.3V、CPU/DC-SCM/NIC及cold plate。[[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=4|PDF p.4]][[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=5|PDF p.5]][[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=6|PDF p.6]] package构想8 optical engines、8HBM、UCIe-A→UCIe-S converter、OCI microring PHY、每accelerator200+Tb/s scale-up。[[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=7|PDF p.7]]

## 指标与条件
p.2图为100MW footprint下throughput（M tokens/s）对single-user tokens/s：32/64socket旧/新配置对1024socket CPO。~10×是作者projection，baseline代际/规模同时变化，不能归因全部来自CPO或当实测p99。
p.8 thermal **simulation**：Ta25°C，流量4.5L/min；SoC112°C、HBM75.4°C、IO59.9°C、OE69.8°C均低于所列spec。ASIC/OE cold-plate压降11.2/18.8kPa；不是现场温度采样。[[fti-workshop-short-reach-optical-interconnects/Optical-Scale-Up-AI-architecture-with-Co-Packaged-Optics-with-Open-Rack-Scale-Infrastructure.pdf#page=8|PDF p.8]]

## 图表与架构
已核p.2 throughput-interactivity tradeoff和p.8热仿真。表写R-TIM=5.2W/mK，单位像导热率而非热阻，按原标记保留不代入错误公式。p.2页脚出现“Confidential - External”标记，原文件已在用户提供仓库；本卡只记录来源，不修改或扩大原始传播范围。

## 关联与比较
[[knowledge/concepts/network-optical-integration]]；[[knowledge/sources/src-47ddbe6839d0]]同合作方ELS冷板单独实测补充另一热域；[[knowledge/concepts/network-inference-acceptance]]。

## 不确定性与待验证
缺模型/precision/context/batch、仿真热源功率、fluid inlet定义、完整failure/repair计划。现场tray demo不能证明1024ASIC pod已部署或10倍推理增益。
