---
type: topic
title: "expo-hall-sessions"
tags: ["ocp2026", "topic"]
---

# expo-hall-sessions

返回 [[knowledge/index|总入口]] · [[knowledge/source-manifest|来源清单]]。

## 阅读路线与主题综合

这是主题导航，不是该目录全部演讲的综合结论。优先从下方已有页级证据的源卡进入；待分析条目只提供原 PDF。跨源概念与比较入口见下方；结论的适用条件仍需回查相应笔记。

<!-- 可在此区域增加真实的主题综合，刷新脚本不会覆盖本段。 -->

<!-- GENERATED:topic-concepts:BEGIN -->
## 关联的跨源概念与比较

以下链接来自本主题源卡的实际引用，按引用它的源卡数量排序；关联不等于独立验证。

- [[knowledge/concepts/expo-evidence-to-deployment|展台方案到架构决策：先识别证据等级与系统边界]]（本主题 20 份源卡引用）
- [[knowledge/comparisons/expo-thermal-performance-contract|液冷验收合同：热容量、温度收益与推理服务效率不可互换]]（本主题 8 份源卡引用）
- [[knowledge/comparisons/expo-power-conversion-boundaries|800V商业评估：先对齐转换边界、可用容量与真实负载]]（本主题 7 份源卡引用）
- [[knowledge/comparisons/network-channel-interface-budget|近封装铜光选型：完整通道预算与接口开放是两张验收表]]（本主题 6 份源卡引用）
- [[knowledge/concepts/network-optical-integration|光学集成边界：LPO、NPO、CPO、XPO 与 Open CPX]]（本主题 6 份源卡引用）
- [[knowledge/comparisons/expo-inference-cost-contract|从CPU到异构AFD：先统一推理SLO，再比较成本与通信]]（本主题 5 份源卡引用）
- [[knowledge/concepts/network-executable-validation|可执行规范：把协议、平台和网络行为变成验收契约]]（本主题 4 份源卡引用）
- [[knowledge/concepts/network-inference-acceptance|推理网络验收：按通信图、尾延迟和可观测性采购]]（本主题 3 份源卡引用）
- [[knowledge/comparisons/network-optics-integration-tradeoffs|光互连选型对照：效率、可维修性与证据成熟度]]（本主题 2 份源卡引用）
- [[knowledge/concepts/network-scaleup-ethernet|Scale-up Ethernet：紧凑 framing、局部重试与端点边界]]（本主题 2 份源卡引用）
- [[knowledge/comparisons/network-laser-fault-domain|激光位置、故障影响与维修边界：ELS/ILS不能只比pJ]]（本主题 1 份源卡引用）
- [[knowledge/comparisons/network-optics-evidence-ladder|线性光的证据阶梯：800G现场、212G-lane仿真平台与未来CPO]]（本主题 1 份源卡引用）
- [[knowledge/concepts/executive-expo-power-control-boundaries|机柜电力：转换、容量、瞬态、保护是四个不同问题]]（本主题 1 份源卡引用）
- [[knowledge/concepts/network-clock-evidence|时间对齐的遥测证据：不确定窗口、缺失语义与安全闭环]]（本主题 1 份源卡引用）
- [[knowledge/concepts/network-multipath-behavior|多路径传输：选择路径、控制在途量与时序互通]]（本主题 1 份源卡引用）
- [[knowledge/concepts/network-optics-reliability|光互连可靠性：从平均 BER 转向中断、故障域与修复时间]]（本主题 1 份源卡引用）
<!-- GENERATED:topic-concepts:END -->

## 来源与分析进度

<!-- GENERATED:topic-sources:BEGIN -->
本主题：35 份 PDF；已分析声明 33；部分分析 0；零字节 2。

