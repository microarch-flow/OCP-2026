---
type: concept
title: "从遥测到控制证据：可信身份、动作、结果与恢复"
tags: [ocp2026, executive-expo]
---

# 从遥测到控制证据：可信身份、动作、结果与恢复

## 定义
遥测回答“观测到什么”，控制证据还需回答“谁有权、对哪个拓扑/版本、执行了什么、结果怎样、失败后如何恢复”。**跨源归纳**：AI机架跨电力、冷却、网络与计算，不能将若干Redfish接口拼接就称为统一控制面。

## 来源与页级证据
- AMI/Lattice要求连接authority、topology、policy、state、commands、evidence；组件attestation不足以证明系统装配与操作正确。[[knowledge/sources/src-39791e90e69b]] [[executive-sessions/53_The AMI Vision for Open Building an Open Control Plane for the AI Data.pdf#page=5|PDF p.5]]
- HPE将发现、策略、遥测与动作推至机架运营单位，目的是减少客户重复集成工作。[[knowledge/sources/src-7491d3c0cf11]] [[executive-sessions/41_Open Rack, Liquid Cooling, Now What Operationalizing the Next Gen Data.pdf#page=5|PDF p.5]]
- ASRock以配置生成及chassis ID控制板级固件差异，解决构建/启动一致性，但不能代替运行时授权契约。[[knowledge/sources/src-811f46606dea]] [[executive-sessions/46_Scaling AI Inference Infrastructure from Silicon to System presented b.pdf#page=20|PDF p.20]] [[executive-sessions/46_Scaling AI Inference Infrastructure from Silicon to System presented b.pdf#page=22|PDF p.22]]
- AiVRES案例实验室验证通过后，只有客户应用+CPU压力才复现GPU/CPU响应时序导致的PCIe completion timeout；“BMC无异常”不等于系统健康。[[knowledge/sources/src-7366dac56317]] [[executive-sessions/31_Innovation on Diagnosis and Maintenance of AI Datacenters presented by.pdf#page=6|PDF p.6]] [[executive-sessions/31_Innovation on Diagnosis and Maintenance of AI Datacenters presented by.pdf#page=7|PDF p.7]]
- Tessera将密钥使用向本地受保护HSM延伸；初始草案不等于所有设备已经认证。[[knowledge/sources/src-cb8cb17b9a8e]] [[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=7|PDF p.7]] [[executive-sessions/51_Spearheading a New Security Standard for Data Centers presented by Mar.pdf#page=9|PDF p.9]]

## 共识与分歧
配置一致性、身份可信、状态可观测与动作安全是四个不同保证。厂商各自覆盖部分环节：MiTAC关注固件管理层次，HPE关注运营界面，AMI/Lattice关注跨层契约，AiVRES暴露诊断盲区；应互补而非合并为已有统一实现。[[knowledge/sources/src-8be3bec59f09]] [[knowledge/sources/src-8dc20c067bc2]]

## 适用条件
一条可审计控制记录至少需拓扑/固件版本、授权主体、策略输入、时间戳、命令参数、执行确认、观测结果与恢复标识。断电后仍可读取的OOB历史是诊断设计方向，不代表今天所有PCIe设备都有该能力。[[executive-sessions/31_Innovation on Diagnosis and Maintenance of AI Datacenters presented by.pdf#page=26|PDF p.26]]

## 未决问题
跨厂商时间同步、失联默认行为、电力与冷却动作冲突、密钥撤销、更新回滚和故障注入尚缺公共统一验收。需真实trace与安全演练，而不是只要仪表盘截图。

## 继续阅读
[[knowledge/sources/src-f47d40d56dce|设计到部署验证连续体]] · [[knowledge/concepts/executive-expo-power-control-boundaries]] · [[knowledge/concepts/executive-expo-manufacturing-service-chain]]
