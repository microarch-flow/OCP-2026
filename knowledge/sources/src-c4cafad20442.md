---
id: "src-c4cafad20442"
type: "source"
title: "Scaling AI Infrastructure: Meta’s Journey with BAG"
source_path: "networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf"
source_git_blob_sha: "99d00284ead8f782d3dcf954c45ec1c8471dd276"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-text"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-buffer-workload-placement]]"]
---

# Scaling AI Infrastructure: Meta’s Journey with BAG

## 核心结论
BAG用L3 super-spine连接多个L2 AI fabrics，重点不是把整个跨站网络都做成无阻塞，而是**把模型replica留在L2内、仅跨BAG做DP同步**，再按通信图与维护/保护冗余配置带宽。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=3|PDF p.3]][[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=6|PDF p.6]][[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=12|PDF p.12]]

## 关键证据
- BAG可承接DSF与NSF，使cell-scheduled与packet-sprayed fabric通过相同L3层互联。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=5|PDF p.5]]
- NSF示例每L2约21K GPUs、intra/inter-pod nonblocking，8 spine planes；跨L2约5:1 oversubscription。因此“单大cluster”不等于任意两GPU获得同等带宽。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=6|PDF p.6]]
- 跨site BAGi只连同plane BAGi；hub-and-spoke使新增site仅触及hub、连接数O(N)，但hub用更大modular chassis。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=7|PDF p.7]][[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=8|PDF p.8]]
- 长距RoCEv2选择J3-class深buffer/credit-based forwarding：更大headroom适应传播距离，共享buffer吸收burst；FADT multi-profile按距离切headroom。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=9|PDF p.9]][[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=10|PDF p.10]]
- WECMP按下游fabric的LBW变化调整比例，避免仍把退化路径当等容量。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=11|PDF p.11]]

## 指标与条件
- transceiver mix示例FR4≤3km、LR4≤10km、ZR+≤1000km，是此平台选型陈述，非所有命名标准的统一reach保证。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=10|PDF p.10]]
- 容量推导：若跨replica AllReduce Ring最低需B Pbps，L2→BAG配B+维护buffer；无optical protection时BAG→BAG配(B+buffer)×2。B未给数值、buffer为容量余量而非packet memory。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=12|PDF p.12]]

## 图表与架构
本卡全文文字审阅，架构图未视觉核对，故只记录明确文字，不从图形恢复端口连接。Prometheus 1GW是cluster背景，不用于计算通信效率。[[networking/Scaling AI Infrastructure Across DC and Beyond- Meta's Journey with BAG.pdf#page=4|PDF p.4]]

## 关联与比较
[[knowledge/concepts/network-buffer-workload-placement]]；[[knowledge/comparisons/network-transport-and-buffer-context]]；与 [[knowledge/sources/src-e41f8d86b57e]] 的浅buffer backbone比较须保留transport和workload差异。

## 不确定性与待验证
没有公开B、link utilization、packet loss、p99或跨站训练效率。推理TP/EP/KV搬移若越过L2，其通信图不同于本例DP ring，不可沿用5:1 oversubscription而不做trace/容量验证。
