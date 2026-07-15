---
type: source
title: "FOCUS-HTS: a new stellarator coil design code for three-dimensional high-temperature superconducting magnets"
title_en: "FOCUS-HTS: a new stellarator coil design code for three-dimensional high-temperature superconducting magnets"
authors: ["Xianyi Nie,Jianlin Peng,Yidong Xie,Guodong Yu,Ke Liu,Caoxiang Zhu"]
year: 2025
citekey: "nie-2025-focus-hts-new-stellarator-coil-design-code"
status: extracted
tags: ["coil-design", "optimization", "transport", "quasi-symmetry", "engineering"]
related: ["topics/coil-design"]
source_file: "../../sources/papers/FOCUS-HTS a new stellarator coil design code for three-dimensional high-temperature superconducting magnets.pdf"
sha256: "8297262aceff0a97f93b07b60e3127961ca1e37db3be77ada0522bb65f35505a"
pages: 15
---

# FOCUS-HTS: a new stellarator coil design code for three-dimensional high-temperature superconducting magnets

> [打开本地 PDF](../../sources/papers/FOCUS-HTS a new stellarator coil design code for three-dimensional high-temperature superconducting magnets.pdf) · 关联主题：[[topics/coil-design]]

## 结构化摘要

以下内容由 PDF 首页文本自动提取，用于初步检索；尚未替代逐页精读：

Stellarators mainly utilize magnetic fields from external coils to confine the plasma, enabling steady-state operation while avoiding instabilities like disruptions raised from plasma currents. Similar to tokamaks, the fusion power of stellarators is proportional to R3B4. High-temperature superconducting (HTS) coils can withstand high currents and thus offer significant advantages in enhancing fusion power or reducing the machine size. However, HTS materials, particularly Rare Earth-Barium-Copper Oxide, present unique electromagnetic and mechanical properties that pose new challenges for designing stellarator coils. To address these challenges, we developed a new code, FOCUS-HTS, built on its predecessor, FOCUS. FOCUS-HTS can model coils as either filaments or finite-build shapes using the Fourier representation or cubic B-splines. In addition to standard physics and engineering targets, FOCUS-HTS can optimize tape strains, electromagnetic (EM) forces, and critical current densities. Developed in Python with automatic differentiation, the code allows easy interfacing and GPU acceleration. For demonstrations, FOCUS-HTS has been used to reduce the EM force of the W7-X coils and design HTS coils for a precisely quasi-axisymmetric stellarator.

## 原文结论

- 首页所述研究目标与摘要见 [[nie-2025-focus-hts-new-stellarator-coil-design-code]]，PDF p. 1。
- 关键定量结论、公式及图表尚需逐页视觉复核。

## 方法与数据

- 待从方法章节补充研究对象、数值工具、目标函数、约束条件和数据规模。

## 局限与适用范围

- 当前页面为全量摄取生成的初步条目；自动抽取可能受双栏排版、公式和字体编码影响。

## 复现线索

- 检查原文中的代码仓库、输入文件、平衡/线圈数据、软件版本及优化参数。

## 跨文献综合

- 通过 [[topics/coil-design]] 与同主题来源进行比较；尚未形成的比较不得视为原文结论。

## LLM 推断

- 暂无。后续推断必须明确标注依据和不确定性。

## 待核验

- [ ] 核验作者、年份和正式出版信息。
- [ ] 渲染并检查关键公式、图表与结论页。
- [ ] 将关键论断补充为页码级引用。
