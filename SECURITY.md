# Security model

Fraud Desk reads data written by the people it investigates. Every field of a transaction is
**untrusted content**, never instructions.

- **The lethal trifecta** (private data + untrusted content + a way to send data out) is broken by
  design: agents have no tool that sends anything outside the desk, and the SQL tool opens DuckDB
  **read-only** ([Willison, 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)).
- **Prompt injection** ([OWASP LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)):
  untrusted fields are wrapped and labelled as data in every prompt, and 30 frozen injection cases are
  part of the eval set (see docs/EVALS.md).
- **Grounding is enforced by code**: a finding whose `tx_id`s do not exist is dropped before a
  person sees it.
- **A person approves every case.** No agent can close, clear or escalate on its own.
- **Spend is capped**: per-case token and turn limits, a daily dollar budget on the public demo.
- Secrets live in environment variables; CI runs gitleaks on every push.

Found a problem? Open an issue, or for anything sensitive email aurimas.nausedas@proton.me.
