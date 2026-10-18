# REAUDIT-9e30e0b: band123 T10R101 (n<=52928, 718 tiers) — PASS

First-hand re-battery by encode-viewer4-r12
in fresh WS detached tree .../r12/reaudit-
9e30e0b/tree (git archive 9e30e0b, full SHA
9e30e0bf3bf839ff0649db8df6cb8dd2ac00ad96),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1587672 bytes == VERIFY).

- PYID (RGRAMC=own r12, corpus 3288 own-
  seat hardlinks ex r11 cbat .rav cache,
  py+C freshly executed per pin):
  RGRAMC-PYID 3288/3288 covered=3288/3288,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r12, fresh oracle):
  6576 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z52928.
- PYBAT (python impl, fresh oracle): 6576
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z52928.
- PINS-RGRAM set-eq 6576/6576 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 52673..52928:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE/VERIFY
  report 26/26 = 13x2 closed+sha — same
  13 cells, pinfail=0.)
- Tables-EQ own script r12: NEW 2/2 EQ
  (_T10R101C/M); FULL 1864/1864 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs cb0ab6f (src/c/rgramc.c only,
  +987/-846 == GATE, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME cb0ab6f. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
