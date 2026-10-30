---
id: "network-buffer-workload-placement"
type: "concept"
title: "缓冲容量不是孤立参数：传播距离、拥塞控制与作业放置"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 缓冲容量不是孤立参数：传播距离、拥塞控制与作业放置

## 定义
所需buffer由credit/反馈往返时间、burst、incast、收发端速差和故障期间行为决定；同样距离可因transport/traffic差异得出不同架构。带宽余量（capacity buffer）与交换机packet memory不可混为一谈。

## 对照证据
BAG将replica留L2，把DP ring放跨L2路径；L2内无阻塞、跨L2约5:1 oversub，长距RoCE选deep-buffer/J3 credit，按距离FADT headroom。[[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=6|PDF p.6]][[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=9|PDF p.9]][[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=10|PDF p.10]][[knowledge/sources/src-c4cafad20442]] [[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=12|PDF p.12]]
RBB为区域共享数据与每W密度选shallow-buffer，GLIDE/ECN在5ms单向测到70%link、常态7%buffer，4.5:1 incast仍可用满32–53MB。[[knowledge/sources/src-e41f8d86b57e]] [[networking/Srv6 powered backbone networks.pdf#page=5|PDF p.5]][[knowledge/sources/src-e41f8d86b57e]] [[networking/Srv6 powered backbone networks.pdf#page=6|PDF p.6]]
推理KV慢接收端会使PFC拥塞向上游传播；单靠加buffer可能只是推迟发生，CC/通信库rate也要调。[[knowledge/sources/src-b704f1f146e0]] [[networking/Bridging On-prem and Cloud - GPU Networking at Meta Scale.pdf#page=10|PDF p.10]]

## 推导出的工程方法
1. 固定traffic graph与placement，再计算cross-domain flow。
2. 分开propagation headroom、shared burst pool、reorder/retry buffer和运营带宽余量。
3. 在steady load、incast、slow receiver与failure四种状态下测queue+p99。
4. 比较深/浅buffer时同时记录transport、ECN/credit阈值、link速率、distance与可用反馈。

## 不确定性
资料尚无同工作负载/同器件公平A/B，不能从RBB个案否定深buffer，也不能由BAG断言所有AI流量必须无损深buffer。

## 关联
[[knowledge/comparisons/network-transport-and-buffer-context]] · [[knowledge/concepts/network-inference-acceptance]]
