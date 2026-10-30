---
type: concept
title: "多厂商芯粒互操作：从PHY到系统契约"
tags: [ocp2026, concept, compute-memory]
---

# 多厂商芯粒互操作：从PHY到系统契约

## 核心判断
“支持同一D2D PHY”只回答电连接的一层问题。真正可复用的芯粒还需一致的transaction mapping、boot/control、安全与故障、模型/工具契约，最后以系统级证据验证。

| 层 | 契约内容 | 本库证据 |
|---|---|---|
| Electrical/PHY | lane/pitch/clock/voltage/BER、package binding | [[knowledge/sources/src-881b8f781aab\|BoW.Flexi]]、[[knowledge/sources/src-7d3aae069517\|光chiplet D2D]] |
| Transaction/link | packet、credit、ordering、retry、profile | [[knowledge/sources/src-67f753f38451\|TLL2.0]]、[[knowledge/sources/src-478d04e7b9df\|LSI]] |
| Management | SCMI服务、MCTP路由、I3C/UCIe/BoW binding | [[knowledge/sources/src-93cbadc7cc60\|Chiplet Systems]] |
| Boot/trust/lifecycle | Ready/Go、RoT、attestation、update、risk policy | [[knowledge/sources/src-39a579937ef7\|FCSA1.1]]、[[knowledge/sources/src-b162bcec7dc8\|Caliptra]] |
| Safety/RAS | fault domains、可观测性、有界恢复/安全态 | [[knowledge/sources/src-fcfa27796971\|PhysicalAI profile]] |
| Model/validation | functional vs timing、接口版本、conformance、validity | [[knowledge/sources/src-d9a3f9a8a723\|Virtual ecosystems]]、[[knowledge/sources/src-f364f1fe74e8\|联邦仿真]] |

## 两个特别重要的边界
1. **Functional compatibility不等于性能可组合**：OCA虚拟平台明确loosely timed/behavioral，不能直接预测p99；TLL profile和credit/buffer仍决定排队与有效带宽。
2. **安全组件不等于系统安全**：Caliptra能提供硬件根，但多vendor package还需威胁模型、授权policy、protected transport、reset/update/recovery与跨die证据。

## 规范成熟度要逐项记录
FCSA1.1在演讲中已release；PhysicalAI profile目标Q3'27；LSI Phase1目标Nov'26；SCMI binding各自处于final-review/draft/not-started。不同演讲的快照不完全一致，保持来源而不是人为生成一个“统一最新标准”。

## 用于架构探索的建议
每条chiplet边界不仅记录bandwidth/latency，还应携带protocol/profile/version、reset/power domain、coherence scope、security owner和failure containment。将启动、降频、容量撤回、link retrain作为状态转换，而非只模拟稳态数据搬运。

## 下一步证据门槛
对候选芯粒索取接口profile、reference models、版本兼容矩阵、跨供应商conformance结果和异常路径测试。未提供时，标记integration risk而不是默认为可组合。
