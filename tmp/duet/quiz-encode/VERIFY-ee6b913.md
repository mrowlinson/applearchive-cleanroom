# VERIFY-ee6b913 cport band107 T10R92 (n<=49796, 682 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at ee6b913 under WS
  tmp/encode-viewer/ee6b913/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/ee6b913/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3056/3056
  covered=3056/3056 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6112 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6112 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 49541..49796: 256 pass / 0 fail;
  pins 26/26.
- py + PINS + test byte-identical to parent merge 8a131dc
  (diff = src/c/rgramc.c only, +934/-793).
- tables: 14 T10R92 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (682).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
