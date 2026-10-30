---
id: "network-channel-interface-budget"
type: "comparison"
title: "近封装铜光选型：完整通道预算与接口开放是两张验收表"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 近封装铜光选型：完整通道预算与接口开放是两张验收表

## 定义
“接口开放”回答机械/电源/引脚/管理是否可组合；“通道通过”回答目标速率、温度与寿命下是否有足够SI/FEC裕量。前者不能代替后者，器件IL也不能代替完整ASIC-to-ASIC链路。

## 把四种漂亮数字放回原边界
- Samtec的1m32AWG56GHz约14.3dB为线缆数据，448G1m PoC未给BER；不能把同一页线路图reach当量产承诺。[[knowledge/sources/src-8b1cd9cf862d]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=5|PDF p.5]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=13|PDF p.13]] [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf#page=3|PDF p.3]]
- BizLink的85cm约14–15dB是110GHz去嵌线缆，而500mm CPC完整fixture约40dB在112GHz，两者差异不表示较长缆反而更好，首先是边界不同。同一1m DUT剥线准备就有1.7dB差异。[[knowledge/sources/src-b3a3d01ab7f5]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=5|PDF p.5]] [[knowledge/sources/src-b3a3d01ab7f5]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=10|PDF p.10]] [[knowledge/sources/src-b3a3d01ab7f5]] [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf#page=12|PDF p.12]]
- Ciena67dB实例是redriver前45dB+后22dB，并非被动67dB或补偿后只剩22dB；BER约7×10⁻⁹对应该分段条件，不是任意分配总损耗都能通过。[[knowledge/sources/src-5ad0cded9ed9]] [[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=8|PDF p.8]]
- Genuine的1.6T Full DSP/LRO/LPO功耗与BER不同，ELSFP<8.5W也不包括整个NPO引擎；不统一激光、host SerDes、DSP/FEC、温度与fiber损耗，无法计算等可靠性pJ/bit。[[knowledge/sources/src-cd099b2e021a]] [[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=11|PDF p.11]] [[knowledge/sources/src-cd099b2e021a]] [[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf#page=13|PDF p.13]]

## 接口开放的收益与边界
Molex共PCB footprint可推迟铜/光选择，但NPO与NPC是不同receptacle，电源/sideband、应力释放和导向不同；不是任意现场热换。100DP包含控制/电源，数据32Tx+32Rx按200G得6.4T每方向，不能用224G capability乘全部触点。[[knowledge/sources/src-221406478e5b]] [[expo-hall-sessions/Enabling-an-Open-Near-Package-Ecosystem-for-AI-Scale-Up-presented-by-Molex.pdf#page=11|PDF p.11]] [[knowledge/sources/src-221406478e5b]] [[expo-hall-sessions/Enabling-an-Open-Near-Package-Ecosystem-for-AI-Scale-Up-presented-by-Molex.pdf#page=12|PDF p.12]]

Sumitomo四芯纤允许先MCF主干+两端FIFO保持端点，再走原生MCF；可节约空间，但增加FIFO、对准与修复负担，同纤多core也共享部分物理故障域。[[knowledge/sources/src-d384bc75e83a]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=10|PDF p.10]] [[knowledge/sources/src-d384bc75e83a]] [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf#page=12|PDF p.12]]

## 两张应交付的验收表（本库归纳）
**接口表：** 版本/合法组合、lane映射和极性、供电/上电顺序、管理/遥测、热机械约束、拔插/维护程序、二供互通证据。

**通道表：** ASIC die/封装/PCB/连接器/缆/有源级各自预算；固定去嵌方法和S参数方向；注明速率/调制/FEC、光源共享、温度、弯折/老化、串扰aggressors；报告pre/post-FEC BER、误码突发、flap、恢复与实际业务p99。ACC相对AEC节电/延迟应按每端加总，并含所省/新增的host补偿，不能用“zero latency”省略传播。[[knowledge/sources/src-5ad0cded9ed9]] [[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=6|PDF p.6]]

## 选择结论
近封装缩短PCB不是无条件优于pluggable，它会迁移散热/返修/激光故障域；开放接口改善供应链选择权，但商业收益须等可维护性和现场错误率明确后再算。

关联：[[knowledge/concepts/network-optical-integration]]、[[knowledge/concepts/network-optics-reliability]]、[[knowledge/comparisons/network-optics-integration-tradeoffs]]。

