.PHONY: setup data db profile test lint

setup:            ## create .venv and install dev + data extras
	uv venv --python 3.13 && uv pip install -e ".[dev,data]"

data:             ## download IBM AML HI-Small from Kaggle (needs ~/.kaggle/kaggle.json)
	bash scripts/download_data.sh

db:               ## raw CSV + patterns -> data/processed/{transactions.parquet,fraud_desk.duckdb}
	.venv/bin/fraud-desk build-db

profile:          ## print the numbers for today's post
	.venv/bin/fraud-desk profile

test:
	.venv/bin/pytest -q

lint:
	.venv/bin/ruff check . && .venv/bin/ruff format --check .
