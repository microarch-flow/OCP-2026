---
id: "src-be4e79c3f608"
type: "source"
title: "Tessera iHSM：集中治理、托盘本地用钥与跨HSM迁移"
source_path: "Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf"
source_git_blob_sha: "899367774a3dc7eaba0ed7c2622d0d7386d259da"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 9, 10, 11, 14]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [6, 9]
updated: "2026-10-30"
---

# Tessera iHSM：集中治理、托盘本地用钥与跨HSM迁移

> 阅读范围：已阅读本文件全部可提取文字（15页）。关键页已视觉核对：6, 9；不代表逐页视觉审核。

## 核心结论

- 提案把HSM能力靠近workload，保留中心HSM治理/存储并安全释钥到tray iHSM，避免因远程延迟而用弱隔离明文缓存绕开HSM。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=3|PDF p.3]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=4|PDF p.4]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=6|PDF p.6]]
- Tessera同时讨论专用ASIC与Confidential TEE backend，guest API栈可相同，但两者物理/侧信道安全属性不能视作相同。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=8|PDF p.8]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=10|PDF p.10]]

## 关键证据

- 软件栈从PKCS#11/OpenSSL/CNG插件、用户API、DDI到PCIe driver；TEE方案可先做CI/CD与软件使能。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=8|PDF p.8]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=10|PDF p.10]]
- DARC示意中心HSM用单次transfer key封装，目标iHSM在masked-key域解封并保持属性，使用attested HPKE sealed key跨不同厂商。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=9|PDF p.9]]
- p.7称2026 Summit揭幕，p.14工作组kickoff在会后；因此开放标准完成度需以实际规范为准。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=7|PDF p.7]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=14|PDF p.14]]

## 指标与条件

FIPS140-3 Level3是目标/定位主张，材料无证书编号或验证范围；没有网络延迟、密钥操作QPS、PCIe开销或本地化提升倍数。[[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=7|PDF p.7]][[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf#page=11|PDF p.11]]

## 图表与架构

已视觉核对p.6中心管理→本地iHSM释放路径和p.9跨HSM封装流程。

## 关联与比较

与L.O.C.K.不同层面：iHSM面向通用密钥操作/跨域治理，L.O.C.K.面向存储MEK生命周期；共享RoT/attestation并不让两者可互换。

## 不确定性与待验证

需正式协议、跨厂商属性映射、防重放/撤销、灾备恢复与目标安全认证。p.12监管支持为厂商陈述，不能当法律合规结论。

