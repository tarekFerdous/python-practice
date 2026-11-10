# Notes

- Deadline: test possibly within a week of 2026-11-01. Compressed path, highest-yield first:
  1 hash maps → 2 strings + sliding window / two pointers → 3 stacks, deque, heapq → 4 data wrangling (logs/JSON/CSV)
  → 5 classes (LRU cache, rate limiter, retry) → 6 AI tasks (chunking, cosine top-k, LLM JSON, asyncio) → 7 BFS/DFS + binary search → 8 timed mock.
- **Own repo, worked in Google Colab** (2026-11-10): workspace moved out of job-search to `D:\gitHub Repos\python-practice`, public at github.com/tarekFerdous/python-practice. The user does the exercises in Colab for portability, so notebooks must be self-contained: the setup cell inlines the `check` helper (copy of `assets/nbcheck.py`), no local imports, no files outside the notebook. Title cell has an Open-in-Colab badge; lessons link to `https://colab.research.google.com/github/tarekFerdous/python-practice/blob/main/exercises/NNNN-name/exercises.ipynb`. Push new notebooks before pointing the user at them. Colab edits are saved to Drive unless the user does File > Save a copy in GitHub; to see their latest code, ask them to do that (or paste it).
- **Exercises are Jupyter notebooks** (user's request 2026-11-09, applies to all future lessons): `exercises/NNNN-name/exercises.ipynb`. Layout: setup cell (inlined `check` helper, see above), then per exercise a markdown heading, a function cell, and a `check(fn, [(args, expected), ...])` cell that prints PASS/FAIL with got vs expected. Teacher `*_v2` versions go in a section at the bottom, each with its own check cell. Lessons 1-3 were converted with a builder script; the old `exercises.py`/`test_exercises.py` remain but the notebook is the source of truth. To "run the tests" for the user, execute the notebook with nbclient without saving it (ipykernel, nbclient and nbformat were installed 2026-11-09).
- Pytest is still a skill to practise (MISSION): write test functions in a notebook cell when a lesson covers it.
- Start each lesson with a 2-minute retrieval warm-up from earlier lessons (spacing + interleaving).
- Practise with AI autocomplete OFF. Give hints, not answers, unless asked.
- Python 3.13.7 and pytest 9.1.1 are installed.
- User prefers plain explanations, "what it is / how it's used / one line to say in the interview" style (from the prep-glossary sessions).
- After Lesson 1 (2026-11-02): ask for time AND space every time; he misses sort costs. He wanted the teacher's idiomatic versions added to the exercise file after solving (`*_v2` functions); keep doing that once tests pass.
- He asks "can you run the test?" — run the notebook checks for him and report, but leave the fixes to him (hints first).
- After Lesson 2 (2026-11-05): the variable sliding window needed the full answer; re-drill it in a later warm-up. Lesson 2 now has a pair_with_sum test that fails until he fixes `right += 1` (Lesson 3 warm-up).
