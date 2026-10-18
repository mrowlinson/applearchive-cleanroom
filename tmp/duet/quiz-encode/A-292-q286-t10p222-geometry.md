# A-292 (viewer r3): Q-286 T10P222 P-head @93993 — CONFIRM all 3

First-hand bed 93993..94356 (q286.py new;
census 94009..94356 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 17120000
  NEW, PB1 3a822100 (==P221B10sig), PBA
  3a820102 NEW (VPOS 9 exact b4+M8
  b34,35,42,43,76-79, b5 const de).
- PBB10 3a822100 (==PB1) single-sig
  (VPOS 13 exact b4+M12 b34,35,41-46,
  80-83 == quad-R positions set-exact, b5
  const de, 10/10 diverge; NO pair/C8).
- QUAD 3a824102 (==P221Q; VPOS 23 exact
  b4,b5+M9+R12; b5-carry de->df @94079->
  94080 ff->01 edge).
- T-RING ae231824 NEW (VPOS 17 exact =
  b4,b5+M6+R9 partition).
- Next @94341 17120000 REPEAT + 94342
  5c1f1200 NEW + PBA first-cell split:
  94343 1ef42101 / 94344.. 00f42101
  (6 probed, split holds).

## 2. quad + T-ring: CONFIRM
- Quad M9 b47-51,76-79 shared 16/16 x3 vs
  row0.
- R8 b34,35,41-46 r2==r3 PAIRED 3/4 EXACT
  (2e7b899abfd3e438 x2; r0/r1 distinct).
- Tails row-shared 4/4 distinct
  09bb7378/d1f01af7/b6f9d055/472ce255
  EXACT; r2/r3 share last 1B 55 ✓.
- M-tails 16/16 ALL NEW vs P221T rows
  (col-0 row reference, true novelty).
- T-ring STANDARD: M6 b6,7,76-79 by COL
  16/16; R9 b47-51,72-75 by ROW 16/16
  UNPAIRED (16 distinct; QM-heads 5/5 in
  rows ✓); tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 93993..94340: 348/348
  exact (whole tier).
- T-ring b4=(0x0b+2off)&FF 256/256;
  b5=0xdf+(off>=123)+(off>=251) 256/256;
  edges 94207->94208 ff/df->01/e0 +
  94335->94336 ff/e0->01/e1.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), PBB 71 (b5-const ✓), quad 61
  (b5 varies carry ✓), T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
