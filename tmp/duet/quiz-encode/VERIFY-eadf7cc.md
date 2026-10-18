# VERIFY-eadf7cc cport band106 T10P94 (n<=49540, 680 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at eadf7cc under WS
  tmp/encode-viewer/eadf7cc/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/eadf7cc/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3043/3043
  covered=3043/3043 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6086 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6086 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 49449..49540: 92 pass / 0 fail;
  pins 28/28.
- py + PINS + test byte-identical to parent merge 9507514
  (diff = src/c/rgramc.c only, +1323/-786).
- tables: 67 T10P94 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (680).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
