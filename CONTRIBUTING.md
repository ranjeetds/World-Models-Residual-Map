# Contributing

Contributions should improve the accuracy, coverage, or reproducibility of the residual map.

## What to Add

- New world-model systems with papers, code, weights, or official project pages.
- Corrections to openness status, licenses, URLs, or domains.
- Benchmarks and datasets that test action, persistence, physics, counterfactuals, uncertainty, planning, sim-to-real, or governance.
- Evidence notes that clarify what a system actually demonstrates.

## Minimum Evidence

Every new system should include at least one of:

- paper URL,
- official project page,
- official repository,
- official model page,
- credible benchmark or dataset page.

Avoid adding entries based only on social media posts, demos without source pages, or reposted summaries.

## Pull Request Checklist

- `python3 scripts/validate_artifact.py` passes.
- `python3 scripts/export_tables.py` has been run so `README.md` and the LaTeX table are up to date.
- New URLs are upstream sources, not only news articles.
- Openness status is conservative when uncertain.
- Caveats are included for closed systems, unofficial implementations, or domain-limited results.
- New systems are mapped to at least one residual capability family.

## Licensing of Contributions

By contributing, you agree that:

- data, metadata, documentation, generated tables, and generated figures are contributed under CC BY 4.0;
- source code and scripts are contributed under the MIT License;
- linked third-party resources remain under their own upstream licenses and terms.