| 原始资料 | 源卡 / 状态 |
| --- | --- |
| [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf\|01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente]] | [[knowledge/sources/src-86e4ca03d02c\|Intel Agentic Rack：CPU关键路径、AMX与内存扩展的证据边界 · analyzed-visual]] |
| [[expo-hall-sessions/02_Aivres Liquid-Cooling AI Data Center Solutions Based on NVIDIA GPUs, p.pdf\|02_Aivres Liquid-Cooling AI Data Center Solutions Based on NVIDIA GPUs, p]] | [[knowledge/sources/src-d9e1255601d0\|AiVRES液冷AI数据中心：机柜规格、液路隔离与交付案例 · analyzed-visual]] |
| [[expo-hall-sessions/04_From Fleet to Firmware Bringing AI-Native Security to Open Hardware wi.pdf\|04_From Fleet to Firmware Bringing AI-Native Security to Open Hardware wi]] | [[knowledge/sources/src-f9135fb89608\|Google Project Equilibrium：威胁模型驱动的持续安全扫描 · analyzed-visual]] |
| [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf\|05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC]] | [[knowledge/sources/src-273c2c87ddf0\|Arm与Meta：AGI CPU双节点参考设计的复用边界 · analyzed-visual]] |
| [[expo-hall-sessions/07_Hyperscale Storage Solutions for NeoClouds presented by Everpure.pdf\|07_Hyperscale Storage Solutions for NeoClouds presented by Everpure]] | [[knowledge/sources/src-26e46c01d184\|Everpure NeoCloud存储：把闪存管理上移到主机软件 · analyzed-visual]] |
| [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf\|08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON]] | [[knowledge/sources/src-e1afbfae08ba\|LITEON 1.1MW HVDC机柜：冗余容量、储能与量产时间分层 · analyzed-visual]] |
| [[expo-hall-sessions/09_MetaRoCE Rethinking RDMA for the AI presented by Meta.pdf\|09_MetaRoCE Rethinking RDMA for the AI presented by Meta]] | [[knowledge/sources/src-84fd3e380dae\|Meta与AMD MetaRoCE：逐路径可靠性、接收端提示与64GPU集合通信 · analyzed-visual]] |
| [[expo-hall-sessions/10_Microgrids at Scale Resilient Power Infrastructure for AI Data Centers.pdf\|10_Microgrids at Scale Resilient Power Infrastructure for AI Data Centers]] | [[knowledge/sources/src-8e92642e8e25\|Microgrids at Scale：Resilient Power Infrastructure for AI Data Centers · analyzed-visual]] |
| [[expo-hall-sessions/A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec.pdf\|A-Pathway-to-224-448-Gbps-Copper-and-Optical-Connectivity-in-AI-Infrastructure-presented-by-Samtec]] | [[knowledge/sources/src-8b1cd9cf862d\|Samtec 224/448G：近芯片铜缆与Open CPX的分层路线 · analyzed-visual]] |
| [[expo-hall-sessions/Any-Rack-Everywhere-Future-Readiness-for-the-800-VDC-Transition-presented-by-Vertiv.pdf\|Any-Rack-Everywhere-Future-Readiness-for-the-800-VDC-Transition-presented-by-Vertiv]] | [[knowledge/sources/src-c70f44205046\|Vertiv 800VDC过渡：固定容量与可更换接口分别规划 · analyzed-visual]] |
| [[expo-hall-sessions/Burning Cash- The Hidden Cost of Ignoring Thermal in Your AI Strategy presented by Frore.pdf\|Burning Cash- The Hidden Cost of Ignoring Thermal in Your AI Strategy presented by Frore]] | [[knowledge/sources/src-f46544da55e0\|Frore LiquidJet：低结温收益必须用设施级每任务能耗验证 · analyzed-visual]] |
| [[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf\|Changing workloads demand Active Compute Fabric presented by Cornelis Networks]] | [[knowledge/sources/src-b9dba4889d3b\|Cornelis Active Compute Fabric：把在售CN5000与CN7000目标分开 · analyzed-visual]] |
| [[expo-hall-sessions/Cooler System, Hotter Innovation presented by HFH Thermal.pdf\|Cooler System, Hotter Innovation presented by HFH Thermal]] | [[knowledge/sources/src-d70b63b16f7b\|HFH微射流冷板与光模块TIM：热阻、压降和可插拔寿命的权衡 · analyzed-visual]] |
| [[expo-hall-sessions/Direct-Medium-Voltage-to-800VDC-Conversion-for-AI-Data-Centers-presented-by-Luxshare-Tech.pdf\|Direct-Medium-Voltage-to-800VDC-Conversion-for-AI-Data-Centers-presented-by-Luxshare-Tech]] | [[knowledge/sources/src-743127b50ad8\|Luxshare-Zinsight Nova Link SST：直接中压转800V的集成收益与风险 · analyzed-visual]] |
| [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf\|Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power]] | [[knowledge/sources/src-817afa57d410\|OmniOn负载区间效率：真实能耗积分优先于峰值百分数 · analyzed-visual]] |
| [[expo-hall-sessions/Enabling-an-Open-Near-Package-Ecosystem-for-AI-Scale-Up-presented-by-Molex.pdf\|Enabling-an-Open-Near-Package-Ecosystem-for-AI-Scale-Up-presented-by-Molex]] | [[knowledge/sources/src-221406478e5b\|Molex近封装生态：共用PCB footprint不等于任意模块即插即用 · analyzed-visual]] |
| [[expo-hall-sessions/Engineering-the-Transition-to-800-VDC-presented-by-MEGMEET.pdf\|Engineering-the-Transition-to-800-VDC-presented-by-MEGMEET]] | [[knowledge/sources/src-7690155542da\|MEGMEET 800VDC：rack、power-center与SST三条部署路径 · analyzed-visual]] |
| [[expo-hall-sessions/Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI.pdf\|Evolving-the-Infrastructure-Stack-Rack-Scale-Designs-Open-Firmware-and-Intelligent-Sustainability-presented-by-AMI]] | [[knowledge/sources/src-5a876f87b7ec\|AMI分层安全控制面：本地及时动作与全局策略协调 · analyzed-visual]] |
| [[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf\|Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena]] | [[knowledge/sources/src-5ad0cded9ed9\|Ciena ACC：线性redriver延长铜距，但67dB不是被动通道能力 · analyzed-visual]] |
| [[expo-hall-sessions/FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu.pdf\|FUJITSU-MONAKA- Optimized for High Performance and Energy Efficiency for AI, presented by Fujitsu]] | [[knowledge/sources/src-7fda851035fa\|Fujitsu MONAKA：CPU推理数值、3D芯粒与上市路线的口径 · analyzed-visual]] |
| [[expo-hall-sessions/Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture.pdf\|Fanless-Servers-Are-Coming-The-Peripheral-Coldplate-Roadmap-Behind-100-Heat-Capture]] | [[knowledge/sources/src-9e459d39cae8\|CoolIT无风扇服务器：15kW热测试与外围100%热捕获分开验收 · analyzed-visual]] |
| [[expo-hall-sessions/From Factory Floor to AI Factory- Deploying Intel® Xeon® 6 AI Infrastructure at Scale.pdf\|From Factory Floor to AI Factory- Deploying Intel® Xeon® 6 AI Infrastructure at Scale]] | 阻塞：原始文件为空 |
| [[expo-hall-sessions/Fungible Power Architectures for the 800V DC Transition presented by Edged Infrastructure.pdf\|Fungible Power Architectures for the 800V DC Transition presented by Edged Infrastructure]] | [[knowledge/sources/src-8247a45d4f9b\|Edged可重配电源架构：在800V母线上兼容AC负载 · analyzed-visual]] |
| [[expo-hall-sessions/How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink.pdf\|How-can-high-speed-interconnect-solutions-drive-next-generation-AI-data-centres-at-448G-and-beyond-presented-by-BizLink]] | [[knowledge/sources/src-b3a3d01ab7f5\|BizLink 448G铜互联：测量去嵌与调制选择比单个插损数更重要 · analyzed-visual]] |
| [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf\|Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec]] | [[knowledge/sources/src-e84fa2f73a45\|Nidec CDU：容量、可维护性与可靠性证据分层 · analyzed-visual]] |
| [[expo-hall-sessions/Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA.pdf\|Liquid-cooling Approaches for E1.S SSDs presented by KIOXIA]] | [[knowledge/sources/src-204a0ecdba21\|KIOXIA E1.S液冷SSD：解除功率约束不等于已证明IO尾延迟 · analyzed-visual]] |
| [[expo-hall-sessions/Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric.pdf\|Multi-Core Fiber - A solution for scale up, out, and across presented by Sumitomo Electric]] | [[knowledge/sources/src-d384bc75e83a\|Sumitomo四芯光纤：线缆密度提升与FIFO迁移代价 · analyzed-visual]] |
| [[expo-hall-sessions/One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix.pdf\|One-Abstraction-Many-Transports-Push-Mode-Communication-from-Chiplet-to-Rack-presented-by-d-Matrix]] | [[knowledge/sources/src-92d1f86e9495\|d-Matrix Push Mode与异构推理：统一传输抽象不消除分解代价 · analyzed-visual]] |
| [[expo-hall-sessions/Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco.pdf\|Open-Trusted-and-Secure-SONiC-at-Scale-presented-by-Cisco]] | [[knowledge/sources/src-3bd82acf3d66\|Cisco与Microsoft SONiC安全：部署准入已生产，运行时shield仍有路线图边界 · analyzed-visual]] |
| [[expo-hall-sessions/Powering AI Infrastructure- Innovations in Compute, Power, Connectivity and Cooling.pdf\|Powering AI Infrastructure- Innovations in Compute, Power, Connectivity and Cooling]] | 阻塞：原始文件为空 |
| [[expo-hall-sessions/Powering Progress- Murata's Role in Advancing OCP Innovation presented by Murata.pdf\|Powering Progress- Murata's Role in Advancing OCP Innovation presented by Murata]] | [[knowledge/sources/src-41638c79ca36\|Murata电源路径：ORv3现货、800V开发与封装近负载供电分开看 · analyzed-visual]] |
| [[expo-hall-sessions/Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects.pdf\|Scaling-AI-Compute-Fabrics-The-Pivotal-Role-of-NPO-in-Full-Stack-Optical-Interconnects]] | [[knowledge/sources/src-cd099b2e021a\|Genuine Optics：NPO、XPO与400G-lane演示的证据边界 · analyzed-visual]] |
| [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf\|Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC]] | [[knowledge/sources/src-e3c54df076ca\|MiTAC与AMD开放AI整柜：软件集成与多冷却路线的验证缺口 · analyzed-visual]] |
| [[expo-hall-sessions/The-Changing-Course-of-Storage-in-an-AI-World-presented-by-FADU.pdf\|The-Changing-Course-of-Storage-in-an-AI-World-presented-by-FADU]] | [[knowledge/sources/src-62274aac9546\|FADU AI上下文存储：减少数据通路与谨慎取消冗余 · analyzed-visual]] |
| [[expo-hall-sessions/Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab.pdf\|Water-or-Glycol-for-D2C-A-Quantitative-Tradeoff-Analysis-Across-Thermal-Operational-and-Programmatic-Domains-presented-by-Ecolab]] | [[knowledge/sources/src-48ba6ea6361c\|Ecolab水与PG25：热性能优势必须通过化学维护兑现 · analyzed-visual]] |
<!-- GENERATED:topic-sources:END -->
