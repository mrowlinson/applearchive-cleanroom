# VERIFY-20363af cport merge w2@1492d3a (python T10PS0..PSQ): PASS

## first-hand (at-commit tree ver-20363af, band16 seat binary)
- delta vs band16: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band16 (cmp SAME), so
  band16 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z26572 zone).
- parity own run: RGRAMC-PYID 1592/1592 covered=1592/1602 =>
  RGRAMC-GREEN. 10 new P28 N correctly UNCOVERED (C sealed
  at T10R26 n<=26480); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-4ad7a4d); python
  delta is w2-verified content (VERIFY-1492d3a PASS).

## verdict: PASS (merge clean, C parity intact 1592/1592)
