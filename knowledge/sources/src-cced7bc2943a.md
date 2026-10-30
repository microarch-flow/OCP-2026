---
id: "src-cced7bc2943a"
type: "source"
title: "Rack Scale Reliability Demonstration Testing of an Intel Datacenter Certified Immersion Solution"
aliases: ["Rack Scale Reliability Demonstration Testing of an Intel Datacenter Certified Immersion Solution"]
speakers: "Samantha Yates（Intel）；Betsy Cossette（ExxonMobil）"
source_path: "cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf"
source_git_blob_sha: "e4ac8dcd97b8b2c50a76a1b8de84bef91149cb5e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
tags: ["ocp2026", "source", "immersion"]
concepts: ["[[knowledge/concepts/power-cooling-fluid-assurance]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder]]", "[[knowledge/concepts/immersion-qualification-evidence]]", "[[knowledge/concepts/immersion-cleanliness-fluid-state]]"]
---

# Rack Scale Reliability Demonstration Testing of an Intel Datacenter Certified Immersion Solution

## 核心结论
材料筛查不是终点：风险材料需要封装可靠性补测或替换，然后以真实rack系统的热、SI、memory、benchmark和流体化学联合验证。该案例最强之处是公开unit-hours与置信界，而不是笼统“零故障、寿命更长”。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=3|PDF p.3]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=4|PDF p.4]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=5|PDF p.5]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16|PDF p.16]]

## 关键证据
实际tested配置：XeonPlatinum8592+、BAC DUG Cool26RU/30kW双CDU、Hypertec CiaraTrident IC610DR-G6、每机16×64GB DDR5-4800、ExxonMobil EM DC3235Super。enveloped配置（其他容量/机柜/流体）与实际tested列分开，不能声称全部等量测试。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=2|PDF p.2]]
PSU wire-insulation fail后替换；Xeon材料high-risk由assembly test vehicle和substrate HSIO可靠性补测通过。commissioning还增加custom hanger以阻止fluid绕过server；这是最终资格配置的一部分。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=4|PDF p.4]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=11|PDF p.11]]

## 指标与条件
|t0→ts观测|原始条件/含义|
|---|---|
|Bromine11.20±0.03→25.09±0.12ppb；UV284nm吸光度3.394→3.654|存在析出/污染变化，并非“流体完全没变”；FTIR仍匹配unused。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=12\|PDF p.12]]|
|εr2.11、tanδ0.0004前后相同|测于约7.1GHz；air参考谐振约10.3GHz，不能推广到所有频段不变。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=13\|PDF p.13]]|
|CPU1/2平均温升增加1.6/1.2°C|与各自t0比；不是绝对结温，也不是零热退化。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=14\|PDF p.14]]|
|Linpack−1.0%、SPECrate−0.8%、GSAT+2.0%|t0/ts benchmark deviation，作者判PASS，缺原始波动/样本统计。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=14\|PDF p.14]]|
|PCIe SSD margin8.5→8.4ps、NIC8.3→8.3ps，mask4.4ps；DDR UPM=0|特定配置与测试条件下的margin/风险指标，不是全协议错误率为零。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=14\|PDF p.14]]|

### 可靠性统计不是寿命点估计
24服务器累计63548 server-hours；48CPU累计127096 CPU-hours；384DIMM累计1016832 DIMM-hours。p.16给**95% lower confidence limit MTBF**为21218/42436/339488h；相应一年survival下界66%/81%/97%，均以恒定失效率模型为前提。不是声称实测有34%服务器一年内坏，也不是保证每台能活21218h。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=15|PDF p.15]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16|PDF p.16]]

## 图表与架构
封闭、恒容、充分混合batch-reactor是建模假设；升高fluid温度以加快到反应steady state，且t0/ts测量保持相同process-water边界（控制±1°C）。p.7只有Arrhenius形式，未给完整Ea/AF校准，**到化学steady state不能直接等同已完成若干年服役寿命**。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=6|PDF p.6]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=7|PDF p.7]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/power-cooling-fluid-assurance|流体保证]]：把污染机制、系统功能和统计置信分开报告。[[knowledge/concepts/power-cooling-capacity-evidence-ladder|证据阶梯]]：unit-hours需要保留计数对象，不与实际经过时长混淆。

## 不确定性与待验证
原页公式有表述疑点：p.6用衰减指数标[P]却图示product增加；p.15标题说LCL而式子写MTBF≤该值，不能直接抄作工程计算规范。p.16 server90%值25570h与CPU55139h不保持其余80%/95%列的2×比例，需作者确认故障计数/计算或排版；本卡不擅改数值。未给逐类failure count、独立性/共同原因验证、完整aging温度时间与加速因子，不能从表外推全行业MTBF。p.17 MTBF和system errors均标Info Only，而非认证独立pass criterion。[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=6|PDF p.6]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=15|PDF p.15]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16|PDF p.16]] [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=17|PDF p.17]]

## 原始页码导航
[[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=2|p.2]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=3|p.3]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=4|p.4]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=5|p.5]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=6|p.6]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=7|p.7]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=8|p.8]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=9|p.9]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=10|p.10]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=11|p.11]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=12|p.12]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=13|p.13]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=14|p.14]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=15|p.15]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=16|p.16]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=17|p.17]] · [[cooling-immersion/Rack-Scale-Reliability-Demonstration-Testing-of-an-Intel-Datacenter-Certified-Immersion-Solution.pdf#page=18|p.18]]

## 跨源概念
[[knowledge/concepts/immersion-qualification-evidence]] · [[knowledge/concepts/immersion-cleanliness-fluid-state]]
