# VERIFY-101d903 cport band129 T10R104 (n<=53972, 730 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 101d903 under WS
  tmp/encode-viewer/101d903/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/101d903/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3362/3362
  covered=3362/3362 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6724 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6724 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 53717..53972: 256 pass / 0 fail;
  pins 24/24 (12 cells x closed+sha).
- py + PINS + test byte-identical to parent merge 20df34c
  (diff = src/c/rgramc.c only, +1006/-865).
- tables: 14 T10R104 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (730).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
