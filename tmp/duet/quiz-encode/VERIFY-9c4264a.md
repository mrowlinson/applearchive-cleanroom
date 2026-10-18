# VERIFY-9c4264a cport band80 T10R69+T10P71 (n<=41472, 588 tiers): PASS

## first-hand (at-commit tree ver-9c4264a)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2477/2477 covered=2477/2477
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4954 pins).
- py byte-identical to merge f14da80 (no py skew).
- tables: 77 T10R69/T10P71 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
