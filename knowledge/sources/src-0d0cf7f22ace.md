---
id: "src-0d0cf7f22ace"
type: "source"
title: "Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications"
source_path: "ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf"
source_git_blob_sha: "18e8c2c2fbc0928e261e6998b51b9379c3df4a97"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [4, 5, 13, 14]
concepts: ["[[knowledge/concepts/ai-infra-deployment-readiness]]"]
---

# Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications

## 核心结论
Meta 的 800G AEC 经验说明量产准入必须覆盖 firmware、cross-NIC interop、真实 RDMA/NCCL/RoCE traffic、动态温度、工厂/产线一致性，而不是仅元器件 SI/BER 通过。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=6|PDF p.6]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=7|PDF p.7]]

## 关键证据
reset cycling 暴露 AEC MCU I2C prefetch 与 status latch 的 race：NIC 读到 stale config-in-progress 而卡住；新 firmware 调整状态停留，字段验证需进入后续回归。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=8|PDF p.8]]
供应商 qualification 是 design→factory→line→pilot→MP→SPC/MES/纠正动作的生命周期；设计合格不代表不同工厂/批次一致。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=9|PDF p.9]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=10|PDF p.10]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=15|PDF p.15]]

## 指标与条件
- 800G OSFP、112Gb/s PAM4 lanes、32AWG/~7.5mm OD、<12W/**每端**、CMIS5.1、2×400G/1×800G/8×100G modes。<12W 不等于整根线缆功耗。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=5|PDF p.5]]
- **内部不一致**：p.4 比较表写 AEC reach “<2m”，p.5 fleet compatibility 写1.0–3.2m。不能自行修正或选其一推广全体 AEC，需询问型号/信道条件。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=4|PDF p.4]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=5|PDF p.5]]
- 样本 A64/B64/C32；3×MiniPack3（DiagOS、400G）、IHS-to-2RHS、800G Spirent/Xena；温度 ramp 约0.7°C/min，目标case约40/50/70°C，分阶段至30/90天。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=13|PDF p.13]]
- p.14 普通运行 >70°C halt；20%fan 的约82°C 为非连续 overstress。不可把82°C当额定持续温度。p.11 EMI设计目标10dB，来源实际约5.7–9.0dB，未全达到目标。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=11|PDF p.11]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=14|PDF p.14]]

## 图表与架构
已看 reach/power 比较、fleet specs、test setup、温控表。p.4 passive DAC 的长距离 budget failure 只在“required length”上下文，不代表所有 DAC 都不合格。

## 关联与比较
[[knowledge/concepts/ai-infra-deployment-readiness]] 与 [[knowledge/concepts/ai-infra-scaleup-acceptance]]：短距铜链路的差异不是简单 optics/DAC/AEC 三栏价格，还在跨厂商 firmware 与长期动态热/制造一致性。

## 不确定性与待验证
标题/正文称数百万互连部署，但未给本文这一 AEC 型号的装机数量、MTBF、failure denominator、价格/总运维成本或实际网络p99。不能用供应商匿名样本推定全部 fleet 故障率。[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=16|PDF p.16]]
