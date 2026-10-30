---
id: "src-dbfa4e967f8b"
type: "source"
title: "Open Flash Platform：DPU 闪存密度方案，不等于已证实 Serverless SLA"
source_path: "storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf"
source_git_blob_sha: "8e94501a40f3b33b962eee651bd106361274ad7b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 4
review_status: "analyzed-visual"
evidence_pages: [1, 2, 3]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: [2]
updated: "2026-10-30"
---

# Open Flash Platform：DPU 闪存密度方案，不等于已证实 Serverless SLA

> 阅读范围：已阅读本文件全部可提取文字（4页）。关键页已视觉核对：2；不代表逐页视觉审核。

## 核心结论

OFP 用 DPU/Linux 替代传统 storage server 形态，把 SSD 聚合为 sled/tray；“serverless”描述移除传统服务器层，不代表没有计算、管理软件或失效域。此四页材料主要是设计与参与邀请。[[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=2|PDF p.2]][[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=3|PDF p.3]]

## 关键证据

每 sled 8 SSD、64 ARM-core DPU、2×400GbE；每 1RU OCP-width tray 最多 6 sled、48 SSD、12×400GbE。结构图显示模块化 drive packs 和 tool-less service 方向，但未给服务操作验证。[[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=2|PDF p.2]]

## 指标与条件

1.97 PB/sled、11.8 PB/tray 明确基于 245.76 TB QLC SSD 的 raw capacity；不包括 RAID/EC/OP 或可用容量折损。端口标称总带宽不能等同 SSD 聚合有效吞吐，也没有尾延迟/功耗实测。[[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=2|PDF p.2]]

## 图表与架构

已核对 p.2 sled/tray 图、数目及 raw-capacity 脚注。未据图片估算冷却、布线、功率或 DPU 内存容量。[[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=2|PDF p.2]]

## 关联与比较

与 NVMe 生态和 Near-Line QLC 相连，但仍需补足元数据、数据保护、failure-in-place、重建以及多租户隔离，才能比较服务器式存储的端到端 TCO。

## 不确定性与待验证

没有 exabyte 规模实测、网络 oversubscription、持久性/一致性、DPU CPU 利用率、软件许可证、HA 或商业交付时间；不能从标题推定已量产部署。[[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=1|PDF p.1]][[storage/The-Open-Flash-Platform-Serverless-Exabyte-Scale-Flash-Storage-with-Xsight-Labs-and-Hammerspace.pdf#page=3|PDF p.3]]

