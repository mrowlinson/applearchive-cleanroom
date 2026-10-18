# VERIFY-17a2872 cport band67 T10P61 (n<=37992, 548 tiers): PASS

## first-hand (at-commit tree ver-17a2872)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2256/2256 covered=2256/2256
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4512 pins).
- py byte-identical to merge 66f5b03 (no py skew).
- tables: 46 T10P61 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
