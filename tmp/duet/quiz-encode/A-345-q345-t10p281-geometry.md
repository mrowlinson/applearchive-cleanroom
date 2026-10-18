# A-345 (viewer r8): Q-345 T10P281 P-head @114525 — CONFIRM all 3

First-hand bed 114525..114872 (qr8bed own
oracle runs; census RC=0 missing=0) +
P280T ref 114269..84 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 5eae0700 NEW, PB1 2557520f
  SAME-as-P280PB1 ✓ (byte-equal to
  n114178 first-hand), PBA16-PLAIN
  c09417fb x16 @114527-42 (VPOS 7
  exact b4+M6 b48,49,76-79; b0 const
  c0, b5 const 7e; 16/16 distinct, NO
  pair in tier).
- C10-4SIG EXACT map first-hand:
  2557520f x6 @114543-48 + 2557e20c
  @114549 + 2557f20b @114550 +
  2557920c x2 @114551-52 (VPOS 13
  exact b4+M12 b2,3,46-51,80-83; b5
  const 7e; 10/10 diverge; FIRST
  6+1+1+2 C10 map ✓).
- QUAD2s 2-sig 5d7225ce x16 (row0) +
  5d7225d4 x48 (rows1-3) EXACT
  row-split (VPOS 21 exact
  b4,b5+QM8+R7+T4; b5 step o>=7).
- T88-RING 0c000000, 88B payload all
  256 ✓ (VPOS 18 exact b4,b5+TM8+TR8
  partition over 0..87).
- Next P282 PB0 @114873 9ef00700 NEW +
  114874 cb3de10f NEW + PBA e0857ffe
  x16 @114875-90 + C10-4SIG map
  3582e40f x6/4dffe70f/8d59ea0f/
  ad85e10f x2 @114891-900 (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b6,7,9,10,76-79 shared 16/16
  x3 vs row0; NO frags (0 MIXED ✓).
- R7 b3,46-51 r1==r2==r3 LAST3-PAIRED
  2/4 EXACT (r123 d4052931b9cf38 x3;
  r0 ceb6f8d1f53ff9 distinct).
- Tails row-shared 4/4 distinct
  e86c5231/4134a70c/53ecad0c/78ecad0c
  EXACT; r2/r3 share last 3B ecad0c ✓.
- M-tails 16/16 ALL NEW vs P280T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [9-11,20,80-83]
  by COL 16/16; TR8 [6,7,12,13,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const af7cecbc EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 114525..114872: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xf3+2off)&FF 64/64;
  b5=0x7e+(off>=7) 64/64; edge
  114559->114560 ff/7e->01/7f (mid-row0
  o=6->7 ✓).
- T88-ring b4=(0x73+2off)&FF 256/256;
  b5=0x7f+(off>=71)+(off>=199) 256/256;
  edges 114687->114688 ff/7f->01/80 +
  114815->114816 ff/80->01/81.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  C10 71 (b5-const), quad 63 (b5-step),
  T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
