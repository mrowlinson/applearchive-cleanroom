# VERIFY-0aea685 cport band119 T10R99 (n<=52232, 710 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 0aea685 under WS
  tmp/encode-viewer/0aea685/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/0aea685/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3238/3238
  covered=3238/3238 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6476 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6476 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 51977..52232: 256 pass / 0 fail;
  pins 26/26 (all new-pin PASS in own C battery).
- py + PINS + test byte-identical to parent merge 0323580
  (diff = src/c/rgramc.c only, +975/-834).
- tables: 14 T10R99 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (710).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
