#!/usr/bin/env bash
# Download the IBM AML HI-Small files from Kaggle into data/raw/.
# Needs a Kaggle account and an API token in ~/.kaggle/kaggle.json
# Auth, any one of: `.venv/bin/kaggle auth login` (browser), KAGGLE_API_TOKEN env var,
# ~/.kaggle/access_token, or a legacy ~/.kaggle/kaggle.json (kaggle.com/settings/api).
# Accept the dataset terms once on its Kaggle page first, or the download is refused.
# Licence of the data: CDLA-Sharing 1.0. It is never committed to this repo.
set -euo pipefail
KAGGLE="${KAGGLE:-.venv/bin/kaggle}"
[[ -x "$KAGGLE" ]] || KAGGLE=kaggle
DATASET="ealtman2019/ibm-transactions-for-anti-money-laundering-aml"
mkdir -p data/raw
for f in HI-Small_Trans.csv HI-Small_Patterns.txt; do
  if [[ -s "data/raw/$f" ]]; then echo "have $f"; continue; fi
  "$KAGGLE" datasets download "$DATASET" -f "$f" -p data/raw
  # Kaggle zips single files that are large; unzip when it did.
  if [[ -f "data/raw/$f.zip" ]]; then unzip -o "data/raw/$f.zip" -d data/raw && rm "data/raw/$f.zip"; fi
done
ls -lh data/raw
