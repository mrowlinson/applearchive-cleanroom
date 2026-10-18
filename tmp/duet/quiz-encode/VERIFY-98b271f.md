# VERIFY-98b271f cport band91 T10P80+T10R79 (n<=44924, 626 tiers): PASS

## first-hand (at-commit tree v-98b271f, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2697/2697
  covered=2697/2697 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5394 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5394 pins, 0 FAIL).
- own-loop fresh-oracle 44577..44924: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge a883904
  (diff = src/c/rgramc.c only, +1263/-700).
- tables: 77 T10P80/T10R79 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (626).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
