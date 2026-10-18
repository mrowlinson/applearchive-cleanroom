# VERIFY-c440e04 cport merge w2@0f16b53 (python T10PY0..PYQ): PASS

## first-hand (at-commit tree ver-c440e04, band25 seat binary)
- delta vs band25: python side only (rgram.py, test list,
  PINS +20). C source byte-identical to band25 (cmp SAME), so
  band25 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z28660 zone).
- parity own run: RGRAMC-PYID 1706/1706 covered=1706/1716 =>
  RGRAMC-GREEN. 10 new P34 N correctly UNCOVERED (C sealed
  at T10R32 n<=28568); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-d3247df); python
  delta is w2-verified content (VERIFY-0f16b53 PASS).

## verdict: PASS (merge clean, C parity intact 1706/1706)
