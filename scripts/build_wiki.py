"""Build the stable navigation and synthesis layer for the Stellarator wiki."""
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def write(rel: str, text: str) -> None:
    path = WIKI / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def page(kind: str, title: str, title_en: str, tags: list[str], body: str) -> str:
    taglist = ", ".join(f'"{x}"' for x in tags)
    return f'''---
type: {kind}
title: "{title}"
title_en: "{title_en}"
status: evolving
tags: [{taglist}]
related: []
---

# {title}

{body}
'''


def main() -> None:
    concepts = {
        "stellarator": ("仿星器", "Stellarator", "仿星器以外部三维线圈产生旋转变换，可在无大等离子体电流的条件下维持环形约束。研究主线连接 [[magnetic-coordinates|磁坐标]]、[[mhd-equilibrium|MHD 平衡]]、[[quasisymmetry|准对称]]、[[omnigenity|全能性]] 与 [[neoclassical-transport|新古典输运]]。\n\n## 学习要点\n\n- 区分磁面几何、磁场强度谱与线圈可制造性。\n- 物理优化与工程优化需要通过 [[../topics/combined-optimization|联合优化]] 协同。"),
        "magnetic-coordinates": ("磁坐标", "Magnetic coordinates", "磁坐标用磁通面标签和沿面角坐标描述三维磁场，是平衡、对称性和输运理论的共同语言。\n\n## 关联\n\n- [[mhd-equilibrium|MHD 平衡]]\n- [[quasisymmetry|准对称]]\n- [[omnigenity|全能性]]"),
        "mhd-equilibrium": ("磁流体平衡", "MHD equilibrium", "理想 MHD 平衡满足力平衡，并为稳定性、输运和线圈反演提供基础状态。固定边界与自由边界问题应分别记录。\n\n## 方法入口\n\n- [[../methods/vmec|VMEC]]\n- [[../methods/desc|DESC]]\n- [[../methods/spec|SPEC]]"),
        "quasisymmetry": ("准对称", "Quasisymmetry", "准对称（quasisymmetry）要求磁场强度在适当磁坐标中呈现隐藏连续对称性。常见类别为准轴对称 QA 与准螺旋对称 QH/QHS。\n\n## 注意\n\n准对称质量、粒子约束与线圈复杂度相关但不等价，比较时必须说明指标与平衡条件。"),
        "quasi-isodynamicity": ("准等动力学", "Quasi-isodynamicity", "准等动力学（quasi-isodynamicity, QI）是全能磁场的重要类别，W7-X 是代表性优化路线。\n\n## 关联\n\n- [[omnigenity|全能性]]\n- [[../configurations/w7-x|W7-X]]\n- [[../topics/transport-and-confinement|输运与约束]]"),
        "omnigenity": ("全能性", "Omnigenity", "全能性（omnigenity）要求受困粒子的径向漂移在反弹平均意义下消失。它提供比精确准对称更广的低新古典输运设计空间。"),
        "neoclassical-transport": ("新古典输运", "Neoclassical transport", "三维磁场中的新古典输运对磁场谱、碰撞率和径向电场敏感。实验或数值结论必须注明工况，不能仅凭构型标签外推。"),
    }
    for slug, (zh, en, body) in concepts.items():
        write(f"concepts/{slug}.md", page("concept", zh, en, ["stellarator", "concept"], body))

    methods = {
        "vmec": ("VMEC", "以嵌套磁通面假设求解三维理想 MHD 平衡；使用时需记录固定/自由边界、分辨率和收敛状态。"),
        "desc": ("DESC", "采用谱表示与可微计算处理平衡和优化；复现时记录目标、约束、分辨率、初值及软件版本。"),
        "spec": ("SPEC", "以多区域松弛 MHD 描述允许不连续和磁岛的平衡；应记录区域划分与界面条件。"),
        "simsopt": ("SIMSOPT", "面向仿星器优化的 Python 框架，可组合平衡、粒子约束与线圈目标；应保存输入、随机种子与提交版本。"),
        "focus": ("FOCUS", "使用磁场误差与几何/工程约束优化线圈；比较结果时需统一线圈表示、距离和曲率定义。"),
        "stellopt": ("STELLOPT", "多目标仿星器优化工具链；复现重点是目标权重、约束、平衡设置和优化器参数。"),
    }
    for slug, (name, body) in methods.items():
        write(f"methods/{slug}.md", page("method", name, name, ["stellarator", "software"], f"{body}\n\n## 复现清单\n\n- 输入与边界表示\n- 软件版本和依赖\n- 目标函数、权重与约束\n- 收敛判据和输出数据\n\n相关主题：[[../topics/equilibrium|平衡]]、[[../topics/optimization|优化]]。"))

    configs = {
        "w7-x": ("W7-X", "准等动力学优化的大型实验装置，是验证低新古典输运、磁场拓扑和高性能运行的重要平台。"),
        "w7-as": ("W7-AS", "先进仿星器实验装置，为后续优化仿星器的实验与运行经验提供历史基础。"),
        "ncsx": ("NCSX", "准轴对称紧凑仿星器设计，文献库中包含其物理优化与模块线圈设计。"),
        "qhs": ("QHS", "准螺旋对称构型族；评估需联合考虑对称误差、粒子约束与线圈复杂度。"),
        "qi": ("QI", "准等动力学构型族；与 [[w7-x|W7-X]]、[[ciemat-qi4x|CIEMAT-QI4X]] 和 [[stellaris|Stellaris]] 等路线关联。"),
        "qa": ("QA", "准轴对称构型族，在保持类似轴对称粒子动力学特征的同时使用三维外部线圈。"),
        "stellaris": ("Stellaris", "面向原型聚变电站的高场准等动力学设计概念；工程可行性需与物理指标共同核验。"),
        "ciemat-qi4x": ("CIEMAT-QI4X", "反应堆相关的准等动力学构型概念，并考虑与岛式偏滤器的兼容性。"),
    }
    for slug, (name, body) in configs.items():
        write(f"configurations/{slug}.md", page("configuration", name, name, ["stellarator", "configuration"], f"{body}\n\n## 比较维度\n\n- 对称性或全能性指标\n- 平衡、稳定性与粒子约束\n- 线圈距离、曲率和制造约束\n- 运行或反应堆工况\n\n本页为综合入口；定量结论须回链来源页并标注 PDF 页码。"))

    topics = {
        "equilibrium": ("平衡", "固定边界、自由边界与多区域松弛 MHD 平衡构成后续优化和分析的基础。", ["../concepts/mhd-equilibrium", "../methods/vmec", "../methods/desc", "../methods/spec"]),
        "transport-and-confinement": ("输运与约束", "汇集新古典输运、碰撞less 高能粒子约束和实验性能证据。", ["../concepts/neoclassical-transport", "../concepts/omnigenity", "../configurations/w7-x"]),
        "stability": ("稳定性", "记录理想 MHD、自由边界和构型相关稳定性结论，并明确平衡与边界条件。", ["equilibrium"]),
        "coil-design": ("线圈设计", "连接等离子体边界、磁场误差、线圈表示、曲率、间距和可制造性。", ["optimization", "engineering-and-manufacturing", "../methods/focus", "../methods/simsopt"]),
        "optimization": ("优化", "记录目标函数、权重、约束、优化器和局部/全局策略，避免脱离定义比较单一最优值。", ["combined-optimization", "coil-design"]),
        "engineering-and-manufacturing": ("工程与制造", "覆盖有限截面线圈、曲率、应变、容差、维护空间和 HTS 兼容性。", ["coil-design", "manufacturing-errors", "hts"]),
        "manufacturing-errors": ("制造误差", "研究制造与装配误差传播、随机优化、事后校正和鲁棒性指标。", ["engineering-and-manufacturing"]),
        "hts": ("高温超导线圈", "关注 ReBCO 等高温超导材料的应变、绕制角和非绝缘线圈约束。", ["engineering-and-manufacturing"]),
        "combined-optimization": ("联合优化", "将等离子体与线圈目标置于同一或交替优化流程，减少先优化等离子体后发现线圈不可实现的风险。", ["optimization", "coil-design", "equilibrium"]),
    }
    for slug, (zh, intro, links) in topics.items():
        linked = "\n".join(f"- [[{x}]]" for x in links)
        write(f"topics/{slug}.md", page("topic", zh, slug.replace("-", " ").title(), ["stellarator", "topic"], f"{intro}\n\n## 关联入口\n\n{linked}\n\n## 证据规则\n\n本页的定量比较必须链接来源页并给出 PDF 页码；未完成核验的自动摘要不作为最终证据。"))

    write("comparisons/methods.md", page("comparison", "平衡与优化方法比较", "Equilibrium and optimization methods", ["comparison"], "| 方法 | 主要用途 | 关键假设/记录项 |\n|---|---|---|\n| [[../methods/vmec|VMEC]] | 嵌套磁面理想 MHD 平衡 | 边界模式、分辨率、收敛 |\n| [[../methods/desc|DESC]] | 谱平衡与可微优化 | 目标、约束、分辨率、版本 |\n| [[../methods/spec|SPEC]] | 多区域松弛 MHD | 区域与界面条件 |\n| [[../methods/simsopt|SIMSOPT]] | 多物理目标和线圈优化 | 模型组合、版本、随机种子 |\n| [[../methods/focus|FOCUS]] | 线圈优化 | 场误差和几何约束定义 |"))
    write("comparisons/configurations.md", page("comparison", "构型路线比较", "Configuration families", ["comparison"], "| 路线 | 核心性质 | 代表入口 |\n|---|---|---|\n| QA | 准轴对称 | [[../configurations/qa|QA]]、[[../configurations/ncsx|NCSX]] |\n| QH/QHS | 准螺旋对称 | [[../configurations/qhs|QHS]] |\n| QI | 准等动力学 | [[../configurations/qi|QI]]、[[../configurations/w7-x|W7-X]] |\n\n本表仅作导航；性能排序必须在统一工况和指标下引用具体来源。"))

    source_pages = sorted((WIKI / "sources").glob("*.md"))
    source_links = "\n".join(f"- [[sources/{p.stem}]]" for p in source_pages)
    write("index.md", page("index", "Stellarator Knowledge Base", "Stellarator Knowledge Base", ["index"], f"## 学习路径\n\n1. [[concepts/stellarator|仿星器]] 与 [[concepts/magnetic-coordinates|磁坐标]]\n2. [[concepts/mhd-equilibrium|MHD 平衡]] 与 [[topics/equilibrium|平衡方法]]\n3. [[concepts/quasisymmetry|准对称]]、[[concepts/omnigenity|全能性]]、[[concepts/quasi-isodynamicity|准等动力学]]\n4. [[topics/transport-and-confinement|输运与约束]] 与 [[topics/stability|稳定性]]\n5. [[topics/optimization|优化]]、[[topics/coil-design|线圈设计]]、[[topics/engineering-and-manufacturing|工程与制造]]\n\n## 导航\n\n- [[../sources/catalog|来源目录]]\n- [[comparisons/methods|方法比较]]\n- [[comparisons/configurations|构型比较]]\n- [[open-questions|开放问题]]\n- [[log|维护日志]]\n\n## 全部来源（{len(source_pages)}）\n\n{source_links}"))
    write("open-questions.md", page("tracker", "开放问题", "Open questions", ["research-gap"], "- [ ] 在统一边界、场强与尺寸条件下，准对称误差如何映射到粒子约束？\n- [ ] QI 构型的线圈复杂度与新古典输运优势之间是否存在稳健的 Pareto 前沿？\n- [ ] 有限截面、制造误差与 HTS 应变约束应在优化流程的哪个阶段进入？\n- [ ] 不同代码对同一平衡和线圈目标的定义、归一化及收敛标准能否建立可复现实验？\n- [ ] 当前来源页中元数据异常与扫描件应优先完成视觉核验。"))
    write("log.md", f"# 维护日志\n\n## [{date.today().isoformat()}] ingest | 初始全量摄取\n\n- 建立中文为主、中英术语并行的 Obsidian Wiki。\n- 根据 SHA-256 为本地 PDF 建立唯一来源页并生成来源目录。\n- 建立概念、方法、构型、专题与比较入口。\n- 自动抽取页面统一标记为 `extracted`；公式、图表与关键定量结论等待视觉复核。\n")


if __name__ == "__main__":
    main()

