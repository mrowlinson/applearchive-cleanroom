# VERIFY w2 0e56f23 T10P81 (P-zone 44925..44952) — PASS

- py battery first-hand: RGRAM-GREEN, 5414 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-0e56f23).
- own-loop fresh-oracle 44925..44952: 28 pass / 0 fail;
  pins 20/20.
- diff parent 4a40af9: rgram.py +104, PINS +20 (10 cells
  x2), test N-list tail extended thru 44952 only.
- non-vacuous: zone edges 44925/44952 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
