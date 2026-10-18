# VERIFY-a07ce91 cport band66 T10P60+T10R59 (n<=37964, 546 tiers): PASS

## first-hand (at-commit tree ver-a07ce91)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2246/2246 covered=2246/2246
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4492 pins).
- py byte-identical to merge d22cdc1 (no py skew).
- tables: 77 T10P60/T10R59 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
