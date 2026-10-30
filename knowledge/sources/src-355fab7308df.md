---
id: "src-355fab7308df"
type: "source"
title: "Microsoft 光scale-up：先限制共同故障域，再谈冗余"
source_path: "ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf"
source_git_blob_sha: "682df2f0075608bff639cd8a10da7a06f32ff457"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8, 10, 12, 13, 14, 15]
text_reviewed: true
key_pages_visual_checked: [7, 8, 12]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optics-reliability]]"]
---

# Microsoft 光scale-up：先限制共同故障域，再谈冗余

## 核心结论
更高光密度会把多lane/λ耦合到同一个laser、PIC或连接器；多逻辑链路不等于多独立故障域。可靠性设计需让激光、光引擎、纤维shuffle与ASIC lane映射共同实现可控降级。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=5|PDF p.5]][[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=6|PDF p.6]][[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=7|PDF p.7]]

## 关键证据、指标与条件
- 单laser可影响100%关联通道；多源分区、波长分区与interleaving图示把单点影响降到25–50%或25%。这些比例是拓扑示意下的容量/通道占比，不是测得故障概率或作业停顿减少比例。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=7|PDF p.7]]
- p.8把redundancy/shuffling候选点画在laser供给、OE互连、ASIC连接附近；若路径仍共用一个dense connector或电源域，lane冗余可能无法抵御共同故障。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=6|PDF p.6]][[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=8|PDF p.8]]
- OCI GEN1共用PHY组合NRZ、WDM、BiDi，8λ标准laser set，一根纤维双向；它统一光链路，未统一整个rack、runtime或transport。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=12|PDF p.12]][[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=13|PDF p.13]]
- 路线图400G“2027(?)”、800G“>2030(?)”有明确问号，不得改写成确定发布时间。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=10|PDF p.10]]

## 图表与架构
已核p.7故障分区、p.8可shuffle位置及p.12PHY范围。材料的Azure产品图与“Maia300”字样不构成该产品规格/状态证据，本卡不据此推断。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=3|PDF p.3]]

## 关联与比较
[[knowledge/concepts/network-optics-reliability]]：和SROI链路flap、ELS/ILS选择、OCS共享spare合看，实际目标应是单故障后仍完成服务SLO，不是单器件FIT最低。

## 不确定性与待验证
缺fault injection、降级带宽、恢复时间、冗余开销及实际MFU；25%lane损失可能在同步collective中产生远大于25%性能影响。作者建议OIF管laser/CMIS/link、OCP管tray/系统、APC管wafer-to-system，是协调倡议，不是已经全覆盖的标准。[[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=14|PDF p.14]][[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=15|PDF p.15]]

