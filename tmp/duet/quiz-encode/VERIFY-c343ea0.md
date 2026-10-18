# VERIFY-c343ea0 cport band114 T10R96 (n<=51188, 698 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at c343ea0 under WS
  tmp/encode-viewer/c343ea0/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/c343ea0/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3156/3156
  covered=3156/3156 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6312 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6312 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 50933..51188: 256 pass / 0 fail;
  pins 26/26.
- py + PINS + test byte-identical to parent merge 6df65ce
  (diff = src/c/rgramc.c only, +975/-816).
- tables: 16 T10R96 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (698).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
