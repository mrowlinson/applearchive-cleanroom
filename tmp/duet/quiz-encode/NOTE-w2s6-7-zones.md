# NOTE-w2s6-7 writer2: ZONE MAP (pos,N) + exact-8 through spread

## Exact rules (single-dev @N=120..135, zeros base)
- HOLES (n=8) ⟺ d = N-pos <= 32. EXACT (13/13 cells; all d>=33 never 8).
- d = 33-35: SPREAD (n=18/32/47, same len) — value STILL exact-8 holes
  (8-value scans @N=129/131: common=0 rewrite, 8 1x-bits), only the
  LOCATION scatters (129: 233-237+317-319; 131: 297-304 contiguous!).
- L32 tier-change: pos19/50 always; pos76 @N>=128; pos77 @N>=129;
  pos96 @N>=132. pos0/10/18 = rewrite at ALL N (absolute early class).
- T0-form rewrites BIGGER than T1 (pos10: 64-66 @N<=127 vs 53-55 @>=128).

## L32 predicate: OPEN (non-monotonic in d AND pos)
- flip-d: 76->52, 77->52, 96->36; pos90 unflipped @d=45, pos100 @d=35.
- "pos <= N-52 -> L" fits 76/77/90/100 but BREAKS on (96,132) [the one
  cell]. N=129/131/132 = +1/+3 spacing. needs denser corner beds, NOT
  chase-now (characterization depth, off critical path).
- PRE-007 N=129 anomaly: reproduced + explained (spread zone, value
  exact-8, tag question moot — no rewrite layer at all there).

## Backlog: T2 regime (85b) / head-field 3-state / grammar pins for lane.
