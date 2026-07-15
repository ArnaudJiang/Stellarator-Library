"""Check source/catalog consistency and Obsidian wikilinks."""
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PAPERS = ROOT / "sources" / "papers"


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    errors, warnings = [], []
    pdfs = list(PAPERS.glob("*.pdf"))
    unique = {digest(p) for p in pdfs}
    source_pages = list((WIKI / "sources").glob("*.md"))
    if len(source_pages) != len(unique):
        errors.append(f"source pages={len(source_pages)}, unique PDFs={len(unique)}")

    # Root documentation contains literal wikilink syntax examples, not links.
    all_md = list((ROOT / "sources").glob("*.md")) + list(WIKI.rglob("*.md"))
    by_stem = {p.stem.lower() for p in all_md}
    for page in all_md:
        text = page.read_text(encoding="utf-8")
        for raw in re.findall(r"\[\[([^\]|#]+)", text):
            target = raw.strip().replace("\\", "/")
            if target.startswith("../"):
                resolved = (page.parent / (target + ("" if target.endswith(".md") else ".md"))).resolve()
                if not resolved.exists():
                    errors.append(f"broken link {page.relative_to(ROOT)} -> {raw}")
            elif Path(target).name.lower() not in by_stem:
                errors.append(f"broken link {page.relative_to(ROOT)} -> {raw}")
        if page.parent == WIKI / "sources":
            source = re.search(r'^source_file:\s*"([^"]+)"', text, re.M)
            if not source or not (page.parent / source.group(1)).resolve().exists():
                errors.append(f"missing local PDF link in {page.name}")
            for field in ("type", "title", "title_en", "authors", "year", "citekey", "status", "tags", "related", "sha256", "pages"):
                if not re.search(rf"^{field}:", text, re.M):
                    errors.append(f"missing {field} in {page.name}")
    if len(pdfs) != len(unique):
        warnings.append(f"{len(pdfs) - len(unique)} duplicate PDF copies remain across {len(pdfs)} files")
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARN:", item)
    print(f"Checked {len(all_md)} markdown files, {len(pdfs)} PDFs, {len(unique)} unique sources")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
