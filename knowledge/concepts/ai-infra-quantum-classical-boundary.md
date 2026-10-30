---
type: "concept"
title: "量子数据中心与经典基础设施：原型、容错目标和商用边界"
tags: ["ai-infra", "inference-architecture"]
---

# 量子数据中心与经典基础设施：原型、容错目标和商用边界

## 已有证据范围
首版保留Xanadu光子量子材料的关键边界；现已完成全部7份量子来源，跨模态与经典耦合比较见 [[knowledge/comparisons/ai-infra-quantum-integration-regimes]]。以下Xanadu数字仍不泛化到超导、中性原子或其他架构。

## 关键区别
- 12 physical qubits、86billion modes的Aurora原型不是12个稳定logical qubits，也不是完整商业通用容错计算服务。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=6|PDF p.6]]
- quantum core的“No cooling required for computation”不等于整个数据中心无冷却/无低温元件；server/FPGA/detector与同步构成经典配套。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=4|PDF p.4]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=14|PDF p.14]]
- 2029 up to200、2030 up to500、2031 1000+ logical qubits与2029–2030QDC是路线目标；逐页免责声明明确research/prototype结果可能不代表商业表现。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=15|PDF p.15]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=2|PDF p.2]]

## 可迁移到加速器系统的思考
模块化扩展、制造整合、实时反馈、状态同步和系统级容错都要端到端设计；但不能以这些词汇相似就推断量子系统可替代AI推理。

## 下一份证据应回答
逻辑错误率在哪个代码距离/噪声模型/门集上定义？real-time decoder的latency/throughput/功率与控制server比例如何扩展？光损耗表单位是什么？最终utility workload的资源估计、装机功率、可维护性与成本是什么？
