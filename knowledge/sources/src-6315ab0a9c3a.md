---
id: "src-6315ab0a9c3a"
type: "source"
title: "SoC/SiP密钥分发：KMTx/KMRx在共享fabric上构造受保护交付"
source_path: "Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf"
source_git_blob_sha: "aca1835d69512499855d0913884293102ab23e72"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 31
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 9, 15, 18, 19, 23, 24, 28, 29, 31]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [28]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-dynamic-trust-lifecycle]]"]
---

# SoC/SiP密钥分发：KMTx/KMRx在共享fabric上构造受保护交付

> 阅读范围：已阅读本文件全部可提取文字（31页）。关键页已视觉核对：28；不代表逐页视觉审核。

## 核心结论

- 大SoC用每块专用私有key bus难扩展，提案用RoT侧KMTx与DCE旁KMRx在共享fabric上AES-GCM封装数据key/metadata。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=3|PDF p.3]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=4|PDF p.4]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=6|PDF p.6]]
- 主要未闭合点是reset时Initial Pairing Key：单SoC方法implementation-defined；多厂商chiplet引入新的跨die信任建立问题。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=8|PDF p.8]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=18|PDF p.18]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=19|PDF p.19]]

## 关键证据

- IPK+nonce派生session key，RoT写KMRx MMIO，KMRx认证解封后把明文key给本地DCE；Status Request可提供密码保护成功回执。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=9|PDF p.9]]
- 每KMRx不同session key抵抗错路由，counter用于replay/reorder/drop检测；这是协议主张，不能保证恶意fabric无法拒绝服务。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=15|PDF p.15]]
- 拟借UCIe Security Director/CTA：SD先与remote CTA安全会话传IPK，CTA本地分配，再在高速fabric上走KMRx协议。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=23|PDF p.23]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=24|PDF p.24]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=28|PDF p.28]]
- 规范为0.7草案，征集RTL与threat-model验证向1.0推进。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=7|PDF p.7]][[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=29|PDF p.29]]

## 指标与条件

无KMRx面积/功耗、key吞吐、MMIO占用或轮换时延数字；“small IP block”是定性描述，不能推定零PPA成本。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=6|PDF p.6]]

## 图表与架构

已视觉核对p.28：最终KMRx路径跨中间chiplets直达远端各DCE旁KMRx，CTA负责先期IPK建立而非每次数据key都经CTA解封。

## 关联与比较

与L.O.C.K./iHSM共享生命周期关切但边界在芯片内部/封装：需结合密码模块边界审视KMRx到DCE明文最后一段。

## 不确定性与待验证

需初始provisioning、reset/断电counter状态、并发轮换、丢包重试、物理探测和部分die失陷模型；安全目标清单p.31不是验证结果。[[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=31|PDF p.31]]

