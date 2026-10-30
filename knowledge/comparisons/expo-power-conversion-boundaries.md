---
id: "expo-power-conversion-boundaries"
type: "comparison"
title: "800V商业评估：先对齐转换边界、可用容量与真实负载"
tags: ["ocp2026", "expo-hall"]
review_status: "synthesized"
---

# 800V商业评估：先对齐转换边界、可用容量与真实负载

## 比较问题
这些演讲并不在销售同一个层级：中压SST、低压AC侧柜、800→50V、50→12V、封装VRM分别改变不同电流路径。把所有“98–99%效率”和“MW机柜”放同一排行榜会误导架构和采购。

## 四种不能省略的口径
1. **能量入口/出口。** Luxshare的35kV→800V整套98.7%与420kW cell峰值99%不是同一物件。[[knowledge/sources/src-743127b50ad8]] [[expo-hall-sessions/Direct-Medium-Voltage-to-800VDC-Conversion-for-AI-Data-Centers-presented-by-Luxshare-Tech.pdf#page=8|PDF p.8]] [[knowledge/sources/src-743127b50ad8]] [[expo-hall-sessions/Direct-Medium-Voltage-to-800VDC-Conversion-for-AI-Data-Centers-presented-by-Luxshare-Tech.pdf#page=9|PDF p.9]] OmniOn的51V→12V DC/DC比230VAC→12V PSU少了前级，图上差距不能当全链路收益。[[knowledge/sources/src-817afa57d410]] [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf#page=8|PDF p.8]] Murata的转换链仍包括800→50→12/6→负载，各级应串联计算。[[knowledge/sources/src-41638c79ca36]] [[expo-hall-sessions/Powering Progress- Murata's Role in Advancing OCP Innovation presented by Murata.pdf#page=3|PDF p.3]]
2. **安装与可用容量。** LITEON安装1.32MW，5+1是1.1MW，N+N是660kW；储能CBU约648kW/5s不能全额覆盖1.1MW。业务容量必须以选择的冗余策略和持续时间计算。[[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=3|PDF p.3]] [[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=5|PDF p.5]] Murata6×5.5kW=33kW只说明安装额定，不是失一模块后的33kW。[[knowledge/sources/src-41638c79ca36]] [[expo-hall-sessions/Powering Progress- Murata's Role in Advancing OCP Innovation presented by Murata.pdf#page=7|PDF p.7]]
3. **功率trace与辅助功。** OmniOn的SiC含风扇而第三方GaN不含，差距量级与33W风扇相当；峰值效率不足以决策。使用同V/T下的P(t)、风扇/泵/控制器功率和冗余模块开关策略。[[knowledge/sources/src-817afa57d410]] [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf#page=6|PDF p.6]] [[knowledge/sources/src-817afa57d410]] [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf#page=9|PDF p.9]]
4. **成熟度与改造范围。** LITEON多部件MP指向2027；Murata33kW released与800V路线图并存；Nidec CDU800V输入仍在评估。更改供电电压需要同步确认冷却基础设施与保护体系，不能只替换IT电源。[[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=4|PDF p.4]] [[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=6|PDF p.6]] [[knowledge/sources/src-41638c79ca36]] [[expo-hall-sessions/Powering Progress- Murata's Role in Advancing OCP Innovation presented by Murata.pdf#page=8|PDF p.8]] [[knowledge/sources/src-e84fa2f73a45]] [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=13|PDF p.13]]

## 统一计算方法（本库归纳）
对每一级按相同时间窗口累积 `E_in = ∫ P_out(t)/η(P_out,T,V) dt + E_aux`；只有当aux尚未计入η时才额外加，避免双计。串联级的输入又是上一级负载，不能把各级最高效率简单相乘来替代实际运行能量。总体效率应取能量比，不是时间平均η。[[knowledge/sources/src-817afa57d410]] [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf#page=9|PDF p.9]]

可部署负载的限制至少包括：故障后可用kW、允许峰值及持续时间、保护选择性、储能时长、母线/连接器热限、冷却降额。MEGMEET的180%EDPP没有持续时间，不能直接换算GPU瞬态功率余量；OmniOn4kW峰值仅3ms也不能当持续额定。[[knowledge/sources/src-7690155542da]] [[expo-hall-sessions/Engineering-the-Transition-to-800-VDC-presented-by-MEGMEET.pdf#page=7|PDF p.7]] [[knowledge/sources/src-817afa57d410]] [[expo-hall-sessions/Driving Efficiency Through Innovation Across the Operating Range and Power Chain, Aligning Power.pdf#page=10|PDF p.10]]

## 商业结论与反证条件
- SST若减少级数/占地，可以改变设施交期；但Luxshare的188m²对9.6m²未统一BBU、通道与冗余边界，不能用它直接做整设施CAPEX节省。[[knowledge/sources/src-743127b50ad8]] [[expo-hall-sessions/Direct-Medium-Voltage-to-800VDC-Conversion-for-AI-Data-Centers-presented-by-Luxshare-Tech.pdf#page=4|PDF p.4]]
- Edged共DC bus减少部分转换/设备，却未删除所有逆变级；公共母线同时需要故障隔离，不能将“少设备”自动视为更高可用率。[[knowledge/sources/src-8247a45d4f9b]] [[expo-hall-sessions/Fungible Power Architectures for the 800V DC Transition presented by Edged Infrastructure.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Fungible Power Architectures for the 800V DC Transition presented by Edged Infrastructure.pdf#page=11|PDF p.11]]
- 推荐把报价归一到**满足故障/动态条件的可用IT kW与年度实际能耗**，再加维护、备件和改造停机。材料没有足够成本/现场故障数据决定赢家。

关联：[[knowledge/concepts/expo-evidence-to-deployment]]。验收需要同一负载trace、整链路计量、冗余切换波形及厂商正式料号/量产承诺；本比较不提供高压实施步骤。

