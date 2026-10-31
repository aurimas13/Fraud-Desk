from pathlib import Path

import duckdb
import pytest

from fraud_desk.data.ibm_aml import build_database, parse_patterns, profile

FIX = Path(__file__).parent / "fixtures"


def test_parse_patterns_reads_typologies_and_rows():
    attempts = parse_patterns(FIX / "mini_Patterns.txt")
    assert [a.typology for a in attempts] == ["FAN-OUT", "CYCLE"]
    assert attempts[0].detail == "Max 16-degree Fan-Out"
    assert len(attempts[0].rows) == 3
    assert attempts[1].rows[0][2] == "8001A8D10"


def test_parse_patterns_rejects_unclosed_block(tmp_path):
    bad = tmp_path / "bad.txt"
    bad.write_text("BEGIN LAUNDERING ATTEMPT - FAN-IN:\n2022/09/01 00:06,1,A,2,B,1,Euro,1,Euro,ACH,1\n")
    with pytest.raises(ValueError, match="ended inside"):
        parse_patterns(bad)


def test_build_database_keeps_identifiers_as_strings(tmp_path):
    db = build_database(FIX / "mini_Trans.csv", FIX / "mini_Patterns.txt", tmp_path)
    con = duckdb.connect(str(db), read_only=True)
    try:
        bank, acct = con.execute("SELECT from_bank, to_account FROM transactions WHERE tx_id = 1").fetchone()
    finally:
        con.close()
    assert bank == "021174"  # leading zero survives
    assert acct == "80011F990"  # hex account id survives
    assert (tmp_path / "transactions.parquet").exists()


def test_profile_counts_labels_and_typologies(tmp_path):
    db = build_database(FIX / "mini_Trans.csv", FIX / "mini_Patterns.txt", tmp_path)
    p = profile(db)
    assert p["transactions"] == 6
    assert p["laundering_transactions"] == 3
    assert p["attempts_by_typology"] == {"FAN-OUT": 1, "CYCLE": 1}
