# VERIFY-d0484b7 cport band73 T10P65+T10R64 (n<=39704, 566 tiers): PASS

## first-hand (at-commit tree ver-d0484b7)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2352/2352 covered=2352/2352
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4704 pins).
- py byte-identical to merge b4de394 (no py skew).
- tables: 67 T10P65/T10R64 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
