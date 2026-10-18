# VERIFY w2 b759db1 T10R81 (R-zone 45301..45620) — PASS

- py battery first-hand: RGRAM-GREEN, 5486 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-b759db1).
- own-loop fresh-oracle 45301..45620: 320 pass / 0 fail;
  pins 26/26.
- diff parent 1ae2af1: rgram.py +111, PINS +26 (13 cells
  x2), test N-list tail extended thru 45620 only.
- non-vacuous: zone edges 45301/45620 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
