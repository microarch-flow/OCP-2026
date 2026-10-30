---
id: "src-576b1cffe203"
type: "source"
title: "OCP LCA at Scale：用 BOM 与数据质量分层补全硬件碳足迹"
source_path: "Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf"
source_git_blob_sha: "3bc77118ab580e66b01cf758811c70ecf86c2acd"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 9, 11, 12, 13, 14]
tags: ["ocp2026", "source", "sustainability"]
concepts: ["[[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]]"]
---

# OCP LCA at Scale：用 BOM 与数据质量分层补全硬件碳足迹

## 核心结论
Google/Meta等工作组要解决“今天必须完整报告，但高质量原始数据不完整”的矛盾：按组件选最佳可用估计，通过BOM聚合并保留质量分数，而不是把缺失值置零或把低质量代理伪装成实测。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=2|PDF p.2]][[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=5|PDF p.5]][[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=8|PDF p.8]]

## 关键证据
- 数据质量0–10：0无数据、1价格EEIO、2营收因子、3类别平均、4通用参数模型、5–7代理PCF、8–10原始数据PCF。分数表达证据质量，不是减排比例或精确误差百分比。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=4|PDF p.4]]
- 示例power shelf由4×10+3×5=55 kgCO₂e构成，rack为20+2×55=130 kgCO₂e；需正确处理数量、备件、边界并传播质量，不能重复计入子组件。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=6|PDF p.6]]
- FMD将材料质量映射LCI活动数据，但图明确不含PCBA装配与测试排放；材料清单不是完整生命周期清单。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=9|PDF p.9]]
- AI代理匹配先给候选与置信度，再自动/人工验证，专家接受后才进入库；没有声称AI输出本身就是认证PCF。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=11|PDF p.11]]

## 指标与条件
18TB硬盘50kg、32–64核CPU100kg的Open Enablers表明确是**示意数据**，不能作为实际产品排放因子。加权DQ也需固定权重定义，不能误用为实际不确定度。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=12|PDF p.12]][[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=6|PDF p.6]]

## 图表与架构
p.13匿名贡献→验证/离群检查→同declared unit分桶聚合→行业平均，兼顾完整性和IP，但行业平均不必然代表具体供应商工艺。实际采购信号用于Scope3报告，预测采购用于预测，二者分开。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=7|PDF p.7]][[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=13|PDF p.13]]

## 关联与比较
与性能归一化隐含碳、供应商能耗参数化及钢结构追踪连接：单位、边界、数量与数据质量是比“漂亮碳仪表盘”更基础的比较条件。

## 不确定性与待验证
框架预计Q1 2027发表；Open Enablers第一阶段H2 2026–2027为工作组PoC、第二阶段制造商贡献目标2028。不能宣称全部行业数据已可下载或已完成独立验证。[[Sustainability/Operationalizing the PCR- LCA at Scale and the Open Enablers Program.pdf#page=14|PDF p.14]]

## 知识网络
[[knowledge/concepts/sustainability-lca-provenance-and-counterfactuals]]
