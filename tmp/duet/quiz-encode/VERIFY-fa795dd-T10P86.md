# VERIFY w2 fa795dd T10P86 (P-zone 46665..46692) — PASS

- py battery first-hand: RGRAM-GREEN, 5644 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-fa795dd).
- own-loop fresh-oracle 46665..46692: 28 pass / 0 fail;
  pins 20/20.
- diff parent 7d215eb: rgram.py +104, PINS +20 (10 cells
  x2), test N-list tail extended thru 46692 only.
- non-vacuous: zone edges 46665/46692 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
