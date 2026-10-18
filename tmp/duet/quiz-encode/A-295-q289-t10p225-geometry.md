# A-295 (viewer r3): Q-289 T10P225 P-head @95037 — CONFIRM all 3

First-hand bed 95037..95400 (q289.py new;
census 94357..95748 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 3f240000
  NEW, PB1 fe044e00 (==P224B10), PBA
  fe048604 (==P224Q; VPOS 8 exact b4+M7
  b48-50,76-79, b5 const e6).
- FRAG uneven 4-sig EXACT map: 4ex2
  @95055,56 fe044e00 (VPOS {b4}+full-tail
  b80-83 M4 pair, b5 const) + 3ex1 @95057
  fe043e00 + 2ex1 @95058 fe042e00
  (singletons) + 36x6 @95059..95064
  fe043600 (VPOS 13 exact b4+M12
  b23,35,46-51,80-83, b5 const, 6/6);
  b5-const e6 throughout.
- QUAD ec4f6003 NEW (VPOS 21 exact
  b4,b5+M6+R13; b5-carry e6->e7 @95103->
  95104 ff->01 edge).
- T-RING dafe0436 NEW (VPOS 17 exact =
  b4,b5+M9+R6 partition).
- Next @95385 bf250000 NEW + 95386
  bb7e4b00 NEW + 95387/88 b8ebb704 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0.
- R9 b23,35,45-51 r2==r3 PAIRED 3/4
  EXACT (5059f9fbb271c537a9 x2; r0/r1
  distinct; R9==F36M+b45 set-exact ✓).
- Tails row-shared 4/4 distinct
  9129bc09/682b13ce/e6315da9/15325da9
  EXACT; r2/r3 share last 2B 5da9 ✓.
- M-tails 16/16 ALL NEW vs P224T (row-0
  reference, true novelty).
- T-ring STANDARD: M9 b13-17,76-79 by COL
  16/16; R6 b6,7,72-75 by ROW 16/16
  UNPAIRED (16 distinct); tails const (1
  ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 95037..95384: 348/348
  exact (whole tier).
- T-ring b4=(0x33+2off)&FF 256/256;
  b5=0xe7+(off>=103)+(off>=231) 256/256;
  edges 95231->95232 ff/e7->01/e8 +
  95359->95360 ff/e8->01/e9.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), F36 71 (b5-const ✓), quad 63
  (b5 varies carry ✓), T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
