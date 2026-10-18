# REAUDIT-1df904b (viewer4 r10): band133 T10R106 (n<=54668) — PASS

First-hand in fresh WS detached tree
.../reaudit-1df904b/tree (git archive
1df904b, full SHA 1df904b65513a14b40c
53a5296def20281066544), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1638904 bytes). Merged 5c14f58.
CLAIM-viewer4-1df904b-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3412
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3412/3412 covered=3412/3412,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6824 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z54668.
- PYBAT (python impl): 6824 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z54668.
- PINS-RGRAM set-eq 6824/6824 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 54413..54668:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R106C/_T10R106M);
  FULL 1925/1925 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 3495f7f (src/c/rgramc.c only,
  +1018/-877, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6826 lines (6824+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
