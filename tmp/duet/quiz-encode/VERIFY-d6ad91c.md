# VERIFY-d6ad91c cport merge w2@85fe578 (python T10R22): PASS

## first-hand (at-commit tree ver-d6ad91c, band9 seat binary)
- delta vs band9: python side only (rgram.py, test list,
  PINS +16). C source byte-identical to band9 (cmp SAME), so
  band9 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z25088 zone).
- parity own run: RGRAMC-PYID 1512/1512 covered=1512/1520 =>
  RGRAMC-GREEN. 8 new R22 N correctly UNCOVERED (C sealed
  at T10PNQ n<=24832); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-84c84e1); python
  delta is w2-verified content (VERIFY-85fe578 PASS).

## verdict: PASS (merge clean, C parity intact 1512/1512)
