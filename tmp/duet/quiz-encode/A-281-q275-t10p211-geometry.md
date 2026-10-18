# A-281 (viewer r3): Q-275 T10P211 P-head @90165 — CONFIRM all 3

First-hand bed 90165..90528 (q275.py new;
census 90181..90528 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 f0070000
  REPEAT (==P210 PB0), PB1 e96d0f00 NEW,
  PBA e96dff00 NEW (VPOS 8 exact b4+M7
  b36-38,76-79, b5 const c0).
- PAIR 90183..90184 ==PB1 (VPOS {b4} +
  FULL-tail b80-83 exact — first
  full-tail pair).
- PBC8 e96d0700 NEW (VPOS 13 exact b4+M12
  b32,33,37-42,80-83, b5 const c0).
- QUAD e96d6300 NEW (VPOS 19 exact
  b4,b5+M6+b42+R10; b5-carry c0->c1
  @90239->90240 ff->01 edge).
- T-RING e96de307 NEW (VPOS 17 exact =
  b4,b5+M8+R7 partition).
- Next @90513 f0070000 REPEAT x3 + 90514
  e96d0f00 (==P211PB1) + 90515/16
  96def600 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M6 b34,43,76-79 shared 16/16 x3 vs
  row0 + b42 row-xor X=[00,02,03,07]
  64/64 (b42^X[row] col-const, P179
  rule).
- R6 b36-41 UNPAIRED 4/4 distinct.
- Tails row-shared 4/4 distinct
  a14d25f5/5907bd9e/23a5c1c0/df267dea
  EXACT.
- M-tails 16/16 ALL NEW vs P210T (true
  novelty polarity).
- T-ring ROLE-SWAP: M8 [48-51,72-75] by
  COL 16/16; R7 [34,42,43,76-79] by ROW
  16/16; transpose-swapped exact
  (vpos partition confirms swapped tail
  sets); tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 90165..90512: 348/348
  exact (whole tier).
- T-ring b4=(0x23+2off)&FF 256/256;
  b5=0xc1+(off>=111)+(off>=239) 256/256;
  edges 90367->90368 ff/c1->01/c2 +
  90495->90496 ff/c2->01/c3.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), PBC 71 (b5-const ✓), quad 65
  (b5 varies carry ✓), T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
