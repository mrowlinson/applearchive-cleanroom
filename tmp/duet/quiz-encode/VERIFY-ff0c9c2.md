# VERIFY-ff0c9c2 (viewer4 r10): band200 T10P142 (n<=66244, 872 tiers) — PASS

First-hand in fresh WS detached tree
.../verify-ff0c9c2/tree (git archive
ff0c9c2, full SHA ff0c9c2806a3c89fe1c9
f074cc6b11e66a3b5221), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
2014632 bytes == GATE byte-identical).
GATE-first satisfied (GATE-ff0c9c2
PASS-functional). CLAIM-viewer4-
ff0c9c2-r10 consumed (claim-check at
claim + pre-filing: no rival).

- PYID (RGRAMC=own r10, corpus 4101
  own-seat hardlinks ex r9 b165 cache
  + 145 fresh-oracle regen, py+C
  freshly executed per pin): RGRAMC-
  PYID 4246/4246 covered=4246/4246,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 8492 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z66244.
- PYBAT (python impl): 8492 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z66244.
- PINS-RGRAM set-eq 8492/8492 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 66153..66244:
  pass=92 fail=0 pins=14 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE reports
  28/28 = 14x2 closed+sha — same 14
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 11/11 EQ (_T10P142AC/BC/QC/AM/
  BM/M/QR/QT/S0/S1/S2); FULL 2371/
  2371 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 14531bb (src/c/rgramc.c only,
  +1556/-1095 == GATE, cpat|libcompre
  ssion|depload|dlopen|dylib): 0 hits.
  PINS 8494 lines (8492+2hdr).
  HYGIENE/CONTAM/LIBCOMP inherit
  OBSERVED (none in lane diff; GATE
  leg-diff IDENTICAL vs b198).

VERDICT: PASS (GATE-ff0c9c2 stands
confirmed; every leg concurs). No
commits, no push.
