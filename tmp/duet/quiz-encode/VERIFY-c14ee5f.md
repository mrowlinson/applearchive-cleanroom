# VERIFY-c14ee5f cport band130 T10P107 (n<=54064, 732 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at c14ee5f under WS
  tmp/encode-viewer/c14ee5f/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/c14ee5f/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3375/3375
  covered=3375/3375 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6750 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6750 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 53973..54064: 92 pass / 0 fail;
  pins 26/26 (13 cells x closed+sha).
- py + PINS + test byte-identical to parent merge bab78db
  (diff = src/c/rgramc.c only, +1312/-866).
- tables: 55 T10P107 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (732).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
