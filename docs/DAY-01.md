# Day 0 and Day 1, step by step

## Day 0 - Sat 1 Nov (set-up, about 1.5 h)
1. **Kaggle token**: kaggle.com -> Settings -> API -> *Create New Token*; move the file:
   `mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json`
2. **Accept the dataset terms** once in the browser: open the IBM AML dataset page on Kaggle and click
   *Download* or accept its licence (the API refuses until you have).
3. **Anthropic spend limit**: console -> Settings -> Limits -> set a monthly limit (USD 25 covers Nov;
   raise to the USD 50 total in Dec). Create a key named `fraud-desk`; keep it in `.env`, never in code.
4. `cd ~/Desktop/Agents_and_Certifications/Agents/Fraud-Desk && make setup && make test`
5. Read the README, docs/PLAN.md and docs/EVALS.md once; change anything you disagree with **today**,
   because EVALS.md locks on Day 5.
6. Create the GitHub repo (public, MIT) and push; pin it on your profile.
7. Post the Day 0 announcement (posts/day-00) on X, Bluesky, Threads and LinkedIn.

## Day 1 - Sun 2 Nov (about 2 h)
1. `make data` - downloads HI-Small_Trans.csv (~500 MB) and HI-Small_Patterns.txt into data/raw/.
2. **Check the real file against the assumptions in the code** (5 minutes, do not skip):
   `head -3 data/raw/HI-Small_Trans.csv` and `head -5 data/raw/HI-Small_Patterns.txt`.
   The loader expects 11 columns with two called "Account", timestamps like `2022/09/01 00:20`, and
   pattern blocks opening with `BEGIN LAUNDERING ATTEMPT - <TYPOLOGY>`. If anything differs, fix the
   fixture in tests/fixtures first, watch the test fail, then fix the loader.
3. `time make db` - note the seconds for the post.
4. `make profile > /tmp/profile.json` and look at it: does the laundering count match the dataset page
   (about 5.1K of 5M)? If not, stop and find out why before posting.
5. `.venv/bin/python scripts/fill_day01.py /tmp/profile.json <seconds>` - fills the three posts.
6. Edit the posts in your own words; check X/Bluesky stays under 290 characters.
7. Commit (`Day 1: data in - IBM AMLworld HI-Small in DuckDB with tx_id`), push, check CI is green.
8. Post. Log the day: one number, one lesson.
