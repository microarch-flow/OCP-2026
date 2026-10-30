---
id: "src-b3a3d01ab7f5"
type: "source"
title: "BizLink 448G铜互联：测量去嵌与调制选择比单个插损数更重要"
source_path: "expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf"
source_git_blob_sha: "d51bd617e1eed07f7368cfdc43aef364dfe174a1"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 9, 10, 11, 12, 13]
text_reviewed: true
key_pages_visual_checked: [4, 5, 9, 10, 12]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# BizLink 448G铜互联：测量去嵌与调制选择比单个插损数更重要

## 核心结论
448G铜通道的挑战包括频谱、SNR、周期结构共振、线缆应力与接头测量。BizLink展示Paralink去嵌S参数与CPC样机，但“Ready for448G”不能代替含实际SerDes/FEC的BER/可靠性验收。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=4|PDF p.4]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=5|PDF p.5]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=9|PDF p.9]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=10|PDF p.10]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=12|PDF p.12]]

## 关键证据、指标与条件
- p4按PAM4/6/8的2/2.585/3bit每symbol算224/173/150GBd，Nyquist112/87/75GHz，SNR相对栏为0/-4.4/-7.4dB，正文明确更密调制要求更紧SNR，不能误读负数为接收要求更宽松。PAM6用理论log2(6)，不等于采用5bit/2symbol映射的实际2.5bit及编码/FEC开销。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=4|PDF p.4]]
- 同1m DUT在53GHz剥线1.0/0.8/0.6mm测插损-16.4/-15.0/-14.7dB，准备工艺就造成1.7dB差异；比较供应商时必须锁定fixture、对称性、夹紧力和去嵌。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=5|PDF p.5]]
- 30AWG双drain、92Ω，缠带pitch4/1.6/1mm对应约25–30/62–72/≥100GHz共振，短pitch改善notch但增加制造难度；不是仅改平均介电常数即可解决。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=9|PDF p.9]]
- p10曲线标题是**85cm、ISD de-embedding**后的SDD21/SDD11/SDC21，110GHz附近IL约14–15dB；不能与p12完整CPC测试通道直接横比。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=10|PDF p.10]]
- p12 no-drain39AWG样机图例标500mm、定制Rosenbergerfixture；SDD21在56/86.7/112GHz约-21/-30/-40dB，图延伸130GHz并在约118GHz有深notch。不是“110GHz全频无损”，也没有448G PAM4/6 BER。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=12|PDF p.12]]
- TeraNano标10×18mm/32DP、<6mm mating height；光连接器典型MPO/MMC IL<0.1dB为另一产品线，未给分布/连接对数，不能作为该铜样机的系统光损预算。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=11|PDF p.11]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=13|PDF p.13]]

## 图表与架构
已核p4/5/9/10/12。薄线靠近ASIC减少PCB损耗，但同时改变机械耐久/assembly margin。woven最多24高速pair与混合电源/光缆是布线选择，不是协议互通证据。[[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=6|PDF p.6]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]；与Samtec1m448G PoC、其他448G connector资料共同建立测试需求，不把不同线规、频点和去嵌边界曲线合成排名。

## 不确定性与待验证
全文Confidential标记保留。需多通道串扰、温度/弯折/老化、active终端、FEC/错误突发、样本数量及量产批间差；部件S参数优良不等于推理网络p99或低flap率。


跨源比较：[[knowledge/comparisons/network-channel-interface-budget]]。
