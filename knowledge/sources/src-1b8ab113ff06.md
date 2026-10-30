---
id: "src-1b8ab113ff06"
type: "source"
title: "Lenovo：可持续仪表盘需要先校验单位、边界与控制约束"
source_path: "Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf"
source_git_blob_sha: "35178fa4db9935d7c5c6e6d9e95b60f79baff6b3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 11, 13, 14, 15]
text_reviewed: true
key_pages_visual_checked: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]"]
---

# Lenovo：可持续仪表盘需要先校验单位、边界与控制约束

## 核心结论
材料提出功耗时序→能量/碳→预测→时空调度与carbon capping的闭环。但实际仪表盘示意存在PUE自相矛盾，不能把UI数字当作已验证测量或节碳收益。图像页已全页视觉/OCR核查。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=6|PDF p.6]][[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=7|PDF p.7]][[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=11|PDF p.11]][[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=14|PDF p.14]]

## 关键证据
- 功率预测比较SARIMA、LSTM、FBProphet后选择单变量功耗+FBProphet，时间窗口用EMA；依据训练时间、模型大小、推理时间，但未给精度或留出测试集。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=11|PDF p.11]]
- Kubernetes调度/路由根据地区和时段碳强度迁移pod或API，方案未量化迁移网络开销与服务尾时延。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=13|PDF p.13]]
- carbon cap按历史预测本月剩余额度、对可控服务器限功率或关机；20 kgCO₂/rack/month是示例，不是普遍合理或合规阈值。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=15|PDF p.15]]

## 指标与条件
p.6写`E=E+W`作为W·s累积，只有采样间隔明确为1s才维度成立，一般需`ΣP×Δt`；碳需乘地点/时间对应kgCO₂e/kWh。340 g/kWh是图内示意因子，不可默认所有地点。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=6|PDF p.6]]
**p.7同屏总能量3.14 MWh、IT能量2.14 MWh却标PUE0.66**；按p.5定义应约1.47（同边界同期间），所以该图不能作为实际PUE成绩。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=5|PDF p.5]][[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=7|PDF p.7]]

## 图表与架构
p.4把IT都视作useful、冷却等都视作wasted是粗粒度教学图，实际闲置IT也可无有效产出，必要冷却也不能删除。p.14电源切换框图是控制设想，不证明切换具备并网安全和服务SLA保证。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=4|PDF p.4]][[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=14|PDF p.14]]

## 关联与比较
与DCEM、Green Tokens及开放控制面联读：先保证计量、碳因子、数据时间对齐与权限正确，再讨论AI优化。低碳调度应输出同SLA、同质量下的净收益。

## 不确定性与待验证
未给实际闭环部署、预测误差、业务质量、节能/减碳基线或安全故障测试。软件RAPL/CPU时间归因不等于完整服务器独立计量。[[Sustainability/Next-Generation Sustainability Dashboards- AI-Powered Optimization for Data Centers.pdf#page=8|PDF p.8]]

## 知识网络
[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries]]
