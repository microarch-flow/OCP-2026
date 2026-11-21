---
type: reference
title: OCP 2026 官方资料补读
tags: [ocp2026, provenance]
updated: 2026-11-21
---

# OCP 2026 补读：光交换、液态金属 TIM 与 ORv3 运输

这三份资料来自 [OCP 2026 官方场次档案](https://www.opencompute.org/events/ocp-summit/2026-ocp-global-summit/recorded-content/)，不是仓库原始 PDF 的替换件。已从官方 Drive 链接取得有效 PDF，并核对封面、物理页数和 SHA-256。正文的页码均为从 1 开始的 PDF 物理页码。仓库的原始空文件和历史统计仍保留；参见 [[knowledge/source-quality|来源质量与缺失材料]] 和 [[knowledge/index|知识库首页]]。Dropbox 和视频链接是主办方提供的备用入口，不代表链接内容逐一核验。

| 官方场次 | 官方链接 | 页数 | 字节数 | Drive 副本 SHA-256 |
| --- | --- | ---: | ---: | --- |
| Wavelength-Granular OCS with Solid-State OPA: Energy-per-Bit for AI Fabrics | [Drive](https://drive.google.com/file/d/1OBXBZTp1y0VxWtv2p-zh1PU8nzAwqqG5/view?usp=drivesdk) / [Dropbox](https://www.dropbox.com/scl/fi/kse85y53ls0nf8cu1q2xb/Wavelength-Granular-OCS-with-Solid-State-OPA-Energy-per-Bit-for-AI-Fabrics.pdf?dl=0&rlkey=5wxb9ri8vzivsx7msv4yd630b) / [Video](https://www.youtube.com/watch?v=1Z9CBk83DQU) | 12 | 1144989 | `d570d1d8f08975b49c024ca518ba2b79189067fbbd3c814ee41acda135211d87` |
| Latest Advancements with Thermal Interface Materials | [Drive](https://drive.google.com/file/d/1tPNYA22CyJA9LPrNe1FRGvlB04g4fHna/view?usp=drivesdk) / [Dropbox](https://www.dropbox.com/scl/fi/i07dmsucti1jlba3ikfk7/Latest-Advancements-with-Thermal-Interface-Materials.pdf?dl=0&rlkey=1p6aco7f8ln6k91u1u274weog) / [Video](https://www.youtube.com/watch?v=6At3oJkB7Xs) | 34 | 3847983 | `5668279983b51bcc7ebba90c4d15ddd7b88c50d25f4a5c148942682310b759d1` |
| ORv3 Risk Assessment of Multi-degree of Freedom Transportation Vibration | [Drive](https://drive.google.com/file/d/1mXNJ4EAHaeEgbVJCd2E7qT3VIPZ1uw84/view?usp=drivesdk) / [Dropbox](https://www.dropbox.com/scl/fi/l98g2twk5fvr9xwnjpzo9/ORv3-Risk-Assessment-of-Multi-degree-of-Freedom-Transportation-Vibration.pdf?dl=0&rlkey=nbh4lzluqytokgfe39debji0q) / [Video](https://www.youtube.com/watch?v=JBb0ja9ath8) | 24 | 2472943 | `72da5539a1608edb3b3e113d2aa03989ea424cec8df87229350f17ea268cfd2d` |

场次名以主办方目录为准：TIM 的 PDF 封面是 *Cold Plate and TIM Lightning Talks*（第 1–2 页是总览）；ORv3 的封面是 *ORv3 Risk Assessment of Real World Transport Conditions*（第 1–3 页列出 TransPak 与 Google 演讲人）。二者都由上方对应官方场次直接链接。

## 光互连：先算每个有用 bit，再谈交换器功耗

- **方案（第 3–7 页）：** 作者把插入损耗、分配带宽的实际利用率、电域转发跳数列为系统能耗的主要影响因素。器件方案是声光驱动的固态光学相控阵（OPA），利用随波长变化的偏转，将一根输入光纤中的波长分别接到不同输出；第 7 页以 8 个 O-band 波长说明。独立收发平面和更细粒度的带宽配置属于方案，不是实网评估。
- **已演示（第 9 页）：** 作者报告芯片级二维波束转向、微秒量级随机访问切换、本征插损 0.7 dB、旁瓣抑制超过 28 dB、连续运行指向稳定度在 ±0.5 mrad 内。系统综合插损约 3 dB 是含耦合、路由、封装的预测；旁瓣抑制也不能替代同时多波长链路的端到端串扰和误码验证。
- **模型和待验证（第 10–12 页）：** 投影曲线在 400G / 800G / 1.6T 给出 8 / 4 / 2 pJ/bit，依赖近似恒定的保持功耗与对应线速，不是已测的整网每有用 bit 能耗。固定波长栅格、多音串扰预算、主动保持与热漂移均影响工程实现；作者将同时多波长与大规模网络验证列为后续工作。做架构比较时，应按实际交付 payload 计 bit，并纳入端点/耦合、空闲与重配开销，报告负载和延迟条件。

## 液冷：TIM 导热率不是装配后的全部热阻

- **实验范围（第 3–10 页）：** 第一组报告对比 LM306 液态金属和 PCM，覆盖 660–2655 W、100–400 W/cm²。作者在本试验范围内观察到流量对有效热阻的影响最大，其次为功率/热流密度，再其次是 TIM；不应推广为所有冷板或界面的固定排序。
- **装配状态（第 13–20 页）：** Graphcore 与 Boston Materials 用 Fit-Freeze-Measure 表征受载形状，并据此调整预成型 TIM 与垫片。案例中翘曲从自由状态 180 μm 到 29.4 psi 受载状态 99 μm；作者报告约 2600 W 热测试载具在 6 L/min、入口 40 °C 下热点下降 6.1 °C（作者给出约 8%）。这是特定试件和工况的实测结果，不是批量 GPU 的普遍温降。测量冻结温度、实际工作温度与热循环时的翘曲还要区分。
- **失效与缓解（第 23–32 页）：** 第三组讨论导电液态金属迁移、材料相容性、氧化和泵出等风险，并展示凝胶态涂层/垫片降低迁移和氧化的实验示例。这不等于完整寿命、重复装配或量产可靠性验证。工程上应同时锁定夹紧压力、间隙、流量、入口温度和围挡材料，在热循环后再检查热阻与泄漏。

## ORv3：运输风险评估应保留真实输入和产品响应

- **为什么做现场测量（第 4–7 页）：** 演讲对照所讨论的标准实验室单自由度振动方法和实车多自由度运动。不能把这一对照理解为所有标准绝无多轴测试，也不能将单轴试验一概视为无效。
- **测到什么（第 12–18 页）：** 作者介绍布置多点加速度计与摄像设备，同时保存时域事件与频域功率谱密度（PSD）；图示/视频示例包括路障或坑洼冲击、横向和前后运动以及空气悬挂位移。该组现场示例不是可推广的跨线路分布、认证门槛或失效率统计。只保留单轴 PSD，会失去瞬态峰值与轴间关系。
- **工程建议（第 19–24 页）：** 从现场输入和机架响应出发构造代表性实验室谱，探索多轴复现，并用失效试验识别裕度与故障模式，再反馈结构设计和包装。作者呼吁共享脱敏线路动态数据和推进公共方法，不是发布新 OCP 认证规范。见 [Google 开放随机振动测试项目](https://github.com/GoogleCloudPlatform/open-random-vibration-testing-of-ots-dc-hardware)（演讲第 22 页所列）。

三份材料可以串成一条评估原则：光交换不能只报器件功耗，液冷不能只报材料导热率，运输不能只报台架 PSD。都要先确定实际系统边界，再用能代表真实工况的量做比较。

## 回到各主题

- [[knowledge/topics/topic-53641b6ba53f|FTS: AI / HPC]]：光交换与端到端能效。
- [[knowledge/topics/topic-bb9471981d21|Cooling：Cold Plate]]：TIM、夹具与系统热阻。
- [[knowledge/topics/topic-3183eb24a958|Rack & Power]]：ORv3 机架运输可靠性。
