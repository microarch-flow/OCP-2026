---
id: "src-204a0ecdba21"
type: "source"
title: "KIOXIA E1.S液冷SSD：解除功率约束不等于已证明IO尾延迟"
source_path: "expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf"
source_git_blob_sha: "30267cf5ccf6257a08ec672eb29f82ab069246a5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7]
text_reviewed: true
key_pages_visual_checked: [3, 4, 5]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# KIOXIA E1.S液冷SSD：解除功率约束不等于已证明IO尾延迟

## 核心结论
NX1采用同一SSD设计适配风冷和液冷，液冷价值是扩大可用热预算，而不是直接保证更高IOPS或更低p99。E1.S的厚度、cold plate与维护接口属于系统配置的一部分。[[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=3|PDF p.3]] [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=5|PDF p.5]] [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=6|PDF p.6]]

## 关键证据、指标与条件
- 示意对比给E1.S典型功率上限：风冷20W、液冷30W；这是功率预算，不是同负载实测耗电或性能提升50%。[[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=3|PDF p.3]]
- p4曲线比较15mm风冷与9.5mm液冷，横轴SSD功率10–40W；纵轴Tsmart没有数值刻度，低功率风冷曲线更低、约17W附近交叉，较高功率液冷温升斜率较小。因此只记录趋势，不提取温差、热阻或安全上限。[[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=4|PDF p.4]]
- NX1：BiCS Gen8 TLC、PCIe5×4/NVMe2.0e、OCP SSD2.6、最高15.36TB、1DWPD、掉电保护。9.5/15mm均支持风冷，**只有9.5mm列DLC支持**；展示Cooler Master冷板。[[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=5|PDF p.5]]
- E1.S参考设计对齐SFF-TA1006 Rev2；另提面向NVIDIA CMX的E3.S液冷开发，不能把该开发状态套到NX1现有E1.S产品。[[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf#page=7|PDF p.7]]

## 图表与架构
已核p3/4/5，特别保留p4无温度刻度这一限制。冷板照片证明演示形态，不能证明带液连接的热插拔、漏液率或全寿命接触压力。

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：对KV/cache工作负载应同时记录SSD功率、稳态温度、降频、写入放大和长尾IO，不能拿30W预算替代存储服务SLO。

## 不确定性与待验证
无IOPS/带宽/延迟分位数、环境/液温/流量、预处理、读写比、稳态测试时长或维护测试；1DWPD也需和保修期及工作负载定义一起读。


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
