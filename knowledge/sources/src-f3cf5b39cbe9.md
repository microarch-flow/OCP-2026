---
id: "src-f3cf5b39cbe9"
type: "source"
title: "A System Architecture using Computational Memory for Differentially Private Training"
aliases: ["A System Architecture using Computational Memory for Differentially Private Training"]
speakers: "Younghoon Min（SK hynix）；Kiwan Maeng（Penn State）"
source_path: "fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf"
source_git_blob_sha: "1112d038fbf812b0c67f37a56f7cb54841ae72c3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 10, 11, 12, 13, 14]
evidence_pages: [4, 5, 6, 8, 9, 10, 11, 12, 13, 14]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-capacity-vs-datapath]]"]
---

# A System Architecture using Computational Memory for Differentially Private Training

## 核心结论
两条不同的近数据计算路径：把 optimizer + checkpoint 合并放到 CXL/SSD 混合内存；把差分隐私训练的相关噪声历史分散在 GPU、CPU、CMM-Ax，并就地做 GEMV 混合。共同点是保存大状态、只传较小的更新或结果，不是让 CXL 普遍替代 GPU。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=5|PDF p.5]] [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=11|PDF p.11]]

## 关键证据
- 混合内存流程：GPU DMA 梯度并提交任务，设备读取 SSD 中参数/动量/方差，融合更新和 checkpoint，持久化后将新参数发布到 CXL 内存，完成队列通知 GPU。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=5|PDF p.5]]
- 相关噪声机制需要历史噪声，不等同于每步独立采样的 DP-SGD。历史随长度和参数量增长；历史长度 64 时，幻灯片给 OPT-1.3B 约 333 GB、OPT-6.7B 约 1.675 TB，解释了为何容量成为算法瓶颈。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=8|PDF p.8]] [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=9|PDF p.9]] [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=10|PDF p.10]]
- Cocoon-NMP 将历史分片到三类内存，在各自邻近计算单元上做混合后汇总，切分必须兼顾容量与计算速度。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=11|PDF p.11]] [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=12|PDF p.12]]

## 指标与条件
|结果|条件及证据边界|
|---|---|
|GPU 参数相关状态 20→4 B/param；GPU–SSD 传输 12→4 B/param|p.4 的状态记账，分别标为减少 80%/66%；不是包括 activation、临时 buffer 的完整训练显存占用。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=4\|PDF p.4]]|
|相对 ZeRO-Offload 4.40×、ZeRO-Infinity 3.62×|作者报告；图按 checkpoint 间隔 1–10 次迭代、host memory sufficient/insufficient 分组。未给完整模型/机器配置，也不能把 headline 视为每个点都达到。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=6\|PDF p.6]]|
|噪声混合 NMP 1.23–2.32×|4×A5000 + CMM-Ax；比较 CXL 扩容但无 NMP，与启用 NMP；OPT-350M/GPT2-L/OPT-1.3B/GPT2-XL，b 分别 256/112/64/56；纵轴为相对 regular training 的 latency。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=14\|PDF p.14]]|
|CMM-Ax 512 GB、200 GB/s、16 Arm@3 GHz|DDR5-6400、CXL 2.0 Type 3、PCIe 5.0×16 的设备规格；200 GB/s 是本地内存带宽，非 host CXL 链路吞吐。[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=13\|PDF p.13]]|

## 图表与架构
p.12 显示计算跟随历史分片，GPU 仍执行反向传播。增加 CXL 容量与避免传回完整噪声历史是两个可分离收益；p.14 的无 NMP 对照对此比单纯 GPU-only 对比更有解释力。

## 关联与比较
联系 [[knowledge/concepts/compute-memory-capacity-vs-datapath|容量收益与数据路径收益的归因]]：训练状态扩容先解决可运行性，再讨论带宽与计算下推。与 KV cache 复用不同，噪声历史有算法正确性/隐私参数约束，不能任意淘汰。

## 不确定性与待验证
“10× less GPUs”是作者摘要声明，缺少明确 GPU-only 配置、等精度/等隐私预算条件及价格。本文不据此推算 TCO。幻灯片未给 ε/δ、收敛曲线及完整训练复现设置；不能以性能图证明隐私或精度保证。

## 原始页码导航
[[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=4|p.4]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=5|p.5]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=6|p.6]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=8|p.8]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=9|p.9]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=10|p.10]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=11|p.11]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=12|p.12]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=13|p.13]] · [[fti-workshop-data-centric-computing/A-System-Architecture-using-Computational-Memory-for-Differentially-Private-Training.pdf#page=14|p.14]]
