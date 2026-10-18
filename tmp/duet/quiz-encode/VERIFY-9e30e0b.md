# VERIFY-9e30e0b cport band123 T10R101 (n<=52928, 718 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 9e30e0b under WS
  tmp/encode-viewer/9e30e0b/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/9e30e0b/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3288/3288
  covered=3288/3288 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6576 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6576 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 52673..52928: 256 pass / 0 fail;
  pins 26/26 (13 cells x closed+sha).
- py + PINS + test byte-identical to parent merge cb0ab6f
  (diff = src/c/rgramc.c only, +987/-846).
- tables: 14 T10R101 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (718).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
