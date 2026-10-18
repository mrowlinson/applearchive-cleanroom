# VERIFY-f3d0773 cport merge w2@4b30e1e (python T10PQ0..PQQ): PASS

## first-hand (at-commit tree ver-f3d0773, band13 seat binary)
- delta vs band13: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band13 (cmp SAME), so
  band13 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z25876 zone).
- parity own run: RGRAMC-PYID 1556/1556 covered=1556/1566 =>
  RGRAMC-GREEN. 10 new P26 N correctly UNCOVERED (C sealed
  at T10R24 n<=25784); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-02b44b4); python
  delta is w2-verified content (VERIFY-4b30e1e PASS).

## verdict: PASS (merge clean, C parity intact 1556/1556)
