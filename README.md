# Stellarator Library

面向仿星器（stellarator）科研学习与复现的本地优先知识库。原始 PDF 是不可修改的证据层，`wiki/` 是由 LLM 持续维护的综合知识层。

## 使用

1. 用 Obsidian 将本仓库目录作为 vault 打开，从 `wiki/index.md` 开始浏览。
2. PDF 放在 `sources/papers/`；该目录不会被 Git 提交。
3. 添加文献后运行 `python scripts/ingest.py`，检查新来源页、`sources/catalog.md` 和 `wiki/log.md`。
4. 重要论断使用 `[[文献键]]，PDF p. N` 引用；页码指 PDF 阅读器显示的页序号。
5. 每次摄取后更新相关概念页、主题页和索引，再运行 `python scripts/lint_wiki.py`。

## 维护原则

- 不修改原始 PDF，不将 PDF、缓存、凭据或本机绝对路径提交到 Git。
- 区分原文结论、跨文献综合和 LLM 推断；无法可靠抽取的内容标为待核验。
- 新证据与旧结论冲突时并列记录适用条件，不静默覆盖。
- `wiki/log.md` 只追加；索引、来源清单与实际文件始终同步。

完整约定见 [WIKI_SCHEMA.md](WIKI_SCHEMA.md)。

