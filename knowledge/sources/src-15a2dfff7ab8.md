---
id: "src-15a2dfff7ab8"
type: "source"
title: "Google 主旨：从为 AI 建系统，到用 AI 改造系统生命周期"
source_path: "keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf"
source_git_blob_sha: "b3085613b61082e11e66096e1c2ff57b507ea0e1"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 31
review_status: "analyzed-visual"
evidence_pages: [1, 6, 7, 11, 12, 13, 15, 16, 17, 18, 19, 23, 24, 25]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: [6, 7, 13, 15, 16, 17, 18, 19]
updated: "2026-10-30"
---

# Google 主旨：从为 AI 建系统，到用 AI 改造系统生命周期

> 阅读范围：已阅读本文件全部可提取文字（31页）。关键页已视觉核对：6, 7, 13, 15, 16, 17, 18, 19；不代表逐页视觉审核。

## 核心结论

本文件正文为 Partha Ranganathan 的 **Intelligent Infrastructure Powering the Intelligence Revolution**，与原文件名的 Microsoft 标题不符；保留路径并以正文归属。主旨从 systems for AI 转向 AI for systems，覆盖硬件搜索、软件安全、设施设计和运营。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=1|PDF p.1]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=15|PDF p.15]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=16|PDF p.16]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=17|PDF p.17]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=18|PDF p.18]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=19|PDF p.19]]

## 关键证据

- Hardware vignette 用 AlphaEvolve 做 evolutionary LLM-guided architecture search；资料只展示方向及论文入口，没有足够结构/结果表来复现。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=16|PDF p.16]]
- Software vignette 将 agent security scanning 放进 merge前开发流程；precision与扫描速度不等于漏洞覆盖和修复安全。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=17|PDF p.17]]
- Facility vignette 用 site-specific、多时间跨度天气模型平衡 provisioning cost 与 downtime risk；operation vignette 用自动化减少重复劳动，并强调安全/速度。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=18|PDF p.18]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=19|PDF p.19]]
- 末尾要求高质量数据/模拟、正负样本、monitoring、safety 和重新设计 AI workflow interfaces，说明闭环不是简单接入LLM。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=23|PDF p.23]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=24|PDF p.24]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=25|PDF p.25]]

## 指标与条件

p.17 声称92% precision、seconds scan time，未给recall、样本量、缺陷类型、误报成本或修复后回归结果；不能写成92%漏洞检测率。p.7 的10×/100×“system efficiency across generations”没有共同分母，不能当统一benchmark。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=7|PDF p.7]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=17|PDF p.17]]

## 图表与架构

已核对 p.6–7 全栈演进、p.13 未标清口径的117×图、p.15–19 四案例；没有将117×转述成某项具体性能增长。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=6|PDF p.6]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=7|PDF p.7]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=13|PDF p.13]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=15|PDF p.15]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=16|PDF p.16]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=17|PDF p.17]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=18|PDF p.18]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=19|PDF p.19]]

## 关联与比较

与 firmware AI pipeline、NPI agent 和测试知识库材料一致：最有价值的落点是数据/接口/审计门禁，而不是把自主生成结果直接送生产。厂商/研究案例需要独立验证才可推广到其他平台。

## 不确定性与待验证

所列外部论文/文章未在本任务独立阅读全文；本卡只分析演讲。没有将完整安全、可靠性或净零效果归因给AI，水/碳和grid合作列表也不是已审计成果。[[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=11|PDF p.11]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=12|PDF p.12]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=16|PDF p.16]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=17|PDF p.17]][[keynotes/15_Intelligence Infrastructure Scaling AI for the Frontier Era.pdf#page=18|PDF p.18]]

