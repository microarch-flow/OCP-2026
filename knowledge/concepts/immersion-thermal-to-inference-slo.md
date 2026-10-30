---
type: concept
title: "从热资格到推理SLO：Denvr案例中不能合并的三组证据"
tags: [ocp2026, concept, immersion]
---

# 从热资格到推理SLO：Denvr案例中不能合并的三组证据

## 核心命题
冷却方案可通过热/功率/链路测试，也可实际运行LLM，但要声称“改善p99、tokens/J或TCO”，仍需要相同服务条件下的对照。Denvr材料难得给出具体推理p99，同时也清楚展示证据不能越级。

## 三组实验分开记账
|组别|硬件/负载与条件|观测|有效结论|
|---|---|---|---|
|H200推理|8×H200-SXM5-141GB，700W TDP；Llama3.1-Instruct70B、TP8、continuous batching、3072输入/1024输出、最多150并发|8068 output tok/s；7.9 responses/s；p99完整响应19.82s|该浸没系统在报告配置能运行此服务点；无air/DLC推理对照。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=10\|PDF p.10]]|
|H200 cluster commissioning|多日HPL/OEM burst/idle分阶段|tank power/flow响应、进出液ΔT约10°C|负载变化下的冷却控制响应；不是请求p99或长期寿命测试。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=11\|PDF p.11]] [[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=12\|PDF p.12]]|
|Blackwell targeted-power|同平台8SXM、每GPU目标1000W、600s DCGM；浸没35°C vs DLC30°C PG25|996/995W；clock1567/1594MHz；peak core77/64°C；均8/8pass|两方案均接近目标功率且低于83°C限制；热边界不同且非LLM吞吐比较。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=15\|PDF p.15]] [[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=16\|PDF p.16]]|

## p99的确切对象
19.82s是生成完整1024-token response的p99，不是TTFT，不是TPOT，不是单token p99。没有运行时/precision、请求到达分布、warmup、测量窗口和逐请求数据，不能反推出尾部各阶段构成；也不能将1024/19.82当作系统总吞吐。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=10|PDF p.10]]

## 链路没有明显性能损失，不等于零风险
另一个DCGMI NVBandwidth比较中directional NVLink差约0.15%以内，PCIe GPU→CPU57.87 vs57.14GB/s；独立监控28360 samples为0 replay/EDATL事件。它支持所测配置的链路行为，不代表所有fluid/温度/长期老化均合格。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=17|PDF p.17]]
ITE委员会另一组106.25G PAM4图显示浸没BER虽低于参考门槛，却高于air；“通过”与“余量保持”应分别表达，不以一个平台的pass取消其他组件的风险。[[cooling-immersion/Community-Update-Immersion-IT-Equipment-ITE-Workstreams-Update.pdf#page=3|PDF p.3]]

## 从性能到成本，缺什么（本库建议）
- 固定模型/质量/precision、软件版本、输入/输出分布、并发/到达过程和SLO。
- 配置相同GPU数量、功率限额和合理可比的冷却边界；记录core/液温/流量/泵功率及throttling。
- 同时测TTFT、TPOT、完整响应分位数、output goodput和实际完成请求，而不只峰值功率。
- 计入server、pump/CDU、facility及闲置/故障恢复的能量边界，才能比较J/output-token。
- 纳入BOM资格、fluid维护、可维修性、故障统计和部署空间；约800W/server节省或PUE<1.04不能单独决定全TCO。[[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=4|PDF p.4]] [[cooling-immersion/Deploying-Immersion-Native-ITE-in-AI-NeoCloud-An-OCP-Collaboration-Story-Continued.pdf#page=6|PDF p.6]]

这些是待验证指标，不是本文已建立的浸没收益。

## 关联
[[knowledge/concepts/immersion-qualification-evidence|可靠性证据链]] · [[knowledge/concepts/power-cooling-capacity-evidence-ladder|冷却能力证据阶梯]] · [[knowledge/concepts/compute-memory-capacity-vs-datapath|同条件归因方法]] · [[knowledge/concepts/compute-memory-power-path-and-dynamics|供电动态边界]]
