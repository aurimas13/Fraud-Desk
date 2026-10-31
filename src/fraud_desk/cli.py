"""`fraud-desk` command line: build the database and print the Day 1 profile."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from fraud_desk.data.ibm_aml import build_database, profile


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="fraud-desk")
    sub = parser.add_subparsers(dest="command", required=True)

    b = sub.add_parser("build-db", help="raw CSV (+ patterns) -> Parquet + DuckDB")
    b.add_argument("--trans", type=Path, default=Path("data/raw/HI-Small_Trans.csv"))
    b.add_argument("--patterns", type=Path, default=Path("data/raw/HI-Small_Patterns.txt"))
    b.add_argument("--out", type=Path, default=Path("data/processed"))

    p = sub.add_parser("profile", help="print dataset numbers as JSON")
    p.add_argument("--db", type=Path, default=Path("data/processed/fraud_desk.duckdb"))

    args = parser.parse_args(argv)
    if args.command == "build-db":
        patterns = args.patterns if args.patterns.exists() else None
        print(build_database(args.trans, patterns, args.out))
    else:
        print(json.dumps(profile(args.db), indent=2, default=str))


if __name__ == "__main__":
    main()
