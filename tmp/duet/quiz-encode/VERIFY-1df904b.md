# VERIFY-1df904b cport band133 T10R106 (n<=54668, 738 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 1df904b under WS
  tmp/encode-viewer/1df904b/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/1df904b/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3412/3412
  covered=3412/3412 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6824 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6824 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 54413..54668: 256 pass / 0 fail;
  pins 24/24 (12 cells x closed+sha).
- py + PINS + test byte-identical to parent merge 3495f7f
  (diff = src/c/rgramc.c only, +1018/-877).
- tables: 14 T10R106 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (738).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
