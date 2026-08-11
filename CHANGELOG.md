# Changelog

All notable changes to the World Models Residual Map artifact are tracked here.

## 0.2.0 - 2026-08-11

- Added per-cell evidence records (source, locator, summary, evidence type, confidence, caveat) for all frontier residual assignments.
- Added an explicit inclusion-threshold (`boundary`) to each debatable residual family.
- Introduced the graded 0-5 capability-evidence scale and piloted `capability_level` on the frontier cells.
- Extended the validator to check evidence records, evidence types, confidence, and capability levels.
- Added Koen Aerts as second author across manuscript and artifact metadata.

## 0.1.0 - 2026-06-22

- Initial public companion artifact for the world models survey paper.
- Added curated metadata for systems, benchmarks, datasets, residual capability families, and related community lists.
- Added validation and export scripts for the human-readable README, LaTeX table, and residual coverage figure.
- Added citation metadata through `CITATION.cff` and Zenodo-ready release metadata through `.zenodo.json`.
- Added split licensing: CC BY 4.0 for data/documentation/generated artifacts and MIT for scripts.
