# VERIFY-a2070eb cport merge w2@c108d1e (python T10P360..P36Q): PASS

## first-hand (at-commit tree ver-a2070eb, band28 seat binary)
- delta vs band28: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band28 (cmp SAME), so
  band28 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z29356 zone).
- parity own run: RGRAMC-PYID 1746/1746 covered=1746/1756 =>
  RGRAMC-GREEN. 10 new P36 N correctly UNCOVERED (C sealed
  at T10R34 n<=29264); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-0d8c629); python
  delta is w2-verified content (VERIFY-c108d1e PASS).

## verdict: PASS (merge clean, C parity intact 1746/1746)
