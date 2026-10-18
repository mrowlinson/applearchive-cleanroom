# VERIFY-cac2faf cport band68 T10R60+T10P62 (n<=38340, 552 tiers): PASS

## first-hand (at-commit tree ver-cac2faf)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2276/2276 covered=2276/2276
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4552 pins).
- py byte-identical to merge 57108c8 (no py skew).
- tables: 67 T10R60/T10P62 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
