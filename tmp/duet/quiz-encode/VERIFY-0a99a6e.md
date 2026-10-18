# VERIFY-0a99a6e cport merge w2@b1f4334 (python T10R37): PASS

## first-hand (at-commit tree ver-0a99a6e, band32 seat binary)
- delta vs band32: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band32 (cmp
  SAME), so band32 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z30308 zone).
- parity own run: RGRAMC-PYID 1796/1796 covered=1796/1806 =>
  RGRAMC-GREEN. 10 new R37 N correctly UNCOVERED (C sealed
  at T10P38Q n<=30052); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-b14a45b); python
  delta is w2-verified content (VERIFY-b1f4334 PASS).

## verdict: PASS (merge clean, C parity intact 1796/1796)
