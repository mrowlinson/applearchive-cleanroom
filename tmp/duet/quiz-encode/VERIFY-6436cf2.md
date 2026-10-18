# VERIFY-6436cf2 cport band102 T10P91+T10R90 (n<=48752, 670 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 6436cf2 under WS
  tmp/encode-viewer/6436cf2/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/6436cf2/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 2965/2965
  covered=2965/2965 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5930 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5930 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 48405..48752: 348 pass / 0 fail;
  pins 60/60.
- py + PINS + test byte-identical to parent merge 76fbe66
  (diff = src/c/rgramc.c only, +1329/-767).
- tables: 77 T10P91/T10R90 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (670).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
