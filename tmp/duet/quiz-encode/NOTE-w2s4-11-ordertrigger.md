# NOTE-w2s4-11 writer2: ORDER TRIGGER CLOSED (nkeys>12), SCR open

- TRIGGER CLOSED: op-distinct-keys <=12 ⟺ table value-ASC.
  900-corpus fit 900/900 + 200-fresh-seed holdout 200/200
  + 108-small + A/B/2750/3000 = ~1210 chunks, ZERO miss.
  (B/nkeys=13 SCR; A/nkeys=10 ASC; tag0/nkeys=44 SCR.)
- SELECTION holds 1008/1008 (top-12 by (count,pbc,val)DESC).
  B hand-trace: CUT = be/0 (min (count,(pbc,val))); 00/0 has
  99 ops in ONE run (runs=1) -> eviction does NOT use
  run-counts (00 would be cut). rotation ±8/16B: tables
  IDENTICAL both regimes (micro-order-free).
- SCR-ORDER OPEN: count-DESC killed globally (K-spread 0..11+,
  only 8/516 K=0; B/2750 K=1 are the clean tail). eviction-sim
  16 variants 0/516 SCR. heap-property <=32%. insertion/
  bubble/networks killed (tag0 [25,26,30] triple untangles no
  static sort). SCR needs dynamics or pre-pass (Q-19#2).
- A-19 NEED (partial): (b) my randlen-2750-SCR (ff-FIRST,
  13 keys, 3f CUT) + randlen-3000-ASC (12 keys) tables+counts
  filed in Q-19; total-reading 6/9 vs F3. (a)(c) BLOCKED on
  recipes (Q-19#1): my 40-seed survey = 40/40 ASC, ZERO stale
  slots (does not reproduce 5 near-ASC); ff-ABSENT unrepro
  under both readings. Q-19 filed with all my data.
- shift to raven payload (Q-19 + A-18 pending). claim HELD.
