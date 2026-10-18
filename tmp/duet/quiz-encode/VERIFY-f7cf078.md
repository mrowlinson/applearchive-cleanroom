# VERIFY-f7cf078 cport band121 T10R100 (n<=52580, 714 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at f7cf078 under WS
  tmp/encode-viewer/f7cf078/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/f7cf078/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3263/3263
  covered=3263/3263 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6526 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6526 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 52325..52580: 256 pass / 0 fail;
  pins 26/26 (all new-pin PASS in own C battery).
- py + PINS + test byte-identical to parent merge 0a076a6
  (diff = src/c/rgramc.c only, +981/-840).
- tables: 14 T10R100 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (714).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
