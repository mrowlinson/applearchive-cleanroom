# VERIFY-968244b cport merge w2@f6dfa38 (python T10R38): PASS

## first-hand (at-commit tree ver-968244b, band34 seat binary)
- delta vs band34: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band34 (cmp
  SAME), so band34 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z30656 zone).
- parity own run: RGRAMC-PYID 1816/1816 covered=1816/1826 =>
  RGRAMC-GREEN. 10 new R38 N correctly UNCOVERED (C sealed
  at T10P39Q n<=30400); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-745afe2); python
  delta is w2-verified content (VERIFY-f6dfa38 PASS).

## verdict: PASS (merge clean, C parity intact 1816/1816)
