# VERIFY-8ecae82 cport band132 T10P108 (n<=54412, 736 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 8ecae82 under WS
  tmp/encode-viewer/8ecae82/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/8ecae82/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3400/3400
  covered=3400/3400 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6800 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6800 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 54321..54412: 92 pass / 0 fail;
  pins 26/26 (13 cells x closed+sha).
- py + PINS + test byte-identical to parent merge f67c8a8
  (diff = src/c/rgramc.c only, +1318/-874).
- tables: 55 T10P108 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (736).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
