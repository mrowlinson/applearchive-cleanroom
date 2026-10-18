# REAUDIT-2205fa1 (viewer3 r8): band173 T10R126 (n<=61628, 818 tiers) — PASS

Interim re-confirm of filed VERIFY-2205fa1
(viewer3 r1) during turf-starved wait (no
GATE-but-no-VERIFY band: b188 GATE pending +
live viewer-r12 VERIFY-claim per PARENT-070;
v2 on b186/b185, v4 on b179). Filed VERIFY
stands regardless. Full first-hand re-battery
in WS detached tree tmp/encode-viewer3/2205fa1/
tree (HEAD 2205fa1 confirmed, status clean),
seat-private build build/rgramc-r8 (cc -O2
-Wall -Wextra -std=c11 rc=0, 0 warnings,
1844360 bytes == r1 size), NVME TMPDIR, all
legs fresh r8 in -r8 workdirs.

- RGRAMC-PYID 3902/3902 covered=3902/3902
  GREEN rc=0 (own-seat corpus seed 7804
  files, py+C freshly executed per pin,
  0 FAIL).
- C-leg RGRAM-GREEN 7804 PASS / 0 FAIL rc=0
  (RGRAM_BIN=own r8, fresh oracle).
- py-leg RGRAM-GREEN 7804 PASS / 0 FAIL rc=0
  (fresh oracle).
- PINS-RGRAM set-eq 7804/7804 (C/py PASS-name
  sets cmp-identical; csv 7806 lines = 7804
  g-z rows + 2 header, both legs all-PASS).
- own-loop fresh-oracle 61373..61628: 256/0
  pins 24/24, OWN-GREEN rc=0 (== GATE).
- Tables-EQ own script v3: NEW 3/3 EQ
  (_T10R126C/_T10R126M/_T10R126QH); FULL
  2184/2184 0-skip 0-mismatch. Consistent
  with GATE's M+QH str n=16 + C 2D n=68 +
  C_N derived split.
- Wall-grep PARENT-032 scope on band diff vs
  2205fa1^ (src/c/rgramc.c only, +1167/-1006
  == GATE): 0 hits. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

Verdict: PASS (re-confirmed). No commits, no push.
