# VERIFY-95e9d30 cport band85 T10R73 (n<=42836, 602 tiers): PASS

## first-hand (at-commit tree v-95e9d30, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  2559 union links, 0 oracle-regen): RGRAMC-PYID 2559/2559
  covered=2559/2559 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5118 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5118 pins, 0 FAIL).
- py + PINS byte-identical to parent merge b8b1278 (cmp);
  diff b8b1278..95e9d30 = src/c/rgramc.c only (+950/-668).
- tables: 31 T10R73 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed (602).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
