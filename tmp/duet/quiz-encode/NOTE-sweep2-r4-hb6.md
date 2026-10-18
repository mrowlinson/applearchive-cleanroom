# NOTE-sweep2-r4-hb6 (b158 gate-tip done, C legs running)

- gate-tip rc=1 expected-shape: RGRAM py 7438/0 GREEN,
  PINS-RGRAM 7438/7438, all other functional legs PASS
  (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2, RB2,
  RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- FAILs = inherit legs only (HYG/CONTAM/LIBC, hit-sets
  IDENTICAL vs b157 + lane 0s -> OBSERVED-inherited);
  ADOPT WARN same c8f52713/c5f921d5 as b156.
- Seat-private own build rc=0 warnings=0. PYID running,
  then C battery + own-loop 58845..58936.
