---
id: "src-f11eeb40a10a"
type: "source"
title: "Dispersion Managed Transceiver：扩展 CWDM 的距离"
source_path: "executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf"
source_git_blob_sha: "1a18160ecce858f916a20fbafbf09aa4099f2bb2"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [4, 7, 8, 9, 10, 12]
text_reviewed: true
key_pages_visual_checked: [4, 7, 8, 9, 10, 11]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-optical-service-boundary]]"]
---

# Dispersion Managed Transceiver：扩展 CWDM 的距离

## 核心结论
Linktel 在CWDM模块中加入DMD色散管理，目标以低附加功耗延长800G/1.6T链路；材料含样机测试，但不能把alpha/beta与400G/lane概念验证写成量产成熟度。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=4|PDF p.4]][[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=10|PDF p.10]]
## 关键证据
800G 20km：TH5、36pcs、10次温度循环；800G FR4 10km：TH5、10pcs、4次循环。图内明确10–70°C，属于厂商测试而非独立认证。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=7|PDF p.7]][[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=8|PDF p.8]]
## 指标与条件
- 800G 20km页称pre-FEC BER<1e-7、FEC BIN≤4、8通道预算>10dB。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=7|PDF p.7]]
- 1.6T 10km：212Gbps BER<1e-11，226Gbps+inner FEC BER<1e-12，预算7.2dB；BER口径随FEC改变，不能同列直接排名。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=9|PDF p.9]]
- “400G/lane”演示实际190GBaud PAM4=380Gbps，1271nm、3km、TFLN调制器；恢复眼图不等于完整3.2T产品可靠性。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=10|PDF p.10]]
## 图表与架构
已视觉核对p.4、7–11，OCR补齐图内测试条件。p.11笑脸评分无量化权重，不能当成本/功耗实测比较。
## 关联与比较
可与 [[knowledge/sources/src-b36ea15b7121|相干scale-across]] 对读，但距离、调制/FEC、功耗及运行温区不同；不能用一份演示得出DMD普遍优于coherent。
## 不确定性与待验证
需绝对模块功耗、观测时长、光纤/连接损耗、锁定漂移与多厂家互通。开放设计访问同时存在专利申请，不等于免许可实施。[[executive-sessions/18_Dispersion Managed Transceiver for Next-Gen AI Fabrics.pdf#page=12|PDF p.12]]

## 知识网络
[[knowledge/concepts/executive-expo-optical-service-boundary]]
