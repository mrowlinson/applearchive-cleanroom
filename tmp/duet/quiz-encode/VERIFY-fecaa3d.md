# VERIFY-fecaa3d cport band94 T10P83+T10R82 (n<=45968, 638 tiers): PASS

## first-hand (at-commit tree v-fecaa3d, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2766/2766
  covered=2766/2766 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5532 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5532 pins, 0 FAIL).
- own-loop fresh-oracle 45621..45968: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 8233b06
  (diff = src/c/rgramc.c only, +1280/-718).
- tables: 67 T10P83/T10R82 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (638).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
