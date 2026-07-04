#!/usr/bin/env python3
from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "database" / "nise_targets.sqlite"
DATA = ROOT / "data" / "processed"
TABLES = {
    "proteome_catalog": "proteome_catalog.csv",
    "core_ecs": "core_all_parasites.csv",
    "intergenomic_summary": "intergenomic_summary.csv",
}

DB.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(DB) as conn:
    for table, filename in TABLES.items():
        path = DATA / filename
        if path.exists():
            pd.read_csv(path).to_sql(table, conn, if_exists="replace", index=False)
            print(f"loaded {table}: {path}")
        else:
            print(f"missing {path}")
print(f"database written to {DB}")
