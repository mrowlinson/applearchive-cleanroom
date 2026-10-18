# A-319 (viewer r3): Q-313 T10P249 P-head @103389 — CONFIRM all 3

First-hand bed 103389..103752 (q313.py
new, 88B-aware; census extended
103405..103752 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 18e10200 NEW, PB1 c503ce05
  (==P248PB1 ✓), PBA 809a1f4a x16
  (==P248PBA sig) but NEW geometry (VPOS
  9 exact b4+M8 b48-51,76-79; b5 const
  27; NO pair in tier).
- C10-MS 7-sig map EXACT: c503ce05 x3
  @103407-09 (==PB1 ✓) + c5034e05/
  c5030e04/c5034e04/c5036e04/c5037e04/
  c503be04 x2 @103410-16 (7 distinct ✓;
  VPOS 14 exact b4+M13 b2,3,35,46-51,
  80-83; b5 const 27; 10/10 diverge).
- QUADms 1B-off row-led 5c3ce047 x16
  (row0) + 5c3ce046 x48 (rows1-3) EXACT
  (VPOS 22 = b4,b5+QM8+R8+T4; b5-carry
  27->28 @103423->103424 ff->01 EARLY
  edge ✓).
- T88-RING 05000000 NEW ✓ (breaks
  02000000 run), 88B payload all 256 ✓
  (VPOS 16 exact b4,b5+TM7+TR7 partition
  over 0..87).
- Next P250 PB0 @103737 90fc0200 NEW +
  103738 3420f905 NEW + 103739..52
  a08fbf52 x14 NEW (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b6-9,76-79 shared 16/16 x3
  vs row0.
- R8 sig-led b3,35,46-51 r1==r2==r3
  TRIPLE 2/4 EXACT (460a99cc5196b776
  x3; r0 47cad1a5d1b2a75c distinct; b3
  row-sigs 47/46/46/46 ✓).
- Tails row-shared 4/4 distinct
  6d6d4ae9/706b3942/9a6b3942/c46b3942
  EXACT; r1/r2/r3 share last 3B 6b3942
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P248T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [9-11,80-83] by
  COL 16/16; TR7 [6,7,12,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT verified explicitly (b80-83
  col-shared 16 cols, b76-79 row-shared
  16 rows); b84-87 const 79ad6284 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 103389..103736: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x73+2off)&FF 256/256;
  b5=0x28+(off>=71)+(off>=199) 256/256;
  edges 103551->103552 ff/28->01/29 +
  103679->103680 ff/29->01/2a.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 70 (b5-const), quad 62 (b5 varies
  carry), T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
