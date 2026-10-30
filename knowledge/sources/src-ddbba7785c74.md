---
id: "src-ddbba7785c74"
type: "source"
title: "Co-Packaged Copper at 448G: Balancing Electrical Efficiency with System Level Complexity"
aliases: ["Co-Packaged Copper at 448G: Balancing Electrical Efficiency with System Level Complexity"]
speakers: "Sakina Naqvi；Usman Saeed（TE Connectivity）"
source_path: "server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf"
source_git_blob_sha: "58ec21c7c443441e1d4fc0cb01c85dfaa878ed95"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 4, 5, 6, 7, 8, 9]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-channel-evidence]]", "[[knowledge/concepts/compute-memory-package-memory-wall]]"]
---

# Co-Packaged Copper at 448G: Balancing Electrical Efficiency with System Level Complexity

## 核心结论
CPC尽早从ASIC package逃逸到低损耗twinax，换取更好的信号预算，但把连接器公差、线缆应变、冷板/封装载荷和热循环耦合到package。电性能收益不是“系统更简单”的充分证据。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=2|PDF p.2]] [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=7|PDF p.7]] [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=8|PDF p.8]]

## 关键证据
channel limiter可能是breakout/termination而非线材；intra-pair skew影响BER、inter-pair skew受de-skew预算约束。弯折/扭转会改变路径，同一ps skew在更高baud下占更多UI。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=3|PDF p.3]] [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=4|PDF p.4]]

## 指标与条件
|对比|条件与证据等级|
|---|---|
|Twinax约4dB vs stripline约23dB@112GHz|250mm 30AWG cable vs254mm trace，示例channel曲线，不能忽略不同结构。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=3\|PDF p.3]]|
|CPC约6dB vs NPC约12dB@90GHz|448G PAM6 backplane **simulation**，不含package loss；图示CPC350mm cable，NPC250mm cable+100mm PCB。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=5\|PDF p.5]]|
|CPC约7dB vs NPC约14dB@112GHz|448G PAM4 I/O **simulation**，同样不含package loss。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=6\|PDF p.6]]|
|1m cable每升10°C，loss(dB值)增约3–5%|p.8温度曲线纵轴是**ΔMagnitude**；90°C约2.4dB是增加量，不是总插损。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=8\|PDF p.8]]|

## 图表与架构
CPC/CPO可以共享部分前面板/背板reference架构和package级机械热设计经验；这并不意味着铜换光是直接BOM drop-in。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=9|PDF p.9]]

## 关联与比较
[[knowledge/concepts/compute-memory-channel-evidence|高速通道证据分层]] · [[knowledge/concepts/compute-memory-package-memory-wall|封装逃逸几何]]。计算有效bandwidth需进一步计SerDes/FEC、误码和重试，而非只看Nyquist插损。

## 不确定性与待验证
缺完整TX/RX均衡、BER/FEC、温度/工艺角、制造良率、插拔和应力测试。材料页脚说明产品只是reference、不是已许可OCP贡献；不能称已标准化可互换器件。

## 原始页码导航
[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=2|p.2]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=3|p.3]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=4|p.4]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=5|p.5]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=6|p.6]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=7|p.7]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=8|p.8]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=9|p.9]] · [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=10|p.10]]
