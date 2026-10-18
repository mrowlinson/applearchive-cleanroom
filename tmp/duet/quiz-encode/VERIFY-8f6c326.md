# VERIFY-8f6c326 cport band105 T10R91 (n<=49448, 678 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 8f6c326 under WS
  tmp/encode-viewer/8f6c326/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/8f6c326/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3029/3029
  covered=3029/3029 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6058 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6058 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 49193..49448: 256 pass / 0 fail;
  pins 26/26.
- py + PINS + test byte-identical to parent merge 79abb83
  (diff = src/c/rgramc.c only, +922/-785).
- tables: 14 T10R91 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (678).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
