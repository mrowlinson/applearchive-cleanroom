# VERIFY w2 2ebec70 T10R80 (R-zone 44953..45272) — PASS

- py battery first-hand: RGRAM-GREEN, 5440 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-2ebec70).
- own-loop fresh-oracle 44953..45272: 320 pass / 0 fail;
  pins 26/26.
- diff parent 0e56f23: rgram.py +111, PINS +26 (13 cells
  x2), test N-list tail extended thru 45272 only.
- non-vacuous: zone edges 44953/45272 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
