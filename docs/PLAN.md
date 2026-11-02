# The 60-day plan

Day 1 = Mon 2 Nov 2026, Day 60 = Thu 31 Dec 2026 (renumbered on 2 Nov). Each day's post goes out at 06:50 EET the next morning, so Day 1 posts Tue 3 Nov and Day 60 posts on New Year's Day. About 2-3 hours a day; weekends carry the heavier
days. Every day ends with **one commit, one number, one lesson, one post**. If a day slips, the next day
shrinks scope, never the streak.

Budget: up to **USD 50** of model calls for all 60 days. Small models (Haiku class) do the sub-agent
work, a larger model only where the eval shows it pays. Batch API for eval runs (50% off).

## Week 1 - Data and the bar to beat (Days 1-8, 2-9 Nov)
| Day | Date | Ship |
|---|---|---|
| 1 | Mon 2 Nov | Foundation (done): repo, IBM AMLworld loader with a stable `tx_id` (4 offline tests), 60-day plan, eval spec, CI. Launch post. |
| 2 | Tue 3 Nov | Data in: download HI-Small, Parquet + DuckDB with `tx_id`, profile (rows, 1-in-N laundering, typologies). Post the numbers. |
| 3 | Wed 4 Nov | Chronological 60/20/20 split; leakage test (no test-period row in train). |
| 4 | Thu 5 Nov | Account-level features in SQL (fan-in/out degree, amounts, currencies, formats, velocity). |
| 5 | Fri 6 Nov | XGBoost triage baseline with `scale_pos_weight`; PR-AUC on validation, not accuracy. |
| 6 | Sat 7 Nov | Build and **freeze** the 200-case set + 30 injection cases; commit ids, seeds and script. |
| 7 | Sun 8 Nov | Arm A (ML only) scored on the frozen set: recall @ 50, false positives @ 50. The bar to beat. |
| 8 | Mon 9 Nov | Week review post: what the ML model misses, and why agents might help. |

## Week 2 - One agent, measured (Days 9-15, 10-16 Nov)
| 9 | Tue 10 Nov | Raw Claude API loop: tool use, turn cap, token cap, cost from `usage`. Fake client for offline tests. |
| 10 | Wed 11 Nov | Tool: read-only SQL over DuckDB with a row cap and allow-listed tables. |
| 11 | Thu 12 Nov | Structured finding schema: claim, `tx_id`s, confidence. Validate every output. |
| 12 | Fri 13 Nov | Deterministic verifier: drop claims whose `tx_id`s do not exist or do not involve the account. |
| 13 | Sat 14 Nov | Arm B (single agent) on 20 cases; first cost per case and latency numbers. |
| 14 | Sun 15 Nov | Fix the worst failure from Day 13, with a test. |
| 15 | Mon 16 Nov | Arm B on all 200 cases (Batch API). Post: single agent vs ML, honestly. |

## Week 3 - Many agents (Days 16-22, 17-23 Nov)
| 16 | Tue 17 Nov | Orchestrator: plan the case, spawn sub-agents in parallel, merge findings. |
| 17 | Wed 18 Nov | Pattern agent (SQL) as a sub-agent with its own prompt and budget. |
| 18 | Thu 19 Nov | Per-case budget across agents; stop early when evidence is enough. |
| 19 | Fri 20 Nov | Trace every step (one event per call, tokens, cost, ms) into DuckDB. |
| 20 | Sat 21 Nov | Prompt caching for shared system prompts and schemas; measure the saving. |
| 21 | Sun 22 Nov | Arm C (pattern agent only) vs B on 50 cases. |
| 22 | Mon 23 Nov | Week review: where parallelism helped and where it only cost tokens. |

## Week 4 - Network and sanctions (Days 23-29, 24-30 Nov)
| 23 | Tue 24 Nov | Graph around an account (k-hop, time window) in networkx. |
| 24 | Wed 25 Nov | Typology detectors: fan-in, fan-out, `simple_cycles` with `length_bound`. |
| 25 | Thu 26 Nov | Network agent: reads the detectors' output, names the typology, cites `tx_id`s. |
| 26 | Fri 27 Nov | Typology accuracy against the patterns file. |
| 27 | Sat 28 Nov | Sanctions lists in (UK + OFAC), normalised names, a small fuzzy matcher with tests. |
| 28 | Sun 29 Nov | Sanctions agent on synthetic name matches (the IBM data has no names; stated in every post). |
| 29 | Mon 30 Nov | Full arm C on 200 cases. Post the first three-way table. |

