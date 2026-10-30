---
id: "src-afd98c5967a4"
type: "source"
title: "Oracle 主旨：用开放接口把运行经验转为设施与设备互操作"
source_path: "keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf"
source_git_blob_sha: "8686600749e60fc865bdd1e530a0d6d2d0f33fee"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 29
review_status: "analyzed-text"
evidence_pages: [1, 3, 5, 9, 11, 12, 16, 17, 19, 20, 21, 22, 24, 25, 26]
tags: ["ocp", "source", "platform", "keynotes"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# Oracle 主旨：用开放接口把运行经验转为设施与设备互操作

> 阅读范围：已阅读本文件全部可提取文字（29页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

正文标题是 Open Ecosystem Can Unlock Velocity for AI DCs；其重点是把 cloud 运行中的设施、光链路和安全问题转成开放工作组/接口。新 workstream、已提交规格、合作实施和生产模型是不同成熟度。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=1|PDF p.1]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=9|PDF p.9]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=16|PDF p.16]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=19|PDF p.19]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=25|PDF p.25]]

## 关键证据

- 可持续性要求 local context 与 holistic metrics；gPUE、compute density、IUE 等列为 newly proposed，不是已统一采纳的计费/验收指标。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=11|PDF p.11]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=12|PDF p.12]]
- Tessera IHSM 设想开放 architecture、protocol、实现与 ASIC ecosystem，使密码操作靠近 workload，但没有在此证明物理安全等级。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=16|PDF p.16]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=17|PDF p.17]]
- 光链路短暂异常可能引发 fabric reconvergence、RDMA timeout 和业务 disruption；需要 vendor-neutral telemetry、link behavior、diagnosis、mitigation，而不只清洁光口。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=20|PDF p.20]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=21|PDF p.21]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=22|PDF p.22]]
- DPU abstraction layer 作为 programmable offload 的 reusable platform model，目标保留创新空间而减少平台绑定。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=24|PDF p.24]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=25|PDF p.25]]

## 指标与条件

220+ regions 包含 **live and planned**、快照 July6 2026，不能写成220+已运行区域。材料没有提供 gPUE 数值、光故障率、DPU效率、IHSM延迟或建设工期对照。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=3|PDF p.3]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=12|PDF p.12]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=19|PDF p.19]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=25|PDF p.25]]

## 图表与架构

未视觉核对图片/图形；只使用文字明确表达的工作域与成熟度。

## 关联与比较

与 Tessera 深入材料、OpenBMC 运维和光互连材料互补。商业化路径是把运行教训变成可测试接口，再做供应商互操作，而非只发布一个抽象 API。

## 不确定性与待验证

社区、微电网、低水耗等是责任建设承诺；未给地方/环境核算数据，不宣称净零影响已实现。多个新工作组应以正式规格与仓库状态确认，不能从 keynote 推断量产覆盖。[[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=5|PDF p.5]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=11|PDF p.11]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=17|PDF p.17]][[keynotes/09_Scaling AI Infrastructure Responsibly Through Open Standards.pdf#page=26|PDF p.26]]

