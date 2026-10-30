---
id: "src-b2f123d4da85"
type: "source"
title: "Genuine Optics：硅光、外置激光与 NPO 的多路径产品证据"
source_path: "executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf"
source_git_blob_sha: "6d40e2f4d02ed579ea68cde65485528bc58fc984"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [6, 7, 10, 11, 12, 13, 14, 15, 16]
text_reviewed: true
key_pages_visual_checked: [6, 7, 11, 12, 13, 14, 15, 16]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]"]
---

# Genuine Optics：硅光、外置激光与 NPO 的多路径产品证据

## 核心结论
Genuine Optics把NPO定位为功耗、维修与成熟度的折中，同时推进XPO、CPO和400G/lane。产品路线图、测试板回环和展台演示不能统一当作大规模现网部署证据。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=6|PDF p.6]][[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=7|PDF p.7]][[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=11|PDF p.11]]

## 关键证据
- 1.6T模块表：full-DSP/LRO/LPO分别<24/<15/<10 W，回环BER约1e-13/约1e-13/<1e-8；LRO在24 dB die-to-die loss测试板条件下声称1e-13。功耗改善与BER/通道能力存在取舍。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=11|PDF p.11]]
- 12.8T XPO LRO演示：<130 W、TDECQ2.5 dB、ER>4 dB、BER约1e-10–1e-11；页面另列130/80 W典型功耗而未完整区分配置，不能混作同一测点。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=12|PDF p.12]]
- 3.2T NPO EVB回环BER<1e-10；ELSFP的<8.5 W是外置光源本身，不是整个3.2T/6.4T光引擎总功耗。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=13|PDF p.13]]
- 400G/lane演示实际为1.6T DR4：电侧8×212.5、光侧4×425 Gbps PAM4、约30 W、500 m、BER约1e-6；标题“for3.2T”表达扩展方向，不是该演示已是3.2T。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=14|PDF p.14]]

## 指标与条件
历史PIC宣称>80亿器件小时、FIT<0.2，基于两年出货统计；缺少失效判定和置信区间。不能直接外推新CPO模块或互连系统可靠性。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=10|PDF p.10]]

## 图表与架构
p.6将CPO概括成难维修甚至整板报废，是该厂商对所比较架构的判断，不涵盖所有可分离CPO设计。p.15玻璃基板封装明确含概念图；p.16量子点comb与DFB阵列雷达图是相对评分，不是带单位的统一实测。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=6|PDF p.6]][[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=15|PDF p.15]][[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=16|PDF p.16]]

## 关联与比较
与TeraHop集成激光方案构成有价值的立场对照：必须用相同光损、冷却、维修边界比较外置/集成激光，而非摘录各自有利结论。

## 不确定性与待验证
未给完整FEC、样本量、温度、运行时长和端到端应用延迟；2027/2028+路线图不是当前交付承诺。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=7|PDF p.7]]

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]]
