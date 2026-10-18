# VERIFY-c875d8e cport merge w2@1821f18 (python T10R24): PASS

## first-hand (at-commit tree ver-c875d8e, band12 seat binary)
- delta vs band12: python side only (rgram.py, test list,
  PINS +16). C source byte-identical to band12 (cmp SAME), so
  band12 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z25784 zone).
- parity own run: RGRAMC-PYID 1548/1548 covered=1548/1556 =>
  RGRAMC-GREEN. 8 new R24 N correctly UNCOVERED (C sealed
  at T10PPQ n<=25528); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-834c297); python
  delta is w2-verified content (VERIFY-1821f18 PASS).

## verdict: PASS (merge clean, C parity intact 1548/1548)
