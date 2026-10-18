# VERIFY-c0deeeb cport band79 T10P70 (n<=41124, 584 tiers): PASS

## first-hand (at-commit tree ver-c0deeeb)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2454/2454 covered=2454/2454
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4908 pins).
- py byte-identical to merge 54efe06 (no py skew).
- tables: 46 T10P70 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
