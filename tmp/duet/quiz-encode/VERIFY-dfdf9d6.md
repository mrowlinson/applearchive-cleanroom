# VERIFY-dfdf9d6 cport band98 T10P87+T10R86 (n<=47360, 654 tiers): PASS

## first-hand (at-commit tree vv-dfdf9d6, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  fresh-seeded own regen): RGRAMC-PYID 2858/2858
  covered=2858/2858 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5716 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5716 pins, 0 FAIL).
- own-loop fresh-oracle 47013..47360: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 2ed27ea
  (diff = src/c/rgramc.c only, +1333/-742).
- tables: 73 T10P87/T10R86 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (654).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
