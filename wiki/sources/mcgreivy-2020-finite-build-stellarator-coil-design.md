---
type: source
title: "Finite build stellarator coil design"
title_en: "Finite build stellarator coil design"
authors: ["Nick McGreivy, Stuart Hudson. Caoxiang Zhu"]
year: 2020
citekey: "mcgreivy-2020-finite-build-stellarator-coil-design"
status: extracted
tags: ["coil-design", "optimization", "engineering"]
related: ["topics/coil-design"]
source_file: "../../sources/papers/OPTIMIZED FINITE-BUILD STELLARATOR COILS USING.pdf"
sha256: "c1f3ef42acc705cb8e29d6dfbde9f0d727110967ee5dac80c6b241bb550df7b0"
pages: 16
---

# Finite build stellarator coil design

> [打开本地 PDF](../../sources/papers/OPTIMIZED FINITE-BUILD STELLARATOR COILS USING.pdf) · 关联主题：[[topics/coil-design]]

## 结构化摘要

以下内容由 PDF 首页文本自动提取，用于初步检索；尚未替代逐页精读：

A new stellarator coil design code is introduced that optimizes the position and winding pack orienta- tion of ﬁnite-build coils. The new code, called FOCUSADD, performs gradient-based optimization in a high-dimensional, non-convex space. The derivatives with respect to parameters of ﬁnite-build coils are easily and efﬁciently computed using automatic differentiation. FOCUSADD parametrizes coil positions in free space using a Fourier series and uses a multi-ﬁlament approximation to the coil winding pack. The orientation of the winding pack is parametrized with a Fourier series and can be optimized as well. Optimized ﬁnite-build coils for a W7-X-like stellarator are found, and compared with ﬁlamentary coil results. The ﬁnal positions of optimized ﬁnite-build W7-X-like coils are shifted, on average, by approximately 2.5mm relative to optimized ﬁlamentary coils. These results suggest that ﬁnite-build effects should be accounted for in the optimization of stellarators with low coil tolerances.

## 原文结论

- 首页所述研究目标与摘要见 [[mcgreivy-2020-finite-build-stellarator-coil-design]]，PDF p. 1。
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
