# VERIFY w2 ed8d830 T10P84 (P-zone 45969..45996) — PASS

- py battery first-hand: RGRAM-GREEN, 5552 PASS / 0 FAIL
  (fresh oracle, rc=0, at-commit tree v-ed8d830).
- own-loop fresh-oracle 45969..45996: 28 pass / 0 fail;
  pins 20/20.
- diff parent fd558ad: rgram.py +104, PINS +20 (10 cells
  x2), test N-list tail extended thru 45996 only.
- non-vacuous: zone edges 45969/45996 probed closed +
  sha-pinned.
- lane py-only (no src/c): no C leg, no wall-grep scope.
