---
id: "src-9b9d2b8872ee"
type: "source"
title: "Microsoft 主旨：Frontier Infrastructure 的产出率、控制面与开放设计"
source_path: "keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf"
source_git_blob_sha: "404d6f3b8436ac2131dcfb82426cfc63202d636e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 30
review_status: "analyzed-visual"
evidence_pages: [1, 6, 8, 9, 10, 14, 15, 19, 21, 22, 23, 25, 26, 27]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [2, 3, 4, 5, 6, 10, 14, 15, 19]
updated: "2026-10-30"
---

# Microsoft 主旨：Frontier Infrastructure 的产出率、控制面与开放设计

> 阅读范围：已阅读本文件全部可提取文字（30页）。关键页已视觉核对：2, 3, 4, 5, 6, 10, 14, 15, 19；不代表逐页视觉审核。

## 核心结论

本 PDF 正文是 Reynold D’Sa 的 **Intelligence Infrastructure: Scaling AI for the Frontier Era**，并非文件名所写的 Google 标题；保留原路径以可追溯。主线是把基础设施投入转为 useful intelligence，结合硅、网络、能源、冷却、密钥安全及 fleet 操作。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=1|PDF p.1]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=6|PDF p.6]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=8|PDF p.8]]

## 关键证据

- Maia300 页称最高 7× gen-over-gen inference、部署时相对 rest of fleet 多40% tokens/MW、2027开始 multi-GW；比较基线和实施条件不同，不能把7×与40%互相推出。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=9|PDF p.9]]
- 多平面 MRC 图配 packet spraying、resilience、burst diagnostic 等，开放 optical scale-up 与开放网络是不同合作路径。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=14|PDF p.14]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=15|PDF p.15]]
- Integrated HSM 强调 key 不离硬件边界；self-managed fleet 强调 RAS、debug、updates、manageability 标准化，以减少人工并增加 nodes-in-service。这是系统目标，不是自动化可靠性实验。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=21|PDF p.21]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=22|PDF p.22]]

## 指标与条件

p.19 Mt.Atlas 图称同 footprint 可接近2× cooling capacity，没有给水温、流量、温差、热负载或实测方法，不能当作通用散热性能。Maia300 的2027部署与功效数字是 roadmap/厂商主张，而非本文确认的运行结果。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=9|PDF p.9]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=19|PDF p.19]]

## 图表与架构

已视觉核对 p.2–6 的 Frontier Firm/yield 叙事图，p.10 硅portfolio、p.14–15 网络图、p.19 冷却图。p.6 字段本身存在乱码，不擅自恢复成具体计量单位；未从 p.10 分散百分比拼接通用性能指标。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=6|PDF p.6]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=10|PDF p.10]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=14|PDF p.14]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=15|PDF p.15]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=19|PDF p.19]]

## 关联与比较

与平台可运营性契约一致：标准化 firmware、diagnostic 和 manageability 是可用节点产出率的基础；网络与能源硬件进步仍需 fleet 级闭环验证。与动态信任概念相连：HSM boundary 是密钥保护，不是整个 workload 自动可信。

## 不确定性与待验证

本文没有完整演讲录音或外部benchmark。能源、碳、水和材料策略列出方向，不证明已经实现 zero waste/carbon negative/water positive；需生命周期边界与审计数据。[[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=23|PDF p.23]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=25|PDF p.25]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=26|PDF p.26]][[keynotes/08_Intelligent Infrastructure for the Intelligence Era.pdf#page=27|PDF p.27]]

