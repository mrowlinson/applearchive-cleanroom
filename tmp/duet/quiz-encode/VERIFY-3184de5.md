# VERIFY-3184de5 cport band81 T10R70 (n<=41792, 590 tiers): PASS

## first-hand (at-commit tree ver-3184de5)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2490/2490 covered=2490/2490
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4980 pins).
- py byte-identical to merge 2bdac59 (no py skew).
- tables: 31 T10R70 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
