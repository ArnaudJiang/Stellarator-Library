"""Index local stellarator PDFs and generate reproducible source stubs.

The script never modifies PDFs. It uses PDF metadata and extracted first/last pages;
uncertain fields remain explicitly unverified.
"""
from __future__ import annotations

import hashlib
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "sources" / "papers"
WIKI_SOURCES = ROOT / "wiki" / "sources"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def clean(value: object) -> str:
    text = unicodedata.normalize("NFKC", str(value or ""))
    return re.sub(r"\s+", " ", text).strip().strip("-_ ")


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "/").replace('"', "\\\"") + '"'


def title_from_filename(path: Path) -> str:
    title = clean(path.stem.replace("_", " "))
    title = re.sub(r"\s*\(z-library.*$", "", title, flags=re.I)
    return title


def guess_year(text: str, filename: str) -> str:
    hits = re.findall(r"\b(?:19|20)\d{2}\b", filename + " " + text[:5000])
    plausible = [x for x in hits if 1900 <= int(x) <= date.today().year]
    return plausible[0] if plausible else "unknown"


def guess_author(metadata: dict, first_text: str) -> str:
    author = clean(metadata.get("/Author", ""))
    if author and author.lower() not in {"unknown", "anonymous"}:
        return author
    lines = [clean(x) for x in first_text.splitlines()[:30] if clean(x)]
    for line in lines[1:]:
        if len(line) < 160 and re.search(r"[A-Za-z]{2,}\s+[A-Za-z]{2,}", line):
            if not re.search(r"abstract|university|institute|journal|doi|arxiv", line, re.I):
                return line
    return "unknown"


def first_author(author: str) -> str:
    if author == "unknown":
        return "unknown"
    part = re.split(r"[,;]|\band\b|&", author, maxsplit=1, flags=re.I)[0]
    words = re.findall(r"[A-Za-z\u4e00-\u9fff]+", part)
    return (words[-1] if words else "unknown").lower()


def slug(text: str, limit: int = 42) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9]+", ascii_text.lower())
    stop = {"a", "an", "the", "of", "for", "and", "with", "to", "in", "on"}
    words = [w for w in words if w not in stop][:7]
    return "-".join(words)[:limit].strip("-") or "source"


def classify(title: str, text: str) -> tuple[list[str], str]:
    hay = (title + " " + text[:10000]).lower()
    rules = [
        ("coil-design", r"coil|线圈", "topics/coil-design"),
        ("optimization", r"optimi[sz]|优化", "topics/optimization"),
        ("equilibrium", r"equilibrium|mhd|平衡", "topics/equilibrium"),
        ("transport", r"transport|confinement|alpha-particle|输运|约束", "topics/transport-and-confinement"),
        ("quasi-symmetry", r"quasi.?sym|quasi.?helical|quasi.?axisym|准对称", "concepts/quasisymmetry"),
        ("quasi-isodynamic", r"quasi.?isodynamic|qi-like|准等动力", "concepts/quasi-isodynamicity"),
        ("engineering", r"manufactur|engineering|strain|finite-build|tolerance|工程|制造", "topics/engineering-and-manufacturing"),
        ("stability", r"stability|稳定", "topics/stability"),
    ]
    tags, related = [], []
    for tag, pattern, page in rules:
        if re.search(pattern, hay):
            tags.append(tag)
            related.append(page)
    if not tags:
        tags = ["stellarator"]
        related = ["concepts/stellarator"]
    return tags, related[0]


def extract_section(text: str) -> str:
    compact = re.sub(r"\s+", " ", text)
    match = re.search(r"\babstract\b\s*[:—-]?\s*(.{250,2200}?)(?=\b(?:keywords|pacs|introduction|1\.?\s+introduction)\b)", compact, re.I)
    if match:
        return match.group(1).strip()
    return compact[:1200].strip()


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(yaml_quote(v) for v in values) + "]"


