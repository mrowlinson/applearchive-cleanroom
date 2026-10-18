# A-290 (viewer r3): Q-284 T10P220 P-head @93297 — CONFIRM all 3

First-hand bed 93297..93660 (q284.py new;
census 92617..93660 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 56110000
  REPEAT x3, PB1 36bf1a00 NEW, PBA
  6ef3ab01 NEW (VPOS 8 exact b4,b5+M6
  b6,7,76-79; b5-carry d8->d9 @93311->
  93312 ff->01 edge).
- PAIR 93315..93316 9d2d2400 NEW (VPOS
  {b4,b80} ONLY exact).
- PBC8 ce161200 NEW (VPOS 11 exact b4+M10
  b6,7,48-51,80-83 == quad-R positions
  set-exact, b5 const d9).
- QUAD 266d2101 NEW (VPOS 18 exact
  b4+M7+R10, b5 const d9).
- T-RING a6d31612 NEW (VPOS 15 exact =
  b4,b5+M6+R7 partition).
- Next @93645 16120000 NEW (5611 run
  ends) + 93646 3a072300 NEW + 93647/48
  3a074302 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b9-11,76-79 shared 16/16 x3 vs
  row0 (== ring-ROW positions 7/7:
  QM==TR ✓).
- R6 b6,7,48-51 r2==r3 PAIRED 3/4 EXACT
  (2a6a505e8d58 x2; r0/r1 distinct).
- Tails row-shared 4/4 distinct
  39264fc9/cd5a03c4/c9973b74/f8973b74
  EXACT; r2/r3 share last 3B 973b74 ✓.
- M-tails 16/16 ALL NEW vs P219T (row-0
  reference, true novelty).
- T-ring ROLE-SWAP3: M6 [16,17,72-75] by
  COL 16/16; R7 [9-11,76-79] by ROW
  16/16; transpose-swapped exact; tails
  const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 93297..93644: 348/348
  exact (whole tier).
- T-ring b4=(0x9b+2off)&FF 256/256;
  b5=0xd9+(off>=51)+(off>=179) 256/256;
  edges 93439->93440 ff/d9->01/da +
  93567->93568 ff/da->01/db.
- Consts ALL 4 EXACT: PBA 76 (b5 varies
  carry ✓), PBC 73 (b5-const ✓), quad 66
  (b5-const ✓), T 69.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
