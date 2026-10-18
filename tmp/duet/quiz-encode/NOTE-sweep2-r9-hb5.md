# NOTE-sweep2-r9-hb5 (b166 gate-tip green, C legs running)

- r9-3504728 gate-tip: RGRAM py 7638/0 GREEN, PINS-RGRAM
  set-eq 7638/7638, all other functional legs PASS
  (RAWENC/PBZE/LZMA/LZ4 +-C, SMOKE/IMPL, OUTER2, RB2,
  RAVFRAME, UNITS, LZ4C, OSS nominated-only).
  FAILs only HYG/CONTAM/LIBC = OBSERVED-inherited (proven
  IDENTICAL vs b164); ADOPT WARN same diff c8f52713/c5f921d5.
- ownbuild + pyid + cbatt + ownloop running (~20 min).
  Quota 0/2. Next: GATE-3504728.md, then b168.
