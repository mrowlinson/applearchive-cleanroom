# VERIFY-779427a cport band120 T10P102 (n<=52324, 712 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 779427a under WS
  tmp/encode-viewer/779427a/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/779427a/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3250/3250
  covered=3250/3250 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6500 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6500 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 52233..52324: 92 pass / 0 fail;
  pins 24/24 (all new-pin PASS in own C battery).
- py + PINS + test byte-identical to parent merge a82a67f
  (diff = src/c/rgramc.c only, +1287/-835).
- tables: 58 T10P102 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (712).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
