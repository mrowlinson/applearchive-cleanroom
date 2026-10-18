# VERIFY-559b878 cport band99 T10P88+T10R87 (n<=47708, 658 tiers): PASS

## first-hand (at-commit tree vv-viewer-559b878, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  fresh-seeded own regen): RGRAMC-PYID 2881/2881
  covered=2881/2881 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5762 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5762 pins, 0 FAIL).
- own-loop fresh-oracle 47361..47708: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge a8b6efd
  (diff = src/c/rgramc.c only, +1316/-748).
- tables: 73 T10P88/T10R87 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (658).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
