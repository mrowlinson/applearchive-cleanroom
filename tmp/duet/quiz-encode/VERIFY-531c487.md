# VERIFY-531c487 cport band134 T10P109 (n<=54760, 740 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 531c487 under WS
  tmp/encode-viewer/531c487/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/531c487/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3424/3424
  covered=3424/3424 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6848 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6848 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 54669..54760: 92 pass / 0 fail;
  pins 24/24 (12 cells x closed+sha).
- py + PINS + test byte-identical to parent merge bc5b47c
  (diff = src/c/rgramc.c only, +1325/-878).
- tables: 55 T10P109 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (740).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
