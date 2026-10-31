# Sources this project leans on

Every link below was fetched and checked on 31 Oct 2026. "Unverified" means the page could not be
fetched; treat it as a lead only.

## Data
- IBM AMLworld on Kaggle (CDLA-Sharing 1.0; HI-Small: 5M transactions, 515K accounts, ~5.1K laundering;
  chronological 60/20/20 split recommended):
  https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
- Altman et al., *Realistic Synthetic Financial Transactions for Anti-Money Laundering Models*
  (NeurIPS 2023): https://arxiv.org/abs/2306.16424 (8 typologies: fan-out, fan-in, cycle, random,
  bipartite, stack, scatter-gather, gather-scatter)
- IBM AMLSim, the simulator behind it (Apache-2.0): https://github.com/IBM/AMLSim
- Rejected: PaySim (no network typologies, https://www.kaggle.com/datasets/ealaxi/paysim1);
  SAML-D (non-commercial licence, https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml)

## Sanctions lists
- UK Sanctions List (CSV/XML, Open Government Licence v3.0):
  https://www.gov.uk/government/publications/the-uk-sanctions-list
- OFAC SDN list: https://ofac.treasury.gov/sanctions-list-service (licence statement unverified)
- OpenSanctions is CC BY-NC 4.0 (https://www.opensanctions.org/licensing/); kept as an optional,
  off-by-default local adapter via yente (MIT): https://github.com/opensanctions/yente

## Agents and evals (Anthropic)
- Building effective AI agents (Dec 2024): https://www.anthropic.com/engineering/building-effective-agents
- How we built our multi-agent research system (Jun 2025; multi-agent +90.2% vs single agent on an
  internal eval; ~15x chat tokens; token usage explains 80% of variance):
  https://www.anthropic.com/engineering/multi-agent-research-system
- Demystifying evals for AI agents (Jan 2026): https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Tool use: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- Prompt caching: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Batch API (50% off): https://platform.claude.com/docs/en/build-with-claude/batch-processing
- Pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Models: https://platform.claude.com/docs/en/about-claude/models/overview
- Claude Agent SDK (Python): https://code.claude.com/docs/en/agent-sdk/python ;
  subagents: https://code.claude.com/docs/en/agent-sdk/subagents
- Cookbook patterns (orchestrator-workers, async multi-agent, evaluator-optimizer):
  https://github.com/anthropics/claude-cookbooks (folder `patterns/agents/`)
- Claude on Google Cloud (Vertex): https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed

## ML, graphs, tracing, deploy
- XGBoost `scale_pos_weight` for imbalance: https://xgboost.readthedocs.io/en/stable/parameter.html
- networkx `simple_cycles` (set `length_bound` on big graphs):
  https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cycles.simple_cycles.html
- Langfuse self-hosting: https://langfuse.com/self-hosting
- OpenTelemetry GenAI conventions: https://github.com/open-telemetry/semantic-conventions-genai
- Cloud Run FastAPI quickstart: https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-fastapi-service
- Cloud Run pricing and free tier: https://cloud.google.com/run/pricing

## Security
- OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- Simon Willison, The lethal trifecta (Jun 2025): https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- AgentDojo benchmark: https://github.com/ethz-spylab/agentdojo

## Domain
- FinCEN SAR narrative guidance (who, what, when, where, why, how; concise and chronological):
  https://www.fincen.gov/system/files/shared/sarnarrcompletguidfinal_112003.pdf
- FATF money-laundering indicators (unverified, 403):
  https://www.fatf-gafi.org/en/publications/Methodsandtrends/Money-laundering-terrorist-financing-indicators.html

## Courses to lean on
- Anthropic Academy (Building with the Claude API, MCP, Claude Code in Action): https://anthropic.skilljar.com/
- Anthropic courses repo: https://github.com/anthropics/courses
- DeepLearning.AI, Evaluating AI Agents: https://www.deeplearning.ai/courses/evaluating-ai-agents
- DeepLearning.AI, AI Agents in LangGraph: https://www.deeplearning.ai/courses/ai-agents-in-langgraph
- DeepLearning.AI, Multi AI Agent Systems with crewAI: https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai

## Reality check on stars (GitHub API, 31 Oct 2026)
Open-source agentic fraud/AML repos mostly sit under 50 stars (ojuri 10, multi-agent-fraud-detection 8);
reusable artefacts do better (IBM/Multi-GNN 125, AgentDojo 970, checkmarble/marble 618). Hence the plan
to publish the frozen case set and injection cases as a reusable benchmark.
