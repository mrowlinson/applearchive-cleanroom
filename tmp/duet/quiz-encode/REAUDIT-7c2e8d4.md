# REAUDIT-7c2e8d4 (viewer2 r7): band185 T10R132 (n<=63716, 842 tiers) — PASS

Independent re-confirm of filed VERIFY-7c2e8d4
(viewer3). No rival re-audit — canonical
filename.

First-hand in WS fresh detached tree
tmp/encode-viewer2/7c2e8d4/tree (local clone,
detached HEAD 7c2e8d4c88bc8dfd56a8ffdeecdd
045f65b1631d confirmed, status clean),
seat-private build build/rgramc-own (cc -O2
-Wall -Wextra -std=c11 rc=0, 0 warnings,
1912632 bytes).

- RGRAMC-PYID 4050/4050 covered=4050/4050
  GREEN rc=0, 0 FAIL (own binary, own-seat
  b187 cache seeded, all pins covered).
- C-leg RGRAM-GREEN 8100 PASS / 0 FAIL
  rc=0, tail g-z63716 (RGRAM_BIN=own bin).
- py-leg RGRAM-GREEN 8100 PASS / 0 FAIL
  rc=0, tail g-z63716.
- C/py PASS-name sets cmp-equal 8100/8100
  (both all-PASS) — PINS-RGRAM set-eq.
- Own-loop fresh-oracle 63461..63716:
  pass=256 fail=0 (py+C agree CLOSED all
  256, rc+stdout+stderr identical); pins
  12 cells 24/24 (closed+sha, fresh .rav
  match PINS). OWNLOOP-GREEN rc=0.
- Tables-EQ own script (tables-eq-r7.py,
  textual C-vs-py parse): 2/2 EQ GREEN
  (M 16/16 + C 66/66 pairs; C_N=66
  row-consistent).
- Lane-diff rgramc.c-only +1188/-1047
  (= GATE-stated); PINS 8102 lines
  (=8100+2 header); wall-grep PARENT-032
  scope 0 hits.

Verdict: PASS (re-confirmed). No commits, no push.
