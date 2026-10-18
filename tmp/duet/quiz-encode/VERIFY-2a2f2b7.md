# VERIFY-2a2f2b7 cport band74 T10P66 (n<=39732, 568 tiers): PASS

## first-hand (at-commit tree ver-2a2f2b7)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2362/2362 covered=2362/2362
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4724 pins).
- py byte-identical to merge bee28c5 (no py skew).
- tables: 36 T10P66 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
