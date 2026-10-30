---
type: "concept"
title: "动态信任不是一次验签：身份、组成、更新政策与密钥生命周期"
review_status: "synthesis"
tags: ["ocp", "concept", "platform"]
sources: ["[[knowledge/sources/src-bbddc7859662]]", "[[knowledge/sources/src-afbb7a2d0d41]]", "[[knowledge/sources/src-e045caa312c6]]", "[[knowledge/sources/src-030fe91a366d]]", "[[knowledge/sources/src-735495fb16d9]]", "[[knowledge/sources/src-ce8c8976d058]]", "[[knowledge/sources/src-6315ab0a9c3a]]", "[[knowledge/sources/src-df74b2260c89]]", "[[knowledge/sources/src-063ec92debe7]]"]
updated: "2026-10-30"
---

# 动态信任不是一次验签：身份、组成、更新政策与密钥生命周期

## 定义与边界

**跨源归纳：** 对可在线更新、可重组、多租户的AI系统，启动时“已验签”只回答过去某个状态。实际运行保证还取决于谁能改状态、允许怎样改、组件如何加入/退出，以及秘密如何撤销。这里把身份真实性、状态正确性、组成完整性、操作授权、时间新鲜性分开，不把SPDM支持当万能安全标签。

## 来源与页级证据

- **设备身份/测量**：Redfish转送SPDM签名transcript，远端校验nonce/证书/签名；验签本身没有known-good参考值。[[knowledge/sources/src-df74b2260c89|源卡]] · [[manageability-workshop/Remote Attestation of Devices with Redfish and SPDM.pdf#page=9|PDF p.9]]
- **运营方归属**：Attested CSR把key与设备绑定，运营方LDevID证书与厂商IDevID链并存；证书deactivation不同于不可逆revocation。[[knowledge/sources/src-735495fb16d9|源卡]] · [[Security/OCP Device Identity Provisioning over SPDM.pdf#page=12|PDF p.12]] [[knowledge/sources/src-735495fb16d9|源卡]] · [[Security/OCP Device Identity Provisioning over SPDM.pdf#page=16|PDF p.16]]
- **组成完整性**：Composite EAT签设备证据digest及Lead Attester测量，Platform CoRIM给预期设备集合；不能把relay未签数据洗成平台签名可信。[[knowledge/sources/src-afbb7a2d0d41|源卡]] · [[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=8|PDF p.8]] [[knowledge/sources/src-afbb7a2d0d41|源卡]] · [[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=10|PDF p.10]]
- **未来更新约束**：hitless系统需要history与直到reset不变的update policy，频繁重测也不能单独消除证明后变更窗口。[[knowledge/sources/src-bbddc7859662|源卡]] · [[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=11|PDF p.11]] [[knowledge/sources/src-bbddc7859662|源卡]] · [[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=16|PDF p.16]]
- **改变状态的权限与交付**：Owner授权发生在staging后activation前；manifest还需另送Verifier更新参考值。[[knowledge/sources/src-ce8c8976d058|源卡]] · [[Security/Out of Band Seamless Updates with Runtime Authorization.pdf#page=5|PDF p.5]] [[knowledge/sources/src-063ec92debe7|源卡]] · [[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=8|PDF p.8]]
- **fabric状态**：pod路由/partition/QoS等能改变安全性质，准入应是条件租约，假设改变则run/restrict/revoke。[[knowledge/sources/src-030fe91a366d|源卡]] · [[Security/From Securing Links to Securing Pods- Security of Scale-Up Networks.pdf#page=8|PDF p.8]] [[knowledge/sources/src-030fe91a366d|源卡]] · [[Security/From Securing Links to Securing Pods- Security of Scale-Up Networks.pdf#page=11|PDF p.11]]
- **秘密终止点**：机密存储需tenant→IDE→VF→namespace→MEK全链隔离；SoC key transport最后仍有KMRx→DCE明文边界。[[knowledge/sources/src-e045caa312c6|源卡]] · [[Security/Confidential Storage.pdf#page=21|PDF p.21]] [[knowledge/sources/src-6315ab0a9c3a|源卡]] · [[Security/Secure Key Distribution Protocol for SoC Hardware Blocks.pdf#page=9|PDF p.9]]

## 共识与分歧

这些演讲共同把静态信任扩展到生命周期，但**并未共同证明一个量产端到端实现**。尤其：Composite Attestation依赖平台RoT与可信预期清单；远端SPDM可以避免盲信BMC自报，但BMC仍能拒绝服务；把密钥放在TEE不自动等价专用HSM的物理安全。

安全机制分层互补而非替代：签名证明来源；参考值判定状态；授权决定谁能改；policy限制未来改法；inventory/composition决定对象是否完整；key revoke/erase终止权限。一个维度通过不能补另一个空白。

## 适用条件

用于GPU/CPU/SSD/交换机采购和rack架构评审。建议对每个生命周期事件（boot、update、retrain、replace、tenant reassignment、retire）列：旧证据何时失效、谁能批准、谁能执行、失败是否隔离、哪些key撤销、何时恢复业务。该清单是本文归纳的审查方法，非演讲声称的标准条款。

## 未决问题

- 同一nonce的多设备证据收集时间偏斜允许多大？更新中如何获得一致composition snapshot？
- 变更授权、参考manifest发布与实际激活是否能原子协调？
- 重分配/翻新时熔丝身份、现场熵、租户证书和介质key分别能否清除/再生？
- 证明/密钥服务不可用时fail-closed、降级与SLA如何取舍？需测握手QPS、p99、恢复时间而非只验schema。
