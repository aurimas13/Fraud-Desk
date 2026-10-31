100 Days With AI ended on 19 October. Tomorrow a new one starts, shorter and harder: 60 days, one project.

🔎 Fraud Desk: a multi-agent fraud and AML investigation desk, built in public from 2 November to 31 December.

How it will work:
(1) A machine-learning model triages 5 million synthetic transactions.
(2) An orchestrator on the raw Claude API sends agents to investigate in parallel: transaction patterns in SQL, the network of linked accounts (fan-in, fan-out, cycles), sanctions screening.
(3) Code, not another model, rejects any finding that does not cite the transactions it rests on.
(4) A report is drafted in the shape investigators file: who, what, when, where, why, how.
(5) A person approves or rejects every case.

Why bother? Anthropic reported its multi-agent research system beat a single agent by 90.2% on an internal eval, at about 15 times the tokens of a chat. Fraud work is parallel by nature. Does the gain survive a cost-per-case budget on labelled data? I will publish the answer either way: ML only vs one agent vs many agents, with recall, false positives, cost, latency and prompt-injection resistance. Losses included.

Rules: evals before agents. A person decides. Untrusted data stays data.

One commit and one post a day. Follow along, and tell me what you would test.

🔗 https://github.com/aurimas13/Fraud-Desk

#AI #AIAgents #FraudPrevention #AML #BuildInPublic

🤝 AI collaboration note: built with Claude Code as a pair. I choose what to build, review every change, run the evals and take responsibility for the result. Full note in the repo README.
