#!/usr/bin/env python3
"""AnEnPi-compatible Python parser for EC-cluster analog target reconstruction.

This script reconstructs EC/cluster matrices from AnEnPi-style Drugtargets outputs.
It supports the public NISE targets resource by separating homologous-only ECs from
candidate analogous ECs where parasite clusters differ from human cluster sets.
"""
from pathlib import Path
import argparse
import collections
import csv
import re

EC_RE = re.compile(r"^(\d+|-)\.(\d+|-)\.(\d+|-)\.(\d+|-)$")


def parse_drug_targets(path):
    records = []
    current_ec = None
    for line in Path(path).read_text(errors="replace").splitlines():
        stripped = line.strip().replace("ec:", "")
        if EC_RE.match(stripped):
            current_ec = stripped
            continue
        if current_ec and "|" in line:
            parts = line.split("||")
            human_numbers = re.findall(r"\d+", parts[0] if parts else "")
            parasite_numbers = re.findall(r"\d+", parts[1] if len(parts) > 1 else "")
            human_cluster = int(human_numbers[-2]) if len(human_numbers) >= 2 else None
            parasite_cluster = int(parasite_numbers[-2]) if len(parasite_numbers) >= 2 else None
            records.append((current_ec, human_cluster, parasite_cluster, line.strip()))
    return records


def reconstruct(records):
    grouped = collections.defaultdict(lambda: {"human": set(), "parasite": set(), "rows": []})
    for ec, human_cluster, parasite_cluster, raw in records:
        if human_cluster is not None:
            grouped[ec]["human"].add(human_cluster)
        if parasite_cluster is not None:
            grouped[ec]["parasite"].add(parasite_cluster)
        grouped[ec]["rows"].append(raw)
    rows = []
    for ec, data in sorted(grouped.items()):
        human = data["human"]
        parasite = data["parasite"]
        unique = parasite - human
        rows.append({
            "EC": ec,
            "human_clusters": ";".join(map(str, sorted(human))),
            "parasite_clusters": ";".join(map(str, sorted(parasite))),
            "parasite_unique_clusters": ";".join(map(str, sorted(unique))),
            "same_ec_in_human_and_parasite": bool(human and parasite),
            "analog_candidate": bool(human and unique),
            "homologous_only": bool(human and parasite and not unique),
            "raw_record_count": len(data["rows"]),
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description="Reconstruct AnEnPi-style EC/cluster analog matrix.")
    parser.add_argument("drug_targets", help="AnEnPi-style Drugtargets output")
    parser.add_argument("--out", default="ec_cluster_matrix.csv")
    args = parser.parse_args()
    rows = reconstruct(parse_drug_targets(args.drug_targets))
    fields = list(rows[0].keys()) if rows else ["EC"]
    with open(args.out, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
