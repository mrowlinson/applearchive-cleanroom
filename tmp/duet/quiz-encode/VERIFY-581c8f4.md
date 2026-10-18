# VERIFY-581c8f4 cport band72 T10R63 (n<=39356, 562 tiers): PASS

## first-hand (at-commit tree ver-581c8f4)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2329/2329 covered=2329/2329
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4658 pins).
- py byte-identical to merge 4b3e3e8 (no py skew).
- tables: 34 T10R63 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
