# VERIFY-996406e cport merge w2@004a2c2 (python P30+R29): PASS

## first-hand (at-commit tree ver-996406e, band19 seat binary)
- delta vs band19: python side only (rgram.py, test list,
  PINS +36: P30 +10N, R29 +8N). C source byte-identical to
  band19 (cmp SAME), so band19 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z27524 zone).
- parity own run: RGRAMC-PYID 1628/1628 covered=1628/1646 =>
  RGRAMC-GREEN. 18 new N correctly UNCOVERED (C sealed at
  T10R28 n<=27176); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-a55b78c); python
  delta is w2-verified content (VERIFY-5874e49 + VERIFY-004a2c2).

## verdict: PASS (merge clean, C parity intact 1628/1628)
