"""Load the IBM "Transactions for Anti Money Laundering" (AMLworld) dataset.

Source: Altman et al., "Realistic Synthetic Financial Transactions for
Anti-Money Laundering Models" (NeurIPS 2023 Datasets and Benchmarks),
https://arxiv.org/abs/2306.16424 . Data on Kaggle under CDLA-Sharing 1.0:
https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml

The data is never committed to this repo. `scripts/download_data.sh` fetches it
into `data/raw/`, and `build_database` turns the CSV into Parquet plus a DuckDB
file that every later stage (ML triage, agents, evals) reads.

Two quirks of the raw files that this module handles on purpose:

* the transactions CSV has two columns both called "Account" (sender and
  receiver), so it is read with explicit column names, never by header;
* bank codes and account ids look numeric but are identifiers with leading
  zeros and hex digits, so both are read as strings.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import duckdb

# Column order of `*_Trans.csv`, renamed so the duplicate "Account" header
# becomes from_account / to_account.
TRANSACTION_COLUMNS: dict[str, str] = {
    "ts": "VARCHAR",
    "from_bank": "VARCHAR",
    "from_account": "VARCHAR",
    "to_bank": "VARCHAR",
    "to_account": "VARCHAR",
    "amount_received": "DOUBLE",
    "receiving_currency": "VARCHAR",
    "amount_paid": "DOUBLE",
    "payment_currency": "VARCHAR",
    "payment_format": "VARCHAR",
    "is_laundering": "INTEGER",
}

_BEGIN = re.compile(r"^BEGIN LAUNDERING ATTEMPT\s*-\s*(?P<kind>[A-Z\- ]+?)(?::\s*(?P<detail>.*))?$")
_END = re.compile(r"^END LAUNDERING ATTEMPT")


@dataclass
class LaunderingAttempt:
    """One attempt from `*_Patterns.txt`: a typology and its transactions."""

    attempt_id: int
    typology: str
    detail: str
    rows: list[list[str]] = field(default_factory=list)


def parse_patterns(path: Path) -> list[LaunderingAttempt]:
    """Parse a `*_Patterns.txt` file into laundering attempts.

    Each attempt is a block that opens with
    `BEGIN LAUNDERING ATTEMPT - <TYPOLOGY>[: <detail>]`, lists its transactions
    in the same column order as the transactions CSV, and closes with
    `END LAUNDERING ATTEMPT ...`. These blocks are the ground truth for the
    network agent's typology labels (fan-in, fan-out, cycle, ...).
    """
    attempts: list[LaunderingAttempt] = []
    current: LaunderingAttempt | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if m := _BEGIN.match(line):
            if current is not None:
                raise ValueError(f"{path}: BEGIN inside an open attempt (#{current.attempt_id})")
            current = LaunderingAttempt(
                attempt_id=len(attempts) + 1,
                typology=m["kind"].strip().upper(),
                detail=(m["detail"] or "").strip(),
            )
        elif _END.match(line):
            if current is None:
                raise ValueError(f"{path}: END without BEGIN")
            attempts.append(current)
            current = None
        elif current is not None:
            current.rows.append([c.strip() for c in line.split(",")])
    if current is not None:
        raise ValueError(f"{path}: file ended inside attempt #{current.attempt_id}")
    return attempts


def build_database(trans_csv: Path, patterns_txt: Path | None, out_dir: Path) -> Path:
    """Convert the raw CSV (and optional patterns file) into Parquet + DuckDB.

    Every transaction gets a stable `tx_id` (its 1-based row number in the
    CSV). Agents must cite `tx_id`s, and the verifier checks that every cited
    id exists - so this id is the backbone of grounding.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    parquet = out_dir / "transactions.parquet"
    db_path = out_dir / "fraud_desk.duckdb"

    con = duckdb.connect(str(db_path))
    try:
        columns = ", ".join(f"'{name}': '{kind}'" for name, kind in TRANSACTION_COLUMNS.items())
        con.execute(
            f"""
            CREATE OR REPLACE TABLE transactions AS
            SELECT row_number() OVER () AS tx_id,
                   strptime(ts, '%Y/%m/%d %H:%M') AS ts,
                   * EXCLUDE (ts)
            FROM read_csv(?, header = true, columns = {{{columns}}})
            """,
            [str(trans_csv)],
        )
        con.execute("COPY transactions TO ? (FORMAT parquet)", [str(parquet)])

        if patterns_txt is not None:
            rows = [
                (a.attempt_id, a.typology, a.detail, r[0], r[2], r[4], float(r[7]))
                for a in parse_patterns(patterns_txt)
                for r in a.rows
            ]
            con.execute(
                """
                CREATE OR REPLACE TABLE pattern_rows (
                    attempt_id INTEGER, typology VARCHAR, detail VARCHAR,
                    ts VARCHAR, from_account VARCHAR, to_account VARCHAR, amount_paid DOUBLE)
                """
            )
            if rows:
                con.executemany("INSERT INTO pattern_rows VALUES (?, ?, ?, ?, ?, ?, ?)", rows)
    finally:
        con.close()
    return db_path


def profile(db_path: Path) -> dict[str, object]:
    """The numbers Day 1 publishes: size, label balance, typology counts."""
    con = duckdb.connect(str(db_path), read_only=True)
    try:
        n, laundering, accounts, start, end = con.execute(
            """
            SELECT count(*), sum(is_laundering),
                   (SELECT count(DISTINCT a) FROM (SELECT from_account a FROM transactions
                                                   UNION SELECT to_account FROM transactions)),
                   min(ts), max(ts)
            FROM transactions
            """
        ).fetchone()
        formats = dict(
            con.execute(
                "SELECT payment_format, count(*) FROM transactions GROUP BY 1 ORDER BY 2 DESC"
            ).fetchall()
        )
        tables = {r[0] for r in con.execute("SHOW TABLES").fetchall()}
        typologies = (
            dict(
                con.execute(
                    "SELECT typology, count(DISTINCT attempt_id) FROM pattern_rows GROUP BY 1 ORDER BY 2 DESC"
                ).fetchall()
            )
            if "pattern_rows" in tables
            else {}
        )
    finally:
        con.close()
    return {
        "transactions": n,
        "laundering_transactions": laundering,
        "laundering_rate": (laundering / n) if n else 0.0,
        "accounts": accounts,
        "first_ts": str(start),
        "last_ts": str(end),
        "payment_formats": formats,
        "attempts_by_typology": typologies,
    }
