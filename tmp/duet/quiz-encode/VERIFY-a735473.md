# VERIFY-a735473 cport band90 T10P79+T10R78 (n<=44576, 622 tiers): PASS

## first-hand (at-commit tree v-a735473, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2674/2674
  covered=2674/2674 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5348 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5348 pins, 0 FAIL).
- own-loop fresh-oracle 44229..44576: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 3367c4b
  (diff = src/c/rgramc.c only, +1282/-694).
- tables: 70 T10P79/T10R78 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (622).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
