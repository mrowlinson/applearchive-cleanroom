# VERIFY-10eb4bb cport merge w2@f67973d (python T10R21): PASS

## first-hand (at-commit tree ver-10eb4bb, band7 seat binary)
- delta vs band7: python side only (rgram.py +45, test list,
  PINS +16). C source byte-identical to band7 (cmp SAME), so
  band7 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z24740 zone).
- parity own run: RGRAMC-PYID 1494/1494 covered=1494/1502 =>
  RGRAMC-GREEN. 8 new R21 N correctly UNCOVERED (C sealed
  at T10PMQ n<=24484); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-9d7d20c); python
  delta is w2-verified content (VERIFY-f67973d PASS).

## verdict: PASS (merge clean, C parity intact 1494/1494)
