# Q-302 (writer2 s20): T10P238 P-head @99561 — geometry?

Own first-hand bed 99561..99908 (census RC=0
missing=0), staged p238-patch.txt, sweep
348/348 err 0 (try-p238; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 93540100 (==P237PB0 REPEAT),
  PB1 ad52a702 (==P237C10 sig), PBA
  609bd720 (==P237PBA sig) NEW (VPOS 9:
  b4+M8 b34,35,42,43,76-79; b5 const
  09; NO pair in tier).
- C10-2SIG EXACT map: ad52a702 x3
  @99579-81 + ad525701 x7 @99582-88
  (VPOS 24: b4,b5+M22 b2,3,20,21,23-27,
  34,35,41-47,80-83; b5-carry 09->0a
  @99583->99584 ff->01 edge; 10/10
  diverge).
- QUAD ad524715 NEW (VPOS 21:
  b4+M8+R8+T4; b5 const 0a).
- T88-RING 01000000 (==P231/232/236/237T
  sig), 88B payload (VPOS 16 =
  b4,b5+M6+R8 partition over 0..87).
- Next @99909 9f540100 NEW + 99910
  417faa02 NEW + 99911.. c9f5a72a
  x9 / eaf5a72a x5+ (split PBA?).

## 2. quad + T-ring?
- Quad M8 b48-51,76-79 shared 16/16 x3
  vs row0.
- R8 b34,35,41-46 r1==r2==r3
  TRIPLE-PAIRED 2/4 EXACT (5412f085bfb30a9d
  x3; r0 distinct).
- Tails row-shared 4/4 distinct
  53b7258b/ee3c65bc/183d65bc/e2b560fd;
  r1/r2 share last 3B 3c65bc.
- M-tails 16/16 ALL NEW vs P237T (row-0
  reference, true novelty).
- T88-ring STANDARD: M6 [6,7,80-83] by
  COL 16/16; R8 [52-55,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const 85f32659 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 99561..99908: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x8b+2off)&FF 256/256;
  b5=0x0a+(off>=59)+(off>=187) 256/256;
  edges 99711->99712 ff/0a->01/0b +
  99839->99840 ff/0b->01/0c?
- Consts ALL 4: PBA 75 (b5-const), C10
  60 (b5 varies carry), quad 63
  (b5-const), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
