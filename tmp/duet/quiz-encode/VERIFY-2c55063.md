# VERIFY-2c55063 cport band104 T10P93 (n<=49192, 676 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 2c55063 under WS
  tmp/encode-viewer/2c55063/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/2c55063/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3016/3016
  covered=3016/3016 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6032 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6032 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 49101..49192: 92 pass / 0 fail;
  pins 36/36.
- py + PINS + test byte-identical to parent merge 8974afa
  (diff = src/c/rgramc.c only, +1229/-779).
- tables: 60 T10P93 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (676).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
