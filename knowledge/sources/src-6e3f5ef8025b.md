---
id: "src-6e3f5ef8025b"
type: "source"
title: "Operating Linear and Co-Packaged Optics at Hyperscale — The Disappearing DSP"
source_path: "ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf"
source_git_blob_sha: "f1d1d949bb8724e5c7e55ae58e400ce38b3d15a7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-text"
evidence_pages: [1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp-2026", "photonics"]
concepts: ["[[knowledge/concepts/network-optics-reliability]]"]
---

# Operating Linear and Co-Packaged Optics at Hyperscale — The Disappearing DSP

## 来源身份提示
**路径名为 Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf，但实际首页是Oracle Cloud Infrastructure Stephen Manley的本标题。** 保留原路径与Git身份，不按文件名臆造另一场演讲。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=1|PDF p.1]]

## 核心结论
去掉DSP不是去掉其运营责任：equalization、FEC/BER证据、时间戳日志、故障边界与远端可达性必须重新分配到host、光引擎和fleet工具。可靠性可以改善，同时可解释性恶化。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=4|PDF p.4]][[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=5|PDF p.5]][[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=6|PDF p.6]]

## 关键证据
- LPO使host SerDes、电通道和光模块成为耦合margin budget；CPO把故障域扩大到package/switch，激光、fiber attach与connector改变维修路径。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=5|PDF p.5]]
- 单侧计数器不能定位local/remote × host/media四个域。裸金属host不可装agent时尤其明显。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=7|PDF p.7]][[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=8|PDF p.8]]
- 五项运营契约：detect、localize、remember（重启后保留间歇事件）、reach远端、remediate并验证。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=9|PDF p.9]]
- 演示POC用DSP-to-DSP messaging实现远端身份/遥测、时间日志、筛选关闭、两端FW升级；是可迁移的运营模式，不是已证明所有DSP-less设备实现了同一协议。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=10|PDF p.10]]

## 指标与条件
8 links/host、10K/100K/1M hosts对应80K/800K/8M link ends，是**说明规模效应的示意值**，不是Oracle部署规模披露。作者只称经脱敏同类部署未发现LPO-LPO更不稳定、混合vendor TX/RX方向性重要，未给量化原始事件数据。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=3|PDF p.3]][[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=6|PDF p.6]]

## 图表与架构
本卡完整阅读可提取文字，未逐页核图，不从示意图提取性能数字。遥测架构建议adaptive polling、靠近物理层的有限event ring、变化触发上报、故障分类后深查；fast path保护链路、slow path做fleet关联。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/network-optics-reliability]]；Meta [[knowledge/sources/src-6ce06488969f]]提供有条件可靠性数据，本来源补足现场归因/MTTR而非独立复制那组统计。

## 不确定性与待验证
Expanded Beam Optics可能降低灰尘和插拔机械风险，但仍需插损、对准、寿命、清洁与多厂互通验证；不能替代可观测性。[[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=13|PDF p.13]] 对推理p99应增加事件时间戳与请求/collective关联，文件本身没有给SLO改善量。
