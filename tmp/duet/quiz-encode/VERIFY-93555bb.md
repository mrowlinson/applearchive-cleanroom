# VERIFY-93555bb cport band113 T10P98 (n<=50932, 696 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 93555bb under WS
  tmp/encode-viewer/93555bb/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/93555bb/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3143/3143
  covered=3143/3143 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6286 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6286 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 50841..50932: 92 pass / 0 fail;
  pins 22/22.
- py + PINS + test byte-identical to parent merge 838e7bf
  (diff = src/c/rgramc.c only, +1249/-811).
- tables: 55 T10P98 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (696).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
