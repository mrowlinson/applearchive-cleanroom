# VERIFY w2 e0b4455 T10R83 (R-zone 45997..46316) — PASS

- py battery first-hand: RGRAM-GREEN, 5578 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-e0b4455).
- own-loop fresh-oracle 45997..46316: 320 pass / 0 fail;
  pins 26/26.
- diff parent ed8d830: rgram.py +112, PINS +26 (13 cells
  x2), test N-list tail extended thru 46316 only.
- non-vacuous: zone edges 45997/46316 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
