---
type: "concept"
title: "固件解耦的四个维度：调用、配置、组件交付与可信发布"
review_status: "synthesis"
tags: ["ocp", "concept", "platform"]
sources: ["[[knowledge/sources/src-c1977f3aeaa1]]", "[[knowledge/sources/src-8d86422c6768]]", "[[knowledge/sources/src-31da84017706]]", "[[knowledge/sources/src-2932dc4cb91f]]", "[[knowledge/sources/src-5d6692d74e79]]", "[[knowledge/sources/src-47080f6e51ac]]", "[[knowledge/sources/src-c6221b62773d]]", "[[knowledge/sources/src-e7442ca742b5]]"]
updated: "2026-10-30"
---

# 固件解耦的四个维度：调用、配置、组件交付与可信发布

## 定义与边界

**跨源归纳：** “开放/模块化固件”不是单一重构。四条独立轴分别是Host–silicon调用契约、平台配置数据格式、厂商组件交付生命周期、产物信任/证明粒度。它们可以配合，却不能互相替代。

## 来源与页级证据

1. **调用契约/openSFI**：Host拥有资源并编排，silicon执行分阶段初始化；v1.0在演讲中仅目标2027Q3。[[knowledge/sources/src-47080f6e51ac|源卡]] · [[Open Platform Firmware (OPF)/openSFI Update- Advancing Silicon Firmware Interoperability.pdf#page=4|PDF p.4]] [[knowledge/sources/src-47080f6e51ac|源卡]] · [[Open Platform Firmware (OPF)/openSFI Update- Advancing Silicon Firmware Interoperability.pdf#page=9|PDF p.9]]
2. **配置数据/UPCI**：HRR经compiler成MRR/FHTL，build/updatable/runtime列表分工；结构仍需finalize。[[knowledge/sources/src-31da84017706|源卡]] · [[Open Platform Firmware (OPF)/From Code to Data- Advancing the Unified Platform Configuration Interface (UPCI).pdf#page=3|PDF p.3]] [[knowledge/sources/src-31da84017706|源卡]] · [[Open Platform Firmware (OPF)/From Code to Data- Advancing the Unified Platform Configuration Interface (UPCI).pdf#page=7|PDF p.7]] [[knowledge/sources/src-31da84017706|源卡]] · [[Open Platform Firmware (OPF)/From Code to Data- Advancing the Unified Platform Configuration Interface (UPCI).pdf#page=12|PDF p.12]]
3. **组件交付/late binding**：厂商组件独立签名与加载减少整BMC重发耦合，但新引入ABI/隔离/anti-rollback/Owner控制。[[knowledge/sources/src-8d86422c6768|源卡]] · [[Open Platform Firmware (OPF)/Decoupling Silicon Dependencies from Control Plane Firmware.pdf#page=6|PDF p.6]] [[knowledge/sources/src-8d86422c6768|源卡]] · [[Open Platform Firmware (OPF)/Decoupling Silicon Dependencies from Control Plane Firmware.pdf#page=8|PDF p.8]]
4. **可信发布/包级证据**：build pipeline需固定来源、可复现、SBOM/digest绑定与人工发布门禁；包级measurement原型补整镜像粒度，但未闭合runtime TOCTOU。[[knowledge/sources/src-5d6692d74e79|源卡]] · [[Open Platform Firmware (OPF)/Trusted, AI-Ready Open Firmware- From Auditable Foundations to Agentic Lifecycle Automation.pdf#page=7|PDF p.7]] [[knowledge/sources/src-5d6692d74e79|源卡]] · [[Open Platform Firmware (OPF)/Trusted, AI-Ready Open Firmware- From Auditable Foundations to Agentic Lifecycle Automation.pdf#page=13|PDF p.13]] [[knowledge/sources/src-c6221b62773d|源卡]] · [[Security/Package-Aware Integrity- From Source-Agnostic Publication to Full-System Attestation.pdf#page=20|PDF p.20]]

另一个正交维度是flash-less/streaming的**存储与交付路径**：Early FW因无DRAM、硬时限需预取并验证，本地副本仍可存在。它不自动提供openSFI可移植性。[[knowledge/sources/src-c1977f3aeaa1|源卡]] · [[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=7|PDF p.7]] [[knowledge/sources/src-c1977f3aeaa1|源卡]] · [[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=9|PDF p.9]]

## 共识与分歧

- FSP内部向无状态对齐是厂商实现演进，不等于最终跨厂商ABI已可用。[[knowledge/sources/src-2932dc4cb91f|源卡]] · [[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=7|PDF p.7]] [[knowledge/sources/src-2932dc4cb91f|源卡]] · [[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=9|PDF p.9]]
- 数据schema可降低审计和发布成本，但硅算法尾部未必可声明表达；late binding把变更范围变小，也把组合依赖与运行时代码授权变重要。
- Runtime SBOM只把已构建SBOM与active/staged/recovery镜像准确关联，不是证明“当前正在执行每一字节”。[[knowledge/sources/src-e7442ca742b5|源卡]] · [[systems-management/Runtime-SBOMs-Extending-DMTF-Redfish-to-Connect-Build-Time-and-Live-Software-State.pdf#page=6|PDF p.6]] [[knowledge/sources/src-e7442ca742b5|源卡]] · [[systems-management/Runtime-SBOMs-Extending-DMTF-Redfish-to-Connect-Build-Time-and-Live-Software-State.pdf#page=8|PDF p.8]]

## 适用条件

整机/加速器架构应对每种变更问：是否要改Host二进制、BMC整镜像、配置文件、组件包、RoT政策、reference manifest？把每一项映射到资格范围、失败恢复和长期支持责任，再评估time-to-market而不是泛称“开源省成本”。

## 未决问题

版本兼容矩阵、持久配置的原子合并、组件API稳定期、安全回滚与引用证据更新如何同步？目前材料多为路线图/设计，无跨代多厂商移植工时和fleet事故对照，不能宣称具体TCO节约比例。
