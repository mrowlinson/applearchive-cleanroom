# VERIFY w2 1ae2af1 T10P82 (P-zone 45273..45300) — PASS

- py battery first-hand: RGRAM-GREEN, 5460 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-1ae2af1).
- own-loop fresh-oracle 45273..45300: 28 pass / 0 fail;
  pins 20/20.
- diff parent 2ebec70: rgram.py +104, PINS +20 (10 cells
  x2), test N-list tail extended thru 45300 only.
- non-vacuous: zone edges 45273/45300 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
