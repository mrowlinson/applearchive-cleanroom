# VERIFY-1b15add cport band71 T10R62+T10P64 (n<=39036, 560 tiers): PASS

## first-hand (at-commit tree ver-1b15add)
- C build 0 warnings.
- `tests/test_rgram_c.sh` own run dedicated workdir (shared
  corpus symlink): RGRAMC-PYID 2316/2316 covered=2316/2316
  RGRAMC-GREEN.
- `RGRAM_BIN=C tests/test_rgram.sh` own run fresh oracle:
  RGRAM-GREEN (4632 pins).
- py byte-identical to merge c19269e (no py skew).
- tables: 70 T10R62/T10P64 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed.
- wall-grep true patterns 0 hits in src/c/.

## verdict: PASS
