# VERIFY-d9730c2 cport merge w2@58da85a (python R25+P27): PASS

## first-hand (at-commit tree ver-d9730c2, band14 seat binary)
- delta vs band14: python side only (rgram.py, test list,
  PINS +36: R25 +8N, P27 +10N). C source byte-identical to
  band14 (cmp SAME), so band14 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z26224 zone).
- parity own run: RGRAMC-PYID 1566/1566 covered=1566/1584 =>
  RGRAMC-GREEN. 18 new N correctly UNCOVERED (C sealed at
  T10PQQ n<=25876); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-ff3ef8a); python
  delta is w2-verified content (VERIFY-11cfc70 + VERIFY-58da85a).

## verdict: PASS (merge clean, C parity intact 1566/1566)
