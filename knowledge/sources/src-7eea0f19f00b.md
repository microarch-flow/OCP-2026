---
id: "src-7eea0f19f00b"
type: "source"
title: "Optical Scale-Up: System Reliability and Resiliency to Flaps"
source_path: "fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf"
source_git_blob_sha: "99e0eda83f1cf08796c3c5029570e9df73ffdd3b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 39
review_status: "analyzed-visual"
evidence_pages: [1, 2, 12, 14, 18, 19, 22, 23, 26, 27, 30, 31, 32, 33, 34, 35, 38]
text_reviewed: true
key_pages_visual_checked: [20, 22, 23, 28, 32]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optics-reliability]]"]
---

# Optical Scale-Up: System Reliability and Resiliency to Flaps

## 来源范围与核心结论
39页合辑包含Marvell Lenin Patra、Ranovus Jeff Hutchins及Microsoft Roytman/Link，不是单一实验。共同结论：光学failures、短时burst/flap、系统job abort要分层设计，真正成功标准是job连续而非平均链路uptime。[[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=1|PDF p.1]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=2|PDF p.2]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=18|PDF p.18]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=26|PDF p.26]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=38|PDF p.38]]

## 关键证据
- 3R：独立path/plane冗余、hardware-local检测恢复、fleet telemetry消除重复flaps；RELIANT分physical/link/application/system多层时间尺度，但没有提供实测分布。[[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=12|PDF p.12]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=14|PDF p.14]]
- 降FEC latency可能减coding gain，需更低raw BER；burst error可在长窗口平均BER不明显时触发retry/flap，需环境/电源瞬态、反射、dust、pattern sensitivity和FW跨层测试。[[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=19|PDF p.19]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=22|PDF p.22]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=23|PDF p.23]]
- 800G做1×800还是4×200改变降级能力；若同laser/connector故障域导致多lane相关失败，P^4估算不成立。只有独立故障域假设下四lane全坏才近似P^4。[[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=30|PDF p.30]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=31|PDF p.31]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=32|PDF p.32]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=33|PDF p.33]]

## 指标与条件
p.28扫10–1M Flap-FIT、16–1024GPU：10K FIT/1024GPU示例MTBF0.76h、首flap50%分位约0.5h。页明确NOT field data；表还隐含每GPU事件机会数，不能直接当真实1K pod每半小时故障。
p.20/22 random-BER近似图用retry限3.2×10^-5，不同FEC曲线阈值~10^-3/~3×10^-5/~10^-8；是理论比较，且页将RS可纠正symbol表述为“corrupted CW”有术语歧义，不能作为精确编码规范。

## 图表与架构
已核p.20/22/23/28/32；error-rate曲线采用log10 axes，burst列为brainstorm不是失效统计。p.20 Meta ECOC2025零UCW为转引，非本合辑新增独立验证。

## 关联与比较
[[knowledge/concepts/network-optics-reliability]]；[[knowledge/concepts/network-multipath-behavior]]；[[knowledge/sources/src-ada5498062ed]]提供另一组有明确device-hours的CPO观测。

## 不确定性与待验证
未给flap duration/cluster conditional probability、软件迁移时限与collective恢复SLO。所有“µs–minutes flaps”需分分布与故障域；将同一connector的lane分到不同logical ports未必形成独立物理故障域。[[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=27|PDF p.27]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=34|PDF p.34]][[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=35|PDF p.35]]
