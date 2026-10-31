Day 1/60 of Fraud Desk.

Data in: {N_TX} synthetic transactions between {N_ACCOUNTS} accounts (IBM AMLworld, HI-Small), loaded into DuckDB. Every transaction gets a tx_id, because every finding an agent makes later must cite one.

The number that matters: only 1 in {ONE_IN} transactions is laundering. Accuracy is useless at that ratio; a model that says "clean" every time scores {ACC_ALL_CLEAN}%.

Lesson: the raw CSV has two columns both called "Account", and bank codes have leading zeros. Read by header with default types and both break silently.

🔗 github.com/aurimas13/Fraud-Desk

🤝 Researched and drafted with Claude Code. Every story is chosen, edited, and approved by me. Full note on the GitHub repo.
