# A-306 (viewer r3): Q-300 T10P236 P-head @98865 — CONFIRM all 3

First-hand bed 98865..99228 (q300.py new,
88B-aware; whole-tier census 98191..99576
RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 83470100 NEW (!=P235PB0), PB1
  45f45702 NEW, PBA 5c447f25 NEW (VPOS 7
  exact b4+M6 b6,7,76-79, b5 const 04;
  NO pair in tier).
- C10-2SIG map EXACT: a826a902 x3
  @98883-85 + 54935401 x7 @98886-92
  (VPOS 19 exact b4+M18 b0-3,6-11,
  48-51,80-83; b5 const 04; 10/10
  diverge).
- QUAD f4344915 NEW (VPOS 19 exact
  b4,b5+M7+R6+T4; b5-carry 04->05
  @98943->98944 ff->01 edge).
- T88-RING 01000000 ==P231T sig ✓, 88B
  payload all 256 ✓ (VPOS 17 exact
  b4,b5+M9+R6 partition over 0..87).
- Next @99213 93540100 NEW + 99214
  b590ac02 NEW + 99215..28 609bd720 x14
  NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b9-11,76-79 shared 16/16 x3
  vs row0.
- NO b42 coupling this tier (b42 const
  0x06 all 64, outside VPOS; R is plain
  R6 b6,7,48-51) — no XOR/ADD leg, as
  staged.
- R6 TRIPLE-PAIRED 2/4 EXACT: r1==r2==r3
  d1dec3de4951 x3; r0 0dc9f25f207c
  distinct.
- Tails row-shared 4/4 distinct
  bec350e6/4906c3ab/7306c3ab/9d06c3ab
  EXACT; r1/r2/r3 share last 3B 06c3ab
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P235T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [8-11,19,76-79]
  by COL 16/16; R6 [13,14,80-83] by ROW
  16/16 UNPAIRED (16 distinct); tails
  INVERTED verified explicitly (b76-79
  col-shared 16 cols, b80-83 row-shared
  16 rows); b84-87 const 09a5a2f2 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 98865..99212: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x1b+2off)&FF 256/256;
  b5=0x05+(off>=115)+(off>=243) 256/256;
  edges 99071->99072 ff/05->01/06 +
  99199->99200 ff/06->01/07.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  C10 65 (b5-const), quad 65 (b5 varies
  carry), T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
