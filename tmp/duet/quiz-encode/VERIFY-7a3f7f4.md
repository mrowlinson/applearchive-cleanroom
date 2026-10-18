# VERIFY-7a3f7f4 cport merge w2@f03ca3b (python T10R26): PASS

## first-hand (at-commit tree ver-7a3f7f4, band15 seat binary)
- delta vs band15: python side only (rgram.py, test list,
  PINS +16). C source byte-identical to band15 (cmp SAME), so
  band15 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z26480 zone).
- parity own run: RGRAMC-PYID 1584/1584 covered=1584/1592 =>
  RGRAMC-GREEN. 8 new R26 N correctly UNCOVERED (C sealed
  at T10PRQ n<=26224); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-55494eb); python
  delta is w2-verified content (VERIFY-f03ca3b PASS).

## verdict: PASS (merge clean, C parity intact 1584/1584)
