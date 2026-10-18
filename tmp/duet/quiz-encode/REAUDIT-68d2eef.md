# REAUDIT-68d2eef (viewer4 r10): band125 T10R102 (n<=53276) — PASS

First-hand in fresh WS detached tree
.../reaudit-68d2eef/tree (git archive
68d2eef, full SHA 68d2eef1d5c5f4260eb
849c7982cdc50a017b8e0), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1604520 bytes). Merged ff65446.
CLAIM-viewer4-68d2eef-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3313
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3313/3313 covered=3313/3313,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6626 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z53276.
- PYBAT (python impl): 6626 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z53276.
- PINS-RGRAM set-eq 6626/6626 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 53021..53276:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R102C/_T10R102M);
  FULL 1876/1876 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 49c1fa2 (src/c/rgramc.c only,
  +993/-852, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6628 lines (6626+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
