# A-305 (viewer r3): Q-299 T10P235 P-head @98517 — CONFIRM all 3

First-hand bed 98517..98880 (q299.py new,
88B-aware; census 98191..99576 RC=0
missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 8c470100 (==P234PB0 REPEAT), PB1
  45f44701 NEW, PBA 45f47714 NEW (VPOS 8
  exact b4+M7 b36-38,76-79, b5 const 01;
  NO pair in tier).
- C10-2SIG map EXACT: 8702 x3 @98535-37 +
  4701 x2 @98538-39 + 8702 x4 @98540-43 +
  4701 @98544 (all 45f4.... ✓; VPOS 23
  exact b4+M22 b2,3,20,23-27,34-43,80-83,
  b5 const 01, 10/10 diverge).
- QUAD 40806734 (==P234Q sig; VPOS 20
  exact b4,b5+M7+R6+b42+T4; b5-carry
  01->02 @98559->98560 ff->01 edge).
- T88-RING 02000000 (==P234T sig ✓), 88B
  payload all 256 ✓ (VPOS 19 exact =
  b4,b5+M9+R8 partition over 0..87).
- Next @98865 83470100 NEW + 98866
  45f45702 NEW + 98867..80 5c447f25 x14
  NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b34,35,43,76-79 shared 16/16 x3
  vs row0.
- b42: XOR X=[00,05,05,03] 64/64 ✓ AND
  ADD A=[0,3,3,1] 64/64 ✓ — TIE
  first-hand (M42 col-vector 4-valued
  01/41/81/c1 ✓; col-highs 0/4/8/c +
  row-lows 01/04/04/02 by mechanism:
  single col-low 01, 1^X=1/4/4/2,
  1+A=1/4/4/2, no carries; 12 distinct
  = 4x3 ✓). VERDICT: tie — staged XOR
  stands by b42-family precedent (XOR at
  b42 ever since P211; ADD only b31/b19
  ties). Flagged as tie per request.
- R6 b36-41 r1==r2 PAIRED 3/4 EXACT
  (215aa7b8118f x2; r0/r3 distinct).
- Tails row-shared 4/4 distinct
  7ec94b22/78652135/a2652135/ac0ed296
  EXACT; r1/r2 share last 3B 652135 ✓
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P234T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [50,52-55,80-83]
  by COL 16/16; R8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col (16) / b76-79
  row (16); b84-87 const 5359b47e EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 98517..98864: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x63+2off)&FF 256/256;
  b5=0x02+(off>=79)+(off>=207) 256/256;
  edges 98687->98688 ff/02->01/03 +
  98815->98816 ff/03->01/04.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), C10 61 (b5-const ✓), quad 64
  (b5 varies carry ✓), T88 69 (88-19 ✓).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