## Week 5 - The analyst's desk (Days 30-36, 1-7 Dec)
| 30 | Tue 1 Dec | Report writer: who, what, when, where, why, how (FinCEN narrative shape), every line cited. |
| 31 | Wed 2 Dec | FastAPI service: start a case, stream every step over SSE. |
| 32 | Thu 3 Dec | Next.js desk: case queue, live trace, findings with clickable `tx_id`s. |
| 33 | Fri 4 Dec | Approve / reject with a reason; decisions logged for evals. |
| 34 | Sat 5 Dec | Analyst agreement: you review 30 cases blind; compare with arm C. |
| 35 | Sun 6 Dec | Replay mode: the demo runs recorded cases at zero model cost. |
| 36 | Mon 7 Dec | Week review + 60-second screen recording for the README. |

## Week 6 - Attack it (Days 37-43, 8-14 Dec)
| 37 | Tue 8 Dec | Run the 30 injection cases on B and C. Publish the failures first. |
| 38 | Wed 9 Dec | Data-labelling of untrusted fields in prompts; re-run. |
| 39 | Thu 10 Dec | Tool-level defences: read-only, row caps, no outbound tool; tests for each. |
| 40 | Fri 11 Dec | Budget attacks: a case built to make agents loop; prove the caps hold. |
| 41 | Sat 12 Dec | Public-demo hardening: rate limits, bot check, daily dollar cap, CSP. |
| 42 | Sun 13 Dec | Deploy API (Railway) + desk (Vercel) in replay mode, then live mode with the cap. |
| 43 | Mon 14 Dec | Security write-up post. |

## Week 7 - Google Cloud and the benchmark (Days 44-50, 15-21 Dec)
| 44 | Tue 15 Dec | Cloud Run deploy of the API from source (time-boxed to two days). |
| 45 | Wed 16 Dec | Claude via Vertex AI behind the same client interface; compare cost and latency. |
| 46 | Thu 17 Dec | **Launch day**: Show HN with the live demo + repo (it must be something people can try). |
| 47 | Fri 18 Dec | Package the frozen cases + injection cases as **Fraud Desk Bench** (reusable, documented). |
| 48 | Sat 19 Dec | Anyone can run their own agent against the bench: one command, one score table. |
| 49 | Sun 20 Dec | Answer issues and feedback from launch; fix the top one. |
| 50 | Mon 21 Dec | Week review. |

## Week 8 - The honest comparison (Days 51-57, 22-28 Dec)
| 51 | Tue 22 Dec | Final runs: arms A, B, C, 3 trials each, Batch API. |
| 52 | Wed 23 Dec | Ablations: C without the network agent, without the verifier, with a larger model. |
| 53 | Thu 24 Dec | Judge against the pass lines in EVALS.md. Write what failed. |
| 54 | Fri 25 Dec | Light day (Christmas): one chart, one paragraph. |
| 55 | Sat 26 Dec | Light day: README results table. |
| 56 | Sun 27 Dec | Optional: the orchestrator ported to the Claude Agent SDK; compare code size and results. |
| 57 | Mon 28 Dec | Write-up draft: "Does a multi-agent desk beat one agent on fraud?" |

## Week 9 - Ship the story (Days 58-60, 29-31 Dec)
| 58 | Tue 29 Dec | Case study page on aurimas.io. |
| 59 | Wed 30 Dec | Molecule to Machine edition on the project. |
| 60 | Thu 31 Dec | Final clean-up, v1.0.0 release, CITATION and bench docs; retrospective (60 days, what worked, what did not, what is next) posted on New Year's Day. |

## Deliberately cut (from the feasibility check)
- A LangGraph port: the `langgraph-supervisor` library is archived; the Agent SDK comparison (Day 56) is optional.
- An LLM verifier: grounding is checked by code.
- Full OpenSanctions data: non-commercial licence; optional local adapter only.
