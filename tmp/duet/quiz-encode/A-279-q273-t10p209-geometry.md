# A-279 (viewer r3): Q-273 T10P209 P-head @89469 — CONFIRM + CORRECTION

First-hand bed 89469..89820 (q273.py new;
census 89129..90180 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 98070000
  (REPEAT P208 PB0 PREDICTED-exact), PB1
  bfab0e00 (repeat), PBA bfabf200 (repeat;
  VPOS 10 exact b4,b5+M8 b48-51,76-79, b5
  CARRY ba->bb @89471->89472 ff/ba->01/
  bb first-cell edge).
- PAIR 89487..89488 bfab0e00 (==PB1, VPOS
  {b4,b80} ONLY exact).
- PBC8 bfab0a00 NEW (VPOS 14 exact b4+M13
  b23,35,45-51,80-83, b5 const bb).
- QUAD f7bbaa00 NEW (VPOS 20 exact ex-b5,
  b5 const 0xbb).
- T-RING 7cbfab0a NEW (VPOS 16).
- Next @89817 f0070000 NEW + 89818
  96e10f00 NEW + 89819/20 6819fe00 NEW.

## 2. quad + T-ring: CONFIRM + 1 tail fix
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0 (heads b6,7 FULL 16/16 x4).
- R9 (derived b23,35,45-51) MIDDLE-paired
  r1==r2 913452d700b18b6770 (3/4
  distinct — first middle-pair); r0/r3
  distinct.
- Tails 4/4 distinct
  (0696ac60/ebc705a9/1bc805a9/50ee0894),
  14/16 bytes. CORRECTION: r1/r2 share
  last 2B (05a9), NOT 3B (c7 vs c8
  differ: ebc705a9 vs 1bc805a9).
- M-tails 16/16 ALL NEW vs P208T (true
  novelty polarity).
- T-ring TRANSPOSED (19th): M8
  b13-15,17,76-79 (b16 gap: b16 const
  ring-wide) by COL 16/16; Q6 b6,7,72-75
  by ROW 16/16.

## 3. counters + dips: CONFIRM counts, NONE
- Odd-lencode all 89469..89560: 92/92 exact.
- T-ring b4=(0xb3+2off)&FF 256/256;
  b5=0xbb+(off>=39)+(off>=167) 256/256;
  edges 89599->89600 ff/bb->01/bc +
  89727->89728 ff/bc->01/bd.
- Consts ALL 4 COUNTS EXACT: PBA 74, PBC
  70, quad 64, T 68.
- CORRECTION (3 tags): PBA b5 VARIES
  ba/bb carry (VPOS 10 in-b5) — IS
  b5-in (untagged in Q); PBC b5 CONST bb
  (VPOS 14 ex-b5) + quad b5 CONST bb
  (VPOS 20 ex-b5; leg-1 "b5 const 0xbb"
  was right) — NOT b5-in. Counts stand.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; r1/r2 tails 2B + 3 b5-tags fixed
