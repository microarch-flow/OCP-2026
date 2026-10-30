---
type: concept
title: "模块化平台的五层契约：外形统一不等于可互换"
tags: [ocp2026, concept, compute-memory]
---

# 模块化平台的五层契约：外形统一不等于可互换

## 核心命题
标准化机械接口可以减少重复设计，但实际可互换性取决于机械、供电、数据、管理、生命周期五层契约同时成立。材料展示的是不同成熟度的规范/原型/经验，不能把每个“open”都解读为已验证的任意跨vendor互换。

|契约层|需要固定或描述的内容|代表材料|
|---|---|---|
|机械与热|卡尺寸、宽度/高度、连接器位置、冷却/维修空间、载荷|[[knowledge/sources/src-426b46f364ab\|OAC 物理边界]]；[[knowledge/sources/src-b681b46ceff2\|光子托盘边界]]|
|供电与时序|AUX/main、最大电流、功率/热限制、interlock、reset|[[knowledge/sources/src-39648bf032a4\|OAC 管理]]；[[knowledge/sources/src-be7d01c8a384\|NIC 更新]]|
|数据与拓扑|协议、lane/pair、clock、路由、隔离、oversubscription|[[knowledge/sources/src-a4497dec3bd9\|OAC 双fabric]]；[[knowledge/sources/src-705c5e1abbc1\|signal conditioner footprint]]|
|发现与管理|schema/profile/version、身份、描述符真实性、配置状态机|[[knowledge/sources/src-e2f8625e9c11\|M-PNP]]；[[knowledge/sources/src-5dcc644d4375\|工具链]]；[[knowledge/sources/src-d53a163f26fd\|MPESTI 扩展]]|
|生命周期|版本组合、更新/回滚、安全、可恢复性、平台/rack/service退出条件|[[knowledge/sources/src-dbbf8121adf7\|SmartNIC 系统集成]]；[[knowledge/sources/src-bcb86bd76e99\|Arm 系统规范]]|

## 从“发现”到“安全上电”
OAC的关键序列是 `AUX供电 → MC_RDY → 读CID → 兼容性检查 → 写SCD → PWR_EN主电源`。所以“上电前识别”准确含义是**主电源前**，不是管理逻辑没有供电。CID/SCD承载lane map、protocol、power、clock与slot context。[[server/Managing-Open-Adapter-Card-OAC.pdf#page=4|PDF p.4]] [[server/Managing-Open-Adapter-Card-OAC.pdf#page=6|PDF p.6]]

M-PNP把netlist/BOM/RTL信息变成JSON、校验/签名并装入FRU，减少手写配置。然而生成工具各自有成熟度，且发现路径必须在器件reset时仍可读；不能让发现本身依赖尚未启动的FPGA user logic。[[server/06_Onward Towards Industry Adoption – Demonstrating Modular Plug-and-Play.pdf#page=7|PDF p.7]] [[server/06_Onward Towards Industry Adoption – Demonstrating Modular Plug-and-Play.pdf#page=8|PDF p.8]] [[server/06_Onward Towards Industry Adoption – Demonstrating Modular Plug-and-Play.pdf#page=13|PDF p.13]]

**本库建议**：兼容性不只是布尔值，应包含版本、所需资源和可接受降级模式；未知profile、损坏描述符、管理端点超时应有明确fail-closed/回退策略。现有材料尚未给出所有异常路径的跨vendor验证矩阵。

## 三种“兼容”必须分开
1. **形状/footprint兼容**：signal conditioner可保留PCB布局，但不同vendor可能需要不同rail、flash/EEPROM及0Ω stuffing。[[server/From-Fragmentation-to-Footprint-The-OCP-Standard-for-AI-Signal-Conditioners.pdf#page=6|PDF p.6]]
2. **协议/软件契约兼容**：BSA/SBSA硬件、SBBR固件、SBMR管理与ACS测试边界不同；ACS通过不是OS认证或性能证明。[[knowledge/sources/src-bcb86bd76e99]]
3. **系统部署兼容**：多FW组件组成version recipe，经过平台、rack、集群/服务验证才达到部署退出条件。link-up不是终点。[[server/Scaling-Hyperscale-Cloud-Networking-from-400G-to-800G-System-Integration-Lessons-and-Implications-for-OCP-Platforms.pdf#page=6|PDF p.6]] [[server/Scaling-Hyperscale-Cloud-Networking-from-400G-to-800G-System-Integration-Lessons-and-Implications-for-OCP-Platforms.pdf#page=8|PDF p.8]]

DC-SCM 3.0是新接口方向、非前后兼容；公开“路线图”不能当旧模块可直接插入新主板。[[knowledge/sources/src-304e4a63c148]]

## 面向推理系统的选择问题
- OAC的224 differential pairs与112全双工lane预算不能混用；5000W是特定50V配置供电能力，不是每卡持续可散热功耗。[[server/Open-Adapter-Card-OAC-Sub-Rackscale-Acceleration-Lives-On.pdf#page=3|PDF p.3]]
- XPU scale-up与PCIe fabric分工不同，拓扑会改变P2P locality、hop和故障域；同样卡数不保证同样有效bandwidth或KV加载时间。[[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=4|PDF p.4]] [[server/Architecting-Openness-How-Switches-Enable-the-Future-of-Open-Adapter-Card-Platforms.pdf#page=6|PDF p.6]]
- 光子模块移近package后，FPO/NPO/CPO维修边界不同；CMIS管理之外仍需ELS、fiber routing、冷却和RAS共设计。[[knowledge/sources/src-b681b46ceff2]]

## 最小互换性验证矩阵（本库建议）
至少覆盖卡×slot×FW版本×协议配置×冷却配置；再加错误描述符、掉电/更新中断、reset/链路恢复、租户隔离、兼容降级。报告通过组合与未覆盖组合，而不是只写“开放互通”。

## 关联
[[knowledge/concepts/compute-memory-chiplet-system-contracts|chiplet系统契约]] · [[knowledge/concepts/compute-memory-cxl-failure-domain|CXL故障域]] · [[knowledge/concepts/compute-memory-channel-evidence|高速通道证据]] · [[knowledge/concepts/compute-memory-kv-placement|KV放置]]
