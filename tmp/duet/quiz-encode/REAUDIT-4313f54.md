# REAUDIT-4313f54 (viewer3 r8): band171 T10R125 (n<=61280, 814 tiers) — PASS

Interim re-confirm of filed VERIFY-4313f54
during turf-starved wait (b188 closed b189
VERIFY-claimed viewer2; PARENT-070 yields).
Filed VERIFY stands regardless. Full
first-hand re-battery in fresh WS detached
tree tmp/encode-viewer3/4313f54/tree (HEAD
4313f54 confirmed, status clean), seat-private
build build/rgramc-r8 (cc -O2 -Wall -Wextra
-std=c11 rc=0, 0 warnings, 1843896 bytes),
NVME TMPDIR, all legs fresh r8.

- RGRAMC-PYID 3877/3877 covered=3877/3877
  GREEN rc=0 (own-seat corpus seed 7804
  files, py+C freshly executed per pin,
  0 FAIL).
- C-leg RGRAM-GREEN 7754 PASS / 0 FAIL rc=0
  (RGRAM_BIN=own r8, fresh oracle).
- py-leg RGRAM-GREEN 7754 PASS / 0 FAIL rc=0
  (fresh oracle).
- PINS-RGRAM set-eq 7754/7754 (C/py PASS-name
  sets cmp-identical; csv 7756 lines = 7754
  g-z rows + 2 header, both legs all-PASS).
- own-loop fresh-oracle 61025..61280: 256/0
  pins 24/24, OWN-GREEN rc=0 (== GATE).
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R125C/_T10R125M); FULL 2169/2169
  0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff vs
  4313f54^ (src/c/rgramc.c only, +1141/-1000
  == GATE): 0 hits. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
