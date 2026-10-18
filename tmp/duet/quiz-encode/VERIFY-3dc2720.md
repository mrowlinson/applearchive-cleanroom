# VERIFY-3dc2720 cport merge w2@1912c73 (python T10R31): PASS

## first-hand (at-commit tree ver-3dc2720, band23 seat binary)
- delta vs band23: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band23 (cmp
  SAME), so band23 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z28220 zone).
- parity own run: RGRAMC-PYID 1676/1676 covered=1676/1686 =>
  RGRAMC-GREEN. 10 new R31 N correctly UNCOVERED (C sealed
  at T10PWQ n<=27964); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-336a303); python
  delta is w2-verified content (VERIFY-1912c73 PASS).

## verdict: PASS (merge clean, C parity intact 1676/1676)
