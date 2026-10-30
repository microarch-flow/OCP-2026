---
type: topic
title: "Security"
tags: ["ocp2026", "topic"]
---

# Security

返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。

## 阅读路线与主题综合

这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。跨源概念与比较入口见下方；结论的适用条件仍需回查相应笔记。

<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->

<!-- GENERATED:topic-concepts:BEGIN -->
## 关联的跨源概念与比较

以下链接来自本主题源卡的实际引用，按引用它的源卡数量排序；关联不等于独立验证。

- [[knowledge/concepts/platform-dynamic-trust-lifecycle|动态信任不是一次验签：身份、组成、更新政策与密钥生命周期]]（本主题 7 份源卡引用）
- [[knowledge/concepts/platform-firmware-decoupling|固件解耦的四个维度：调用、配置、组件交付与可信发布]]（本主题 1 份源卡引用）
<!-- GENERATED:topic-concepts:END -->

## 来源与分析进度

<!-- GENERATED:topic-sources:BEGIN -->
本主题：19 份 PDF；已分析声明 19；部分分析 0；零字节 0。

| 原始资料 | 源卡 / 状态 |
| --- | --- |
| [[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf\|Advancing Caliptra Security Through Open-Source DV Infrastructure]] | [[knowledge/sources/src-72bfbb7678a0\|Caliptra开源DV：验证资产必须随IP交付并持续复用 · analyzed-text]] |
| [[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf\|Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum]] | [[knowledge/sources/src-cbd1e3d6f4f9\|TCG数据中心信任：DICE身份、TPM安全通道与PQC迁移 · analyzed-visual]] |
| [[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf\|An Introduction to Attesting Hitlessly Updatable Systems]] | [[knowledge/sources/src-bbddc7859662\|无中断更新的证明：从静态测量转向不变更新策略 · analyzed-visual]] |
| [[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf\|Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity]] | [[knowledge/sources/src-14ff6cb09ed6\|Adam’s Bridge 3.0：用NTT线性与双share换掉算术路径masking · analyzed-visual]] |
| [[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf\|BMC-Mediated Platform Composite Attestation via Redfish]] | [[knowledge/sources/src-afbb7a2d0d41\|平台Composite Attestation：签名绑定设备集合而非拼一袋证据 · analyzed-visual]] |
| [[Security/Baremetal Security Architecture.pdf\|Baremetal Security Architecture]] | [[knowledge/sources/src-0d9b3cfe421f\|裸金属双BMC层级：租户控制与云方恢复权的分离 · analyzed-visual]] |
| [[Security/Beyond Static Identity- Enabling Secure Certificate Refresh in Silicon Roots of Trust.pdf\|Beyond Static Identity- Enabling Secure Certificate Refresh in Silicon Roots of Trust]] | [[knowledge/sources/src-a66434a3e8a2\|RoT身份刷新：证书续期与可翻新设备的秘密生命周期不同 · analyzed-text]] |
| [[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf\|Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot]] | [[knowledge/sources/src-3aec6a7ea52c\|Caliptra 2.2 USB流式启动：共享物理链路、分离设备所有权 · analyzed-visual]] |
| [[Security/Confidential Storage.pdf\|Confidential Storage]] | [[knowledge/sources/src-e045caa312c6\|机密存储：将TEE信任边界延伸至介质和密钥生命周期 · analyzed-visual]] |
| [[Security/Endorsements for Attestation- A Common Language for the Whole Supply Chain.pdf\|Endorsements for Attestation- A Common Language for the Whole Supply Chain]] | [[knowledge/sources/src-b12834a7003e\|CoSERV：把供应链背书与参考值分发给异构Verifier · analyzed-text]] |
| [[Security/From Securing Links to Securing Pods- Security of Scale-Up Networks.pdf\|From Securing Links to Securing Pods- Security of Scale-Up Networks]] | [[knowledge/sources/src-030fe91a366d\|Scale-up Pod安全：组合与租约是保证单位 · analyzed-visual]] |
| [[Security/Future-proof security in TPM with SPDM and PQC capabilities.pdf\|Future-proof security in TPM with SPDM and PQC capabilities]] | [[knowledge/sources/src-1c58790bb860\|TPM+SPDM+PQC演示：通道保护与密码敏捷分层落地 · analyzed-visual]] |
| [[Security/Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray.pdf\|Integrated HSM- Bringing Silicon-Level Key Security to the Server Tray]] | [[knowledge/sources/src-be4e79c3f608\|Tessera iHSM：集中治理、托盘本地用钥与跨HSM迁移 · analyzed-visual]] |
| [[Security/OCP Device Identity Provisioning over SPDM.pdf\|OCP Device Identity Provisioning over SPDM]] | [[knowledge/sources/src-735495fb16d9\|设备身份由运营方背书：SPDM Attested CSR与双证书链 · analyzed-visual]] |
| [[Security/OCP L.O.C.K. and FIPS.pdf\|OCP L.O.C.K. and FIPS]] | [[knowledge/sources/src-51022da80730\|L.O.C.K.的FIPS边界：密钥生命周期是SoC集成问题 · analyzed-visual]] |
| [[Security/Out of Band Seamless Updates with Runtime Authorization.pdf\|Out of Band Seamless Updates with Runtime Authorization]] | [[knowledge/sources/src-ce8c8976d058\|带外无影响微码更新：先分发、后所有者授权、再多插槽协调激活 · analyzed-visual]] |
| [[Security/Package-Aware Integrity- From Source-Agnostic Publication to Full-System Attestation.pdf\|Package-Aware Integrity- From Source-Agnostic Publication to Full-System Attestation]] | [[knowledge/sources/src-c6221b62773d\|包级完整性原型：发布透明度不等于实时执行证明 · analyzed-visual]] |
| [[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf\|Secure Key Distribution Protocol for SoC Hardware Blocks]] | [[knowledge/sources/src-6315ab0a9c3a\|SoC/SiP密钥分发：KMTx/KMRx在共享fabric上构造受保护交付 · analyzed-visual]] |
| [[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf\|Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age]] | [[knowledge/sources/src-15ac818ed33e\|S.A.F.E./S.O.L.I.D.：可复用安全审查与AI辅助但非自评 · analyzed-text]] |
<!-- GENERATED:topic-sources:END -->
