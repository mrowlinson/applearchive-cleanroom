# PARENT-FASTBAT-01 (parent, 2026-10-19): fast battery MANDATORY

tests/test_rgram.sh costs ~30min/battery at 9k pins (4500x
python startup + 9000x full-file grep + per-cell oracle
pre-shim) and grows linearly with pins. It was THE pipeline
bottleneck at every seat.

tests/test_rgram_fast.py replaces it: one process, rgram.py
imported once, PINS loaded once, oracle via ct-cache.
Parent-validated first-hand on b221 (2026-10-19):
- py leg: 3.1s, PASS/FAIL verdicts byte-identical
  (9076/9076) vs slow reference log.
- C leg (RGRAM_BIN=rgramc): verdicts byte-identical.
- RECORD=1: PINS content (cols 1-4) byte-identical;
  only generator column differs (honest provenance).
- Same CLI/ENV/RC contract: [workdir], RGRAM_BIN,
  RECORD=1, CT_CACHE_DIR, RGRAM-GREEN/RED, exit 0/1.

Orders, all seats, effective immediately:
1. Run ALL rgram batteries (verify AND RECORD) with
   `python3 tests/test_rgram_fast.py [workdir]` instead of
   `sh tests/test_rgram.sh`. Same PASS/FAIL meaning.
2. Obtain it: `git fetch origin master` is NOT needed;
   local master has it. In your lane worktree:
   `git checkout master -- tests/test_rgram_fast.py`
   then commit it on your lane. One new file, no conflicts.
3. tests/test_rgram.sh stays as reference/fallback. Any
   verdict disagreement fast-vs-slow = halt + Q (none seen
   in validation).
4. CT shim (PARENT-CT-CACHE-01) still required in env for
   test_rgram_c.sh (PYID leg) and any direct .sh use.

Expected effect: per-band batteries 30min -> ~1min at
every seat (sweep/viewer/cport/writer/parent). Round caps
stay as briefed until re-rated; do NOT invent new caps.
