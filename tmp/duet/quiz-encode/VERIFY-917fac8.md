# VERIFY-917fac8 cport band112 T10R95 (n<=50840, 694 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 917fac8 under WS
  tmp/encode-viewer/917fac8/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/917fac8/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3132/3132
  covered=3132/3132 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6264 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6264 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 50585..50840: 256 pass / 0 fail;
  pins 26/26.
- py + PINS + test byte-identical to parent merge 4313132
  (diff = src/c/rgramc.c only, +951/-810).
- tables: 14 T10R95 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (694).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
