# The 60-day plan

Day 1 = Tue 3 Nov 2026, Day 60 = Fri 1 Jan 2027 (moved one day on 2 Nov; Day 0 = Mon 2 Nov). About 2-3 hours a day; weekends carry the heavier
days. Every day ends with **one commit, one number, one lesson, one post**. If a day slips, the next day
shrinks scope, never the streak.

Budget: up to **USD 50** of model calls for all 60 days. Small models (Haiku class) do the sub-agent
work, a larger model only where the eval shows it pays. Batch API for eval runs (50% off).

## Week 1 - Data and the bar to beat (Days 1-7, 3-9 Nov)
| Day | Date | Ship |
|---|---|---|
| 1 | Tue 3 Nov | Data in: download HI-Small, Parquet + DuckDB with `tx_id`, profile (rows, 1-in-N laundering, typologies). Post the numbers. |
| 2 | Wed 4 Nov | Chronological 60/20/20 split; leakage test (no test-period row in train). |
| 3 | Thu 5 Nov | Account-level features in SQL (fan-in/out degree, amounts, currencies, formats, velocity). |
| 4 | Fri 6 Nov | XGBoost triage baseline with `scale_pos_weight`; PR-AUC on validation, not accuracy. |
| 5 | Sat 7 Nov | Build and **freeze** the 200-case set + 30 injection cases; commit ids, seeds and script. |
| 6 | Sun 8 Nov | Arm A (ML only) scored on the frozen set: recall @ 50, false positives @ 50. The bar to beat. |
| 7 | Mon 9 Nov | Week review post: what the ML model misses, and why agents might help. |

## Week 2 - One agent, measured (Days 8-14, 10-16 Nov)
| 8 | Tue 10 Nov | Raw Claude API loop: tool use, turn cap, token cap, cost from `usage`. Fake client for offline tests. |
| 9 | Wed 11 Nov | Tool: read-only SQL over DuckDB with a row cap and allow-listed tables. |
| 10 | Thu 12 Nov | Structured finding schema: claim, `tx_id`s, confidence. Validate every output. |
| 11 | Fri 13 Nov | Deterministic verifier: drop claims whose `tx_id`s do not exist or do not involve the account. |
| 12 | Sat 14 Nov | Arm B (single agent) on 20 cases; first cost per case and latency numbers. |
| 13 | Sun 15 Nov | Fix the worst failure from Day 12, with a test. |
| 14 | Mon 16 Nov | Arm B on all 200 cases (Batch API). Post: single agent vs ML, honestly. |

## Week 3 - Many agents (Days 15-21, 17-23 Nov)
| 15 | Tue 17 Nov | Orchestrator: plan the case, spawn sub-agents in parallel, merge findings. |
| 16 | Wed 18 Nov | Pattern agent (SQL) as a sub-agent with its own prompt and budget. |
| 17 | Thu 19 Nov | Per-case budget across agents; stop early when evidence is enough. |
| 18 | Fri 20 Nov | Trace every step (one event per call, tokens, cost, ms) into DuckDB. |
| 19 | Sat 21 Nov | Prompt caching for shared system prompts and schemas; measure the saving. |
| 20 | Sun 22 Nov | Arm C (pattern agent only) vs B on 50 cases. |
| 21 | Mon 23 Nov | Week review: where parallelism helped and where it only cost tokens. |

## Week 4 - Network and sanctions (Days 22-28, 24-30 Nov)
| 22 | Tue 24 Nov | Graph around an account (k-hop, time window) in networkx. |
| 23 | Wed 25 Nov | Typology detectors: fan-in, fan-out, `simple_cycles` with `length_bound`. |
| 24 | Thu 26 Nov | Network agent: reads the detectors' output, names the typology, cites `tx_id`s. |
| 25 | Fri 27 Nov | Typology accuracy against the patterns file. |
| 26 | Sat 28 Nov | Sanctions lists in (UK + OFAC), normalised names, a small fuzzy matcher with tests. |
| 27 | Sun 29 Nov | Sanctions agent on synthetic name matches (the IBM data has no names; stated in every post). |
| 28 | Mon 30 Nov | Full arm C on 200 cases. Post the first three-way table. |

