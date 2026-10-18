# VERIFY-6a04351 cport band62 T10P57+T10R56 (n<=36920, 534 tiers): PASS

## first-hand (at-commit tree ver-6a04351)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2186/2186 covered=2186/2186
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4372 pins).
- py byte-identical to merge 6b8939e (no py skew).
- tables: 67 T10P57/T10R56 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
