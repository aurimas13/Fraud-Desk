# Getting started: tonight (Mon 2 Nov) and Day 2 (Tue 3 Nov)

Numbering: **Day 1 = Mon 2 Nov** (the foundation already in this repo); Day N's post goes out at 06:50 EET
the next morning, so Day 1 posts Tue 3 Nov and Day 60 (Thu 31 Dec) posts on New Year's Day.

## Tonight - Mon 2 Nov (about 1 h)
1. **Kaggle account and token.** Sign in at kaggle.com, then pick the easiest of these:
   - **Browser login (simplest):** `cd ~/Desktop/Brain/programming-channel/Process/fraud-desk && make setup && .venv/bin/kaggle auth login`
     and approve in the browser.
   - **Token:** https://www.kaggle.com/settings/api, then **API**, then **Generate New Token**. Save the token
     to `~/.kaggle/access_token` (`mkdir -p ~/.kaggle && chmod 700 ~/.kaggle`, paste the token into the file
     with your editor, then `chmod 600 ~/.kaggle/access_token`).
   - **Legacy:** on the same page, **Create Legacy API Key** gives `kaggle.json`. Move it to
     `~/.kaggle/kaggle.json` and `chmod 600` it.
   Never paste the token into a chat or commit it.
2. **Accept the dataset terms once:** open
   https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml and click
   **Download**, or accept the licence prompt. Until you do, the API refuses the download (403).
3. **Download now, so tomorrow is not blocked:** `make data` (about 500 MB). Then
   `ls -lh data/raw` should show `HI-Small_Trans.csv` and `HI-Small_Patterns.txt`.
   - **If it fails:** a 401 means the token is wrong or missing (redo step 1). A 403 means the terms
     are not accepted yet (redo step 2).
   - **Last resort:** on the dataset page's **Data Explorer**, download just those two files by hand into
     `data/raw/`. The loader does not care how they arrived.
4. **Anthropic:** the monthly spend limit you set is already a hard cap; requests are refused once it
   is reached. Also add an **email notification at USD 10**, and create a key named `fraud-desk` kept
   only in `.env` (gitignored).
5. **Hacker News:** create an account today (news.ycombinator.com). Make a few genuine comments over the
   coming weeks, so the account is six weeks old with some karma by the Show HN post (Thu 17 Dec).

## Day 2 - Tue 3 Nov (about 2 h, finish by 21:00)
At 06:50 the Day 1 launch post goes out on X and Bluesky (and Threads, if its API works by then). At
~07:00, paste the LinkedIn post from the Gmail draft "Fraud Desk LAUNCH". Then:

1. **Check the real file against the code's assumptions** (5 minutes, do not skip):
   `head -3 data/raw/HI-Small_Trans.csv` and `head -5 data/raw/HI-Small_Patterns.txt`.
   Expected: 11 columns with two called "Account", timestamps like `2022/09/01 00:20`, and pattern blocks
   opening with `BEGIN LAUNDERING ATTEMPT - <TYPOLOGY>`. If anything differs, fix the fixture in
   tests/fixtures first, watch the test fail, then fix the loader.
2. `time make db` and note the seconds.
3. `make profile > /tmp/profile.json` and read it. Is it about 5.1K laundering of 5M? If not, stop and
   find out why before anything is posted.
4. Commit and push your code (`Day 2: data in - HI-Small in DuckDB with tx_id`) and check CI is green.
5. **Write the day note before 21:00.** Copy `Inputs/fraud-desk/notes/TEMPLATE.md` (in the Brain
   programming-channel) to `Inputs/fraud-desk/notes/2026-11-03.md` and fill in:
   - what shipped;
   - ONE number (rows, laundering ratio or build seconds);
   - ONE lesson.
6. That's it. At 21:00 the prep job turns your commits and note into the Day 2 posts, logs the day in
   the README and leaves the LinkedIn draft in Gmail. Wed 4 Nov at 06:50 the posts go out.

The rhythm for all 60 days: **build, commit, push, note by 21:00.** Running late? Finish before going to
bed: the 05:00 catch-up builds the day if the Mac is awake then.
