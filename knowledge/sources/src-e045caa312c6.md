---
id: "src-e045caa312c6"
type: "source"
title: "机密存储：将TEE信任边界延伸至介质和密钥生命周期"
source_path: "Security/Confidential Storage.pdf"
source_git_blob_sha: "a163d29b53ec51d013679fb2f0cd366e5b2d7f7b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 54
review_status: "analyzed-visual"
evidence_pages: [7, 10, 12, 16, 21, 25, 28, 33, 39, 41, 42, 49, 50, 52, 53]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [21, 39, 41]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-dynamic-trust-lifecycle]]"]
---

# 机密存储：将TEE信任边界延伸至介质和密钥生命周期

> 阅读范围：已阅读本文件全部可提取文字（54页）。关键页已视觉核对：21, 39, 41；不代表逐页视觉审核。

## 核心结论

- 作者提出机密计算只保护内存并不覆盖checkpoint、模型权重、KV/prompt cache和存储介质，需把身份、链路、设备隔离与介质密钥串成端到端链。[[Security/Confidential Storage.pdf#page=12|PDF p.12]][[Security/Confidential Storage.pdf#page=16|PDF p.16]][[Security/Confidential Storage.pdf#page=49|PDF p.49]]
- 隔离路径是每租户CVM → IDE stream → VF → NVMe namespace → TCG locking range → MEK；这是一组跨标准契约，不是单独“SSD加密”功能。[[Security/Confidential Storage.pdf#page=21|PDF p.21]]
- 这是参考架构与标准组合，没有端到端系统基准或生产规模数据；“去掉最后可信方”是作者总结，应保留硬件RoT/实现/证明服务等信任假设。[[Security/Confidential Storage.pdf#page=39|PDF p.39]][[Security/Confidential Storage.pdf#page=52|PDF p.52]][[Security/Confidential Storage.pdf#page=53|PDF p.53]]

## 关键证据

- 威胁范围包含恶意/被攻破的运营方、hypervisor或fabric，但排除侵入式硅攻击/物理开封。[[Security/Confidential Storage.pdf#page=7|PDF p.7]][[Security/Confidential Storage.pdf#page=10|PDF p.10]]
- MEK留在设备内不以明文离开，MEK-MPA多方授权配合OCP L.O.C.K.密钥安装、轮换、crypto-erase。[[Security/Confidential Storage.pdf#page=25|PDF p.25]]
- SPDM/DICE证据与参考值匹配后才释钥；生命周期还包含更新重测量、故障撤销并重证明、退租销毁密钥。[[Security/Confidential Storage.pdf#page=28|PDF p.28]][[Security/Confidential Storage.pdf#page=33|PDF p.33]]
- p.39会话图组合TSM/TDISP、SPDM认证、IDE、VF/namespace、TCG MEK-MPA、客户与云方密钥管理。[[Security/Confidential Storage.pdf#page=39|PDF p.39]]

## 指标与条件

- “line rate” IDE/AES-XTS与“near-native” TEE均无GB/s、IOPS、p99、功耗、CPU开销或基线，不可当作实测零开销。[[Security/Confidential Storage.pdf#page=39|PDF p.39]][[Security/Confidential Storage.pdf#page=42|PDF p.42]][[Security/Confidential Storage.pdf#page=50|PDF p.50]]
- p.41为定性架构对照，未给具体产品配置。它把Host加密等列为不保护云方/Hypervisor，但不同密钥控制/执行位置可能改变结果，不能当通用产品评级。[[Security/Confidential Storage.pdf#page=41|PDF p.41]]
- “Hourly checkpoints”是AI示例频率，不是耐久/吞吐测试条件。[[Security/Confidential Storage.pdf#page=49|PDF p.49]]

## 图表与架构

已视觉核对p.21租户隔离链、p.39会话组合及p.41定性表；因此确认不同租户IDE stream与MEK路径并列，而不是共享单一租户密钥。

## 关联与比较

架构选型应分别验证机密计算、可信I/O、存储隔离和运营密钥主权；单点合规/加密芯片不能替代端到端验证。对AI服务还需把恢复时间和密钥/证明服务故障列入SLA预算。

## 不确定性与待验证

缺namespace/key密度上限、共享SSD故障域、认证缓存失效、迁移/备份、介质错误完整性与p99影响。演讲不构成所有列举标准已在同一量产平台互通的证据。

