# VERIFY-f145c51 cport merge w2@f949df5 (python T10PM0..PMQ): PASS

## first-hand (at-commit tree ver-f145c51, band6 seat binary)
- delta vs band6: python side only (rgram.py +165, test list,
  PINS +20). C source byte-identical to band6 (cmp SAME), so
  band6 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail PASS g-z24484-closed, PASS g-z24484).
- parity own run: RGRAMC-PYID 1484/1484 covered=1484/1494 =>
  RGRAMC-GREEN. 10 new P22 N correctly UNCOVERED (C sealed
  at T10R20 n<=24392); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-e64e2da); python
  delta is w2-verified content (VERIFY-f949df5 PASS).

## verdict: PASS (merge clean, C parity intact 1484/1484)
