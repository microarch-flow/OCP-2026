---
id: "src-3bd82acf3d66"
type: "source"
title: "Cisco与Microsoft SONiC安全：部署准入已生产，运行时shield仍有路线图边界"
source_path: "expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf"
source_git_blob_sha: "0e181d04ee9eede1f636661e5423d12cae4413dc"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8, 10]
text_reviewed: true
key_pages_visual_checked: [6, 7]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-executable-validation]]"]
---

# Cisco与Microsoft SONiC安全：部署准入已生产，运行时shield仍有路线图边界

## 核心结论
开放交换系统需要把设备身份、可信启动和运行完整性纳入准入与生命周期，不能只在采购时信任硬件。文件明确区分当前生产的Nexus One/SONiC生命周期管理与计划Q2’27提供的SONiC运行时vulnerability shielding。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=5|PDF p.5]] [[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=7|PDF p.7]]

## 关键证据、指标与条件
- 安全启动/attestation以TPM等硬件可信根和客户所有权为重点；转移后不再使用Cisco密钥是方案要求，应查验实际provisioning、吊销与恢复流程。TAM、Aikido、TPM、OpenTitan、Caliptra是不同硬件选择，不能当作同一系统全都集成。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=5|PDF p.5]]
- 准入链路：到货→证明身份→准入→恢复到合法状态→加入fabric；允许、限制、隔离、调查是策略结果。该生命周期能力被标为已生产。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=6|PDF p.6]]
- Shield图覆盖管理/控制平面与kernel，主张在线施策、先防护后计划窗口修补、不重启交换机、持续重验证；**SONiC available from Q2’27**，不是当前已交付零停机能力。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=7|PDF p.7]]
- 文件还列签名容器、文件完整性、最小权限、安全通道与响应；冗余启动分区用于回退，多磁盘恢复明确属roadmap。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=8|PDF p.8]] [[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=10|PDF p.10]]

## 图表与架构
已核p6/7，启动时证明与运行时防护是两个控制点；“不停交换机”不意味着控制面CPU开销、转发丢包或推理尾延迟均为零。

## 关联与比较
[[knowledge/concepts/network-executable-validation]]：与功能/互通测试并行建立可信状态证据、升级回退和隔离演练；AMI的分层控制面可与此对照，但不假定两家产品已经联调。

## 不确定性与待验证
无攻击覆盖率、误报率、隔离时延、更新失败统计或业务p99。行业贡献者/市场规模、其他行业40–50%TCO案例不是AI网络的安全效果或成本benchmark。[[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf#page=3|PDF p.3]]

