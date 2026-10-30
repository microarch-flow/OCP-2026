---
id: "src-0d9b3cfe421f"
type: "source"
title: "裸金属双BMC层级：租户控制与云方恢复权的分离"
source_path: "Security/Baremetal Security Architecture.pdf"
source_git_blob_sha: "951e1b50b0a673264fc2fa98e82a60238e59b570"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [6]
updated: "2026-10-30"
---

# 裸金属双BMC层级：租户控制与云方恢复权的分离

> 阅读范围：已阅读本文件全部可提取文字（9页）。关键页已视觉核对：6；不代表逐页视觉审核。

## 核心结论

- 裸金属租户要求平台管理权，但CSP仍承担硬件、安全与后台fabric责任；单一BMC所有权不能简单复用VM模型。[[Security/Baremetal Security Architecture.pdf#page=3|PDF p.3]][[Security/Baremetal Security Architecture.pdf#page=4|PDF p.4]][[Security/Baremetal Security Architecture.pdf#page=5|PDF p.5]]
- 提案采用动态层级：正常模式CSP BMC服务System BMC；恢复模式CSP BMC接管，先恢复System BMC为云方镜像，再由后者恢复其他组件。[[Security/Baremetal Security Architecture.pdf#page=6|PDF p.6]]

## 关键证据

- System BMC位于租户边界，CSP BMC管理CSP组件；该隔离同时针对更新授权、带外更新、退租与变砖恢复。[[Security/Baremetal Security Architecture.pdf#page=5|PDF p.5]][[Security/Baremetal Security Architecture.pdf#page=6|PDF p.6]]
- 演讲称展台demo把CSP BMC放入SmartNIC，System BMC在DC-SCM，集成DC-SCM 1.x且不改变平台外形；这是演示方案，不是规模部署证据。[[Security/Baremetal Security Architecture.pdf#page=7|PDF p.7]]

## 指标与条件

没有中断时长、恢复成功率、附加BOM、功耗或SmartNIC资源开销。Streaming boot“解决耐久”未给flash寿命和更新频率的量化模型。[[Security/Baremetal Security Architecture.pdf#page=6|PDF p.6]][[Security/Baremetal Security Architecture.pdf#page=7|PDF p.7]]

## 图表与架构

已视觉核对p.6：CSP BMC/SmartNIC在CSP边界，System BMC/compute/storage/iHSM在租户边界。图表现管理职责划分，未给全部物理互连。

## 关联与比较

与hitless证明互补：双BMC解决“谁可操作与谁可救援”；更新政策证明解决“用户如何信任未来变化”。两者都不能只由BMC网络ACL替代。

## 不确定性与待验证

需明确恢复接管的硬件授权条件、防恶意租户阻断、租户密钥清除、云方越权防护和跨租户重新分配流程。展台demo不是上述安全性质的证明。

