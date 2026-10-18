# VERIFY-ae6ab12 cport band64 T10R57+T10P59 (n<=37296, 540 tiers): PASS

## first-hand (at-commit tree ver-ae6ab12)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2216/2216 covered=2216/2216
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4432 pins).
- py byte-identical to merge d228eb4 (no py skew).
- tables: 70 T10R57/T10P59 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
