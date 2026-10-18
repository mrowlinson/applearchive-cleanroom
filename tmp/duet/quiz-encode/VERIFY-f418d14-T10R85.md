# VERIFY w2 f418d14 T10R85 (R-zone 46693..47012) — PASS

- py battery first-hand: RGRAM-GREEN, 5670 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-f418d14).
- own-loop fresh-oracle 46693..47012: 320 pass / 0 fail;
  pins 26/26.
- diff parent fa795dd: rgram.py +111, PINS +26 (13 cells
  x2), test N-list tail extended thru 47012 only.
- non-vacuous: zone edges 46693/47012 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
