---
id: "src-14ff6cb09ed6"
type: "source"
title: "Adam’s Bridge 3.0：用NTT线性与双share换掉算术路径masking"
source_path: "Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf"
source_git_blob_sha: "e18c9e3c1bb69fee77e3dbea0672e9c69320c544"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [9, 10, 11, 16]
updated: "2026-10-30"
---

# Adam’s Bridge 3.0：用NTT线性与双share换掉算术路径masking

> 阅读范围：已阅读本文件全部可提取文字（18页）。关键页已视觉核对：9, 10, 11, 16；不代表逐页视觉审核。

## 核心结论

- 作者用NTT线性把秘密拆成两share，分别经过既有未保护算术datapath后再组合，以存储和并行路径换掉昂贵的算术级masking。该线性论证针对乘公开量等上下文，不能泛化所有秘密乘法。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=5|PDF p.5]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=6|PDF p.6]]
- ABR 3.0报告面积下降且敏感运算masking范围扩大；但TVLA“未观察泄漏”不是无条件侧信道安全证明。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=9|PDF p.9]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=14|PDF p.14]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=16|PDF p.16]]

## 关键证据

- ABR2反馈包括INTT首层、B2A、MLDSA PWA和MLKEM PWM问题；3.0表中给对应masking/删除B2A方案。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=4|PDF p.4]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=14|PDF p.14]]
- 配置分shuffle-only、core masking、extended masking（加Keccak），必须说明使用哪档再比较面积/安全。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=13|PDF p.13]]

## 指标与条件

- 作者5 nm面积：ABR2 protected ML-DSA-87+ML-KEM-1024为0.1096 mm²，ABR3 highly protected为0.0459 mm²，约58%下降；不是完整Caliptra面积。SRAM由59.7 KB到86.7 KB、+27 KB/45%。未给库/PVT/布局利用率或硅实测说明。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=8|PDF p.8]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=9|PDF p.9]]
- cycle比较：ML-DSA单轮sign 36,700→34,928（4.8%）；平均3.85轮141,295→134,473；ML-KEM decap 12,117→11,056（8.8%）；KeyGen 6,603→6,640反而约0.6%退步。无频率条件，不转成ns。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=10|PDF p.10]]
- 标准单元0.0860→0.0123 mm²按数值计算约85.7%减少，但页文称80%，存在口径/四舍五入不一致需问作者。Keccak页4x面积/8x慢针对子模块，整ABR图109%约为总面积+9%，不可当全系统4x。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=9|PDF p.9]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=11|PDF p.11]]
- FPGA侧信道实验10 MHz、156 MS/s，TVLA用Welch t-test；未给trace数量/完整阈值/高阶测试。[[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=15|PDF p.15]][[Security/Architectural Masking for PQC- Adam's Bridge 3.0 Leveraging NTT Linearity.pdf#page=16|PDF p.16]]

## 图表与架构

已视觉核对p.9、10指标，p.11总面积与Keccak子模块区别，p.16 t-score图。SIGENC区高t作者解释为公开值，不能因该区域峰值直接判定秘密泄漏。

## 关联与比较

PPA比较必须锁定masking配置及安全目标；面积与SRAM相反变化意味着制程SRAM宏、带宽和时钟约束可改变收益。

## 不确定性与待验证

需同库综合/布局、功耗、随机数吞吐、glitch/高阶DPA验证与目标ASIC复测。图未证明所有攻击模型安全，p.17集成Caliptra2.2为作者状态陈述。

