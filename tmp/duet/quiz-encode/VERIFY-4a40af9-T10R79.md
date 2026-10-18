# VERIFY w2 4a40af9 T10R79 (R-zone 44605..44924) — PASS

- py battery first-hand: RGRAM-GREEN, 5394 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-4a40af9).
- own-loop fresh-oracle 44605..44924: 320 pass / 0 fail;
  pins 26/26.
- diff parent 9740232: rgram.py +112, PINS +26 (13 cells
  x2), test N-list tail extended thru 44924 only.
- non-vacuous: zone edges 44605/44924 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