## Week 5 - The analyst's desk (Days 29-35, 1-7 Dec)
| 29 | Tue 1 Dec | Report writer: who, what, when, where, why, how (FinCEN narrative shape), every line cited. |
| 30 | Wed 2 Dec | FastAPI service: start a case, stream every step over SSE. |
| 31 | Thu 3 Dec | Next.js desk: case queue, live trace, findings with clickable `tx_id`s. |
| 32 | Fri 4 Dec | Approve / reject with a reason; decisions logged for evals. |
| 33 | Sat 5 Dec | Analyst agreement: you review 30 cases blind; compare with arm C. |
| 34 | Sun 6 Dec | Replay mode: the demo runs recorded cases at zero model cost. |
| 35 | Mon 7 Dec | Week review + 60-second screen recording for the README. |

## Week 6 - Attack it (Days 36-42, 8-14 Dec)
| 36 | Tue 8 Dec | Run the 30 injection cases on B and C. Publish the failures first. |
| 37 | Wed 9 Dec | Data-labelling of untrusted fields in prompts; re-run. |
| 38 | Thu 10 Dec | Tool-level defences: read-only, row caps, no outbound tool; tests for each. |
| 39 | Fri 11 Dec | Budget attacks: a case built to make agents loop; prove the caps hold. |
| 40 | Sat 12 Dec | Public-demo hardening: rate limits, bot check, daily dollar cap, CSP. |
| 41 | Sun 13 Dec | Deploy API (Railway) + desk (Vercel) in replay mode, then live mode with the cap. |
| 42 | Mon 14 Dec | Security write-up post. |

## Week 7 - Google Cloud and the benchmark (Days 43-49, 15-21 Dec)
| 43 | Tue 15 Dec | Cloud Run deploy of the API from source (time-boxed to two days). |
| 44 | Wed 16 Dec | Claude via Vertex AI behind the same client interface; compare cost and latency. |
| 45 | Thu 17 Dec | **Launch day**: Show HN with the live demo + repo (it must be something people can try). |
| 46 | Fri 18 Dec | Package the frozen cases + injection cases as **Fraud Desk Bench** (reusable, documented). |
| 47 | Sat 19 Dec | Anyone can run their own agent against the bench: one command, one score table. |
| 48 | Sun 20 Dec | Answer issues and feedback from launch; fix the top one. |
| 49 | Mon 21 Dec | Week review. |

## Week 8 - The honest comparison (Days 50-56, 22-28 Dec)
| 50 | Tue 22 Dec | Final runs: arms A, B, C, 3 trials each, Batch API. |
| 51 | Wed 23 Dec | Ablations: C without the network agent, without the verifier, with a larger model. |
| 52 | Thu 24 Dec | Judge against the pass lines in EVALS.md. Write what failed. |
| 53 | Fri 25 Dec | Light day (Christmas): one chart, one paragraph. |
| 54 | Sat 26 Dec | Light day: README results table. |
| 55 | Sun 27 Dec | Optional: the orchestrator ported to the Claude Agent SDK; compare code size and results. |
| 56 | Mon 28 Dec | Write-up draft: "Does a multi-agent desk beat one agent on fraud?" |

## Week 9 - Ship the story (Days 57-60, 29 Dec-1 Jan)
| 57 | Tue 29 Dec | Case study page on aurimas.io. |
| 58 | Wed 30 Dec | Molecule to Machine edition on the project. |
| 59 | Thu 31 Dec | Final clean-up, v1.0.0 release, CITATION and bench docs. |
| 60 | Fri 1 Jan | New Year's Day retrospective post: 60 days, what worked, what did not, what is next. |

## Deliberately cut (from the feasibility check)
- A LangGraph port: the `langgraph-supervisor` library is archived; the Agent SDK comparison (Day 55) is optional.
- An LLM verifier: grounding is checked by code.
- Full OpenSanctions data: non-commercial licence; optional local adapter only.
