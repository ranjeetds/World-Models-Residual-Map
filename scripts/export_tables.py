#!/usr/bin/env python3
"""Generate the single-file human README and paper-ready LaTeX table."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TABLES = ROOT / "generated" / "tables"
VERSION = "0.2.0"
RELEASE_DATE = "2026-08-11"
REPO_URL = "https://github.com/ranjeetds/World-Models-Residual-Map"
PAPER_TITLE = "From Pattern Completion to Counterfactual Simulation: A Survey of World Models as the Residual Frontier of Foundation AI"

FRIENDLY_RESIDUALS = {
    "action_semantics": "Action Semantics",
    "state_persistence": "State Persistence",
    "physical_law_extrapolation": "Physical Law Extrapolation",
    "counterfactual_reasoning": "Counterfactual Reasoning",
    "uncertainty_calibration": "Uncertainty Calibration",
    "planning_utility": "Planning Utility",
    "sim_to_real_transfer": "Sim-to-Real Transfer",
    "spatial_consistency": "Spatial Consistency",
    "social_physical_coupling": "Social-Physical Coupling",
    "governance_readiness": "Governance Readiness",
}

SHORT_RESIDUALS = {
    "action_semantics": "action",
    "state_persistence": "state",
    "physical_law_extrapolation": "physics",
    "counterfactual_reasoning": "counterfactual",
    "uncertainty_calibration": "uncertainty",
    "planning_utility": "planning",
    "sim_to_real_transfer": "sim2real",
    "spatial_consistency": "spatial",
    "social_physical_coupling": "social-physical",
    "governance_readiness": "governance",
}


def load(name: str) -> list[dict[str, Any]]:
    with (DATA / name).open("r", encoding="utf-8") as f:
        return json.load(f)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def md_link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else "not recorded"


def first_url(urls: dict[str, str], labels: list[str]) -> str:
    for label in labels:
        if label in urls:
            return urls[label]
    return ""


def yes(value: Any) -> str:
    if value is True:
        return "yes"
    if value is False:
        return "no"
    return str(value)


def titleize_id(text: str) -> str:
    acronyms = {
        "ai": "AI",
        "mbrl": "MBRL",
        "rl": "RL",
        "jepa": "JEPA",
        "3d": "3D",
        "4d": "4D",
        "td": "TD",
        "mpc": "MPC",
        "eqa": "EQA",
        "qa": "QA",
        "iq": "IQ",
    }
    parts = re.split(r"([ _-]+)", text)
    rendered: list[str] = []
    for part in parts:
        if re.fullmatch(r"[ _-]+", part):
            rendered.append(" ")
        else:
            rendered.append(acronyms.get(part.lower(), part.capitalize()))
    return "".join(rendered).strip()


def escape_table(text: Any) -> str:
    return str(text).replace("|", "/").replace("\n", " ")


def pretty_text(text: Any) -> str:
    value = str(text)
    replacements = {
        r"\b2d\b": "2D",
        r"\b3d\b": "3D",
        r"\b4d\b": "4D",
        r"\blidar\b": "LiDAR",
        r"\bnuScenes\b": "nuScenes",
        r"\bdmcontrol\b": "DMControl",
        r"\bmetaworld\b": "MetaWorld",
        r"\bmaniskill2\b": "ManiSkill2",
        r"\bmyosuite\b": "MyoSuite",
        r"\batari\b": "Atari",
        r"\bminecraft\b": "Minecraft",
        r"\bdoom\b": "DOOM",
        r"\bgaussian splats\b": "Gaussian splats",
    }
    for pattern, repl in replacements.items():
        value = re.sub(pattern, repl, value)
    return value


def join_pretty(values: list[Any]) -> str:
    return ", ".join(pretty_text(x) for x in values)


def escape_tex(text: Any) -> str:
    replacements = {
        "\\": "\\textbackslash{}",
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
        "~": "\\textasciitilde{}",
        "^": "\\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in str(text))


def link_list(urls: dict[str, str]) -> str:
    preferred = ["paper", "project", "code", "model", "devkit", "blog", "pypi", "kaggle", "ale"]
    parts: list[str] = []
    for key in preferred:
        if key in urls:
            parts.append(md_link(key, urls[key]))
    for key, url in urls.items():
        if key not in preferred:
            parts.append(md_link(key, url))
    return ", ".join(parts) if parts else "none recorded"


def openness(item: dict[str, Any]) -> str:
    return f"code {yes(item.get('open_code'))}; weights {yes(item.get('open_weights'))}; {item.get('evidence_level')}"


def residual_names(item: dict[str, Any]) -> str:
    return ", ".join(FRIENDLY_RESIDUALS.get(x, titleize_id(x)) for x in item.get("residuals", []))


def snapshot(systems: list[dict[str, Any]], benchmarks: list[dict[str, Any]], datasets: list[dict[str, Any]], families: list[dict[str, Any]]) -> list[str]:
    categories = len({x["category"] for x in systems})
    open_code = sum(1 for x in systems if x.get("open_code") is True)
    open_weights = sum(1 for x in systems if x.get("open_weights") is True)
    closed = sum(1 for x in systems if x.get("evidence_level") == "closed_reference")
    return [
        "## Current Snapshot",
        "",
        "| Item | Count |",
        "|---|---:|",
        f"| World-model systems | {len(systems)} |",
        f"| Benchmarks and evaluation suites | {len(benchmarks)} |",
        f"| Datasets and simulators | {len(datasets)} |",
        f"| Residual capability families | {len(families)} |",
        f"| Method categories | {categories} |",
        f"| Open-code systems | {open_code} |",
        f"| Open-weight systems | {open_weights} |",
        f"| Closed reference systems | {closed} |",
        "",
        "The counts are conservative. A system is not marked open unless an upstream source clearly exposes code and/or weights.",
        "",
    ]


def count_by_residual(items: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for item in items:
        for residual in item.get("residuals", []):
            counts[residual] += 1
    return dict(counts)


def how_to_use_section() -> list[str]:
    return [
        "## How to Use This Artifact",
        "",
        "| Reader goal | Start with | What to look for |",
        "|---|---|---|",
        "| Understand the paper's evidence base | Current Snapshot and Residual Capability Taxonomy | Counts behind the residual map and why a residual was credited. |",
        "| Find runnable baselines | Open Code and Open Weight Systems | Code/weight status, domain, and caveat before attempting reproduction. |",
        "| Identify paper ideas | Research Gap Map | Missing capability, what to build, and what evidence would convince reviewers. |",
        "| Extend the catalog | Coding Methodology and Contributing | Required fields, evidence levels, residual definitions, and validation commands. |",
        "| Prepare a citable release | Citation and Public Release Quality Gates | Validation, generated artifacts, DOI, and citation metadata. |",
        "",
    ]


def citation_section() -> list[str]:
    return [
        "## Citation",
        "",
        "If this artifact supports your work, cite the frozen release used in your study. Until a DOI-backed archive exists, cite the public GitHub snapshot and include the version.",
        "",
        "```bibtex",
        "@misc{dhumal2026worldmodelsresidualmap,",
        "  title = {World Models Residual Map},",
        "  author = {Dhumal, Ranjeet and Aerts, Koen},",
        "  year = {2026},",
        f"  version = {{{VERSION}}},",
        "  publisher = {GitHub},",
        "  howpublished = {GitHub repository},",
        f"  url = {{{REPO_URL}}},",
        f"  note = {{Companion artifact for {PAPER_TITLE}}}",
        "}",
        "```",
        "",
        "GitHub also reads `CITATION.cff`, so the repository's **Cite this repository** button should expose the same citation metadata. After creating a Zenodo or institutional archive, replace the GitHub-only citation with the DOI-backed release citation.",
        "",
    ]


def headline_findings_section(systems: list[dict[str, Any]], benchmarks: list[dict[str, Any]]) -> list[str]:
    system_counts = count_by_residual(systems)
    benchmark_counts = count_by_residual(benchmarks)
    return [
        "## Headline Findings",
        "",
        "1. **The field is dense where model-based RL already gave it tools.** Action semantics and planning utility dominate the coded systems, with "
        f"{system_counts.get('action_semantics', 0)} and {system_counts.get('planning_utility', 0)} systems respectively.",
        "2. **The defining world-model claims are thinly evidenced.** Counterfactual reasoning, calibrated uncertainty, and social-physical coupling remain the weakest system-side residuals in this snapshot.",
        "3. **Evaluation is uneven.** State persistence and physical-law extrapolation have multiple benchmarks, but counterfactual reasoning and uncertainty calibration still need stronger dedicated measurement.",
        "4. **Open code is not the same as reproducibility.** Several systems release code without weights, or release platform components whose exact model claims need upstream license and model-card checks.",
        "5. **The catalog should be read as evidence tracking, not leaderboard ranking.** Counts measure whether a residual is credibly attacked, not whether the residual is solved.",
        "",
        "| Residual | Systems | Benchmarks | Reading |",
        "|---|---:|---:|---|",
        f"| Action semantics | {system_counts.get('action_semantics', 0)} | {benchmark_counts.get('action_semantics', 0)} | Widely claimed; needs more action-contrast benchmarks. |",
        f"| Planning utility | {system_counts.get('planning_utility', 0)} | {benchmark_counts.get('planning_utility', 0)} | Strong MBRL lineage; planner exploitation remains under-tested. |",
        f"| Counterfactual reasoning | {system_counts.get('counterfactual_reasoning', 0)} | {benchmark_counts.get('counterfactual_reasoning', 0)} | A central gap for decision-facing world models. |",
        f"| Uncertainty calibration | {system_counts.get('uncertainty_calibration', 0)} | {benchmark_counts.get('uncertainty_calibration', 0)} | Crucial for risk-aware planning but rarely measured directly. |",
        f"| Social-physical coupling | {system_counts.get('social_physical_coupling', 0)} | {benchmark_counts.get('social_physical_coupling', 0)} | Benchmarks exist, but system evidence is essentially absent. |",
        "",
    ]


def research_gap_section() -> list[str]:
    return [
        "## Research Gap Map",
        "",
        "This table turns the residual map into a workbench for researchers. Each row is a possible paper contribution if paired with a clear method and convincing evidence.",
        "",
        "| Gap | Why it matters | What a contribution could add | Evidence target |",
        "|---|---|---|---|",
        "| Counterfactual consequence | World models should answer what changes under a different action, not only what happens next. | Paired-intervention data, causal state updates, or counterfactual rollout objectives. | Matched-history tests where changed actions or layouts cause the expected outcome shift. |",
        "| Calibrated uncertainty for planning | A planner needs to know when imagined futures are unreliable. | Uncertainty-aware dynamics, abstention, ensembles, distributional rollouts, or risk-aware planning heads. | Calibration under off-policy and rare-state shifts; lower regret when planning uses uncertainty. |",
        "| Social-physical dynamics | Real agents move through spaces governed by physics, goals, norms, and other agents. | Multi-agent world models with hidden beliefs, social rules, contact, affordances, and strategic response. | Human or agent response prediction under interventions; better decisions in mixed social-physical tasks. |",
        "| Persistent state with correction | Long rollouts drift unless memory can be corrected by new observations. | Memory architectures that preserve identity, inventory, maps, and latent state over long horizons. | Occlusion and re-observation tests; stable object identity and map consistency across long rollouts. |",
        "| Action abstraction | Actions may be torques, skills, language instructions, social moves, or tool calls. | Hierarchical action representations that bridge language-level intent and executable controls. | Action-contrast tests across abstraction levels and transfer to unseen tasks. |",
        "| Geometry-to-dynamics bridge | 3D assets can look navigable without obeying contact, support, material, or affordance dynamics. | Representations that bind metric geometry to dynamics and interaction constraints. | Multi-view consistency plus collision, support, conservation, and affordance diagnostics. |",
        "| Planner-in-the-loop robustness | Passive replay can hide model exploitation by optimizers. | Benchmarks where planners actively search against the learned model. | Exploitation rate, closed-loop regret, recovery behavior, and transfer to real or high-fidelity simulators. |",
        "| Validity and governance envelope | Deployment-facing simulators need known limits, provenance, and audit trails. | World-model model cards, datasheets, operational design domains, and risk registers. | Public invalid regions, monitoring hooks, audit logs, and safety-case evidence. |",
        "",
    ]


def residual_section(families: list[dict[str, Any]], systems: list[dict[str, Any]], benchmarks: list[dict[str, Any]]) -> list[str]:
    by_residual_systems: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_residual_benchmarks: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in systems:
        for residual in item.get("residuals", []):
            by_residual_systems[residual].append(item)
    for item in benchmarks:
        for residual in item.get("residuals", []):
            by_residual_benchmarks[residual].append(item)

    lines = [
        "## Residual Capability Taxonomy",
        "",
        "These residuals are the conceptual bridge between the paper and the repository. They describe what world models must prove beyond fluent text, static perception, or visually plausible video.",
        "",
        "| Residual | Question | Minimum evidence | Systems | Benchmarks |",
        "|---|---|---|---:|---:|",
    ]
    for family in families:
        rid = family["id"]
        lines.append(
            "| {name} | {question} | {evidence} | {systems} | {benchmarks} |".format(
                name=escape_table(family["name"]),
                question=escape_table(family["question"]),
                evidence=escape_table(", ".join(family["minimum_evidence"])),
                systems=len(by_residual_systems.get(rid, [])),
                benchmarks=len(by_residual_benchmarks.get(rid, [])),
            )
        )
    lines += [
        "",
        "Detailed residual mapping is encoded in `data/capability_families.json` and `data/systems.json`.",
        "",
    ]
    return lines


def open_systems_section(systems: list[dict[str, Any]]) -> list[str]:
    open_items = [
        item for item in systems
        if item.get("open_code") is True or item.get("open_weights") is True
    ]
    lines = [
        "## Open Code and Open Weight Systems",
        "",
        "This is the most important table for readers who want to inspect, run, or build on existing work. It deliberately separates code openness from weight openness.",
        "",
        "| System | Year | Category | Code | Weights | Domains | Main link | Caveat |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for item in sorted(open_items, key=lambda x: (x["year"], x["name"])):
        urls = item.get("urls", {})
        link = first_url(urls, ["code", "model", "project", "paper"])
        lines.append(
            "| {name} | {year} | {category} | {code} | {weights} | {domains} | {link} | {caveat} |".format(
                name=escape_table(item["name"]),
                year=item["year"],
                category=escape_table(titleize_id(item["category"])),
                code=yes(item["open_code"]),
                weights=yes(item["open_weights"]),
                domains=escape_table(join_pretty(item["domains"][:3])),
                link=md_link("link", link),
                caveat=escape_table(item["caveats"]),
            )
        )
    lines.append("")
    return lines


def systems_section(systems: list[dict[str, Any]]) -> list[str]:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in systems:
        by_category[item["category"]].append(item)

    lines = [
        "## Full Systems Catalog",
        "",
        "Systems are grouped by method family. Each entry includes the evidence domain and a caveat so the catalog is useful without opening JSON files.",
        "",
    ]
    for category, items in sorted(by_category.items()):
        lines += [f"### {titleize_id(category)}", ""]
        for item in sorted(items, key=lambda x: (x["year"], x["name"])):
            lines += [
                f"#### {item['name']} ({item['year']})",
                "",
                f"- **Organizations:** {', '.join(item['organizations'])}",
                f"- **Domains:** {join_pretty(item['domains'])}",
                f"- **Modalities:** {join_pretty(item['modalities'])}",
                f"- **Action conditioned:** {yes(item['action_conditioned'])}",
                f"- **Openness:** {openness(item)}",
                f"- **Residuals:** {residual_names(item)}",
                f"- **Evaluation modes:** {join_pretty(item['evaluation_modes'])}",
                f"- **Links:** {link_list(item.get('urls', {}))}",
                f"- **Caveat:** {item['caveats']}",
                "",
            ]
    return lines


def benchmarks_section(benchmarks: list[dict[str, Any]]) -> list[str]:
    lines = [
        "## Benchmarks and Evaluation Suites",
        "",
        "Benchmarks are included with explicit limitations because world-model validity cannot be reduced to one media-quality score.",
        "",
        "| Benchmark | Year | What it tests | Residuals | Links | Limitation |",
        "|---|---:|---|---|---|---|",
    ]
    for item in sorted(benchmarks, key=lambda x: (x["year"], x["name"])):
        lines.append(
            "| {name} | {year} | {tests} | {residuals} | {links} | {limitation} |".format(
                name=escape_table(item["name"]),
                year=item["year"],
                tests=escape_table(join_pretty(item["tests"])),
                residuals=escape_table(residual_names(item)),
                links=link_list(item.get("urls", {})),
                limitation=escape_table(item["limitations"]),
            )
        )
    lines.append("")
    return lines


def datasets_section(datasets: list[dict[str, Any]]) -> list[str]:
    lines = [
        "## Datasets and Simulators",
        "",
        "Datasets and simulators are listed separately because they support evaluation and training claims but are not world models by themselves.",
        "",
        "| Dataset / simulator | Year | Access | Modalities | Relevance | Links | Caveat |",
        "|---|---:|---|---|---|---|---|",
    ]
    for item in sorted(datasets, key=lambda x: (x["year"], x["name"])):
        lines.append(
            "| {name} | {year} | {access} | {modalities} | {relevance} | {links} | {caveat} |".format(
                name=escape_table(item["name"]),
                year=item["year"],
                access=escape_table(item["access"]),
                modalities=escape_table(join_pretty(item["modalities"])),
                relevance=escape_table(item["world_model_relevance"]),
                links=link_list(item.get("urls", {})),
                caveat=escape_table(item.get("caveats", "")),
            )
        )
    lines.append("")
    return lines


def community_lists_section(lists: list[dict[str, Any]]) -> list[str]:
    lines = [
        "## Related Community Lists",
        "",
        "These lists are useful for auditing missing work. Entries from them should still be verified against primary sources before being added here.",
        "",
        "| List | Focus | Link | How to use |",
        "|---|---|---|---|",
    ]
    for item in lists:
        lines.append(
            "| {name} | {focus} | {url} | {how} |".format(
                name=escape_table(item["name"]),
                focus=escape_table(item["focus"]),
                url=md_link("link", item["url"]),
                how=escape_table(item["how_to_use"]),
            )
        )
    lines.append("")
    return lines


def methodology_section() -> list[str]:
    return [
        "## Coding Methodology",
        "",
        "The catalog follows three rules.",
        "",
        "1. **Be conservative about openness.** If code or weights are unclear, they are marked `unknown`, `partial`, or `no`.",
        "2. **Separate demos from evidence.** A visually impressive rollout is not treated as proof of general physical simulation.",
        "3. **Code by residual, not hype.** Each system is mapped to the residual capability it plausibly attacks, such as action semantics or planning utility.",
        "",
        "### Evidence Levels",
        "",
        "| Label | Meaning |",
        "|---|---|",
        "| `official_open` | Official code and/or weights are available. |",
        "| `official_partial` | Official paper/project exists, but release is incomplete, limited, or partly open. |",
        "| `unofficial_open` | Community implementation exists, but not an official release. |",
        "| `closed_reference` | Important comparator, but no verified public implementation or weights. |",
        "| `dataset_or_benchmark` | Evaluation resource rather than a model. |",
        "",
        "### Inclusion Criteria",
        "",
        "Included systems must have at least one reliable upstream source: paper, project page, official repository, model page, or benchmark page. The catalog excludes social-media-only claims, unclear forks, and copied third-party assets.",
        "",
    ]


def maintenance_section() -> list[str]:
    return [
        "## Reproducing and Updating the Artifact",
        "",
        "The single README is generated from the JSON files in `data/`. Edit the JSON, then regenerate.",
        "",
        "```bash",
        "python3 scripts/validate_artifact.py",
        "python3 scripts/export_tables.py",
        "python3 scripts/export_figures.py",
        "```",
        "",
        "The scripts update this README, the paper-facing LaTeX table at `generated/tables/open_systems_table.tex`, and the system-by-residual coverage figure at `generated/figures/residual_heatmap.tikz`.",
        "",
        "Recommended submission workflow:",
        "",
        "1. Finalize metadata before submission.",
        "2. Run validation and export.",
        "3. Commit `README.md`, `data/`, `scripts/`, and `generated/tables/open_systems_table.tex`.",
        "4. Tag a paper snapshot, for example `v0.1-paper-submission`.",
        "5. Archive the tag on Zenodo or a similar archival service.",
        "6. Cite the DOI in the paper.",
        "",
        "## Public Release Quality Gates",
        "",
        "Before tagging a release or creating a Zenodo archive, run these checks:",
        "",
        "- `python3 scripts/validate_artifact.py` passes with no warnings.",
        "- `python3 scripts/export_tables.py` and `python3 scripts/export_figures.py` have been run after the last data edit.",
        "- `README.md` contains the same counts as the paper abstract and residual-coverage table.",
        "- `CITATION.cff` has the final release date, version, and repository URL after the GitHub repository exists.",
        "- `paper/repository_note.md` has the final GitHub URL and DOI after the archived snapshot exists.",
        "- Every new entry has an upstream source and a caveat that prevents overclaiming.",
        "- Generated files are committed only when they are deterministic outputs of the JSON source.",
        "",
        "Known limits of the current snapshot: it is a curated corpus rather than an exhaustive census; closed systems are evidence-limited; openness can change after release; and residual labels are conservative binary codings rather than full capability scores.",
        "",
        "## Repository Files",
        "",
        "```text",
        "README.md                         # single human-readable artifact",
        "data/*.json                       # machine-readable source of truth",
        "scripts/validate_artifact.py       # schema and consistency checks",
        "scripts/export_tables.py           # regenerates README and LaTeX table",
        "scripts/export_figures.py          # regenerates the residual coverage figure",
        "generated/tables/open_systems_table.tex",
        "generated/figures/residual_heatmap.tikz",
        "CITATION.cff",
        ".zenodo.json",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "LICENSE-DATA",
        "LICENSE-CODE",
        "paper/repository_note.md",
        "```",
        "",
        "## License and Disclaimer",
        "",
        "This repository uses a split license. Original data, metadata, documentation, generated tables, and generated figures are licensed under CC BY 4.0. Source code and scripts are licensed under the MIT License.",
        "",
        "External repositories, papers, model weights, datasets, and benchmarks remain governed by their upstream licenses and terms.",
        "",
        "This artifact is a research index, not an endorsement of any model's safety, licensing terms, or deployment readiness. Always review upstream licenses, acceptable-use policies, model cards, and dataset terms before use.",
        "",
        "Views are personal and do not represent Wolters Kluwer.",
        "",
    ]


def readme(
    systems: list[dict[str, Any]],
    benchmarks: list[dict[str, Any]],
    datasets: list[dict[str, Any]],
    families: list[dict[str, Any]],
    community_lists: list[dict[str, Any]],
) -> str:
    lines = [
        "# World Models Residual Map",
        "",
        "[![Data License: CC BY 4.0](https://img.shields.io/badge/data%20license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)",
        "[![Code License: MIT](https://img.shields.io/badge/code%20license-MIT-green.svg)](LICENSE-CODE)",
        "[![Citation: CFF](https://img.shields.io/badge/citation-CFF-lightgrey.svg)](CITATION.cff)",
        "",
        "Companion artifact for the survey paper:",
        "",
        f"> **{PAPER_TITLE}**",
        "",
        "Authors: **Ranjeet Dhumal** (Senior Data Scientist, Wolters Kluwer India Private Limited); **Koen Aerts** (Senior Application & Product Architect, Wolters Kluwer, Mechelen, Belgium)  ",
        f"Repository: **{REPO_URL}**  ",
        f"Version: **{VERSION}**  ",
        "License: **CC BY 4.0 for data/docs/generated artifacts; MIT for scripts**",
        "",
        "This repository is a curated map of world-model systems, open-source implementations, open-weight releases, benchmarks, datasets, and evaluation criteria. It is intentionally kept as a single human-readable document so a reviewer can understand the artifact without opening JSON files.",
        "",
        "The core thesis is simple: world models should be compared by the residual capabilities they address after LLMs, vision models, and generative media models are accounted for. Those residuals include action semantics, state persistence, physical law extrapolation, counterfactual reasoning, uncertainty calibration, planning utility, sim-to-real transfer, spatial consistency, social-physical coupling, and governance readiness.",
        "",
        "The JSON files in `data/` remain the machine-readable backend; this README is generated from them.",
        "",
    ]
    for section in (
        citation_section(),
        how_to_use_section(),
        headline_findings_section(systems, benchmarks),
        snapshot(systems, benchmarks, datasets, families),
        research_gap_section(),
        residual_section(families, systems, benchmarks),
        open_systems_section(systems),
        systems_section(systems),
        benchmarks_section(benchmarks),
        datasets_section(datasets),
        community_lists_section(community_lists),
        methodology_section(),
        maintenance_section(),
    ):
        lines.extend(section)
    return "\n".join(lines).rstrip() + "\n"


def latex_open_systems(systems: list[dict[str, Any]]) -> str:
    open_items = [
        item for item in systems
        if item.get("open_code") is True or item.get("open_weights") is True
    ]
    rows = []
    for item in sorted(open_items, key=lambda x: (x["year"], x["name"])):
        rows.append(
            "{name} & {year} & {category} & {code} & {weights} & {residuals} \\\\".format(
                name=escape_tex(item["name"]),
                year=item["year"],
                category=escape_tex(titleize_id(item["category"])),
                code=escape_tex(yes(item["open_code"])),
                weights=escape_tex(yes(item["open_weights"])),
                residuals=escape_tex(", ".join(SHORT_RESIDUALS.get(x, titleize_id(x)) for x in item.get("residuals", [])[:3])),
            )
        )
    body = "\n".join(rows)
    return (
        "\\begin{table}[t]\n"
        "\\centering\n"
        "\\scriptsize\n"
        "\\renewcommand{\\arraystretch}{0.95}\n"
        "\\begin{tabularx}{\\linewidth}{@{}P{0.18\\linewidth}P{0.08\\linewidth}P{0.23\\linewidth}P{0.08\\linewidth}P{0.1\\linewidth}Y@{}}\n"
        "\\toprule\n"
        "System & Year & Category & Code & Weights & Residuals \\\\\n"
        "\\midrule\n"
        f"{body}\n"
        "\\bottomrule\n"
        "\\end{tabularx}\n"
        "\\caption{Open-code and open-weight systems in the companion artifact snapshot.}\n"
        "\\label{tab:artifact-open-systems}\n"
        "\\end{table}\n"
    )


def main() -> int:
    systems = load("systems.json")
    benchmarks = load("benchmarks.json")
    datasets = load("datasets.json")
    families = load("capability_families.json")
    community_lists = load("community_lists.json")

    write(ROOT / "README.md", readme(systems, benchmarks, datasets, families, community_lists))
    write(TABLES / "open_systems_table.tex", latex_open_systems(systems))
    print(f"Wrote single-file README to {ROOT / 'README.md'}")
    print(f"Wrote LaTeX table to {TABLES / 'open_systems_table.tex'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
