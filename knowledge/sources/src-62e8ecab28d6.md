---
id: "src-62e8ecab28d6"
type: "source"
title: "224G AECs for AI Data Centers"
source_path: "executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf"
source_git_blob_sha: "de1561201ce571f15c5225e79964bb23e25bd1c6"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [5, 10, 14]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]"]
---

# 224G AECs for AI Data Centers

## 核心结论
- Molex/Broadcom 将 224G AEC 的 6 m 以上距离看作完整通道协同优化问题，而非只更换 retimer：封装、paddle card、Twinax 的偏斜、串扰、反射都要共同约束。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=7|PDF p.7]][[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=11|PDF p.11]]
- 对推理集群，价值不仅是可达距离，还有现场 BER/SNR/FEC 尾部遥测与通道建模，可减少坏线缆造成的 fabric 长尾问题；材料没有量化实际停机减少。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=12|PDF p.12]][[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=13|PDF p.13]]
## 关键证据
- p.5 区分 DAC、ACC、AEC 的距离范围；“Excellent”是厂商定性等级，不是统一 BER 标准。p.10 是 6.5 m、1.6T 的端到端**仿真** pre-FEC BER，不应当作整条量产线缆的实测分布。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=5|PDF p.5]][[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=10|PDF p.10]]
- p.14 将 1.6T AGERA3/3U 标为 in production，3.2T AGERA4 标为 coming soon；这是演讲中的产品状态主张。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=14|PDF p.14]]
## 指标与条件
- 1.6T 产品列示 >45 dB 通道能力、6 m+；3.2T 路线列示 >40 dB，不能直接按位率比较距离或功耗。没有绝对 W 或 pJ/bit 数值支持“最低能耗”。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=14|PDF p.14]]
- 引用 LightCounting 的 1.6T AEC 出货由 2027 年 137 万到 2030 年 885 万，是预测而非订单。[[executive-sessions/01_224G AECs for AI Data Centers Extending Reach, Enhancing Telemetry, an.pdf#page=6|PDF p.6]]
## 图表与架构
已视觉核对 p.5、10、14；p.10 的纵轴为对数 pre-FEC BER，图题明确 simulated。没有据曲线像素生成精确新数值。
## 关联与比较
同为延长铜互连寿命，本方案同时引入主动器件功耗与可观测性；选型应比较链路功耗、故障定位时间、误码尾部以及维护成本，而不能只比线长。
## 不确定性与待验证
需要获取目标 GPU/交换机组合上的温度、连接器插拔、批次、FEC 类型和长时间误码测试；公开演示和厂商 in production 标注不证明特定客户规模部署。

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]]
