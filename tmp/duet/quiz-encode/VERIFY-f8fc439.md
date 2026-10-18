# VERIFY-f8fc439 cport band63 T10P58 (n<=36948, 536 tiers): PASS

## first-hand (at-commit tree ver-f8fc439)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2196/2196 covered=2196/2196
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4392 pins).
- py byte-identical to merge eaed6ba (no py skew).
- tables: 36 T10P58 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
