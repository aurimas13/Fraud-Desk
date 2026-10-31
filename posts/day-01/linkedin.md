Day 1 of 60: Fraud Desk.

Today was not about agents. It was about the data the agents will stand on.

📦 {N_TX} synthetic transactions between {N_ACCOUNTS} accounts (IBM's AMLworld HI-Small set, NeurIPS 2023), loaded into DuckDB in {LOAD_SECONDS} seconds.
🏷️ Each transaction got a tx_id. Later, every claim an agent makes must cite one, and code will throw out any claim that does not.
⚖️ Only 1 in {ONE_IN} transactions is laundering. A model that answers "clean" every time is {ACC_ALL_CLEAN}% accurate and catches nothing. So accuracy will not appear in this project; recall within an analyst's budget will.
🧩 The patterns file names each laundering attempt: {TOP_TYPOLOGIES}. That is the ground truth the network agent will be judged on.

Two traps in the raw file, both silent:
(1) Two columns are both called "Account" (sender and receiver).
(2) Bank codes and account ids look like numbers but are not: leading zeros and hex digits.
Read it the default way and you lose data without an error. Tests now pin both.

Tomorrow: a chronological train / validation / test split, and a test that proves no future transaction leaks into training.

🔗 https://github.com/aurimas13/Fraud-Desk

#AI #AML #FraudPrevention #DataEngineering #BuildInPublic

🤝 AI collaboration note: built with Claude Code as a pair. I choose what to build, review every change, run the evals and take responsibility for the result. Full note in the repo README.
