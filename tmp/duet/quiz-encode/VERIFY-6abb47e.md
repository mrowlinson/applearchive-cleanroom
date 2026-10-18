# VERIFY-6abb47e cport merge w2@965f4dd (python T10R35): PASS

## first-hand (at-commit tree ver-6abb47e, band29 seat binary)
- delta vs band29: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band29 (cmp
  SAME), so band29 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z29612 zone).
- parity own run: RGRAMC-PYID 1756/1756 covered=1756/1766 =>
  RGRAMC-GREEN. 10 new R35 N correctly UNCOVERED (C sealed
  at T10P36Q n<=29356); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-81c73cb); python
  delta is w2-verified content (VERIFY-965f4dd PASS).

## verdict: PASS (merge clean, C parity intact 1756/1756)
