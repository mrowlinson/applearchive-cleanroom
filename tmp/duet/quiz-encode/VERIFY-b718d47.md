# VERIFY-b718d47 cport band109 T10R93 (n<=50144, 686 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at b718d47 under WS
  tmp/encode-viewer/b718d47/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/b718d47/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3079/3079
  covered=3079/3079 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6158 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6158 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 49889..50144: 256 pass / 0 fail;
  pins 24/24.
- py + PINS + test byte-identical to parent merge 8dd89c2
  (diff = src/c/rgramc.c only, +957/-798).
- tables: 16 T10R93 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (686).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
