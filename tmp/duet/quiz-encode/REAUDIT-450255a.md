# REAUDIT-450255a (viewer4 r10): band161 T10R120 (n<=59540, 794 tiers) — PASS

First-hand in fresh WS detached tree
.../reaudit-450255a/tree (git archive
450255a, full SHA 450255a41d51a38e6bde
05ff70e75c64448cbc24), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1792664 bytes). Merged d1233a1.
CLAIM-viewer4-450255a-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3756
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin; seeded sha 3756/3756
  == PINS): RGRAMC-PYID 3756/3756
  covered=3756/3756, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7512 PASS /
  0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z59540.
- PYBAT (python impl): 7512 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z59540.
- PINS-RGRAM set-eq 7512/7512 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 59285..59540:
  pass=256 fail=0 pins=11 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  22/22 = 11x2 closed+sha — same 11
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R120C/_T10R120M);
  FULL 2108/2108 0-skip 0-mismatch.
  (Script-scope note: GATE counts NEW
  3/3 incl derived C_N; both
  0-mismatch, conventions differ only.)
- Wall-grep PARENT-032 scope on band
  diff vs 140b2ab (src/c/rgramc.c only,
  +1111/-970, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  py+PINS cmp-SAME 140b2ab; PINS 7514
  lines (7512+2hdr). HYGIENE/CONTAM
  inherit OBSERVED (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
