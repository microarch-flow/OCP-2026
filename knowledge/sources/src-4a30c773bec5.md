---
id: "src-4a30c773bec5"
type: "source"
title: "Vera-Rubin IPS：能量缓存与 GPU 控制协作削峰，不等于等比例节能"
source_path: "market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf"
source_git_blob_sha: "77dc371896e72bd27ccd0f73fd869abb1feaa888"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 8
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8]
tags: ["ocp", "source", "platform", "market-impact-adoption"]
text_reviewed: true
key_pages_visual_checked: [4, 5]
updated: "2026-10-30"
comparisons: ["[[knowledge/comparisons/platform-inference-metric-boundaries]]"]
---

# Vera-Rubin IPS：能量缓存与 GPU 控制协作削峰，不等于等比例节能

> 阅读范围：已阅读本文件全部可提取文字（8页）。关键页已视觉核对：4, 5；不代表逐页视觉审核。

## 核心结论

IPS 把机架能量存储与 GPU 控制结合，用受控 ramp-up/down 和更平稳的steady-state，减少 provisioned power 被瞬态峰值占据。削峰、平均能量、有效吞吐是三个指标；本材料主要证明峰值曲线改善。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=2|PDF p.2]][[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=3|PDF p.3]][[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=4|PDF p.4]][[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=5|PDF p.5]]

## 关键证据

每GPU配400J rack energy storage，多tray闭环通信；SOC策略依赖允许AC ramp rate、workload power profile及GPU efficiency controller。不是固定储能SOC对所有负载都适用。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=3|PDF p.3]]

硬件支持限定于AVL power shelves（110kW AC/DC，或800V power rack+90kW DC/DC）与Rubin-equipped trays，其他vendor仍final validation；不能宣称任意ORv3机架可直接启用。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=6|PDF p.6]]

## 指标与条件

两组Vera-Rubin NVL72 LLM training案例在 **AC whip power** 边界报告13%、51% peak reduction；图窗约20s，未列模型、训练吞吐、平均功耗、储能效率、稳定性或长时间SOC循环。不能把51%说成电费或J/token下降51%。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=4|PDF p.4]][[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=5|PDF p.5]]

示例配置有PSU AC ramp400W/s、GPU up/down20W/s、idle hysteresis10s；它们是来源示例而非通用安全推荐，不能跨硬件套用。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=7|PDF p.7]]

## 图表与架构

已核对p.4–5 IPS on/off曲线和测量边界，平稳线与峰谷变化可见；图未提供误差条或总能量积分。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=4|PDF p.4]][[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=5|PDF p.5]]

## 关联与比较

与NVIDIA keynote的同功率额度扩容互补：削峰可释放provisioned capacity，但实际部署更多GPU是否保持可靠性/SLA仍需验证。与EPRI需求响应不同，秒级rack平滑不能自动满足小时级grid flexibility。

## 不确定性与待验证

没有控制环协同失效、通信丢失、储能寿命、应急断电与保护配合测试。p.8只有Open Discussion，无可引用问答。[[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=8|PDF p.8]]

