# A-294 (viewer r3): Q-288 T10P224 P-head @94689 — CONFIRM + CORRECTION

First-hand bed 94689..95052 (q288.py new;
census 94357..95748 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 1f120000
  NEW, PB1 fe042600 NEW, PBA fe044602 NEW
  (VPOS 8 exact b4+M7 b32-34,76-79, b5
  const e3).
- PBB10 fe044e00 NEW single-sig (VPOS 12
  exact b4+M11 b22,23,30,31,36-38,80-83,
  b5 const e3, 10/10 diverge; NO pair/C8).
- QUAD fe048604 NEW (VPOS 19 exact
  b4,b5+M6+R11; b5-carry e3->e4 @94719->
  94720 ff->01 edge).
- T-RING 409dff48 NEW (VPOS 15 exact =
  b4,b5+M7+R6 partition).
- Next @95037 3f240000 NEW + 95038
  fe044e00 (==P224B10sig) + 95039/40
  fe048604 (==P224Qsig).

## 2. quad + T-ring: CONFIRM + count fix
- Quad M6 b36,37,76-79 shared 16/16 x3 vs
  row0.
- R7 b22,23,30-34 r0==r1+r2==r3
  DOUBLE-PAIRED 2/4 EXACT (01aae8f8749ec7
  / 89b8ccf914329a).
- CORRECTION (count only): B10M/QR share
  8/11 (not 7/11) — intersection
  {22,23,30,31,80,81,82,83} is 8
  positions; B-only 36-38 + Q-only 32-34
  as listed, both exact.
- Tails row-shared 4/4 distinct
  70ec9d9c/9cec9d9c/09ee0259/38ee0259
  EXACT; r0/r1 share last 3B ec9d9c ✓ +
  r2/r3 share last 3B ee0259 ✓ (matching
  R-pairs).
- M-tails 16/16 ALL NEW vs P223T (row-0
  reference, true novelty).
- T-ring STANDARD: M7 b35,42,43,76-79 by
  COL 16/16; R6 b36,37,72-75 by ROW 16/16
  UNPAIRED (16 distinct); tails const (1
  ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 94689..95036: 348/348
  exact (whole tier).
- T-ring b4=(0x7b+2off)&FF 256/256;
  b5=0xe4+(off>=67)+(off>=195) 256/256;
  edges 94847->94848 ff/e4->01/e5 +
  94975->94976 ff/e5->01/e6.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), PBB 72 (b5-const ✓), quad 65
  (b5 varies carry ✓), T 69.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; B10M/QR share 8/11 (not 7)
