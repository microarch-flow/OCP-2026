---
id: "src-48ba6ea6361c"
type: "source"
title: "Ecolab水与PG25：热性能优势必须通过化学维护兑现"
source_path: "expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf"
source_git_blob_sha: "5c30901fe4023639e4df86b0ce79127392116d3f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [3, 7, 8, 9, 10, 12, 13, 16]
text_reviewed: true
key_pages_visual_checked: [3, 7, 8, 9]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# Ecolab水与PG25：热性能优势必须通过化学维护兑现

## 核心结论
水的导热/比热与低黏度优势不直接等于低TCO：洁净启动、材料相容、腐蚀/微生物控制和持续监测决定优势能否维持。PG25降低部分生物控制负担，但并不免维护。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=3|PDF p.3]] [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=7|PDF p.7]] [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=10|PDF p.10]]

## 关键证据、指标与条件
- 文件区分设施FWS与技术TCS：设施25–50% glycol主要考虑防冻；技术回路PG25强调生物抑制，treated water需另加biocontrol。所有浸润材料相容是前置条件。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=3|PDF p.3]]
- 50°C物性对比：PG25/水导热率约0.49/0.63W/(m·K)，比热3.9/4.1kJ/(kg·K)，黏度1.3/0.5mPa·s。黏度比2.6不能直接当泵功比2.6，流态、管路与泵效率不同；也不是整机冷却能力28.6%提升的证据。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=7|PDF p.7]]
- 本讲PG25操作参考为24–29%v/v、azole>400ppm、PBA pH8–10.5或OAT6.5–9.5，且明确coolant dependent；水类的微生物理想<1000CFU/mL、Cu/Fe及Ca/Mg阈值又不同。**这些是演讲给定化学体系的参考，不是可直接下发到任意供应商/现场的配方或运维指令。**[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=8|PDF p.8]] [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=9|PDF p.9]]
- 电导/浊度强调趋势，低电导液的电导趋势未必有效；腐蚀金属也可能受biocide引入影响。需要结合化学体系、采样方法和基线判断，而非单阈值告警。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=9|PDF p.9]]
- 节点更换/补液污染或稀释、混入不兼容液、浸润材料不匹配、故障及泄漏都可能破坏冷却，说明补液供应链和变更流程属于系统可靠性。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=16|PDF p.16]]

## 图表与架构
已核p3/7/8/9。CDU隔开FWS/TCS，不能把设施防冻需求简单套到室内技术循环；也不能把技术循环“非防冻用途”理解为任何补液路径都没有低温风险。决策页明确补液路径存在冻害时倾向PG25。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：与MiTAC的第二供应商混合液ΔT演示互补，短时热性能相近不能替代腐蚀/生物/弹性体验证。与Nidec监测接口互补，传感器可读值不等于已建立闭环化学保障。

## 不确定性与待验证
未给成体系的泵功、冷板温差、人工/停机成本或长期对照试验；“未来转向水”是作者路线判断。处置法规和所引OCP指南在本次未外部核验，不能据本卡作合规决策。现场须依设备/液体供应商批准规格和专业维护方案；本讲末页也注明仅供信息用途。[[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf#page=13|PDF p.13]]


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
