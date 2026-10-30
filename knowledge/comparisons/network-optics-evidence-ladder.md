---
id: "network-optics-evidence-ladder"
type: "comparison"
title: "线性光的证据阶梯：800G现场、212G-lane仿真平台与未来CPO"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 线性光的证据阶梯：800G现场、212G-lane仿真平台与未来CPO

## 问题与比较口径
为什么Oracle/Meta现场说LPO优于FRO，而Microsoft/Arista又认为LPO余量不足？**跨源归纳：结论首先属于某一lane rate、channel、调参和证据层级，不属于“LPO”三个字母本身。**

## 不能混合的三层证据
1. **800G现场**：Oracle同ASIC/T0-T1角色、24小时最大BER的跨链路分布，156591 LPO与202042 FRO，p99分别5.165e-10与2.888e-8；需按电损调参。一月≥1次down的链路比例3.244%与5.681%，不同于事件总次数。Meta另一组100G/lane四个月生产对比也支持较少中断，但其模块、分母与事件定义不同。[[knowledge/sources/src-9f511e524c56]] [[ocp-special-focus-photonics/Lessons-learned-from-GW-scale-AI-deployments.pdf#page=6|PDF p.6]][[knowledge/sources/src-9f511e524c56]] [[ocp-special-focus-photonics/Lessons-learned-from-GW-scale-AI-deployments.pdf#page=7|PDF p.7]][[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=8|PDF p.8]]
2. **212G/lane系统原型**：XPO emulation用4×16lane retimer，300–900mm铜飞线、0/3dB光衰减。FRO表现稳，LRO有衰减敏感，LPO-LPO的3dB点可到1e-6量级；实际accelerator/switch验证仍是下一步。不能用800G历史稳定性直接担保下一代线性接口。[[knowledge/sources/src-c5a42a17b5cf]] [[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=9|PDF p.9]][[knowledge/sources/src-c5a42a17b5cf]] [[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=18|PDF p.18]][[knowledge/sources/src-c5a42a17b5cf]] [[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=19|PDF p.19]]
3. **集成光未来架构**：Broadcom的200G OCI7pJ/bit/500m对比DR-LRO23pJ/bit是total-link表，缺实测方法；90%效率只是无尺度checkpoint示意。它与PIC低FIT、connector带宽或封装yield不是同一证据。[[knowledge/sources/src-3f2d49fba822]] [[ocp-special-focus-photonics/CPO, OCI.pdf#page=6|PDF p.6]][[knowledge/sources/src-3f2d49fba822]] [[ocp-special-focus-photonics/CPO, OCI.pdf#page=13|PDF p.13]]

## 对工程决策的分解
- **能工作**：BER/FEC margin，在指定温度、损耗、lane和tuning下。
- **能生产**：多模块/多vendor、PVT角落、错误burst、flap、老化和可维修性。
- **值得部署**：功耗、风扇/液冷、故障影响GPU时间、tuning/安装工时、备件与采购价格。

Oracle整机1528→1270W说明系统热负担可能放大模块节能，但文内混用half-LPO/LRO与half-LPO/FRO，66W风扇归因也是差额推断；在澄清前不进入精确成本模型。[[knowledge/sources/src-9f511e524c56]] [[ocp-special-focus-photonics/Lessons-learned-from-GW-scale-AI-deployments.pdf#page=8|PDF p.8]] Meta CPO数据又表明平均BER更差但中断更少，故BER不充分预测可用性。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=5|PDF p.5]]

## 需避免的“p99”偷换
Oracle的p99是**跨链路BER统计**；XPO的阴影是**通道结果IQR**；它们都不是推理请求p99。推理要关联optical interruption→transport retry→collective/KV stall→TTFT/ITL，并保留时间不确定性。[[knowledge/concepts/network-clock-evidence]]

## 共识与待验证
去DSP可省电且在某些代际可靠，但必须搬走而不是丢掉诊断功能。采购验收应锁定真实host/module pairing、FEC和firmware；不要采购一个抽象“线性”标签。[[knowledge/concepts/network-optical-integration]] · [[knowledge/concepts/network-optics-reliability]]

