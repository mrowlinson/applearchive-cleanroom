# VERIFY-1050d3d cport merge w2@b490c4e (python T10R34): PASS

## first-hand (at-commit tree ver-1050d3d, band27 seat binary)
- delta vs band27: python side only (rgram.py, test list,
  PINS +20 = 10N). C source byte-identical to band27 (cmp
  SAME), so band27 seat binary reused for parity (no rebuild skew).
- python `tests/test_rgram.sh` (own run, fresh oracle):
  RGRAM-GREEN (tail g-z29264 zone).
- parity own run: RGRAMC-PYID 1736/1736 covered=1736/1746 =>
  RGRAMC-GREEN. 10 new R34 N correctly UNCOVERED (C sealed
  at T10PZQ n<=29008); all previously-covered N still
  byte-identical => merge broke no C behavior.
- wall-grep: C unchanged (clean per VERIFY-c2fdbce); python
  delta is w2-verified content (VERIFY-b490c4e PASS).

## verdict: PASS (merge clean, C parity intact 1736/1736)
