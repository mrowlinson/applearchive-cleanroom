# VERIFY w2 3a0891e T10R78 (R-zone 44257..44576) — PASS

- py battery first-hand: RGRAM-GREEN, 5348 PASS / 0 FAIL/MISS
  (3 runs: tail GREEN + count + fail-grep empty).
- own-loop fresh-oracle 44257..44576: 320 pass / 0 fail;
  pins 26/26.
- diff parent 7a14d14: rgram.py +117, PINS +26, test N-list
  only (R78 boundary probes appended, no logic change).
- non-vacuous: zone edges 44257/44576 probed closed +
  sha-pinned; T10R78 geometry matches A-50 answers.
- lane py-only (no src/c): no C leg, no wall-grep scope.
