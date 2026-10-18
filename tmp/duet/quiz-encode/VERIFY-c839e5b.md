# VERIFY-c839e5b cport merge w2@9783bf5 (python R23+P25): PASS

## first-hand (at-commit tree ver-c839e5b, band11 seat binary)
- delta vs band11: python side only (rgram.py, test list,
  PINS +36: R23 +8N, P25 +10N). C source byte-identical to
  band11 (cmp SAME), so band11 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z25528 zone).
- parity own run: RGRAMC-PYID 1530/1530 covered=1530/1548 =>
  RGRAMC-GREEN. 18 new N correctly UNCOVERED (C sealed at
  T10POQ n<=25180); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-a0adca4); python
  delta is w2-verified content (VERIFY-d3afa19 + VERIFY-9783bf5).

## verdict: PASS (merge clean, C parity intact 1530/1530)
