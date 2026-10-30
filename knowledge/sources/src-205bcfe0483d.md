---
id: "src-205bcfe0483d"
type: "source"
title: "05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc"
source_path: "ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf"
source_git_blob_sha: "49ec1db72ee816647ec637f746f6c03c948d7719"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [3, 5, 7]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# 05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc

## 核心结论
NVIDIA AI Factory Flex提出可计量、可约束的负载弹性换取更快interconnection：优先功率上限/冷却调节、储能/现场发电、移动或延后非紧急任务，而非直接把在线推理关机。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=2|PDF p.2]] [[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=4|PDF p.4]] [[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=6|PDF p.6]]

## 关键证据
generator提供能量、buffer维持power quality、energy control协调grid-forming与瞬态分工；distribution本身也可能影响电能质量，不能把储能当独立黑箱。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=5|PDF p.5]]
ESS按facility buffer、abnormal-event response、bridge power、grid dispatchability分工，需profile、ramp、latency/interface、SOC/C-rate与degradation共同定容。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=7|PDF p.7]]

## 指标与条件
p.3引用Duke研究称76/98/126GW对应0.25%/0.5%/1%annual curtailment，并列85/177/366h。这些百分比与小时**不是简单全年停机时间换算**：0.5%×8760=43.8h，不是177h；本页未解释energy/partial-curtailment/duration分母，不能据其直接计算服务availability。p.6把177h作hard downtime是警示场景，不是原研究等价结论。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=3|PDF p.3]] [[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=6|PDF p.6]]

## 图表与架构
已看p.3、5、7。protected workloads保持运行是设计目标；没有真实inference p99、降载预算、跨站切换延迟或grid event下的业务数据。

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]；[[knowledge/concepts/ai-infra-inference-serving-shapes]]。在线服务的power cap必须同时受TTFT/TPOT、admission与reserve约束。

## 不确定性与待验证
接入容量、停电风险、服务收益均依站点合同与配电模型；原文号召统一large-load标准，不代表已存在一套全球统一现行要求。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=8|PDF p.8]] [[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=9|PDF p.9]]
