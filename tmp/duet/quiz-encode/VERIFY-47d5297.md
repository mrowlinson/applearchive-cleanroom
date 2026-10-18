# VERIFY-47d5297 cport band128 T10P106 (n<=53716, 728 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 47d5297 under WS
  tmp/encode-viewer/47d5297/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/47d5297/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3350/3350
  covered=3350/3350 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6700 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6700 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 53625..53716: 92 pass / 0 fail;
  pins 26/26 (13 cells x closed+sha).
- py + PINS + test byte-identical to parent merge 84785e0
  (diff = src/c/rgramc.c only, +1316/-859).
- tables: 60 T10P106 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (728).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
