# VERIFY-59cbad2 cport merge w2@3dd5f7b (python R33+P35): PASS

## first-hand (at-commit tree ver-59cbad2, band26 seat binary)
- delta vs band26: python side only (rgram.py, test list,
  PINS +40: R33 +10N, P35 +10N). C source byte-identical to
  band26 (cmp SAME), so band26 seat binary reused for parity.
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z29008 zone).
- parity own run: RGRAMC-PYID 1716/1716 covered=1716/1736 =>
  RGRAMC-GREEN. 20 new N correctly UNCOVERED (C sealed at
  T10PYQ n<=28660); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-6325c15); python
  delta is w2-verified content (VERIFY-2c07079 + VERIFY-3dd5f7b).

## verdict: PASS (merge clean, C parity intact 1716/1716)
