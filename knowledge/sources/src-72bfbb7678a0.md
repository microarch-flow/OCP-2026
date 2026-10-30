---
id: "src-72bfbb7678a0"
type: "source"
title: "Caliptra开源DV：验证资产必须随IP交付并持续复用"
source_path: "Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf"
source_git_blob_sha: "979c54204041612b843748e95908f2d3380bd6af"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-text"
evidence_pages: [3, 4, 5, 7, 8, 9, 11, 12]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# Caliptra开源DV：验证资产必须随IP交付并持续复用

> 阅读范围：已阅读本文件全部可提取文字（16页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- 演讲的缺口不是“完全没验证”，而是原有验证偏软件驱动、覆盖率驱动DV曾在封闭环境中，难以独立复现/评审。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=4|PDF p.4]]
- 作者主张把激励、检查器、覆盖模型和回归基础设施作为IP的可复用属性，集成商改参数/扩展后必须重新验证。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=11|PDF p.11]]

## 关键证据

- 块级测试可直接刺激和检查IP，尤其适合错误路径与罕见时序，而不只经由CPU固件触达。OpenTitan迁移步骤包括总线替换、原特性复用和Caliptra新增特性补测。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=3|PDF p.3]][[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=5|PDF p.5]]
- SHA3_CTRL移植测试在数周后通过，但明确尚未覆盖Caliptra特有wrapper；“全部测试通过”不等于该模块新增逻辑已完整验证。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=8|PDF p.8]]
- 共享DVSim、UVM代理/抽象库和公共环境，并允许渐进采用。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=12|PDF p.12]]

## 指标与条件

- VeeR示例：约22个块级testbench，另有顶层PyUVM；Verilator可选VCS，cocotb/PyUVM、RISC-V随机与合规测试、锁步故障注入。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=7|PDF p.7]]
- I3C示例：约90个cocotb测试、约87k LOC，支持AHB/AXI，约24个块/单元测试加全核测试。数字描述测试资产规模，不是缺陷逃逸率或安全证明；未给覆盖率百分比/目标。[[Security/Advancing Caliptra Security Through Open-Source DV Infrastructure.pdf#page=9|PDF p.9]]

## 图表与架构

图p.5未视觉核对；这里只使用文字所列块级/系统级验证分工，不推断精确连接。

## 关联与比较

架构评审应要求供应商交付可重跑DV及配置差异清单，而非只提交一次通过截图；这是从作者证据导出的集成验收建议，不是演讲量化结论。

## 不确定性与待验证

缺最终功能/代码覆盖率、未覆盖项、正式验证边界与逃逸缺陷数据；开源、测试数和代码行数均不能单独证明安全。

