# VERIFY w2 fd558ad T10R82 (R-zone 45649..45968) — PASS

- py battery first-hand: RGRAM-GREEN, 5532 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-fd558ad).
- own-loop fresh-oracle 45649..45968: 320 pass / 0 fail;
  pins 26/26.
- diff parent bd42dc0: rgram.py +111, PINS +26 (13 cells
  x2), test N-list tail extended thru 45968 only.
- non-vacuous: zone edges 45649/45968 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
