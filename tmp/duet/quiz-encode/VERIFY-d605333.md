# VERIFY-d605333 cport merge w2@1b1e2f3 (python R36+P38): PASS

## first-hand (at-commit tree ver-d605333, band31 seat binary)
- delta vs band31: python side only (rgram.py, test list,
  PINS +40: R36 +10N, P38 +10N). C source byte-identical to
  band31 (cmp SAME), so band31 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z30052 zone).
- parity own run: RGRAMC-PYID 1776/1776 covered=1776/1796 =>
  RGRAMC-GREEN. 20 new N correctly UNCOVERED (C sealed at
  T10P37Q n<=29704); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-f21727f); python
  delta is w2-verified content (VERIFY-34f853f + VERIFY-1b1e2f3).

## verdict: PASS (merge clean, C parity intact 1776/1776)
