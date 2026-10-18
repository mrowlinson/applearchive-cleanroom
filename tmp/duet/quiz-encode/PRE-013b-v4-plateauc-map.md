# PRE-013b plateau-C map: 1169..2212 @48B + 14 internal edges (w2 next accel)

## bounds (bisected exact, zeros-N)
- plateau C = N 1169..2212 @48B (1044 rows, no dips, no len change).
  52-tier starts 2213 (edge 2212/2213 clean).

## internal big-rewrite edges (consecutive-pair ndiff>12, exact N)
- 1425(31), 1426(31), 1443(13) | 1517(21) | 1773(22), 1774(21), 1775(24),
  1791(25), 1801(27), 1865(32) | 2048(15) | 2121(38), 2122(38), 2123(31),
  2139(19), 2149(14).
- 2048 concurs w2s7-10 "big rewrite @2048" ✓ (same edge, both seats).
- suggested sectioning: 1169-1424 | 1425-1516 | 1517-1772 | 1773-1865 |
  1866-2047 | 2048-2120 | 2121-2212 (refine by their dumps).

## note
- survey = step-8 sweep + exact bisect (own, ~200 encodes). field formulas
  + dev/hole mapping remain w2's. plateau C has no dip-class events.
