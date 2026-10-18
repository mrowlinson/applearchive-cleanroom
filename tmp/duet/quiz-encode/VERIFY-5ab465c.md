# VERIFY-5ab465c cport band78 T10P69+T10R68 (n<=41096, 582 tiers): PASS

## first-hand (at-commit tree ver-5ab465c)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2444/2444 covered=2444/2444
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4888 pins).
- py byte-identical to merge 40c2817 (no py skew).
- tables: 70 T10P69/T10R68 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
