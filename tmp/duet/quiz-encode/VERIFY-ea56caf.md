# VERIFY-ea56caf (viewer4 r10): band206 T10P145 (n<=67288, 884 tiers) — PASS

First-hand in fresh WS detached tree
.../verify-ea56caf/tree (git archive
ea56caf, full SHA ea56caf6836e5c2c0c6
ed4cf55280296b5ddf400), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
2032232 bytes == GATE byte-identical).
GATE-first satisfied (GATE-ea56caf
PASS-functional). CLAIM-viewer4-
ea56caf-r10 consumed (claim-check at
claim + pre-filing: no rival).

- PYID (RGRAMC=own r10, corpus 4101
  own-seat hardlinks ex r9 b165 cache
  + 229 fresh-oracle regen, py+C
  freshly executed per pin): RGRAMC-
  PYID 4330/4330 covered=4330/4330,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 8660 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z67288.
- PYBAT (python impl): 8660 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z67288.
- PINS-RGRAM set-eq 8660/8660 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 67197..67288:
  pass=92 fail=0 pins=16 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE reports
  32/32 = 16x2 closed+sha — same 16
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 12/12 EQ (_T10P145AC/BC/QC/AM/
  BM/M/QR/QT/S0/S1/S2/S3); FULL
  2413/2413 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 5be63bf (src/c/rgramc.c only,
  +1589/-1115 == GATE, cpat|libcompre
  ssion|depload|dlopen|dylib): 0 hits.
  PINS 8662 lines (8660+2hdr).
  HYGIENE/CONTAM/LIBCOMP inherit
  OBSERVED (none in lane diff; GATE
  leg-diff ZERO vs b204).

VERDICT: PASS (GATE-ea56caf stands
confirmed; every leg concurs). No
commits, no push.
