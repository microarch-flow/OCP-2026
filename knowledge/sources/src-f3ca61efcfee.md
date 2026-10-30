---
id: "src-f3ca61efcfee"
type: "source"
title: "Infrastructure of the AI Era：模块化 OCP 系统方法"
source_path: "executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf"
source_git_blob_sha: "9ead53a403c05878fb052c705ed1793c27a47652"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 7, 8, 10, 11]
text_reviewed: true
key_pages_visual_checked: [3, 7, 11]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-power-control-boundaries]]", "[[knowledge/concepts/executive-expo-liquid-cooling-evidence]]"]
---

# Infrastructure of the AI Era：模块化 OCP 系统方法

## 核心结论
- Rittal 将 AI 工厂约束整理为首次产出 token 的时间、每瓦 token 和跨代生命周期；建议以固定 OCP 机架接口解耦 IT、供电 sidecar、冷却模块。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=2|PDF p.2]][[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=5|PDF p.5]]
- 800V DC、CDU 容量和 rack mechanics 是耦合设计问题；“保持机架接口、升级外围模块”是降低跨代搁浅风险的架构主张，而不是已验证的全寿命 TCO。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=4|PDF p.4]][[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=5|PDF p.5]]
## 关键证据
- 电力路径分成传统 rack 内 AC/DC、sidecar 转换、设施级 SST/800V 分配三阶段；侧柜和建筑级 800V 不能视为同一种迁移工程。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=7|PDF p.7]]
- 冷却区分 rack-based、row-based、in-row：冗余位置和维护占地不同。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=10|PDF p.10]]
## 指标与条件
- 100 MW 示意案例：30 天满功率对应 72 GWh 未利用供电；PUE 1.3→1.2 时 IT 容量约增加 6 MW，是算术示例，不是现场节能测量。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=3|PDF p.3]]
- sidecar 产品标称上限 2 MW；冷却产品列示后门 80 kW、in-rack CDU 250 kW@4K ATD、in-row CDU 1.25 MW@4K ATD；另示 1.5 MW 模组聚合 13.5 MW@N+1。[[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=8|PDF p.8]][[executive-sessions/03_A system approach to AI infrastructure presented by Rittal.pdf#page=11|PDF p.11]]
## 图表与架构
已视觉核对 p.3、7、11，尤其纠正文字提取中 1.25 MW/1.5 MW 的位置关系。标称能力仍需结合供回水温度、流量和冗余模式。
## 关联与比较
与 GPU 峰值 PPA 相比，模块化收益主要落在交付周期、可用 IT 功率和换代资本复用；评估必须将设施接口和维护政策纳入。
## 不确定性与待验证
140 kW 的 48V“实际天花板”是该演讲的概括，不是普适物理上限。需要项目级交付时间、成本、故障率与认证范围，才能把方案转成商业回报。

## 知识网络
[[knowledge/concepts/executive-expo-power-control-boundaries]] · [[knowledge/concepts/executive-expo-liquid-cooling-evidence]]
