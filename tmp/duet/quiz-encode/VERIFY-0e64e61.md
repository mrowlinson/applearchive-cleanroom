# VERIFY-0e64e61 cport band97 T10P86+T10R85 (n<=47012, 650 tiers): PASS

## first-hand (at-commit tree v-0e64e61, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2835/2835
  covered=2835/2835 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5670 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5670 pins, 0 FAIL).
- own-loop fresh-oracle 46665..47012: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge fa89957
  (diff = src/c/rgramc.c only, +1298/-736).
- tables: 67 T10P86/T10R85 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (650).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
