# Q-303 (writer2 s20): T10P239 P-head @99909 — geometry?

Own first-hand bed 99909..100256 (census RC=0
missing=0), staged p239-patch.txt, sweep
348/348 err 0 (try-p239; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 9f540100 NEW, PB1 417faa02
  NEW, PBA-SPLIT9/7 c9f5a72a x9 @99911-19
  + eaf5a72a x7 @99920-26 NEW (VPOS 11:
  b4+M7+split3 b9-11,76-79 + b0/b12/b13
  c9d644/ea9645 @off9; b5 const 0c; NO
  pair in tier).
- C10-2SIG EXACT map: 5e7faa02 x3
  @99927-29 + af3f5501 x7 @99930-36
  (VPOS 16: b4+M15 b0-3,13-19,80-83; b5
  const 0c; 10/10 diverge).
- QUADms 15-sig NEW (VPOS 19:
  b4,b5+M6+R6+b19+T4; b5-carry 0c->0d
  @99967->99968 ff->01 edge).
- T88-RING 01000000 (==P231/232/236/237/
  238T sig), 88B payload (VPOS 16 =
  b4,b5+M7+R7 partition over 0..87).
- Next @100257 3f550100 NEW + 100258
  4dc2a402 NEW + 100259.. a0955736 NEW
  (x14 probed).

## 2. quad + T-ring?
- Quad M6 b0,11,76-79 shared 16/16 x3
  vs row0 (sig-led col b0: 15 sigs
  bf/c1/c6/c9/ca/cd/d1 x2/d6/d8/dc/e3/
  e6/e9/ed/ee by column).
- b19 row-add A=[0,9,9,9] 64/64 vs row-0
  M19 (col-vector 2-valued 45/c5; r1==
  r2==r3 rows). NOTE: XOR X=[00,0b,0b,0b]
  fits equally (single col-low 5) —
  staged ADD by b19 precedent (P231);
  flag if tie preferred.
- R6 b13-18 r2==r3 PAIRED 3/4 EXACT
  (ee7ce21a7a80 x2; r0 distinct; r1
  1B-off ed7c...).
- Tails row-shared 4/4 distinct
  de328733/c3741d50/b1ea2893/dbea2893;
  r2/r3 share last 3B ea2893 (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P238T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [29-31,80-83] by
  COL 16/16; R7 [16,17,23,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const a23b39be (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 99909..100256: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x43+2off)&FF 256/256;
  b5=0x0d+(off>=95)+(off>=223) 256/256;
  edges 100095->100096 ff/0d->01/0e +
  100223->100224 ff/0e->01/0f?
- Consts ALL 4: PBA 73 (b5-const), C10
  68 (b5-const), quad 65 (b5 varies
  carry), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
