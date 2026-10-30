---
id: "src-a4b99dc36d1b"
type: "source"
title: "AI原生硬件验证：本地上下文、受控执行与原始证据闭环"
source_path: "Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf"
source_git_blob_sha: "c578cd89bca719a808cab3ea1d583132d4712835"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-text"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp", "source", "platform", "test-&-validation"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# AI原生硬件验证：本地上下文、受控执行与原始证据闭环

> 阅读范围：已阅读本文件全部可提取文字（11页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- 作者的差异化不在自研基础模型，而在把项目KB、实验室命令、console adapter和日志证据暴露给agent，使其能执行/观察/分析/回写。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=2|PDF p.2]][[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=4|PDF p.4]]
- 文件把已有raw-log signature分析与未来OCP T&V JSONL adapter/step IDs区分，不能称所有日志已标准化。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=7|PDF p.7]][[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=8|PDF p.8]]

## 关键证据

- KB定期把文档、会议、bugs转Markdown并project-scoped索引；执行链是intent→command template→router→adapter→SUT→archive，由工程师控制命令层。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=5|PDF p.5]][[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=6|PDF p.6]]
- 原始日志按node/run/date/type/version保存，FTS5/SQL索引回答“去哪找”，AI回到证据区分known defect/new issue/noise。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=7|PDF p.7]][[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=8|PDF p.8]]
- McConsole前端串接Connect/Run/Observe/Reason/Update，并列公开log_analyzer/mcconsole仓库。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=9|PDF p.9]][[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=10|PDF p.10]]

## 指标与条件

2024→2026三阶段为作者演进叙述，没有执行成功率、人工节省、漏报/误报或guardrail失败统计；“proven in practice”未附可比较实验。[[Test & Validation/AI-Native Hardware Validation- Building a Local-Context Agentic Test and Debug Platform.pdf#page=3|PDF p.3]]

## 图表与架构

未视觉核对GUI图或现场执行；仅分析文字记录的架构和计划状态。

## 关联与比较

与NPI spec-to-signoff相比更偏实验室运行/故障复现，本地证据索引是共同基础；执行授权和写回权限必须区分，模型推断不能直接覆盖事实日志。

## 不确定性与待验证

需危险操作门禁、目标识别、并发资源占用、可重放命令日志、失败恢复和跨版本KB新鲜性验证。

