# VERIFY-f563e5f cport band75 T10R65+T10P67 (n<=40080, 572 tiers): PASS

## first-hand (at-commit tree ver-f563e5f)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2385/2385 covered=2385/2385
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4770 pins).
- py byte-identical to merge 97e5ee8 (no py skew).
- tables: 67 T10R65/T10P67 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
