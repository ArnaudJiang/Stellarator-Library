---
type: source
title: "ConStellaration: A dataset of QI-like stellarator plasma boundaries and optimization benchmarks"
title_en: "ConStellaration: A dataset of QI-like stellarator plasma boundaries and optimization benchmarks"
authors: ["Santiago A. Cadena"]
year: 2025
citekey: "cadena-2025-constellaration-dataset-qi-like-stellarato"
status: extracted
tags: ["coil-design", "optimization", "equilibrium", "transport", "quasi-isodynamic", "engineering"]
related: ["topics/coil-design"]
source_file: "../../sources/papers/ConStellaration- A dataset of QI-like stellaratorplasma boundaries and optimization benchmarks.pdf"
sha256: "d6499ede73862c1a97e0214f10d5bdb11357b24983c988417da72559d908c530"
pages: 27
---

# ConStellaration: A dataset of QI-like stellarator plasma boundaries and optimization benchmarks

> [打开本地 PDF](../../sources/papers/ConStellaration- A dataset of QI-like stellaratorplasma boundaries and optimization benchmarks.pdf) · 关联主题：[[topics/coil-design]]

## 结构化摘要

以下内容由 PDF 首页文本自动提取，用于初步检索；尚未替代逐页精读：

Stellarators are magnetic confinement devices under active development to deliver steady-state carbon-free fusion energy. Their design involves a high-dimensional, constrained optimization problem that requires expensive physics simulations and significant domain expertise. Recent advances in plasma physics and open-source tools have made stellarator optimization more accessible. However, broader com- munity progress is currently bottlenecked by the lack of standardized optimization problems with strong baselines and datasets that enable data-driven approaches, particularly for quasi-isodynamic (QI) stellarator configurations, considered as a promising path to commercial fusion due to their inherent resilience to current- driven disruptions. Here, we release an open dataset of diverse QI-like stellarator plasma boundary shapes, paired with their ideal magnetohydrodynamic (MHD) equilibria and performance metrics. We generated this dataset by sampling a variety of QI fields and optimizing corresponding stellarator plasma boundaries. Weintroducethreeoptimizationbenchmarksofincreasingcomplexity: (1)asingle- objective geometric optimization problem, (2) a “simple-to-build" QI stellarator, and(3)amulti-objectiveideal-MHDstableQIstellaratorthatinvestigatestrade-offs between compactness and coil simplicity. For every benchmark, we provide refer- ence code, evaluation scripts, and strong baselines based on classical optimization techniques. Finally, we show how learned models trained on our dataset can effi- ciently generate novel, feasible configurations without querying expensive physics oracles. Byopenlyreleasingthedataset( https://huggingface.co/datasets/ proxima-fusion/constellaration)alongwithbenchmarkproblemsandbase- lines (https://github.com/proximafusion/constellaration), we aim to lower the entry barrier for optimization and machine learning researchers to engage in stellarator design and to accelerate cross-disciplinary progress toward bringing fusion energy to the grid.

## 原文结论

- 首页所述研究目标与摘要见 [[cadena-2025-constellaration-dataset-qi-like-stellarato]]，PDF p. 1。
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
