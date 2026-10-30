---
id: "src-f8b63b9cf196"
type: "source"
title: "xFusion：兆瓦机柜的电力、冷板与机架级协同"
source_path: "executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf"
source_git_blob_sha: "6cfce6749de42f4c7b05deb15048856487697caf"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [1, 8, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [8, 11, 12, 14]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-power-control-boundaries]]", "[[knowledge/concepts/executive-expo-liquid-cooling-evidence]]", "[[knowledge/concepts/sustainability-thermal-validation-ladder]]"]
---

# xFusion：兆瓦机柜的电力、冷板与机架级协同

## 核心结论
按实际封面识别为 xFusion／Arthur Wang 的 Next-Generation Power & Cooling Solutions，而非从文件名推断厂商。方案把 800 V、VPD、先进冷板和机柜制造能力组合为系统路径，但多项数字是厂商目标或规格宣称。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=1|PDF p.1]][[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=8|PDF p.8]][[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=13|PDF p.13]]

## 关键证据
- 冷板标称 4 kW+／芯片，平均热流密度 200 W/cm²、局部热点 400+ W/cm²，铜金刚石材料导热率 ≥650 W/(m·K)；未给冷却液温度、流量和芯片结温。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=8|PDF p.8]]
- 电源方案展示 10×3U 的 1.2 MW 结构，或 6 电源架+6 BBU 的 720 kW 配置；功率与冗余/储能配置不可脱离组合比较。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=13|PDF p.13]]
- 20% 较低故障率、最高 97% 效率及 15% 更低 OPEX 属厂商主张，行业基线和成本边界不充分。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=14|PDF p.14]]

## 指标与条件
p.12 图标题写“48 V Bus Current”，但 10 kW/185 A、1 MW/18,519 A 等数值对应约 **54 V**；此处保留原文矛盾，不能用图题复算并当成一致测量。I²R 优势只在导体电阻等条件明确时成立。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=12|PDF p.12]]

## 图表与架构
p.11 比较 AC、HVDC sidecar、HVDC direct，但“转换级数 4→3”与表中侧挂结构仍四级应分开解释；单级峰值效率相乘也需要相同负载点。p.8 的材料导热率不等于冷板整体热阻或封装结温能力。[[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=11|PDF p.11]][[executive-sessions/38_Next-Generation Power & Cooling Solutions presented by TCT.pdf#page=8|PDF p.8]]

## 关联与比较
评估推理集群时，应将“更高机柜功率”转换成可用 GPU 容量、功率预算下吞吐和冷却故障时降额，而不是直接认作服务性能收益。

## 不确定性与待验证
需索取整机功耗/温度/流量矩阵、故障率样本口径以及 VPD 实际损耗。产能数字与累计出货宣称不等于本代方案的部署验证。

## 知识网络
[[knowledge/concepts/executive-expo-power-control-boundaries]] · [[knowledge/concepts/executive-expo-liquid-cooling-evidence]] · [[knowledge/concepts/sustainability-thermal-validation-ladder]]
