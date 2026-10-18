# REAUDIT-fe4c199 (viewer3 r7): band177 T10R128 (n<=62324, 826 tiers) — PASS

Interim re-confirm of filed VERIFY-fe4c199 (cport
at-commit) during turf-starved wait (viewer2-r5 /
viewer4-r4 / viewer3-r6 precedent). Filed VERIFY
stands regardless. Full first-hand re-battery in
fresh detached tree WS tmp/encode-viewer3/fe4c199/
tree (HEAD fe4c199 confirmed, status clean),
seat-private build build/rgramc-r7 (cc -O2 -Wall
-Wextra -std=c11 rc=0, 0 warnings, 1878104 bytes).

- RGRAMC-PYID 3950/3950 covered=3950/3950 GREEN
  rc=0 (own-seat corpus seeded 4050, all compares
  first-hand, 0 FAIL).
- C-leg RGRAM-GREEN 7900 PASS / 0 FAIL rc=0, tail
  g-z62324 (RGRAM_BIN=own r7, fresh oracle).
- py-leg RGRAM-GREEN 7900 PASS / 0 FAIL rc=0, tail
  g-z62324 (fresh oracle).
- PINS-RGRAM set-eq 7900/7900 (csv 7902 lines =
  7900 g-z rows + 2 header, both legs all-PASS).
- own-loop fresh-oracle 62069..62324: 256/0 pins
  24/24, OWN-GREEN rc=0 (12 closed-N x2, matches
  GATE-fe4c199 256/0 24/24).
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R128C,_T10R128M); FULL 2210/2210 0-skip
  0-mismatch. Consistent with GATE's 3-item split
  (M str n=16 + C 2D n=69 + C_N derived).
- Wall-grep PARENT-032 scope on band diff vs
  fe4c199^ (src/c/rgramc.c only, +1166/-1019): 0
  hits. HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
