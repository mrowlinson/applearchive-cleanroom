# VERIFY w2 7d215eb T10R84 (R-zone 46345..46664) — PASS

- py battery first-hand: RGRAM-GREEN, 5624 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-7d215eb).
- own-loop fresh-oracle 46345..46664: 320 pass / 0 fail;
  pins 26/26.
- diff parent 7781f12: rgram.py +121, PINS +26 (13 cells
  x2), test N-list tail extended thru 46664 only.
- non-vacuous: zone edges 46345/46664 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
