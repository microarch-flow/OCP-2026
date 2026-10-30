---
id: "src-96d8cd0fedf0"
type: "source"
title: "Prediction Error Budgets for Time-Scheduled Circuit Fabrics in Distributed AI Training"
source_path: "Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf"
source_git_blob_sha: "a9918c3a129752390b709b417d7240bc1842bc48"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 7, 10, 14]
tags: ["ocp-2026", "networking"]
concepts: ["[[knowledge/concepts/network-ocs-control]]"]
---

# Prediction Error Budgets for Time-Scheduled Circuit Fabrics in Distributed AI Training

## 来源身份提示
原路径标题为Precision-Time Circuit Switching…，首页实际标题如上；以正文为准，保留原始文件身份。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=1|PDF p.1]]

## 核心结论
电路调度收益只存在于exposed、contended、predictable流量；单个round晚结束可能使后续event-triggered rounds错过窗口并级联崩塌。论文式实验主张用绝对时间独立调度rounds及按预测误差配置slack，而非单纯追求更高PTP精度。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=2|PDF p.2]][[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=8|PDF p.8]][[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=9|PDF p.9]][[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=10|PDF p.10]]

## 关键证据
- **实验不是光交换机部署**：一台EPYC上7×T4、每GPU一个container，NCCL/TCP over veth，tc/HTB模拟switch ports，3+4两pod，所有rank/controller共享kernel clock，以构造方式排除同步误差。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=4|PDF p.4]]
- 24个circuits需分4轮，每次6个；transfer135ms+dark25ms+slack10ms=170ms窗口，fallback/trickle慢40倍。766 steps/63 cells另加25预注册shared-time cells。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=5|PDF p.5]]
- event-triggered依赖前一轮wait返回；462个collapsed early-error steps中72%代价超出一个stranded residual可解释范围。早先90%因CSV不可复现被作者撤回，应只引用72%。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=8|PDF p.8]]

## 指标与条件
- 基线：pinned floor544ms、perfect-prediction oracle651ms、4:1 packet baseline2365ms、all-trickle ceiling16.3s。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=4|PDF p.4]]
- early tolerance约11ms vs late约1.7s；这是本窗口/误差注入条件下的非对称性，不是通用光链路容限。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=6|PDF p.6]]
- Gaussian预测误差σ60ms：slack10ms时约7.5s；slack=3σ=180ms时约1.16s，约6.5倍差距，代价是slack自身延迟。239ms可容忍σ来自本实验拟合，不是实时predictor已达成的精度。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=7|PDF p.7]]
- ε=-20ms的same-cell：event-triggered11.44s，time-triggered增加37ms；oracle649 vs652ms。拟合斜率38.8±0.1接近trickle ratio，25 cells/5 batches/2 seeds/3 payloads，非生产SLO。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=10|PDF p.10]]

## 图表与架构
已核p.4–7/10/14。p.6 early横轴反向log尺度、纵轴seconds，不可线性估斜率；p.10图中另标+111ms的点与文字强调的-20ms/+37ms不是同一横坐标。p.14是**gated analytical model**：400Gb/s、20ms MEMS、Llama3-405B DP window、外引PRISM抖动；16K/64K列不是本机实测GPU规模。模型中“mixed cannot lose”依赖设定的fallback，不能当普适定理。

## 关联与比较
[[knowledge/concepts/network-ocs-control]]；[[knowledge/concepts/network-clock-evidence]]。与 [[knowledge/sources/src-8fba6503c4b7]] 的OCS标准API对接时，需要定义absolute schedule、drain/settle、fallback与rollback，而不仅是Set连接。

## 不确定性与待验证
作者明确所有实测是dense workload，MoE all-to-all是下一实验；real optical switch、PTP in loop、真实open-loop predictor均列future work。[[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=11|PDF p.11]][[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=12|PDF p.12]] 外引Jupiter/TPUv4/PRISM数字属于二手引用，本卡不独立确认或将它们算作本研究实测。推理不规则到达/专家路由下可预测性仍未知。
