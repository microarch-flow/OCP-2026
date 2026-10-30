---
id: "src-3f2d49fba822"
type: "source"
title: "Broadcom CPO/OCI：大规模光互连路线与光纤部署预算"
source_path: "ocp-special-focus-photonics/CPO, OCI.pdf"
source_git_blob_sha: "2a9f5158adc3fffd699d9985b5b732c37968f9c3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 12, 13, 14, 15]
text_reviewed: true
key_pages_visual_checked: [3, 4, 6, 12, 13, 14, 15]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Broadcom CPO/OCI：大规模光互连路线与光纤部署预算

## 核心结论
从前面板SerDes到贴近芯片的D2D光I/O，可把功率与带宽密度边界向外推，但此材料主要是路线、组件制造与拓扑推演。与同仓库另一版本 [[knowledge/sources/src-664a269af69f]] 实质同源，不能当两项独立验证。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=3|PDF p.3]][[ocp-special-focus-photonics/CPO, OCI.pdf#page=15|PDF p.15]]

## 关键证据、指标与条件
- TH4/TH5/TH6分别25.6/51.2/102.4T，100/100/200G-lane；2028第四代在开发。页称>1M device-hours零flap，未说明具体代际、设备定义/温度/错误阈值，不能当作MTBF或零风险。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=4|PDF p.4]]
- 90% efficiency improvement 是无数值时间轴的checkpoint示意，不含workload、计算公式与测量样本；不等于训练吞吐提升90%。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=6|PDF p.6]]
- OCI图允许板上、基板和interposer等不同OE实现；BiDi TypeA/TypeB对接，每方向4λ、以1311/1331nm两组为示意，不能把OCI直接等同某一CPO封装。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=12|PDF p.12]]
- 200G“total link”表：DAC7pJ/bit/2m、integratedOCI7pJ/bit/500m、DR-LRO23pJ/bit/500m；无器件/测试方法/温度，按架构估计记录，不能与单端optical-engine pJ/bit混比。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=13|PDF p.13]]
- 1024XPU示例：每GPU25.6Tb/s、128双向fibers，16柜×64；switch列204.8Tb/s、1024fibers/unit、4柜×32=128台。GPU侧131072条纤维端接量与switch侧相当，不能把两端相加当独立光纤线路数。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=14|PDF p.14]]

## 图表与架构
已核关键图。p.15以1024pods×1024XPU推1048576端点，图却标×1000，属概念量级示意；未给scale-out每XPU带宽、超售或collective时延，不能把“一层scale-out”理解为整个百万GPU任意全带宽无阻塞。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=15|PDF p.15]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]、[[knowledge/concepts/network-optics-reliability]]：规模假设须继续落实为fiber shuffle、connector、ELS、可拆FAU和量产测试。[[ocp-special-focus-photonics/CPO, OCI.pdf#page=7|PDF p.7]]

## 不确定性与待验证
10×可靠性和铜级可靠性是厂商主张，未附本材料内的充分归因数据。需将组件/device/system hours分开，补完整电源边界、激光冗余、维修粒度与密集光背板安装成本。

