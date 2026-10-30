---
id: "src-5b5f8a5b557e"
type: "source"
title: "04_Bring Your Own XPU An Open Rack for Inference Performance and TCO"
source_path: "ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf"
source_git_blob_sha: "e54f3294558386609552960549673f199ad612c3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
evidence_pages: [2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
tags: ["ai-infra", "ai-clusters"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [13]
concepts: ["[[knowledge/concepts/ai-infra-scaleup-acceptance]]"]
---

# 04_Bring Your Own XPU An Open Rack for Inference Performance and TCO

## 核心结论
Astera Labs以320-lane Scorpio X-series、Orion compute/fabric trays提出开放memory-semantic scale-up，Hypercast处理one-to-many、INC处理many-to-one，试图让多XPU共享rack基础设施。它是厂商方案与性能claim，不等同任意XPU无缝互通。[[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=5|PDF p.5]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=7|PDF p.7]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=8|PDF p.8]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=12|PDF p.12]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=15|PDF p.15]]

## 关键证据
多级switching宣称up to160GPUs；MoE动态expert routing需要大量multicast groups，legacy group不足会fallback unicast。RAS区分signal/link/fabric，COSMOS管理configuration、metrics、events。[[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=9|PDF p.9]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=10|PDF p.10]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=11|PDF p.11]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=14|PDF p.14]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=16|PDF p.16]]

## 指标与条件
p.13 Qwen3.5-122B balanced prefill/decode图比较1×Scorpio2 320L（8GPU全P2P）与2×small switches（各4GPU）；横轴64/128/256/512 active requests，作者标+50%TPS、prefill-heavy+90%、collective up to2×。此处拓扑与switch数量同时变化，未给GPU型号、精度、上下文、SLA/TTFT/TPOT、功耗/价格或重复测量，不能归因单一Hypercast或换算TCO收益。[[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=13|PDF p.13]]

## 图表与架构
已看p.13实际图，确认“1大switch vs2小switch”而非同拓扑仅开关INC。p.14“99%links/1%耗99%部署时间”是修辞性经验说法，无统计分母。

## 关联与比较
[[knowledge/concepts/ai-infra-scaleup-acceptance]]：要求对等拓扑/软件/collective并发与灰故障测试；[[knowledge/concepts/ai-infra-inference-serving-shapes]]：先固定SLA再比较。

## 不确定性与待验证
“largest/open/interop-tested”未给参与XPU/版本矩阵和认证；market demand p.2为外部预测，未外查，也非技术性能证据。[[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=2|PDF p.2]] [[ai-clusters/04_Bring Your Own XPU An Open Rack for Inference Performance and TCO.pdf#page=17|PDF p.17]]
