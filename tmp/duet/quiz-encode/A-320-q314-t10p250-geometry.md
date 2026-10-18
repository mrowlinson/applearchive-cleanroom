# A-320 (viewer r3): Q-314 T10P250 P-head @103737 — CONFIRM all 3

First-hand bed 103737..104100 (q314.py
new, 88B-aware; census extended
103753..104100 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 90fc0200 NEW, PB1 3420f905 NEW,
  PBA a08fbf52 NEW (VPOS 10 exact b4+M9
  b12-15,19,76-79, b5 const 2a; NO pair
  in tier).
- C10-MS 7-sig map EXACT: 8506f905 x3
  @103755-57 + fd85f602/8510f602/6dbcf002/
  9deaf302/bd2bf902/7d9ff902 x2 @103758-64
  (7 distinct ✓; VPOS 16 exact b4+M15
  b0-3,11,18-23,80-83; b5 const 2a;
  10/10 diverge).
- QUAD 00882f26 x64 NEW (VPOS 20 exact
  b4,b5+QM8+R6+T4 — b21 SKIPPED as
  staged; b5-carry 2a->2b @103807->
  103808 ff->01 edge).
- T88-RING 02000000 (back to 02 after
  P249 05 ✓ — P249T re-read 05000000),
  88B payload all 256 ✓ (VPOS 18 exact
  b4,b5+TM8+TR8 partition over 0..87).
- Next P251 PB0 @104085 90fc0200
  (==P250PB0 REPEAT) + 104086 5d16fd05
  NEW + 104087..100 00882f46 x14 NEW
  (P250Q-adjacent 26->46 1B-off last
  byte, derived; window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b24-27,76-79 shared 16/16 x3
  vs row0.
- R6 b13,14,18-20,22 (b21 SKIPPED ✓)
  r1==r2==r3 TRIPLE 2/4 EXACT
  (541f9874d247 x3; r0 e409fc799251
  distinct).
- Tails row-shared 4/4 distinct
  36735045/e43d6c14/0e3e6c14/383e6c14
  EXACT; r2/r3 share last 3B 3e6c14;
  r1 2nd-B 3d 1B-off (not full
  triple-share) ✓.
- M-tails 16/16 ALL NEW vs P249T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [18,27,34,35,
  80-83] by COL 16/16; TR8 [28-31,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT verified explicitly
  (b80-83 col-shared 16 cols, b76-79
  row-shared 16 rows); b84-87 const
  dc735045 EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 103737..104084: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x2b+2off)&FF 256/256;
  b5=0x2b+(off>=107)+(off>=235) 256/256;
  edges 103935->103936 ff/2b->01/2c +
  104063->104064 ff/2c->01/2d.
- Consts ALL 4 EXACT: PBA 74 (b5-const),
  C10 68 (b5-const), quad 64 (b5 varies
  carry), T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
