# VERIFY-5dca1be cport band111 T10P97 (n<=50584, 692 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 5dca1be under WS
  tmp/encode-viewer/5dca1be/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/5dca1be/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3119/3119
  covered=3119/3119 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6238 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6238 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 50493..50584: 92 pass / 0 fail;
  pins 28/28.
- py + PINS + test byte-identical to parent merge 8147e8f
  (diff = src/c/rgramc.c only, +1243/-805).
- tables: 55 T10P97 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (692).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
