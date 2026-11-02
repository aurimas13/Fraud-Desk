# Contributing to Fraud Desk

Fraud Desk is a 60-day build in public (#60DaysOfAgents, 2 Nov - 31 Dec 2026). The daily build is a
one-person streak, but the parts that make the result trustworthy are where outside help counts most.

## The most useful contributions

1. **Attack cases.** Try to make an agent clear a laundering account, cite a `tx_id` that does not
   exist, leak its prompt or burn its budget. Open an
   [attack case](https://github.com/aurimas13/Fraud-Desk/issues/new?template=attack-case.yml).
   Accepted cases are credited in the README Hall of Fame.
2. **Test and eval ideas.** A metric that is easy to game, a failure mode nobody is measuring, a case
   the frozen set should have had. Open a
   [test idea](https://github.com/aurimas13/Fraud-Desk/issues/new?template=test-idea.yml).
3. **Bug reports.** Something does not run as the README says. Open a
   [bug report](https://github.com/aurimas13/Fraud-Desk/issues/new?template=bug.yml).

Small pull requests (a test, a doc fix, a clearer error message) are welcome at any time. Large feature
pull requests may be held until after Day 60 so the daily plan stays honest; open an issue first.

## Ground rules

- **Synthetic data only.** No real people, accounts or transactions, in code, tests or issues.
- **The data is never committed.** IBM AMLworld is CDLA-Sharing 1.0 and is downloaded by script.
- **No secrets.** CI runs gitleaks on every push and pull request.
- **The frozen eval does not move silently.** The case set and pass lines lock on Day 6. Any change is
  logged in [docs/EVALS.md](docs/EVALS.md) with a reason.
- **Untrusted data stays data.** Any new tool or prompt must keep transaction fields labelled as data,
  never instructions (see [SECURITY.md](SECURITY.md)).

## Local setup

```bash
make setup   # create .venv and install dev + data extras
make test    # offline: no API key, no dataset needed
make lint    # ruff check + format check
```

Before opening a pull request, `make test` and `make lint` should both pass. The
[pull request template](.github/pull_request_template.md) has the short checklist.

## Style

- Python 3.12+, formatted and linted with ruff (line length 120).
- British spelling in docs and comments. Plain hyphens, not em dashes.
- If an AI tool helped write your change, say which one in the pull request. This project is built with
  Claude Code and says so; see the [AI collaboration note](README.md#-ai-collaboration).

## Conduct

Everyone taking part is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
