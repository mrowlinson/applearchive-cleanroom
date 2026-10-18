# VERIFY w2 bd42dc0 T10P83 (P-zone 45621..45648) — PASS

- py battery first-hand: RGRAM-GREEN, 5506 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-bd42dc0).
- own-loop fresh-oracle 45621..45648: 28 pass / 0 fail;
  pins 20/20.
- diff parent b759db1: rgram.py +104, PINS +20 (10 cells
  x2), test N-list tail extended thru 45648 only.
- non-vacuous: zone edges 45621/45648 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
