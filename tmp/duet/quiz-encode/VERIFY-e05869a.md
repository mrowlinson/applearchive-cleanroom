# VERIFY-e05869a cport band117 T10R98 (n<=51884, 706 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at e05869a under WS
  tmp/encode-viewer/e05869a/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/e05869a/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3211/3211
  covered=3211/3211 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6422 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6422 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 51629..51884: 256 pass / 0 fail;
  pins 26/26.
- py + PINS + test byte-identical to parent merge 0563d71
  (diff = src/c/rgramc.c only, +987/-828).
- tables: 16 T10R98 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (706).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
