# Q-301 (writer2 s20): T10P237 P-head @99213 — geometry?

Own first-hand bed 99213..99560 (census RC=0
missing=0), staged p237-patch.txt, sweep
348/348 err 0 (try-p237; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 93540100 NEW, PB1 b590ac02
  NEW, PBA 609bd720 NEW (VPOS 7: b4+M6
  b24,25,76-79; b5 const 07; NO pair in
  tier).
- C10-2SIG EXACT map: ad52a702 x3
  @99231-33 + ad525701 x7 @99234-40
  (VPOS 19: b4+M18 b2,3,20-31,80-83; b5
  const 07; 10/10 diverge).
- QUAD ad520714 NEW (VPOS 20:
  b4+M8+R7+T4; b5 const 07).
- T88-RING 01000000 (==P231/232/236T
  sig), 88B payload (VPOS 17 =
  b4,b5+M7+R8 partition over 0..87).
- Next @99561 93540100 (==P237PB0
  REPEAT) + 99562 ad52a702 (==P237C10
  sig) + 99563.. 609bd720 (==P237PBA
  sig; x14 probed).

## 2. quad + T-ring?
- Quad M8 b21-23,31,76-79 shared 16/16
  x3 vs row0.
- R7 b24-30 r1==r2==r3 TRIPLE-PAIRED
  2/4 EXACT (e63c528914eb60 x3; r0
  distinct).
- Tails row-shared 4/4 distinct
  4d4c1e83/0e319725/a0160327/ca160327;
  r2/r3 share last 3B 160327; r1 tail
  0e319725 (no triple share).
- M-tails 16/16 ALL NEW vs P236T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [40-42,76-79]
  by COL 16/16; R8 [25-27,35,80-83] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails INVERTED b76-79 col / b80-83
  row; b84-87 const 7acdc10e (1
  ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 99213..99560: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xd3+2off)&FF 256/256;
  b5=0x07+(off>=23)+(off>=151) 256/256;
  edges 99327->99328 ff/07->01/08 +
  99455->99456 ff/08->01/09?
- Consts ALL 4: PBA 77 (b5-const), C10
  65 (b5-const), quad 64 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
