# VERIFY-3ada400 cport merge w2@b689490 (python P33+R32): PASS

## first-hand (at-commit tree ver-3ada400, band24 seat binary)
- delta vs band24: python side only (rgram.py, test list,
  PINS +40: P33 +10N, R32 +10N). C source byte-identical to
  band24 (cmp SAME), so band24 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z28568 zone).
- parity own run: RGRAMC-PYID 1686/1686 covered=1686/1706 =>
  RGRAMC-GREEN. 20 new N correctly UNCOVERED (C sealed at
  T10R31 n<=28220); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-9f87a07); python
  delta is w2-verified content (VERIFY-8da8428 + VERIFY-b689490).

## verdict: PASS (merge clean, C parity intact 1686/1686)
