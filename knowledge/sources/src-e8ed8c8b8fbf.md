---
id: "src-e8ed8c8b8fbf"
type: "source"
title: "L10–L12验收：启动一台服务器不等于交付可训练集群"
source_path: "Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf"
source_git_blob_sha: "7ad688716e643769920ecaf34c3f69ad0a9f9c99"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 22
review_status: "analyzed-visual"
evidence_pages: [4, 5, 8, 9, 10, 12, 15, 16, 19]
tags: ["ocp", "source", "platform", "test-&-validation"]
text_reviewed: true
key_pages_visual_checked: [16]
updated: "2026-10-30"
---

# L10–L12验收：启动一台服务器不等于交付可训练集群

> 阅读范围：已阅读本文件全部可提取文字（22页）。关键页已视觉核对：16；不代表逐页视觉审核。

## 核心结论

- L10证明tray在声明fixture/workload下识别、启动、driver-ready和稳定；L11证明完整rack的物理/设施/72GPU NVLink域；L12才验证跨rack fabric、调度和training canary。每级明确不覆盖下一层。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=4|PDF p.4]][[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=8|PDF p.8]][[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=12|PDF p.12]]
- 可交付件不只是pass，而是serial可追踪的inventory、firmware/SBOM、时序对齐电/热/错误、collective正确性与工作负载结果。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=4|PDF p.4]][[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=8|PDF p.8]][[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=10|PDF p.10]]

## 关键证据

- NVL72例为18 compute trays+9 switch trays、72GPU；机架需连线/插接、power冗余、CDU流量压力温差/leak及collective一起验。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=8|PDF p.8]][[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=9|PDF p.9]]
- L12限定已测topology/profile可完成training gate，不保证长期availability、所有workload或外推性能。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=12|PDF p.12]]
- 小至tray测试已有GPU pulse1/4kHz与CPU–GPU1–500Hz同步应力例，反映只稳态burn-in不足。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=5|PDF p.5]]

## 指标与条件

- ib_write_bw样例RC/16QP、MTU4096、8MiB消息/80,000迭代、Ethernet链路报391.53Gb/s，文件标sample/snipped，不外推全cluster。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=15|PDF p.15]]
- NCCL样例144 ranks、float sum、50iters，#wrong=0且Avg busbw300.901GB/s；但标“actual results may vary”，且部分行algbw/busbw与列出的公式/时间不完全一致，不用它作为可复现产品性能。busbw是collective归一化带宽，不能无条件等同实际NIC利用率。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=16|PDF p.16]]
- p.19“1.6T model over100G in minutes”缺权重字节/precision/并行链路/缓存条件，不构成加载时间承诺。[[Test & Validation/From Tray to Training Job- L10-L12 Manufacturing Test.pdf#page=19|PDF p.19]]

## 图表与架构

已视觉核对p.16样例及脚注，确认截断输出和算法指标，避免把739–742GB/s样例峰值当单NIC实测速率。

## 关联与比较

与可运营性契约互补：制造验收提供初始状态/证据基线，后续fleet仍需故障/更新/再修复筛选；训练canary不能替代推理p99/SLA。

## 不确定性与待验证

缺L12 training JCT结果、阈值依据、样本/批次、测试持续时间、长期重现性；已图示的report不等于拿到原始可重分析数据。

