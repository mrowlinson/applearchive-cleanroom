# VERIFY-ee8a9b5 cport band2 T3..T7D3 (n<=6040, 68 tiers): PASS

## first-hand (at-commit tree ver-ee8a9b5, seat-local build)
- C build: rc=0, 0 warnings. single-file delta (+5617 rgramc.c).
- parity own run: RGRAMC-PYID 341/341 covered=341/1411 =>
  RGRAMC-GREEN (rc+stdout+stderr identical all covered N).
- python side byte-identical to band1 tree (src/rgram.py,
  vectors/rgram-PINS.csv, tests/test_rgram.sh all cmp SAME):
  RGRAM-GREEN carries from VERIFY-0f57814 first-hand run.
- code-read: 181 static tables, growth consistent with band
  range; scope gate "N out of scope" rc=2 above band.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band2 341/341 py-identical)
