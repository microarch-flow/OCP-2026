---
id: "src-a9eed6924fac"
type: "source"
title: "Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge"
source_path: "Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf"
source_git_blob_sha: "8ef2a4e4cf1375038c17d925ba38be7d93defc61"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7]
text_reviewed: true
key_pages_visual_checked: [6, 7]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-clock-evidence]]"]
---

# Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge

## 核心结论
OTS-C在OTS参考架构上研究cluster timing resiliency；演示6个CM4+GNSS通过Chrony组合，展示offset分散收窄，但没有真实失效/恶意源注入或holdover保证。[[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=3|PDF p.3]][[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=4|PDF p.4]][[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=5|PDF p.5]]

## 关键证据
6 CM4各有GNSS receiver形成timing network，用Chrony探索clock combining algorithms；架构也考虑wired/wireless PTP links及多个UTC timing sources。[[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=4|PDF p.4]][[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=5|PDF p.5]]

## 指标与条件
p.6文字称6 clocks在±1µs；**核图可见少量点越过±1000ns虚线**，因此只可说主体集中该范围，不能记录严格worst-case≤1µs。p.7组合后点云明显变窄，仍有负向尖峰；无RMS、p99、confidence interval或完整原始数据，不能编造提升倍率。[[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=6|PDF p.6]][[Time Appliances/Raspberry Pi Compute Module based Open Time Server Cluster (OTS-C) for Resilient Timing at the Edge.pdf#page=7|PDF p.7]]

## 图表与架构
已核p.6/7，纵轴为Chrony estimated offset（ns），不是独立仪器测得的绝对UTC误差；横轴为09-21约05到12时的观察窗口。estimated error改善不自动证明源被spoof时能识别真实时间。

## 关联与比较
[[knowledge/concepts/network-clock-evidence]]；[[knowledge/sources/src-fef1d5b111ed]]强调多源独立性与trust；[[knowledge/sources/src-a1c813b65c00]]强调fleet bound不能只从典型波动判断。

## 不确定性与待验证
缺少组合权重、GNSS独立程度、网络介质、CPU load、掉源与recovery实验。对数据中心高精度部署只可借鉴开放cluster探索，不把edge demo当生产SLA。
