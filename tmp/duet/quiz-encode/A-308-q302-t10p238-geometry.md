# A-308 (viewer r3): Q-302 T10P238 P-head @99561 — CONFIRM all 3

First-hand bed 99561..99928 (q302.py new,
88B-aware; census extended 99577..99928
RC=0 missing=0 verified per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 93540100 (==P237PB0 REPEAT ✓), PB1
  ad52a702 (==P237C10 sig ✓), PBA sig
  609bd720 (==P237PBA sig) but NEW
  geometry (VPOS 9 exact b4+M8
  b34,35,42,43,76-79, b5 const 09; NO
  pair in tier).
- C10-2SIG map EXACT: ad52a702 x3
  @99579-81 + ad525701 x7 @99582-88
  (VPOS 24 exact b4,b5+M22 b2,3,20,21,
  23-27,34,35,41-47,80-83 — b22 skipped
  as staged; b5-carry 09->0a @99583->
  99584 ff->01 edge; 10/10 diverge).
- QUAD ad524715 NEW (VPOS 21 exact
  b4+M8+R8+T4; b5 const 0a).
- T88-RING 01000000 (==P231/232/236/237T
  sig ✓), 88B payload all 256 ✓ (VPOS 16
  exact b4,b5+M6+R8 partition over
  0..87).
- Next @99909 9f540100 NEW + 99910
  417faa02 NEW + split PBA c9f5a72a x9
  @99911-19 + eaf5a72a x7 @99920-26
  (staged x9/x5+ ✓, resolved 9+7=16);
  99927-28 already next-C10 sig 5e7faa02.

## 2. quad + T-ring: CONFIRM
- Quad M8 b48-51,76-79 shared 16/16 x3
  vs row0.
- R8 b34,35,41-46 TRIPLE-PAIRED 2/4
  EXACT: r1==r2==r3 5412f085bfb30a9d x3;
  r0 cc2e70849f53448a distinct (b42
  2-valued row-split 132/133 as a member
  of R8 — derived, no coupling leg).
- Tails row-shared 4/4 distinct
  53b7258b/ee3c65bc/183d65bc/e2b560fd
  EXACT; r1/r2 share last 3B 3c65bc.
- M-tails 16/16 ALL NEW vs P237T (row-0
  reference, true novelty).
- T88-ring STANDARD: M6 [6,7,80-83] by
  COL 16/16; R8 [52-55,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT verified explicitly (b80-83
  col-shared 16 cols, b76-79 row-shared
  16 rows); b84-87 const 85f32659 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 99561..99908: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x8b+2off)&FF 256/256;
  b5=0x0a+(off>=59)+(off>=187) 256/256;
  edges 99711->99712 ff/0a->01/0b +
  99839->99840 ff/0b->01/0c.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 60 (b5 varies carry), quad 63
  (b5-const), T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
