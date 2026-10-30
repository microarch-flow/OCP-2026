---
id: "src-c0b1a4f05c97"
type: "source"
title: "Microsoft：可规模化余热回收取决于可用负载与责任边界"
source_path: "Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf"
source_git_blob_sha: "f058a6d266f56ca5d2f111a43d2d280444d3842f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [4, 6, 8, 10, 11, 16]
text_reviewed: true
key_pages_visual_checked: [4, 6, 8, 10, 11]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-water-energy-heat-tradeoffs]]"]
---

# Microsoft：可规模化余热回收取决于可用负载与责任边界

## 核心结论
余热应按实际投入运营的IT负载和回收接口温度设计，不能按园区铭牌MW或芯片最高温度承诺供热。系统价值来自供需匹配、可靠隔离与清晰责任，而非只追求最热回水。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=4|PDF p.4]][[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=6|PDF p.6]][[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=10|PDF p.10]][[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=11|PDF p.11]]

## 关键证据
- 1 MW运行IT负载约产生1 MW热是经验量级；实际可回收热还受部署爬坡、利用率及冷却可靠性约束。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=4|PDF p.4]]
- 设备进液17–45°C、出液25–55°C为范围示意，回收点还受换热器和位置影响，作者要求按低于25至55°C级热源规划后再现场核验。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=6|PDF p.6]]
- 推荐pre-chiller位置保留主冷却路径，先预留连接、随可行需求分期启用。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=8|PDF p.8]]
- HX为水力隔离及责任分界：数据中心负责到换热器，热用户负责下游及必要热泵；是该提案分工，不是普遍合同强制条款。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=10|PDF p.10]]

## 指标与条件
热量MW、年度交付MWh与可售温度品位不可互换。没有全年小时供需、热泵COP、输送距离、泵耗、备用热源和价格，就不能算净减排或回本期。

## 图表与架构
p.4的年份条形图是示例爬坡而非实际项目；p.10将热用户干扰隔在HX外，图不能证明所有故障都已测试。p.11按温度、时间、规模、地点四维匹配需求。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=4|PDF p.4]][[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=10|PDF p.10]][[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=11|PDF p.11]]

## 关联与比较
与两相高温出汽方案及数字孪生retrofit示例对照：提高温度可能增加可用价值，也可能改变IT资格、材料可靠性和运行风险，不能只比较理论热回收率。

## 不确定性与待验证
未提供具名项目经济模型或实测利用率；白皮书在2026峰会后计划提交社区审阅。多页为相同内容的重复/构建页，不应按页数当作独立案例。[[Sustainability/Enabling Scalable Waste Heat Recovery- Operational Realities, Design Principles, and Value.pdf#page=16|PDF p.16]]

## 知识网络
[[knowledge/concepts/sustainability-water-energy-heat-tradeoffs]]
