# Q-305 (writer2 s20): T10P241 P-head @100605 — geometry?

Own first-hand bed 100605..100952 (census RC=0
missing=0), staged p241-patch.txt, sweep
348/348 err 0 (try-p241; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 3f550100 (==P240PB0 REPEAT),
  PB1 4dc2a402 (==P240PB1 REPEAT), PBA
  a0955736 (==P240PBA sig) but NEW
  geometry (VPOS 11: b4,b5+M9
  b47-51,76-79; b5-carry 11->12 @100607->
  100608 ff->01 edge; NO pair in tier).
- C10-MS 6-sig EXACT map: 4dc2a402 x3
  @100623-25 + 4dc2f401 + 4dc2d401 +
  4dc2f401 + 4dc20402 + 4dc21402 +
  4dc22402 + 4dc2f401 (VPOS 21: b4+M20
  b2,3,20,21,23-27,35,46-51,80-83; b5
  const 12; 10/10 diverge).
- QUADms row-led de244c1f (row 0) /
  de244c20 (rows 1-3) NEW (VPOS 24:
  b4+M6+R13+T4; b5 const 12).
- T88-RING 03000000 NEW, 88B payload
  (VPOS 15 = b4,b5+M7+R6 partition over
  0..87).
- Next @100953 4b620100 NEW + 100954
  6197c402 NEW + 100955.. 608fd732 NEW
  (x14 probed).

## 2. quad + T-ring?
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0.
- R13 b3,20,21,24-27,35,46,47,49-51
  r1==r2==r3 TRIPLE-PAIRED 2/4 EXACT
  (2089f9b03c37ecc1fbfb745f57 x3; r0
  distinct; sig-led b3 row-sig
  1f/20/20/20).
- Tails row-shared 4/4 distinct
  a46dc517/a6780a47/d0780a47/fa780a47;
  r1/r2/r3 share last 2B 0a47.
- M-tails 16/16 ALL NEW vs P240T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [9-11,80-83] by
  COL 16/16; R6 [6,7,76-79] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b80-83 col / b76-79 row; b84-87
  const 6bafef49 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 100605..100952: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xb3+2off)&FF 256/256;
  b5=0x12+(off>=39)+(off>=167) 256/256;
  edges 100735->100736 ff/12->01/13 +
  100863->100864 ff/13->01/14?
- Consts ALL 4: PBA 73 (b5 varies
  carry), C10 63 (b5-const), quad 60
  (b5-const), T88 73 (88-15)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
