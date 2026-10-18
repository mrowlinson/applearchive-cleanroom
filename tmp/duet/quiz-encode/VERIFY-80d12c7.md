# VERIFY-80d12c7 cport band70 T10P63 (n<=38688, 556 tiers): PASS

## first-hand (at-commit tree ver-80d12c7)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2296/2296 covered=2296/2296
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4592 pins).
- py byte-identical to merge 2a7fa9a (no py skew).
- tables: 36 T10P63 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
