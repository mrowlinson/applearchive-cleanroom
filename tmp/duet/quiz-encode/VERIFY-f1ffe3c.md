# VERIFY-f1ffe3c cport merge w2@8e0d740 (python T10R30): PASS

## first-hand (at-commit tree ver-f1ffe3c, band21 seat binary)
- delta vs band21: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band21 (cmp
  SAME), so band21 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z27872 zone).
- parity own run: RGRAMC-PYID 1656/1656 covered=1656/1666 =>
  RGRAMC-GREEN. 10 new R30 N correctly UNCOVERED (C sealed
  at T10PVQ n<=27616); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-6b87eaf); python
  delta is w2-verified content (VERIFY-8e0d740 PASS).

## verdict: PASS (merge clean, C parity intact 1656/1656)
