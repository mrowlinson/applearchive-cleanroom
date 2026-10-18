# VERIFY-a63744d cport band69 T10R61 (n<=38660, 554 tiers): PASS

## first-hand (at-commit tree ver-a63744d)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2286/2286 covered=2286/2286
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4572 pins).
- py byte-identical to merge dc6552e (no py skew).
- tables: 31 T10R61 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
