---
id: "src-df915f7ad91c"
type: "source"
title: "Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid"
source_path: "ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf"
source_git_blob_sha: "cb4901f571a4b763d292c4367e228ffa8f2a0340"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 8, 9, 10, 12, 13, 14]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [5, 7, 8, 9, 10, 11, 12, 13]
concepts: ["[[knowledge/concepts/ai-infra-deployment-readiness]]"]
---

# Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid

## 核心结论
CMU研究用相同服务假设比较AC/DC PV+BESS、islanded gas和grid，并把time-to-power造成的idle GPU机会成本加入LCOE。结论不是“DC在任何站点最便宜”，而是选型取决于气候、规模、能源价格、建设时差和GPU每小时价值。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=3|PDF p.3]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=4|PDF p.4]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=6|PDF p.6]]

## 关键证据
模型用经验校准的近baseload训练负载、气象/PUE、混合整数优化及电池退化；基线各架构包含MV campus spine，DC hall为±400V。GPU spot price作为价值代理，但不等于实际可售需求、利润或推理收入。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=4|PDF p.4]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=5|PDF p.5]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=6|PDF p.6]]

## 指标与条件
p.10为100000GPU、MV、99%uptime模型：like-for-like PV+BESS DC成本均值低约18.3%；同为grid供电仅DC hall对AC的energy cost约低7.9%，不可把18%全归于机房转换效率。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=10|PDF p.10]]
p.13独立New Mexico 30MW IT、99%uptime、gas$4.58/MMBtu案例：DC PV+BESS建设2年LCOE$0.212/kWh、含机会成本$0.642；grid4年$0.054→$1.01。后者不是用户电价，差别主要来自假设的供电延迟。PV241MW/B168MW中的B单位是MW，不可当MWh。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=13|PDF p.13]]

## 图表与架构
已看p.5、7–13。p.8横轴是islanded share of annual energy，不是服务时间availability；不能由年能量覆盖率推导p99或连续停机。p.9称13年replacement时保留89%，p.13称约9%fade，来源内部口径不一致，不选一个当确定寿命。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=8|PDF p.8]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=9|PDF p.9]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=13|PDF p.13]]

## 关联与比较
[[knowledge/concepts/ai-infra-deployment-readiness]]；[[knowledge/concepts/ai-infra-inference-serving-shapes]]。推理架构TCO需加入受SLO约束的利用率与真实commercial demand，而非照搬训练near-baseload。

## 不确定性与待验证
详细component reliability、inference/mixed workloads、不同dispatch与额外发电技术列为future work。地图和美元结果为模型非建设承诺；需敏感性、融资/折现、设备交期、储能持续时长与outage分布。[[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=12|PDF p.12]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=14|PDF p.14]]
