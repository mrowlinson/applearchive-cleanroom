# VERIFY-cc81d7f cport band77 T10R67 (n<=40748, 578 tiers): PASS

## first-hand (at-commit tree ver-cc81d7f)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2421/2421 covered=2421/2421
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4842 pins).
- py byte-identical to merge 7d2affe (no py skew).
- tables: 31 T10R67 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
