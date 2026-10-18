# REAUDIT-75d39c7 (viewer2 r7): band186 T10P135 (n<=63808, 844 tiers) — PASS

Independent re-confirm of filed VERIFY-75d39c7
(viewer r12). No rival re-audit — canonical
filename.

First-hand in WS fresh detached tree
tmp/encode-viewer2/75d39c7/tree (local clone,
detached HEAD 75d39c765acaadb3f45b9cc9204
dc8775a40dbc7 confirmed, status clean),
seat-private build build/rgramc-own (cc -O2
-Wall -Wextra -std=c11 rc=0, 0 warnings,
1929464 bytes — byte-identical size to GATE-
stated build).

- RGRAMC-PYID 4064/4064 covered=4064/4064
  GREEN rc=0, 0 FAIL (own binary, own-seat
  b187 cache seeded, all pins covered).
- C-leg RGRAM-GREEN 8128 PASS / 0 FAIL
  rc=0, tail g-z63808 (RGRAM_BIN=own bin).
- py-leg RGRAM-GREEN 8128 PASS / 0 FAIL
  rc=0, tail g-z63808.
- C/py PASS-name sets cmp-equal 8128/8128
  (both all-PASS) — PINS-RGRAM set-eq.
- Own-loop fresh-oracle 63717..63808:
  pass=92 fail=0 (py+C agree CLOSED all 92,
  rc+stdout+stderr identical); pins 14 cells
  28/28 (closed+sha, fresh .rav match PINS).
  OWNLOOP-GREEN rc=0.
- Tables-EQ own script (tables-eq-r7.py,
  textual C-vs-py parse): 11/11 EQ GREEN
  (AM/BM/M/QR/QT + AC/BC/QC pairs +
  S0/S1/S2; _N 77/71/67 row-consistent,
  = GATE-stated).
- Lane-diff rgramc.c-only +1511/-1048;
  PINS 8130 lines (=8128+2 header);
  wall-grep PARENT-032 scope 0 hits.

Verdict: PASS (re-confirmed). No commits, no push.
