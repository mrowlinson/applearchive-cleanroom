# VERIFY-4d27cf1 cport merge w2@8e4f4f2 (python T10PW0..PWQ): PASS

## first-hand (at-commit tree ver-4d27cf1, band22 seat binary)
- delta vs band22: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band22 (cmp SAME), so
  band22 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z27964 zone).
- parity own run: RGRAMC-PYID 1666/1666 covered=1666/1676 =>
  RGRAMC-GREEN. 10 new P32 N correctly UNCOVERED (C sealed
  at T10R30 n<=27872); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-1cc206b); python
  delta is w2-verified content (VERIFY-8e4f4f2 PASS).

## verdict: PASS (merge clean, C parity intact 1666/1666)
