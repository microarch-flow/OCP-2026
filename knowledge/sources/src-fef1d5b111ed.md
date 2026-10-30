---
id: "src-fef1d5b111ed"
type: "source"
title: "A Timecard as a R-PNT Custom Solution"
source_path: "Time Appliances/A timecard as a resilient A-PNT custom solution.pdf"
source_git_blob_sha: "10a6ea5c2ec875e6151c55c1525fd536a3f652de"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 14, 15, 16, 17, 18]
text_reviewed: true
key_pages_visual_checked: [6, 7, 15, 16, 17]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-clock-evidence]]"]
---

# A Timecard as a R-PNT Custom Solution

## 核心结论
Oscilloquartz将timecard从GNSS输入设备扩展成可信时间入口：多源比较、干扰/欺骗检测、源隔离、holdover、确定性切换和可审计trust state。共用GNSS可能成为全DC相关故障，增加同源timecards不等于增加独立冗余。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=14|PDF p.14]][[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=16|PDF p.16]][[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=18|PDF p.18]]

## 关键证据
OCP TAP开放参考/driver与IEEE P3335通用架构并非同一认证范围；timecard也可为M.2/USB而不局限PCIe。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=3|PDF p.3]][[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=5|PDF p.5]] 推荐保护架构包含独立PTP/PPS、高稳定oscillator、源confidence、secure boot和phase-slew limit，页内明确**不属于当前OCP认证**。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=17|PDF p.17]]

## 指标与条件
p.6转引2023 TAP webinar：无PTM loaded平均offset1297ns、峰峰2148ns；PTM idle/loaded均平均2ns、峰峰15ns。不是本演讲OSA5400新实验，更不能推广至任意PCIe topology。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=6|PDF p.6]] p.7另展示OSA5400+I226+Z890、timecard/NIC均启PTM、ptp4l G.8275.1 setup，缺少完整原始测量条件。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=7|PDF p.7]]

## 图表与架构
已核p.15匿名mobile operator案例：985 GMs，后一个audit窗口458台/46.5%报alarm、earlier20.7%；两月24,022 jamming events、89%集中前三地区。它说明外部源相关风险，但不是AI机群故障率，匿名案例无法独立复核。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=15|PDF p.15]] 已核p.16–17可信源到PTP fabric的故障传播与隔离边界。

## 关联与比较
[[knowledge/concepts/network-clock-evidence]]；[[knowledge/sources/src-aba4b9355d9b]]的多GM hot standby还需防止多个GM共享同一坏源；[[knowledge/sources/src-25482e5ef2a3]]提醒PTM精度依赖平台与负载。

## 不确定性与待验证
source quarantine/holdover的duration、spoofing detection误报漏报、切换phase jump均未给实测。金融页的法规/亚纳秒宣传不能当法律要求证明；本卡只分析时间架构。贡献里程碑尚待TAP对齐。[[Time Appliances/A timecard as a resilient A-PNT custom solution.pdf#page=18|PDF p.18]]
