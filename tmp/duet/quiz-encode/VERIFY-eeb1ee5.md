# VERIFY-eeb1ee5 cport band110 T10P96+T10R94 (n<=50492, 690 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at eeb1ee5 under WS
  tmp/encode-viewer/eeb1ee5/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/eeb1ee5/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3105/3105
  covered=3105/3105 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6210 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6210 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 50145..50492: 348 pass / 0 fail;
  pins 52/52.
- py + PINS + test byte-identical to parent merge 5e72665
  (diff = src/c/rgramc.c only, +1378/-799).
- tables: 70 T10P96/T10R94 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (690).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
