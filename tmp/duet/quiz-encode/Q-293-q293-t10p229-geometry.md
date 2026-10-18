# Q-293 (writer2 s20): T10P229 P-head @96429 — geometry?

Own first-hand bed 96429..96776 (census RC=0
missing=0), staged p229-patch.txt, sweep
348/348 err 0 (try-p229).

## 1. shape?
- 348 cells sizes {(100,84)}. PB0 994e0000
  NEW, PB1 e6969900 NEW, PBA e696d109 NEW
  (VPOS 7: b4+M6 b24,25,76-79; b5 const
  f1).
- PAIR-3T 96447..96448 32f79900 NEW (diff
  b4+b80,81,82 only; b83 same 96).
- PBC8 32f74900 NEW (VPOS 14: b4+M13
  b20,21,25-31,80-83, b5 const f1).
- QUAD 32f7c107 NEW (VPOS 21:
  b4,b5+M7+R7+b31+T4; b5-carry f1->f2
  @96511->96512 ff->01 edge).
- T-RING e096d758 NEW (VPOS 18 =
  b4,b5+M8+R8 partition).
- Next @96777 984e0000 NEW + 96778
  32f79900 (==P229PAIR) + 96779..
  32f7f108 NEW.

## 2. quad + T-ring?
- Quad M7 b21-23,76-79 shared 16/16 x3
  vs row0.
- b31 row-add A=[0,1,0,0] 64/64 vs row-0
  M31 (r1-only +1; rows 0,2,3 identical;
  32 distinct).
- R7 b24-30 r0==r2 EVEN-PAIRED 3/4 EXACT
  (fabc851eb404f9 x2; r1/r3 distinct).
- Tails row-shared 4/4 distinct
  d08feaa6/29215901/2690eaa6/26d52267;
  r0/r2 share last 3B 90eaa6 (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P228T (row-0
  reference, true novelty).
- T-ring STANDARD: M8 [32,33,38,39,72-75]
  by COL 16/16; R8 [21-23,31,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b72-75 col / b76-79 row;
  b80-83 const (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 96429..96776: 348/348
  exact (whole tier)?
- T-ring b4=(0x13+2off)&FF 256/256;
  b5=0xf2+(off>=119)+(off>=247) 256/256;
  edges 96639->96640 ff/f2->01/f3 +
  96767->96768 ff/f3->01/f4?
- Consts ALL 4: PBA 76 (b5-const), PBC
  69 (b5-const), quad 63 (b5 varies
  carry), T 66?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
