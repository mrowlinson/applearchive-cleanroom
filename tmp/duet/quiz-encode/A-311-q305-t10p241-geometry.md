# A-311 (viewer r3): Q-305 T10P241 P-head @100605 — CONFIRM all 3

First-hand bed 100605..100968 (q305.py
new, 88B-aware; census extended
100621..100968 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 3f550100 (==P240PB0 REPEAT ✓), PB1
  4dc2a402 (==P240PB1 REPEAT ✓), PBA sig
  a0955736 (==P240PBA sig) but NEW
  geometry (VPOS 11 exact b4,b5+M9
  b47-51,76-79; b5-carry 11->12 @100607->
  100608 ff->01 edge; NO pair in tier).
- C10-MS 6-sig map EXACT: 4dc2a402 x3
  @100623-25 + 4dc2f401/4dc2d401/
  4dc2f401/4dc20402/4dc21402/4dc22402/
  4dc2f401 @100626-32 (6 distinct ✓;
  VPOS 21 exact b4+M20 b2,3,20,21,23-27,
  35,46-51,80-83 — b22 skipped as
  staged; b5 const 12; 10/10 diverge).
- QUADms row-led de244c1f (row 0) /
  de244c20 (rows 1-3) EXACT (VPOS 24 =
  b4+M6+R13+T4; b5 const 12).
- T88-RING 03000000 NEW ✓, 88B payload
  all 256 ✓ (VPOS 15 exact b4,b5+M7+R6
  partition over 0..87).
- Next @100953 4b620100 NEW + 100954
  6197c402 NEW + 100955..68 608fd732 x14
  NEW.

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0.
- R13 b3,20,21,24-27,35,46,47,49-51
  TRIPLE-PAIRED 2/4 EXACT: r1==r2==r3
  2089f9b03c37ecc1fbfb745f57 x3; r0
  1f09fbcc61796e01b02aca478b distinct;
  sig-led b3 row-sigs 1f/20/20/20 ✓
  (b48 skipped as staged).
- Tails row-shared 4/4 distinct
  a46dc517/a6780a47/d0780a47/fa780a47
  EXACT; r1/r2/r3 share last 2B 0a47.
- M-tails 16/16 ALL NEW vs P240T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [9-11,80-83] by
  COL 16/16; R6 [6,7,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT verified explicitly (b80-83
  col-shared 16 cols, b76-79 row-shared
  16 rows); b84-87 const 6bafef49 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 100605..100952: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xb3+2off)&FF 256/256;
  b5=0x12+(off>=39)+(off>=167) 256/256;
  edges 100735->100736 ff/12->01/13 +
  100863->100864 ff/13->01/14.
- Consts ALL 4 EXACT: PBA 73 (b5 varies
  carry), C10 63 (b5-const), quad 60
  (b5-const), T88 73 (88-15).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
