---
id: "src-5fd8c43de698"
type: "source"
title: "Credo：宽并行低速光链路的冗余、功耗与成本假设"
source_path: "executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf"
source_git_blob_sha: "d57eaca99ba5c2e9335496ccc4ed560034f0a75f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 8, 10, 11, 12, 14]
text_reviewed: true
key_pages_visual_checked: [1, 5, 6, 7, 8, 10, 11, 12, 14]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]"]
---

# Credo：宽并行低速光链路的冗余、功耗与成本假设

## 核心结论
微发射器路线用大量低速光通道减少均衡代价，并以备用通道实现底层容错；重要创新是“宽度换速率+链路重映射”，不是光纤天然比铜更可靠或零维护。可靠性和成本数字在此主要是厂商主张。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=5|PDF p.5]][[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=6|PDF p.6]][[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=12|PDF p.12]]

## 关键证据
- 表中红µLED/蓝µLED/µVCSEL分别<1/<2/<2 pJ/bit、距离≤2/≤10/≤50 m，纤维数量级分别万/千/百；不能把不同器件的最长距离与最低能耗拼成同一产品规格。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=5|PDF p.5]]
- VR200 NVL72背板示例以260 TB/s、约5 pJ/bit推算约10 kW；若降至<2 pJ/bit，可节约约60%链路能耗、约6 kW/机柜。**不是整机柜节能60%**。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=7|PDF p.7]]
- 1.6T ZeroFlap ALC列12 W/端、50 m和2027年量产，不能将这一有源线缆整端功耗直接与微发射器器件pJ/bit比较。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=10|PDF p.10]]
- 30 Pb/s/100万纤维背板主张15%超额通道支持无损切换、1.8 Pb/托盘、50 m、相对铜减重90%。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=12|PDF p.12]]

## 指标与条件
100 million hours MTBF/MTBI未给样本、统计置信区间、失效分布或现场时间，既不是保证寿命，也不是本卡独立验证。“$100/W机会成本”来自业务/功率估算，不是电价或必然可兑现收入；$600k背板机会损失依赖此假设。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=6|PDF p.6]][[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=8|PDF p.8]]

## 图表与架构
p.6包含gearbox、crossbar、管理MCU和data/spare/management光路，容错不是无源线缆单独完成。p.11的2028/29、2030+属于路线图；p.14的SRMO参与方图不是客户交付证明。[[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=6|PDF p.6]][[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=11|PDF p.11]][[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=14|PDF p.14]]

## 关联与比较
与传统高速硅光/NPO/CPO和多芯光纤比较时，应统一host SerDes、gearbox、激光/发射器、冗余及维修边界，再评估可用带宽与总功耗。

## 不确定性与待验证
需实际BER/FEC、备用通道耗尽行为、共同原因失效、重映射时延、污染/弯曲容忍度和现场维修数据；“zero clean/zero maintenance”暂不能当作操作规范。

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]]
