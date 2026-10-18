# A-309 (viewer r3): Q-303 T10P239 P-head @99909 — CONFIRM all 3

First-hand bed 99909..100272 (q303.py
new, 88B-aware; census extended
99929..100272 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 9f540100 NEW, PB1 417faa02 NEW,
  PBA-SPLIT9/7 c9f5a72a x9 @99911-19 +
  eaf5a72a x7 @99920-26 EXACT (VPOS 11 =
  b4+M7 b9-11,76-79 + split3 b0/b12/b13:
  group triples c9d644/ea9645 EXACT,
  each group const; b5 const 0c; NO pair
  in tier).
- C10-2SIG map EXACT: 5e7faa02 x3
  @99927-29 + af3f5501 x7 @99930-36
  (VPOS 16 exact b4+M15 b0-3,13-19,80-83;
  b5 const 0c; 10/10 diverge).
- QUADms 15-sig NEW (VPOS 19 exact
  b4,b5+M6+R6+b19+T4; b5-carry 0c->0d
  @99967->99968 ff->01 edge).
- T88-RING 01000000 (==P231/232/236/237/
  238T sig ✓), 88B payload all 256 ✓
  (VPOS 16 exact b4,b5+M7+R7 partition
  over 0..87).
- Next @100257 3f550100 NEW + 100258
  4dc2a402 NEW + 100259..72 a0955736 x14
  NEW.

## 2. quad + T-ring: CONFIRM
- Quad M6 b0,11,76-79 shared 16/16 x3
  vs row0; sig-led col b0 15 distinct by
  column bf/c1/c6/c9/ca/cd/d1 x2/d6/d8/
  dc/e3/e6/e9/ed/ee EXACT (all ??adf614;
  d1 doubled).
- b19: row-ADD A=[0,9,9,9] 64/64 ✓ AND
  XOR X=[00,0b,0b,0b] 64/64 ✓ — TIE
  first-hand (M19 col-vector 2-valued
  45/c5 ✓ 6+10; r1==r2==r3 rows).
  VERDICT: tie — staged ADD stands by
  b19 precedent (P231). Flagged as tie
  per request.
- R6 b13-18 r2==r3 PAIRED 3/4 EXACT
  (ee7ce21a7a80 x2; r0 7f3c403a8b1d
  distinct; r1 ed7ce21a7a80 1B-off ✓).
- Tails row-shared 4/4 distinct
  de328733/c3741d50/b1ea2893/dbea2893
  EXACT; r2/r3 share last 3B ea2893
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P238T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [29-31,80-83]
  by COL 16/16; R7 [16,17,23,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT verified explicitly
  (b80-83 col-shared 16 cols, b76-79
  row-shared 16 rows); b84-87 const
  a23b39be EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 99909..100256: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x43+2off)&FF 256/256;
  b5=0x0d+(off>=95)+(off>=223) 256/256;
  edges 100095->100096 ff/0d->01/0e +
  100223->100224 ff/0e->01/0f.
- Consts ALL 4 EXACT: PBA 73 (b5-const),
  C10 68 (b5-const), quad 65 (b5 varies
  carry), T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
