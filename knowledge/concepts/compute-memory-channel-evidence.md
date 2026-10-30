---
type: concept
title: "从通道插损到应用带宽：高速互连的证据阶梯"
tags: [ocp2026, concept, compute-memory]
---

# 从通道插损到应用带宽：高速互连的证据阶梯

## 核心命题
S-parameter好看，不等于BER合规；BER合规，不等于多端点fabric非阻塞；fabric峰值带宽，也不等于推理goodput。比较铜、光、连接器或signal conditioner时，先问证据在哪一层。

## 证据阶梯
1. **几何/材料与仿真**：模型、reference plane、package/PCB/cable边界及是否含全部过渡。
2. **通道实测**：VNA带宽、校准与de-embedding、IL/RL/串扰、样本与机械/温度状态。
3. **运行链路**：TX/RX/equalization、lane rate/调制、BER、FEC、眼图与恢复。
4. **fabric服务**：拓扑、流量矩阵、oversubscription、拥塞控制、重试与隔离。
5. **应用结果**：有效payload、request distribution、token/s、TTFT/TPOT、p99与SLO-goodput。

上述分层是本库综合方法；层间转换需要新增证据，不能用一个无条件“效率因子”代替。

## 同为铜互连，证据并不同质
|材料|实际支持|不可扩大的结论|
|---|---|---|
|TE CPC vs NPC|448G PAM6 @90GHz约6 vs12dB，PAM4 @112GHz约7 vs14dB；**仿真不含package loss**，两方案cable/PCB长度不同。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=5\|PDF p.5]] [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=6\|PDF p.6]]|不能称整个package-to-package通道实测减半，更不能推出应用吞吐2倍|
|Luxshare CPC|300mm assembly，VNA测至110GHz；raw/de-embedded曲线。[[server/Copper-Interconnect-Innovations-for-Realizing-400G-Electrical.pdf#page=6\|PDF p.6]] [[server/Copper-Interconnect-Innovations-for-Realizing-400G-Electrical.pdf#page=7\|PDF p.7]]|设计“120+GHz”主张不等于仪器测到了120GHz|
|Luxshare串扰|2×3 diff-pair subset，2 NEXT+3 FEXT邻居的**仿真**。[[server/Copper-Interconnect-Innovations-for-Realizing-400G-Electrical.pdf#page=9\|PDF p.9]]|不能当作完整高radix系统所有aggressor实测|
|OCP conditioner footprint|200mil板/170mil via，给出至54GHz的串扰例子；方法未完整说明。[[server/From-Fragmentation-to-Footprint-The-OCP-Standard-for-AI-Signal-Conditioners.pdf#page=3\|PDF p.3]]|不能据此证明128GBaud/256Gbps PAM4全链路BER合规|

## 将可制造性纳入有效带宽
CPC缩短高损耗PCB路径，但增加package附近的线缆应力、弯折/skew、冷板载荷、热循环耦合。铜和光的选择是系统共同设计，不只是固定长度插损曲线比较。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=7|PDF p.7]] [[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=8|PDF p.8]]

两项具体证据边界：
- 90°C曲线约2.4dB是**ΔMagnitude增加量**，不是总插损；loss(dB值)每10°C约增3–5%的说法也不能直接作线性功率百分比。[[server/Co-Packaged-Copper-at-448G-Balancing-Electrical-Efficiency-with-System-Level-Complexity.pdf#page=8|PDF p.8]]
- 五次remove/reseat差0.51dB说明小样本重装一致性，不是量产公差、长期插拔或温度循环寿命。[[server/Copper-Interconnect-Innovations-for-Realizing-400G-Electrical.pdf#page=8|PDF p.8]]

## 架构模型应存什么（本库建议）
`ChannelObservation`至少包含：频率轴与单位、调制/baud、reference plane、包含/排除段、长度/线规、温度、机械状态、样本数、测量或仿真、校准方法。随后把链路FEC/重试、协议payload比例、fabric拥塞建成不同层，不用“400G”一项覆盖全部。

对推理系统尤其要区分：一次KV远端读取的传输时间、排队尾部、链路恢复与调度停顿；没有端到端联合分布，不声称p99改善。封装beachfront给几何上限，TLL给协议开销，二者都不是应用实测带宽。

## 关联
[[knowledge/concepts/compute-memory-package-memory-wall|封装几何与内存墙]] · [[knowledge/concepts/compute-memory-chiplet-link-efficiency|链路有效带宽]] · [[knowledge/concepts/compute-memory-modular-platform-contract|平台契约]] · [[knowledge/concepts/compute-memory-capacity-vs-datapath|数据路径收益归因]]
