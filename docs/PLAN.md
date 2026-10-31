# The 60-day plan

Day 1 = Sun 2 Nov 2026, Day 60 = Wed 31 Dec 2026. About 2-3 hours a day; weekends carry the heavier
days. Every day ends with **one commit, one number, one lesson, one post**. If a day slips, the next day
shrinks scope, never the streak.

Budget: up to **USD 50** of model calls for all 60 days. Small models (Haiku class) do the sub-agent
work, a larger model only where the eval shows it pays. Batch API for eval runs (50% off).

## Week 1 - Data and the bar to beat (Days 1-7, 2-8 Nov)
| Day | Date | Ship |
|---|---|---|
| 1 | Sun 2 Nov | Data in: download HI-Small, Parquet + DuckDB with `tx_id`, profile (rows, 1-in-N laundering, typologies). Post the numbers. |
| 2 | Mon 3 Nov | Chronological 60/20/20 split; leakage test (no test-period row in train). |
| 3 | Tue 4 Nov | Account-level features in SQL (fan-in/out degree, amounts, currencies, formats, velocity). |
| 4 | Wed 5 Nov | XGBoost triage baseline with `scale_pos_weight`; PR-AUC on validation, not accuracy. |
| 5 | Thu 6 Nov | Build and **freeze** the 200-case set + 30 injection cases; commit ids, seeds and script. |
| 6 | Fri 7 Nov | Arm A (ML only) scored on the frozen set: recall @ 50, false positives @ 50. The bar to beat. |
| 7 | Sat 8 Nov | Week review post: what the ML model misses, and why agents might help. |

## Week 2 - One agent, measured (Days 8-14, 9-15 Nov)
| 8 | Sun 9 Nov | Raw Claude API loop: tool use, turn cap, token cap, cost from `usage`. Fake client for offline tests. |
| 9 | Mon 10 Nov | Tool: read-only SQL over DuckDB with a row cap and allow-listed tables. |
| 10 | Tue 11 Nov | Structured finding schema: claim, `tx_id`s, confidence. Validate every output. |
| 11 | Wed 12 Nov | Deterministic verifier: drop claims whose `tx_id`s do not exist or do not involve the account. |
| 12 | Thu 13 Nov | Arm B (single agent) on 20 cases; first cost per case and latency numbers. |
| 13 | Fri 14 Nov | Fix the worst failure from Day 12, with a test. |
| 14 | Sat 15 Nov | Arm B on all 200 cases (Batch API). Post: single agent vs ML, honestly. |

## Week 3 - Many agents (Days 15-21, 16-22 Nov)
| 15 | Sun 16 Nov | Orchestrator: plan the case, spawn sub-agents in parallel, merge findings. |
| 16 | Mon 17 Nov | Pattern agent (SQL) as a sub-agent with its own prompt and budget. |
| 17 | Tue 18 Nov | Per-case budget across agents; stop early when evidence is enough. |
| 18 | Wed 19 Nov | Trace every step (one event per call, tokens, cost, ms) into DuckDB. |
| 19 | Thu 20 Nov | Prompt caching for shared system prompts and schemas; measure the saving. |
| 20 | Fri 21 Nov | Arm C (pattern agent only) vs B on 50 cases. |
| 21 | Sat 22 Nov | Week review: where parallelism helped and where it only cost tokens. |

## Week 4 - Network and sanctions (Days 22-28, 23-29 Nov)
| 22 | Sun 23 Nov | Graph around an account (k-hop, time window) in networkx. |
| 23 | Mon 24 Nov | Typology detectors: fan-in, fan-out, `simple_cycles` with `length_bound`. |
| 24 | Tue 25 Nov | Network agent: reads the detectors' output, names the typology, cites `tx_id`s. |
| 25 | Wed 26 Nov | Typology accuracy against the patterns file. |
| 26 | Thu 27 Nov | Sanctions lists in (UK + OFAC), normalised names, a small fuzzy matcher with tests. |
| 27 | Fri 28 Nov | Sanctions agent on synthetic name matches (the IBM data has no names; stated in every post). |
| 28 | Sat 29 Nov | Full arm C on 200 cases. Post the first three-way table. |

