---
id: "src-cb8cb17b9a8e"
type: "source"
title: "Marvell／Microsoft／Oracle：Tessera 集成 HSM 的信任边界提案"
source_path: "executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf"
source_git_blob_sha: "d46b55703f340a7c4d38bab2b22039087603c3f9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 9]
text_reviewed: true
key_pages_visual_checked: [7, 8, 9]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-system-control-evidence]]"]
---

# Marvell／Microsoft／Oracle：Tessera 集成 HSM 的信任边界提案

## 核心结论
Tessera希望把集中HSM的受保护密钥使用延伸至服务器托盘，用本地集成HSM减少密码操作的网络往返，同时保持受保护密钥存储。资料描述工作组与初始草案，不是所有实现已经获得认证的证明。[[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=4|PDF p.4]][[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=5|PDF p.5]][[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=6|PDF p.6]]

## 关键证据
- 工作组目标为硬件、可证明身份的集成HSM，面向FIPS140-3 Level3要求，并用attestation驱动服务器级安全密钥缓存与生命周期。[[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=6|PDF p.6]][[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=7|PDF p.7]]
- 演讲中的时间线：2026年10月初始 **v.05** 草案，v1.0列在后续阶段。不得将后续目标改写为已完成标准。[[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=9|PDF p.9]]
- 对齐Caliptra、OCP LOCK、DC-SCM、SPDM/TDISP，并列混合ML-KEM/ECDHE、ML-DSA/ECDSA作为post-quantum-ready方向。[[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=8|PDF p.8]]

## 指标与条件
没有每秒密码操作、延迟分位、功耗、密钥容量、实际认证编号或攻击测试结果；“无需网络往返”只适用本地受授权操作，不意味着整个密钥生命周期脱离中心系统。

## 图表与架构
p.7三栏分别是认证目标、开放硅模型、集中HSM信任扩展；p.8标准列表不是它们之间安全组合正确性的验证。[[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=7|PDF p.7]][[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=8|PDF p.8]]

## 关联与比较
与系统级控制面联读：证明组件身份并不足以证明当前拓扑、授权命令及恢复状态可信；密钥释放与撤销须与生命周期控制联动。

## 不确定性与待验证
尚需威胁模型、多租户隔离、失联/撤销语义、故障恢复、物理攻击边界及正式认证材料。本卡只解读上传讲稿，不提供合规认证结论。

## 知识网络
[[knowledge/concepts/executive-expo-system-control-evidence]]
