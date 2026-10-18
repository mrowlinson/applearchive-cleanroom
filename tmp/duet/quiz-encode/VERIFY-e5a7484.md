# VERIFY-e5a7484 cport merge w2@875a127 (python T10PO0..POQ): PASS

## first-hand (at-commit tree ver-e5a7484, band10 seat binary)
- delta vs band10: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band10 (cmp SAME), so
  band10 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z25180 zone).
- parity own run: RGRAMC-PYID 1520/1520 covered=1520/1530 =>
  RGRAMC-GREEN. 10 new P24 N correctly UNCOVERED (C sealed
  at T10R22 n<=25088); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-a99d06a); python
  delta is w2-verified content (VERIFY-875a127 PASS).

## verdict: PASS (merge clean, C parity intact 1520/1520)
