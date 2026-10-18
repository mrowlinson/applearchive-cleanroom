# VERIFY-19bea75 cport band126 T10P105 (n<=53368, 724 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 19bea75 under WS
  tmp/encode-viewer/19bea75/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/19bea75/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3325/3325
  covered=3325/3325 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6650 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6650 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 53277..53368: 92 pass / 0 fail;
  pins 24/24 (12 cells x closed+sha).
- py + PINS + test byte-identical to parent merge 814a732
  (diff = src/c/rgramc.c only, +1297/-853).
- tables: 55 T10P105 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (724).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
