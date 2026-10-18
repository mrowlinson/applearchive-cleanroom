# VERIFY-0303b7a cport merge w2@55dcb98 (python T10P400..P40Q): PASS

## first-hand (at-commit tree ver-0303b7a, band35 seat binary)
- delta vs band35: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band35 (cmp SAME), so
  band35 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z30748 zone).
- parity own run: RGRAMC-PYID 1826/1826 covered=1826/1836 =>
  RGRAMC-GREEN. 10 new P40 N correctly UNCOVERED (C sealed
  at T10R38 n<=30656); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-8bd65c3); python
  delta is w2-verified content (VERIFY-55dcb98 PASS).

## verdict: PASS (merge clean, C parity intact 1826/1826)
