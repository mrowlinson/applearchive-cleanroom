# VERIFY-c12fcc6 cport band3 T7..T9B2 (n<=13696): PASS

## first-hand (at-commit tree ver-c12fcc6, seat-local build)
- C build: rc=0, 0 warnings. single-file delta (rgramc.c).
- parity own run: RGRAMC-PYID 855/855 covered=855/1411 =>
  RGRAMC-GREEN (rc+stdout+stderr identical all covered N).
- python side byte-identical to band1 tree (3 files cmp SAME):
  RGRAM-GREEN carries from VERIFY-0f57814 first-hand run.
- code-read: 420 static tables. count note: commit msg says
  "165 tiers total", cport NOTE-05 already self-corrected to
  169 measured — writer-owned erratum, no functional impact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band3 855/855 py-identical)