def main() -> None:
    WIKI_SOURCES.mkdir(parents=True, exist_ok=True)
    files = sorted(PAPERS.glob("*.pdf"), key=lambda p: p.name.lower())
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        groups[sha256(path)].append(path)

    used: set[str] = set()
    rows = []
    duplicates = []
    failures = []
    for digest, paths in sorted(groups.items(), key=lambda item: item[1][0].name.lower()):
        path = paths[0]
        try:
            reader = PdfReader(str(path))
            pages = len(reader.pages)
            sample_indices = sorted(set([0, 1 if pages > 1 else 0, pages - 1]))
            texts = []
            for i in sample_indices:
                try:
                    texts.append(reader.pages[i].extract_text() or "")
                except Exception:
                    texts.append("")
            first_text = "\n".join(texts[:2])
            sample_text = "\n".join(texts)
            metadata = dict(reader.metadata or {})
        except Exception as exc:
            pages, first_text, sample_text, metadata = 0, "", "", {}
            failures.append(f"{path.name}: {exc}")

        file_title = title_from_filename(path)
        meta_title = clean(metadata.get("/Title", ""))
        title = meta_title if len(meta_title) > 8 and meta_title.lower() not in {"untitled", "unknown"} else file_title
        author = guess_author(metadata, first_text)
        year = guess_year(first_text, path.name)
        base = f"{first_author(author)}-{year}-{slug(title)}"
        citekey = base
        n = 2
        while citekey in used:
            citekey = f"{base}-{n}"
            n += 1
        used.add(citekey)
        tags, related = classify(title, sample_text)
        abstract = extract_section(first_text)
        if not abstract:
            abstract = "文本自动抽取为空，可能是扫描件或受字体编码影响；需渲染页面后人工核验。"

        aliases = [p.name for p in paths]
        rel_source = "../../sources/papers/" + path.name
        body = f'''---
type: source
title: {yaml_quote(title)}
title_en: {yaml_quote(title)}
authors: {yaml_list([author])}
year: {year}
citekey: {yaml_quote(citekey)}
status: extracted
tags: {yaml_list(tags)}
related: {yaml_list([related])}
source_file: {yaml_quote(rel_source)}
sha256: {yaml_quote(digest)}
pages: {pages}
---

# {title}

> [打开本地 PDF]({rel_source}) · 关联主题：[[{related}]]

## 结构化摘要

以下内容由 PDF 首页文本自动提取，用于初步检索；尚未替代逐页精读：

{abstract}

## 原文结论

- 首页所述研究目标与摘要见 [[{citekey}]]，PDF p. 1。
- 关键定量结论、公式及图表尚需逐页视觉复核。

## 方法与数据

- 待从方法章节补充研究对象、数值工具、目标函数、约束条件和数据规模。

## 局限与适用范围

- 当前页面为全量摄取生成的初步条目；自动抽取可能受双栏排版、公式和字体编码影响。

## 复现线索

- 检查原文中的代码仓库、输入文件、平衡/线圈数据、软件版本及优化参数。

## 跨文献综合

- 通过 [[{related}]] 与同主题来源进行比较；尚未形成的比较不得视为原文结论。

## LLM 推断

- 暂无。后续推断必须明确标注依据和不确定性。

## 待核验

- [ ] 核验作者、年份和正式出版信息。
- [ ] 渲染并检查关键公式、图表与结论页。
- [ ] 将关键论断补充为页码级引用。
'''
        (WIKI_SOURCES / f"{citekey}.md").write_text(body, encoding="utf-8")
        rows.append((citekey, title, author, year, pages, path.name, tags[0]))
        if len(paths) > 1:
            duplicates.append((digest, aliases))

    catalog = [
        "# 来源目录", "", f"- 本地 PDF：{len(files)}", f"- 唯一内容：{len(groups)}",
        f"- 重复组：{len(duplicates)}", "", "| 文献键 | 标题 | 作者 | 年份 | 页数 | 分类 |",
        "|---|---|---|---:|---:|---|",
    ]
    for key, title, author, year, pages, _, tag in rows:
        catalog.append(f"| [[{key}]] | {title.replace('|', '/')} | {author.replace('|', '/')} | {year} | {pages} | {tag} |")
    (ROOT / "sources" / "catalog.md").write_text("\n".join(catalog) + "\n", encoding="utf-8")

    dup = ["# 重复文件映射", "", "相同 SHA-256 的原文只生成一个来源页；所有本地副本仍保留。", ""]
    for digest, names in duplicates:
        dup += [f"## `{digest}`", ""] + [f"- `{name}`" for name in names] + [""]
    (ROOT / "sources" / "duplicates.md").write_text("\n".join(dup), encoding="utf-8")

    report = ["# 摄取报告", "", f"- 文件：{len(files)}", f"- 唯一来源：{len(groups)}", f"- 失败：{len(failures)}", ""]
    report += [f"- {x}" for x in failures]
    (ROOT / "sources" / "ingest-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Indexed {len(files)} PDFs into {len(groups)} unique source pages; failures={len(failures)}")


if __name__ == "__main__":
    main()

