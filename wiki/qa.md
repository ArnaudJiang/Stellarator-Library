---
type: qa
title: "质量核验"
title_en: "Quality assurance"
status: current
tags: ["maintenance"]
related: ["index"]
---

# 质量核验

## 初始摄取

- PDF 解析失败：0。
- 来源页数量与 SHA-256 唯一内容数量一致。
- 所有来源页均包含必需 YAML 字段、本地相对链接和至少一个主题入口。
- Obsidian wikilink 检查无断链。

## 视觉抽检

已渲染并检查以下类型的 PDF 首页：

- 基础教材：*An Introduction to Stellarators*。
- 理论/构型：*A quasi-isodynamic stellarator configuration towards a fusion power plant*。
- 实验：*Demonstration of reduced neoclassical energy transport in Wendelstein 7-X*。
- 软件：*SIMSOPT: A flexible framework for stellarator optimization*。
- 工程优化：*Optimization of finite-build stellarator coils*。

抽检页面标题、作者、摘要和版面可读。双栏正文、公式、图表与非标准字体仍须按具体论断逐页核验，不能仅依赖文本抽取。

## 已知事项

- 当前原文目录仍含一组 SHA-256 完全相同的 QI 论文副本；知识层只生成一个来源页，文件名映射见 [[../sources/duplicates|重复文件映射]]。
- 自动抽取元数据质量受原始 PDF 影响，异常作者或年份保留待核验状态，不作为确定性书目信息。

