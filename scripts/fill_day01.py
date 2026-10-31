"""Fill the Day 1 post placeholders from `fraud-desk profile` output.

Usage: .venv/bin/fraud-desk profile > /tmp/profile.json
       .venv/bin/python scripts/fill_day01.py /tmp/profile.json <load_seconds>
Prints each filled post; edit by hand before posting. Nothing is posted from here.
"""

import json
import sys
from pathlib import Path

p = json.loads(Path(sys.argv[1]).read_text())
load_seconds = sys.argv[2] if len(sys.argv) > 2 else "?"
rate = p["laundering_rate"]
top = sorted(p["attempts_by_typology"].items(), key=lambda kv: -kv[1])[:4]
values = {
    "N_TX": f"{p['transactions']:,}",
    "N_ACCOUNTS": f"{p['accounts']:,}",
    "ONE_IN": f"{round(1 / rate):,}" if rate else "?",
    "ACC_ALL_CLEAN": f"{(1 - rate) * 100:.2f}",
    "LOAD_SECONDS": load_seconds,
    "TOP_TYPOLOGIES": ", ".join(f"{k.lower()} ({v})" for k, v in top) or "?",
}
for name in ("x.md", "threads.md", "linkedin.md"):
    text = (Path(__file__).parent.parent / "posts" / "day-01" / name).read_text()
    for key, val in values.items():
        text = text.replace("{" + key + "}", val)
    print(f"===== {name} ({len(text.rstrip())} chars)\n{text}")
