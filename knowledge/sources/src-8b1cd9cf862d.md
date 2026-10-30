---
id: "src-8b1cd9cf862d"
type: "source"
title: "Samtec 224/448G：近芯片铜缆与Open CPX的分层路线"
source_path: "expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf"
source_git_blob_sha: "338caf6ac94b760494d66b02e5ce626a820e256e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
text_reviewed: true
key_pages_visual_checked: [5, 6, 7, 12, 13]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Samtec 224/448G：近芯片铜缆与Open CPX的分层路线

## 核心结论
Si-Fly HD把高速launch从长PCB转到封装基板或近芯片连接器，以短电通道接铜缆/光引擎。Open CPX定义可插拔混合介质接口，并不固定光学调制、激光器或网络协议；448G示范仍是PoC。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=4|PDF p.4]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=8|PDF p.8]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=13|PDF p.13]]

## 关键证据、指标与条件
- p3的DAC~2m、ACC~5m、AEC~7m、LPO~50m、AOC100m+是路线级示意，缺统一lane速率、功率及FEC，不能当产品reach保证。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=3|PDF p.3]]
- EyeSpeed 32AWG、1m、56GHz插损14.3dB、skew最大1.75ps/m。图是电缆本体的差分插损，不包括两端ASIC/封装/连接器；图例92.5Ω而正文92Ω，选型应索取正式规格。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=5|PDF p.5]]
- Type1分离高速与电源控制socket：64DP=32Tx+32Rx，32×200G=6.4Tb/s每方向，10mm高速/10或13mm电控高度、<15mm beachfront；Type2合并72DP/36lane，7.2Tb/s每方向、7mm高、<16mm宽。不能把DP数量全部乘200G当单向带宽。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=9|PDF p.9]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=10|PDF p.10]]
- 已看路线图：2026年9月Rev1.0，2027年3月Rev1.1加入铜介质/Type3等，6月Rev2.0瞄准64/72×200G，2027末/2028初Rev3.0瞄准N×400G，均subject to change。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=12|PDF p.12]]
- 448Gbps演示为两substrate socket+1m低skew缆，支持PAM4和/或PAM6；无BER、测试时长、FEC或功率数据。现场展示照片不是量产448G端到端资格证明。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=13|PDF p.13]]

## 图表与架构
已检查p5/6/7/12/13。p6 co-packaged与near-chip示意分别标95×95和90×90封装，显示launch位置不同；p7同时画铜缆与光模块，支持接口复用而非必然相同维护流程。[[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=6|PDF p.6]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]] 与 [[knowledge/comparisons/network-optics-integration-tradeoffs]]。与Samtec其他CPX材料同厂同路线，不能当独立验证；需区分OPEN NPO与Open CPX命名及机械pin map。

## 不确定性与待验证
全文带Confidential标识。需全通道S参数、温度/弯折/串扰与老化、448G接收算法、插拔寿命及多供方互换记录，方能将PoC写入推理scale-up成本/可靠性预算。


跨源比较：[[knowledge/comparisons/network-channel-interface-budget]]。
