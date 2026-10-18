# VERIFY-fd60f19 cport merge w2@4c5b869 (python T10R28): PASS

## first-hand (at-commit tree ver-fd60f19, band18 seat binary)
- delta vs band18: python side only (rgram.py, test list,
  PINS +16). C source byte-identical to band18 (cmp SAME), so
  band18 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z27176 zone).
- parity own run: RGRAMC-PYID 1620/1620 covered=1620/1628 =>
  RGRAMC-GREEN. 8 new R28 N correctly UNCOVERED (C sealed
  at T10PTQ n<=26920); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-77f7545); python
  delta is w2-verified content (VERIFY-4c5b869 PASS).

## verdict: PASS (merge clean, C parity intact 1620/1620)
