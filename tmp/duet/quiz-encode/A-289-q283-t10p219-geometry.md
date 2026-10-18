# A-289 (viewer r3): Q-283 T10P219 P-head @92949 — CONFIRM all 3

First-hand bed 92949..93312 (q283.py new;
census 92617..93660 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 56110000
  REPEAT, PB1 36bf2200 NEW, PBA 36bf2a02
  NEW (VPOS 8 exact b4+M7 b36-38,76-79,
  b5 const d6).
- PAIR 92967..92968 36bf2200 (==PB1, VPOS
  {b4,b80} ONLY exact).
- PBC8 36bf1200 NEW (VPOS 13 exact b4+M12
  b32,33,37-42,80-83, b5 const d6).
- QUAD 36bf1a01 NEW (VPOS 20 exact
  b4+M8+b42+R10, b5 const d6).
- T-RING 36bf5a11 NEW (VPOS 17 exact =
  b4,b5+M6+R9 partition).
- Next @93297 56110000 REPEAT x3 + 93298
  36bf1a00 NEW + 93299/93300 6ef3ab01
  NEW.

## 2. quad + T-ring: CONFIRM
- Quad M8 b23,34,35,43,76-79 shared 16/16
  x3 vs row0 + b42 row-xor X=[00,04,05,
  05] 64/64 (P211 rule; X[2]==X[3]
  matches R-pair ✓).
- R6 b36-41 r2==r3 PAIRED 3/4 EXACT
  (ffdf4b9030d1 x2; r0/r1 distinct).
- Tails row-shared 4/4 distinct
  7cc4b6cf/298c9e0c/df24e910/0e25e910
  EXACT; r2/r3 share last 2B e910 ✓.
- M-tails 16/16 ALL NEW vs P218T (row-0
  reference, true novelty).
- T-ring STANDARD: M6 b48,49,76-79 by COL
  16/16; R9 b23,34,35,42,43,72-75 by ROW
  16/16 UNPAIRED (16 distinct; QM-heads
  4/4 in rows ✓); tails const (1
  ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 92949..93296: 348/348
  exact (whole tier).
- T-ring b4=(0xe3+2off)&FF 256/256;
  b5=0xd6+(off>=15)+(off>=143) 256/256;
  edges 93055->93056 ff/d6->01/d7 +
  93183->93184 ff/d7->01/d8.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), PBC 71 (b5-const ✓), quad 64
  (b5-const ✓), T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
