# VERIFY-42b1e16 cport band61 T10R55 (n<=36572, 530 tiers): PASS

## first-hand (at-commit tree ver-42b1e16)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2166/2166 covered=2166/2166
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4332 pins).
- py byte-identical to merge cb10c8b (no py skew).
- tables: 70 T10R55/T10P56 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed.
- wall-grep: 13 `r2` hits all false positives (tier labels
  T8R2/T10R2 in comments/printf/failf); true patterns 0 hits.

## verdict: PASS
