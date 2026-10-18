# A-293 (viewer r3): Q-287 T10P223 P-head @94341 — CONFIRM all 3

First-hand bed 94341..94704 (q287.py new;
census 94357..95748 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 17120000
  REPEAT, PB1 5c1f1200 NEW, PBA split-sig
  94343 1ef42101 + 94344..94358 00f42101
  x15 NEW (VPOS 10 exact b4+M9 b0,9-12,
  76-79; b0/b12 cell0-only 1e/95 vs
  00/b5 exact, rest single-valued; b5
  const e1).
- PBB10 813e2400 NEW single-sig (VPOS 12
  exact b4+M11 b13-19,80-83 == quad-R
  positions set-exact, b5 const e1, 10/10
  diverge; NO pair/C8).
- QUAD 1de84302 NEW (VPOS 19 exact
  b4+M7+R11, b5 const e1).
- T-RING 20827f28 NEW (VPOS 19 exact =
  b4,b5+M9+R8 partition).
- Next @94689 1f120000 NEW + 94690
  fe042600 NEW + 94691/92 fe044602 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b20-22,76-79 shared 16/16 x3 vs
  row0.
- R7 b13-19 r2==r3 PAIRED 3/4 EXACT
  (e6fc877a5b8d9c x2; r0/r1 distinct).
- Tails row-shared 4/4 distinct
  7f7a1c5f/5dfc677c/d8397426/073a7426
  EXACT; r2/r3 share last 2B 7426 ✓.
- M-tails 16/16 ALL NEW vs P222T (row-0
  reference, true novelty).
- T-ring STANDARD: M9 b20,21,25-27,76-79
  by COL 16/16; R8 b12-14,19,72-75 by
  ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 94341..94688: 348/348
  exact (whole tier).
- T-ring b4=(0xc3+2off)&FF 256/256;
  b5=0xe1+(off>=31)+(off>=159) 256/256;
  edges 94463->94464 ff/e1->01/e2 +
  94591->94592 ff/e2->01/e3.
- Consts ALL 4 EXACT: PBA 74 (b5-const
  ✓), PBB 72 (b5-const ✓), quad 65
  (b5-const ✓), T 65.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
