---
id: "src-5a876f87b7ec"
type: "source"
title: "AMI分层安全控制面：本地及时动作与全局策略协调"
source_path: "expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf"
source_git_blob_sha: "ecfbf2b3c165194273a1ce11ecc220460f65ceba"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [6]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-executable-validation]]"]
---

# AMI分层安全控制面：本地及时动作与全局策略协调

## 核心结论
管理范围从server扩到rack/pod/DC不意味着每个快闭环都上传云端。AMI主张时间敏感决策与即时恢复留在硬件附近，上层负责策略授权、聚合/降采样与跨域优化；每个管理边界同时是信任边界。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=2|PDF p.2]] [[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=3|PDF p.3]] [[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=6|PDF p.6]]

## 关键证据、指标与条件
- 共同底座包括UEFI/EDK2、OpenBMC、Redfish、OpenRMC，统一discovery/telemetry/control/lifecycle，再允许运营商差异化。这是合同/抽象分层，不是自动消除设备差异。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=4|PDF p.4]]
- “open foundation”仍需silicon enablement、security、qualification、interop、observability和生命周期工程，明确不把开源等同可生产部署。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=5|PDF p.5]]
- 产品映射：Tektagon+Lattice FPGA做平台RoT，OneTree/OpenBMC做平台及固件rack管理，AMI RM做rack/pod，AMI DCM做row/DC/multi-DC。文件展示定位，没有具体版本、时延/规模benchmark或第三方合规结果。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=8|PDF p.8]]

## 图表与架构
已看p6：全局policy/intent/authorization向下，trusted state/filtered telemetry/attestation向上；FPGA提供硬件rooted trust与确定性控制是方案主张，未给确定性最坏响应上界。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=6|PDF p.6]] 遥测→分析→预测/优化/动作→新遥测是闭环设计，不是预测准确率证据。[[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-executable-validation]] 与 [[knowledge/concepts/network-clock-evidence]]：公共API必须伴随语义、时间质量和动作授权；局部故障恢复不能依赖全局汇总周期。

## 不确定性与待验证
原件标AMI Confidential。需API/schema版本、数据所有权、租户权限、控制器失联策略、更新回滚、密钥生命周期与可观测审计；没有证明预测维护已减少停机或能耗的测量。

