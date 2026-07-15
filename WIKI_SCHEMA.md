# Wiki 维护规范

## 三层结构

- `sources/papers/`：不可修改的本地原文，不进入 Git。
- `wiki/`：可演化的 Markdown 知识层，由 Git 管理。
- 本文件与 `AGENTS.md`：维护知识库的行为规范。

## 来源页元数据

来源页必须包含：`type`、`title`、`title_en`、`authors`、`year`、`citekey`、`status`、`tags`、`related`、`source_file`、`sha256` 和 `pages`。未知值写 `unknown`，不得猜测。

`status` 使用：`indexed`（已登记）、`extracted`（已提取并形成初步摘要）、`verified`（人工或视觉复核关键证据）。

## 引用与证据

- 文献键格式：`第一作者-年份-短标题`，全库唯一且生成后保持稳定。
- 页码引用：`[[文献键]]，PDF p. N`。
- 直接来自摘要或正文的内容写入“原文结论”；跨来源归纳写入“跨文献综合”；分析性外推写入“LLM 推断”。
- 公式、表格、图片、双栏错序或乱码内容必须查看 PDF 渲染页后才能标为 `verified`。

## 摄取事务

每次摄取都要同步完成：来源页、来源目录、相关概念或主题页、总索引、日志和 lint。重复文件按 SHA-256 只生成一个来源页，但全部文件名记录在去重清单中。

