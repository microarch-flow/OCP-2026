---
id: "src-b1f7ae75bdcf"
type: "source"
title: "Neutral-atoms-for-computing-and-sensing"
source_path: "fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf"
source_git_blob_sha: "dc710caa573e5ab4a5cb44415c694312e0d72bc5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 8, 9, 10]
tags: ["ai-infra", "fts-quantum-data-center-design"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [6, 7, 8, 10]
concepts: ["[[knowledge/concepts/ai-infra-quantum-classical-boundary]]"]
---

# Neutral-atoms-for-computing-and-sensing

## 核心结论
Infleqtion以neutral-atom逻辑电路、AI辅助门优化和GPU训练/QPU采样展示协同方向；需区分有限电路演示、完整容错通用计算与未来商业能力。标题路径提sensing，实际正文主要讲计算。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=4|PDF p.4]] [[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=6|PDF p.6]] [[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=9|PDF p.9]]

## 关键证据
30逻辑qubits来自80physical qubits的10组编码：初态用$\left[\!\left[8,3,3\right]\!\right]$，运行时为$\left[\!\left[8,3,2\right]\!\right]$ detection/loss-correction。不能仅用80/30比值声称任意容错算法都只需2.67physical/logical。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=6|PDF p.6]]

## 指标与条件
p.7称AI辅助CCZ构造把每逻辑entanglement物理2Q gates从8降到4；p.8为含4个逻辑CCZ的30逻辑qubit IQP circuit。门数减半不是整机runtime、错误率或成本减半，未给fidelity/yield实测值及统计。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=7|PDF p.7]] [[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=8|PDF p.8]]
p.10的100 logical@2028、1000@2030明确target且illustrative；2026的1KiloQuOp为physical operations，不是1000个逻辑门。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=10|PDF p.10]]

## 图表与架构
已核编码脚注、电路和路线图。p.5“no cryogenics/low power”不能替代包括激光、真空、控制与classical compute的墙上功耗。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=5|PDF p.5]]

## 关联与比较
[[knowledge/concepts/ai-infra-quantum-classical-boundary]]。QPU用于inference/sampling是算法方向，不证明可以替代当前LLM GPU推理。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=9|PDF p.9]]

## 不确定性与待验证
需logical error率、连续纠错轮数、postselection开销、完整gate set和同精度time-to-solution；roadmap有明确forward-looking disclaimer，本卡不分析股票或收入指导。[[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=2|PDF p.2]]