## Week 5 - The analyst's desk (Days 29-35, 30 Nov-6 Dec)
| 29 | Sun 30 Nov | Report writer: who, what, when, where, why, how (FinCEN narrative shape), every line cited. |
| 30 | Mon 1 Dec | FastAPI service: start a case, stream every step over SSE. |
| 31 | Tue 2 Dec | Next.js desk: case queue, live trace, findings with clickable `tx_id`s. |
| 32 | Wed 3 Dec | Approve / reject with a reason; decisions logged for evals. |
| 33 | Thu 4 Dec | Analyst agreement: you review 30 cases blind; compare with arm C. |
| 34 | Fri 5 Dec | Replay mode: the demo runs recorded cases at zero model cost. |
| 35 | Sat 6 Dec | Week review + 60-second screen recording for the README. |

## Week 6 - Attack it (Days 36-42, 7-13 Dec)
| 36 | Sun 7 Dec | Run the 30 injection cases on B and C. Publish the failures first. |
| 37 | Mon 8 Dec | Data-labelling of untrusted fields in prompts; re-run. |
| 38 | Tue 9 Dec | Tool-level defences: read-only, row caps, no outbound tool; tests for each. |
| 39 | Wed 10 Dec | Budget attacks: a case built to make agents loop; prove the caps hold. |
| 40 | Thu 11 Dec | Public-demo hardening: rate limits, bot check, daily dollar cap, CSP. |
| 41 | Fri 12 Dec | Deploy API (Railway) + desk (Vercel) in replay mode, then live mode with the cap. |
| 42 | Sat 13 Dec | Security write-up post. |

## Week 7 - Google Cloud and the benchmark (Days 43-49, 14-20 Dec)
| 43 | Sun 14 Dec | Cloud Run deploy of the API from source (time-boxed to two days). |
| 44 | Mon 15 Dec | Claude via Vertex AI behind the same client interface; compare cost and latency. |
| 45 | Tue 16 Dec | **Launch day**: Show HN with the live demo + repo (it must be something people can try). |
| 46 | Wed 17 Dec | Package the frozen cases + injection cases as **Fraud Desk Bench** (reusable, documented). |
| 47 | Thu 18 Dec | Anyone can run their own agent against the bench: one command, one score table. |
| 48 | Fri 19 Dec | Answer issues and feedback from launch; fix the top one. |
| 49 | Sat 20 Dec | Week review. |

## Week 8 - The honest comparison (Days 50-56, 21-27 Dec)
| 50 | Sun 21 Dec | Final runs: arms A, B, C, 3 trials each, Batch API. |
| 51 | Mon 22 Dec | Ablations: C without the network agent, without the verifier, with a larger model. |
| 52 | Tue 23 Dec | Judge against the pass lines in EVALS.md. Write what failed. |
| 53 | Wed 24 Dec | Optional: the orchestrator ported to the Claude Agent SDK; compare code size and results. |
| 54 | Thu 25 Dec | Light day (Christmas): one chart, one paragraph. |
| 55 | Fri 26 Dec | Light day: README results table. |
| 56 | Sat 27 Dec | Write-up draft: "Does a multi-agent desk beat one agent on fraud?" |

## Week 9 - Ship the story (Days 57-60, 28-31 Dec)
| 57 | Sun 28 Dec | Case study page on aurimas.io. |
| 58 | Mon 29 Dec | Molecule to Machine edition on the project. |
| 59 | Tue 30 Dec | Final clean-up, v1.0.0 release, CITATION and bench docs. |
| 60 | Wed 31 Dec | Retrospective post: 60 days, what worked, what did not, what is next. |

## Deliberately cut (from the feasibility check)
- A LangGraph port: the `langgraph-supervisor` library is archived; the Agent SDK comparison (Day 53) is optional.
- An LLM verifier: grounding is checked by code.
- Full OpenSanctions data: non-commercial licence; optional local adapter only.
