# VERIFY-0af5482 cport merge w2@64d23ac (python T10PN0..PNQ): PASS

## first-hand (at-commit tree ver-0af5482, band8 seat binary)
- delta vs band8: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band8 (cmp SAME), so
  band8 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z24832 zone).
- parity own run: RGRAMC-PYID 1502/1502 covered=1502/1512 =>
  RGRAMC-GREEN. 10 new P23 N correctly UNCOVERED (C sealed
  at T10R21 n<=24740); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-b6a42aa); python
  delta is w2-verified content (VERIFY-64d23ac PASS).

## verdict: PASS (merge clean, C parity intact 1502/1502)
