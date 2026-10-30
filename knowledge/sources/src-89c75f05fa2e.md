---
id: "src-89c75f05fa2e"
type: "source"
title: "From Switches to Systems：工厂也是 AI 架构的一部分"
source_path: "executive-sessions/30_From Switches to Systems presented by Jabil.pdf"
source_git_blob_sha: "3d3832cf703f6b527617849a8a5e2ed4bfcd9b37"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 8
review_status: "analyzed-text"
evidence_pages: [2, 3, 4, 5, 6, 7]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]", "[[knowledge/concepts/executive-expo-manufacturing-service-chain]]"]
---

# From Switches to Systems：工厂也是 AI 架构的一部分

## 核心结论
Arista/Jabil认为专用网络柜的光纤、液冷、电源、机械和制造应在同一团队共设计；工厂的装配、检验、返修与追溯成为架构边界，而非设计完成后的外包步骤。[[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=2|PDF p.2]][[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=3|PDF p.3]][[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=7|PDF p.7]]
## 关键证据
- 优先项包括FAT/L11/cluster验证、CDU/QD漏测、fiber弯曲/标签、rack twin/hot-swap、MES genealogy与技能培训。[[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=4|PDF p.4]]
- 明确尚未解决switch储存时N2衰减、带液储存行为、fiber清洁protocol，以及100%入厂检测对节拍的影响。[[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=5|PDF p.5]]
## 指标与条件
51.2T→102.4T+、数百→数千fiber是复杂度趋势；“每周数百rack”是scale readiness目标，没有公开实际良率、节拍或出货统计。[[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=2|PDF p.2]][[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=4|PDF p.4]]
## 图表与架构
完整文字已读，未视觉检查图；仅归纳列举的生产/验证职责，不推算未知架构连线。
## 关联与比较
与 [[knowledge/sources/src-9742774db30d|Foxconn自动化]] 对照：前者给制造量化自述，本源提供具体未闭合风险。CPO经济性应包含清洁、测试、返修和备件，而不仅是光engine BOM。
## 不确定性与待验证
需要储存环境/时间规范、污染验收标准、返修成功率和量产数据；共同责任主张需在接口契约、可追溯日志与现场服务中实现。[[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=6|PDF p.6]][[executive-sessions/30_From Switches to Systems presented by Jabil.pdf#page=7|PDF p.7]]

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]] · [[knowledge/concepts/executive-expo-manufacturing-service-chain]]
