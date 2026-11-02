# Day 0 and Day 1, step by step

## Day 0 - Mon 2 Nov (set-up, about 1.5 h)
1. **Kaggle token**: kaggle.com -> Settings -> API -> *Create New Token*; move the file:
   `mkdir -p ~/.kaggle && mv ~/Downloads/kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json`
2. **Accept the dataset terms** once in the browser: open the IBM AML dataset page on Kaggle and click
   *Download* or accept its licence (the API refuses until you have).
3. **Anthropic spend limit**: console -> Settings -> Limits -> set a monthly limit (USD 25 covers Nov;
   raise to the USD 50 total in Dec). Create a key named `fraud-desk`; keep it in `.env`, never in code.
4. `cd ~/Desktop/Brain/programming-channel/Process/fraud-desk && make setup && make test`
5. Read the README, docs/PLAN.md and docs/EVALS.md once; change anything you disagree with **today**,
   because EVALS.md locks on Day 5.
6. **Download the data today** so tomorrow is not blocked: `make data`, then step 2 of Day 1 below.
   The repo already exists (github.com/aurimas13/Fraud-Desk); pin it on your GitHub profile.
7. Post the Day 0 announcement (posts/day-00) on X, Bluesky, Threads and LinkedIn.

## Day 1 - Tue 3 Nov (about 2 h, finish by 21:00)
06:50 the launch post goes out on X and Bluesky automatically; at ~07:00 paste the LinkedIn launch
post (Gmail draft "Fraud Desk LAUNCH - LinkedIn") and the Threads text by hand.

1. `make data` if you did not finish it yesterday (HI-Small_Trans.csv ~500 MB + HI-Small_Patterns.txt).
2. **Check the real file against the code's assumptions** (5 minutes, do not skip):
   `head -3 data/raw/HI-Small_Trans.csv` and `head -5 data/raw/HI-Small_Patterns.txt`.
   Expected: 11 columns with two called "Account", timestamps like `2022/09/01 00:20`, pattern blocks
   opening with `BEGIN LAUNDERING ATTEMPT - <TYPOLOGY>`. If anything differs: fix the fixture in
   tests/fixtures first, watch the test fail, then fix the loader.
3. `time make db` - note the seconds.
4. `make profile > /tmp/profile.json` and read it: about 5.1K laundering of 5M? If not, stop and find out
   why before posting anything.
5. Commit and push your code (`Day 1: data in - HI-Small in DuckDB with tx_id`); check CI is green.
6. **Write the day note before 21:00**: copy `Inputs/fraud-desk/notes/TEMPLATE.md` (in the Brain
   programming-channel) to `Inputs/fraud-desk/notes/2026-11-03.md` and fill in: shipped, ONE number
   (e.g. rows, laundering ratio, build seconds), ONE lesson.
7. Done. At 21:00 the prep job turns your commits + note into the Day 1 posts, logs the day in the
   README, and leaves the LinkedIn draft in Gmail. Wed 4 Nov 06:50 it posts; you paste LinkedIn at 07:00.
   Late? Commit + write the note before 05:00 and the catch-up run builds it.

The same rhythm holds for all 60 days: **build, commit, note by 21:00.**
