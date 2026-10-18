# VERIFY-4104b6a cport merge w2@c406622 (python T10PV0..PVQ): PASS

## first-hand (at-commit tree ver-4104b6a, band20 seat binary)
- delta vs band20: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band20 (cmp SAME), so
  band20 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z27616 zone).
- parity own run: RGRAMC-PYID 1646/1646 covered=1646/1656 =>
  RGRAMC-GREEN. 10 new P31 N correctly UNCOVERED (C sealed
  at T10R29 n<=27524); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-696bb26); python
  delta is w2-verified content (VERIFY-c406622 PASS).

## verdict: PASS (merge clean, C parity intact 1646/1646)
