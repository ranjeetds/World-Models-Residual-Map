#!/usr/bin/env python3
"""Validate the World Models Residual Map metadata."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def require_fields(entry: dict[str, Any], fields: list[str], file_name: str) -> list[str]:
    errors: list[str] = []
    for field in fields:
        if field not in entry:
            errors.append(f"{file_name}:{entry.get('id', '<missing-id>')} missing field '{field}'")
    return errors


def validate_urls(entry: dict[str, Any], file_name: str) -> list[str]:
    errors: list[str] = []
    urls = entry.get("urls", {})
    if not isinstance(urls, dict):
        return [f"{file_name}:{entry.get('id', '<missing-id>')} urls must be an object"]
    for label, value in urls.items():
        if not isinstance(value, str) or not value.startswith(("http://", "https://")):
            errors.append(f"{file_name}:{entry.get('id', '<missing-id>')} URL '{label}' is invalid: {value!r}")
    return errors


def validate_unique_ids(entries: list[dict[str, Any]], file_name: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        item_id = entry.get("id")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{file_name}: entry has missing or invalid id")
            continue
        if item_id in seen:
            errors.append(f"{file_name}: duplicate id '{item_id}'")
        seen.add(item_id)
    return errors


def validate_list_file(file_name: str, required_fields: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    path = DATA / file_name
    entries = load_json(path)
    errors: list[str] = []
    if not isinstance(entries, list):
        return [], [f"{file_name} must contain a JSON list"]
    typed_entries: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(f"{file_name}: every entry must be an object")
            continue
        typed_entries.append(entry)
        errors.extend(require_fields(entry, required_fields, file_name))
        errors.extend(validate_urls(entry, file_name))
    errors.extend(validate_unique_ids(typed_entries, file_name))
    return typed_entries, errors


def main() -> int:
    schema = load_json(DATA / "schema.json")
    families = load_json(DATA / "capability_families.json")
    residual_ids = {entry["id"] for entry in families}
    allowed_evidence = set(schema["allowed_evidence_levels"])
    evidence_record_fields = schema.get("residual_evidence_record_fields", [])
    allowed_evidence_types = set(schema.get("allowed_evidence_types", []))
    allowed_confidence = set(schema.get("allowed_confidence_levels", []))

    systems, errors = validate_list_file("systems.json", schema["systems_required_fields"])
    benchmarks, benchmark_errors = validate_list_file("benchmarks.json", schema["benchmark_required_fields"])
    datasets, dataset_errors = validate_list_file("datasets.json", schema["dataset_required_fields"])
    errors.extend(benchmark_errors)
    errors.extend(dataset_errors)

    community_lists = load_json(DATA / "community_lists.json")
    if not isinstance(community_lists, list):
        errors.append("community_lists.json must contain a JSON list")
    else:
        errors.extend(validate_unique_ids([x for x in community_lists if isinstance(x, dict)], "community_lists.json"))

    for entry in systems:
        evidence = entry.get("evidence_level")
        if evidence not in allowed_evidence:
            errors.append(f"systems.json:{entry['id']} invalid evidence_level {evidence!r}")
        residuals = entry.get("residuals", [])
        if not isinstance(residuals, list) or not residuals:
            errors.append(f"systems.json:{entry['id']} residuals must be a non-empty list")
            continue
        for residual in residuals:
            if residual not in residual_ids:
                errors.append(f"systems.json:{entry['id']} unknown residual '{residual}'")
        evidence_map = entry.get("residual_evidence")
        if evidence_map is not None:
            if not isinstance(evidence_map, dict):
                errors.append(f"systems.json:{entry['id']} residual_evidence must be an object")
            else:
                for rkey, record in evidence_map.items():
                    if rkey not in residuals:
                        errors.append(f"systems.json:{entry['id']} residual_evidence key '{rkey}' is not in residuals")
                    if not isinstance(record, dict):
                        errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] must be an object")
                        continue
                    for field in evidence_record_fields:
                        if field not in record:
                            errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] missing '{field}'")
                    if record.get("evidence_type") not in allowed_evidence_types:
                        errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] invalid evidence_type {record.get('evidence_type')!r}")
                    if record.get("confidence") not in allowed_confidence:
                        errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] invalid confidence {record.get('confidence')!r}")
                    src = record.get("source_url", "")
                    if not isinstance(src, str) or not src.startswith(("http://", "https://")):
                        errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] source_url is invalid: {src!r}")
                    level = record.get("capability_level")
                    if level is not None and (not isinstance(level, int) or isinstance(level, bool) or level < 0 or level > 5):
                        errors.append(f"systems.json:{entry['id']} residual_evidence['{rkey}'] capability_level must be an integer 0-5: {level!r}")

    for entry in benchmarks:
        residuals = entry.get("residuals", [])
        if not isinstance(residuals, list):
            errors.append(f"benchmarks.json:{entry['id']} residuals must be a list")
            continue
        for residual in residuals:
            if residual not in residual_ids:
                errors.append(f"benchmarks.json:{entry['id']} unknown residual '{residual}'")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(systems)} systems, {len(benchmarks)} benchmarks, {len(datasets)} datasets validated.")
    print(f"OK: {len(residual_ids)} residual capability families validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

