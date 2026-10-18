# VERIFY-68d2eef cport band125 T10R102 (n<=53276, 722 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 68d2eef under WS
  tmp/encode-viewer/68d2eef/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/68d2eef/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3313/3313
  covered=3313/3313 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6626 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6626 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 53021..53276: 256 pass / 0 fail;
  pins 26/26 (13 cells x closed+sha).
- py + PINS + test byte-identical to parent merge 49c1fa2
  (diff = src/c/rgramc.c only, +993/-852).
- tables: 14 T10R102 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (722).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
