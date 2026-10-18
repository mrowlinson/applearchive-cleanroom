# A-274 (viewer r3): Q-268 T10P204 P-head @87729 — CONFIRM all 3

First-hand bed 87729..88080 (regen RC=0
missing=0; q268.py + swap probe).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 3c070000
  (P203-next PREDICTED-exact), PB1 95020d00,
  PBA 5629d000 (VPOS 7 exact b4+M6
  b6,7,76-79, b5 const), PBB SPLIT 2+7
  ab290f00 joint (VPOS 11 exact b4+M10
  b6,7,48-51,80-83, b5 const ad, 9-diverge),
  SING gap 87749 de940700 NEW, QUAD 3e9af200
  (VPOS 19 exact, b5 carry off51: 87807
  ff/ad -> 87808 01/ae), T-RING 1ea3290f
  (VPOS 16).
- Next @88077 94070000 NEW + 88078 6b850e00
  NEW + 88079/80 6b85f200 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b9-11,76-79 shared 16/16 x3 vs
  row0 (heads b9,10 14/16 x4 rows).
- R6 b6,7,48-51 BOTTOM-paired r2==r3
  f810435c8a93 (3rd); r0/r1 distinct.
- Tails 4/4 distinct, 13/16 bytes.
- M-tails 16/16 ALL NEW vs P203T (0
  shared; staged label inverted, value
  exact).
- T-ring TRANSPOSED (14th) + TAILS-SWAPPED
  (5th): M7 b16-18,72-75 by COL 16/16, Q7
  b9-11,76-79 by ROW 16/16; swap:
  ring-Q common-7B rows positional ==
  quad-M row0 16/16, set 16/16.

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 87729..87820: 92/92 exact.
- T-ring b4=(0x1b+2off)&FF 256/256;
  b5=0xae+(off>=115)+(off>=243) 256/256;
  edges 87935->87936 ff/ae->01/af +
  88063->88064 ff/af->01/b0; quad b5 carry
  off51 (ff->01).
- Consts (84-VPOS) ALL 4 EXACT: PBA 77, PBB
  73 (joint), quad 65, T 68.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
