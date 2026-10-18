# VERIFY-ead5f7c cport band86 T10P75+T10R74 (n<=43184, 606 tiers): PASS

## first-hand (at-commit tree v-ead5f7c, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  2559 union + 23 own-loop seed, 0 oracle-regen):
  RGRAMC-PYID 2582/2582 covered=2582/2582 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5164 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5164 pins, 0 FAIL).
- py + PINS byte-identical to parent merge cd3037c (cmp);
  diff cd3037c..ead5f7c = src/c/rgramc.c only (+1230/-670).
- tables: 67 T10P75/T10R74 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (606).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
