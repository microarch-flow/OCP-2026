---
id: "src-cd099b2e021a"
type: "source"
title: "Genuine Optics：NPO、XPO与400G-lane演示的证据边界"
source_path: "expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf"
source_git_blob_sha: "89931ed155a11559133807876599400aa0da6ce3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [6, 7, 10, 11, 12, 13, 14, 15]
text_reviewed: true
key_pages_visual_checked: [6, 7, 10, 11, 12, 13, 14, 15]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Genuine Optics：NPO、XPO与400G-lane演示的证据边界

## 核心结论
厂商选择NPO为密度、可维护性和短电通道的折中，但同时开发DSP/LRO/LPO、XPO和MRM CPO。必须把已出货SiPh模块、实验板BER、展台demo和2027–2028路线图分开，不把NPO优先的商业判断当普适技术结论。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=7|PDF p.7]]

## 关键证据、指标与条件
- 厂商称超过百万SiPh模块、超过80亿device-hours、**PIC FIT<0.2**，依据约两年出货；这是PIC失效口径，不是整模块、链路flap或系统可用率。没有故障数及置信区间；随着分母增加统计估计下降不证明真实危险率必然下降。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=10|PDF p.10]]
- 1.6T表：Full DSP<24W/~10⁻¹³ loopback BER，LRO<15W/~10⁻¹³，LPO<10W/<10⁻⁸。LRO图是测试板在24dB die-to-die电损耗下的结果；不同图测量链/FEC条件未统一，不是等可靠性功耗排名。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=11|PDF p.11]]
- 12.8T XPO演示列500m、8×MPO16；LRO/Sian3-L<130W、TDECQ2.5dB、ER>4dB、BER10⁻¹⁰–10⁻¹¹。另列typical130/80W但未清楚绑定版本，不把80W套到该LRO演示。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=12|PDF p.12]]
- NPO页**<8.5W属于ELSFP光源**，其参数为≥20dBm/lane、8PMF、1311nm、0–70°C；并非整个3.2/6.4T光引擎功耗。光引擎最多32通道、100/200G每通道、0–85°C；3.2T EVB loopback BER<10⁻¹⁰，6.4T为展台demo，12.8T为400G/lane扩展方向。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=13|PDF p.13]]
- 400G/lane页标题写面向3.2T，但实物和测试框图为**1.6T DR4**：8×212.5Gbps电→4×425Gbps光、SiPh/TFLN+3nm DSP、100mW激光1×4分光、约30W、500m、0–70°C，截图BER约8×10⁻⁶。不能记为完整3.2T链路验证。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=14|PDF p.14]]

## 图表与架构
已核p6/7/10–15。NPO/CPO比较表把CPO概括为board scrap/early R&D、节电50%+，未给共同基线，且属于厂商路线定位，不能覆盖其他来源的可维修和现场部署结果。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=6|PDF p.6]]

p15是玻璃基板CPO概念图、2×8λ×200G的3.2T MRM、量子点comb外置光源、12层TGV封装路径；右侧同时出现53G NRZ眼图，不能单凭该眼图证明所有通道200G及>3Tbps/mm单向密度已在整机达标。[[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=15|PDF p.15]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]、[[knowledge/concepts/network-optics-reliability]] 与 [[knowledge/comparisons/network-optics-evidence-ladder]]。把PIC FIT和Meta/Oracle的整链路运维统计放不同栏，不做直接优劣排序。

## 不确定性与待验证
原件标Confidential。需每演示的bit数/时长、温度、纤长、宿主SerDes、FEC、功耗边界和眼图通道覆盖；没有推理p99、热插拔现场维修或全生命周期成本实测。


跨源比较：[[knowledge/comparisons/network-channel-interface-budget]]。
