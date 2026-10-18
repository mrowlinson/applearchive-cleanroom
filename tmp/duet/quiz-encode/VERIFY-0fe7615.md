# VERIFY-0fe7615 cport merge w2@f43ec6a (python T10P370..P37Q): PASS

## first-hand (at-commit tree ver-0fe7615, band30 seat binary)
- delta vs band30: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band30 (cmp SAME), so
  band30 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z29704 zone).
- parity own run: RGRAMC-PYID 1766/1766 covered=1766/1776 =>
  RGRAMC-GREEN. 10 new P37 N correctly UNCOVERED (C sealed
  at T10R35 n<=29612); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-1de982e); python
  delta is w2-verified content (VERIFY-f43ec6a PASS).

## verdict: PASS (merge clean, C parity intact 1766/1766)
