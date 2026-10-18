# VERIFY-b6151b1 cport band84 T10R72+T10P74 (n<=42516, 600 tiers): PASS

## first-hand (at-commit tree v-b6151b1, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  2559 union links, 0 oracle-regen): RGRAMC-PYID 2546/2546
  covered=2546/2546 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5092 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5092 pins, 0 FAIL).
- py + PINS byte-identical to parent merge bea3fac (cmp);
  diff bea3fac..b6151b1 = src/c/rgramc.c only (+1222/-662).
- tables: 67 T10R72/T10P74 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (600).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
