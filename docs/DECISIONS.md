# Decisions

One entry per decision that would be expensive to reverse. Newest last.

## D1 (Day 0) Dataset: IBM AMLworld HI-Small
Labelled per transaction, with a patterns file that names each laundering attempt's typology, and small
enough for a laptop (5M rows). PaySim lacks network typologies; SAML-D is non-commercial. Data is
CDLA-Sharing 1.0, so it is downloaded by script and never committed.

## D2 (Day 0) Storage: DuckDB over Parquet, opened read-only by agents
No server to run, fast analytical SQL, and `read_only=True` makes the SQL tool unable to change data,
whatever an agent or an injected instruction asks for.

## D3 (Day 0) Agents on the raw Claude API, no framework
Same approach as Calculator Agent, Claude Agent From Scratch and Code-Editing Agent: the loop, tool
pairing, caps and cost accounting stay visible and testable offline with a fake client. A framework port
is an optional comparison, not the foundation.

## D4 (Day 0) The verifier is code, not a model
"Does every cited `tx_id` exist and involve this account?" has an exact answer. A model would add cost
and a new way to be wrong.

## D5 (Day 0) Sanctions: UK list + OFAC SDN, OpenSanctions optional
OpenSanctions is CC BY-NC 4.0; the UK list is under the Open Government Licence. The IBM data has no
names, so sanctions matching runs on synthetic names attached to a test subset, and every post says so.
