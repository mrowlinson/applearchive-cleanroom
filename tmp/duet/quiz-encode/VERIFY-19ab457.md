# VERIFY-19ab457 cport band103 T10P92+T10B91 (n<=49100, 674 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 19ab457 under WS
  tmp/encode-viewer/19ab457/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/19ab457/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 2998/2998
  covered=2998/2998 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5996 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5996 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 48753..49100: 348 pass / 0 fail;
  pins 66/66.
- py + PINS + test byte-identical to parent merge 73df8f0
  (diff = src/c/rgramc.c only, +1374/-773).
- tables: 73 T10P92/T10B91 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (674).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
