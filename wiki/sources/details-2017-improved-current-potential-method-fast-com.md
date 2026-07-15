---
type: source
title: "An improved current potential method for fast computation of stellarator coil shapes"
title_en: "An improved current potential method for fast computation of stellarator coil shapes"
authors: ["Download details:"]
year: 2017
citekey: "details-2017-improved-current-potential-method-fast-com"
status: extracted
tags: ["coil-design", "optimization", "equilibrium", "transport", "engineering", "stability"]
related: ["topics/coil-design"]
source_file: "../../sources/papers/An improved current potential method for fast computation of stellarator coil shapes.pdf"
sha256: "a4fca244ca77002913418c6b6209f42fec27a8a4ad676398be98be5da30d468f"
pages: 16
---

# An improved current potential method for fast computation of stellarator coil shapes

> [打开本地 PDF](../../sources/papers/An improved current potential method for fast computation of stellarator coil shapes.pdf) · 关联主题：[[topics/coil-design]]

## 结构化摘要

以下内容由 PDF 首页文本自动提取，用于初步检索；尚未替代逐页精读：

Several fast methods for computing stellarator coil shapes are compared, including the classical NESCOIL procedure (Merkel 1987 Nucl. Fusion 27 867), its generalization using truncated singular value decomposition, and a Tikhonov regularization approach we call REGCOIL in which the squared current density is included in the objective function. Considering W7-X and NCSX geometries, and for any desired level of regularization, we find the REGCOIL approach simultaneously achieves lower surface-averaged and maximum values of both current density (on the coil winding surface) and normal magnetic field (on the desired plasma surface). This approach therefore can simultaneously improve the free-boundary reconstruction of the target plasma shape while substantially increasing the minimum distances between coils, preventing collisions between coils while improving access for ports and maintenance. The REGCOIL method also allows finer control over the level of regularization, it preserves convexity to ensure the local optimum found is the global optimum, and it eliminates two pathologies of NESCOIL: the resulting coil shapes become independent of the arbitrary choice of angles used to parameterize the coil surface, and the resulting coil shapes converge rather than diverge as Fourier resolution is increased. We therefore contend that REGCOIL should be used instead of NESCOIL for applications in which a fast and robust method for coil calculation is needed, such as when targeting coil complexity in fixed- boundary plasma optimization, or for scoping new stellarator geometries.

## 原文结论

- 首页所述研究目标与摘要见 [[details-2017-improved-current-potential-method-fast-com]]，PDF p. 1。
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
