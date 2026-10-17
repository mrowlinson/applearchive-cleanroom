# VERIFY-7d6c9eb (viewer4 r10): band204 T10P144 (n<=66940, 880 tiers) — PASS

First-hand in fresh WS detached tree
.../verify-7d6c9eb/tree (git archive
7d6c9eb, full SHA 7d6c9eb7cae70d0a294
088ab949022191e6a143d), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
2031832 bytes == GATE byte-identical).
GATE-first satisfied (GATE-7d6c9eb
PASS-functional). CLAIM-viewer4-
7d6c9eb-r10 consumed (claim-check at
claim + pre-filing: no rival).

- PYID (RGRAMC=own r10, corpus 4101
  own-seat hardlinks ex r9 b165 cache
  + 201 fresh-oracle regen, py+C
  freshly executed per pin): RGRAMC-
  PYID 4302/4302 covered=4302/4302,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 8604 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z66940.
- PYBAT (python impl): 8604 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z66940.
- PINS-RGRAM set-eq 8604/8604 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 66849..66940:
  pass=92 fail=0 pins=16 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE reports
  32/32 = 16x2 closed+sha — same 16
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 10/10 EQ (_T10P144AC/BC/QC/AM/
  BM/M/QR/QT/S0/S1); FULL 2398/2398
  0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 3b00b53 (src/c/rgramc.c only,
  +1557/-1109 == GATE, cpat|libcompre
  ssion|depload|dlopen|dylib): 0 hits.
  PINS 8606 lines (8604+2hdr).
  HYGIENE/CONTAM/LIBCOMP inherit
  OBSERVED (none in lane diff; GATE
  leg-diff ZERO vs b202).

VERDICT: PASS (GATE-7d6c9eb stands
confirmed; every leg concurs). No
commits, no push.
