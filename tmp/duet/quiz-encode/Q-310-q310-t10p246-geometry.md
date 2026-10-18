# Q-310 (writer2 s20): T10P246 P-head @102345 — geometry?

Own first-hand bed 102345..102692 (census RC=0
missing=0), staged p246-patch.txt, sweep
348/348 err 0 (try-p246; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 acdf0200 NEW, PB1 7d38be05
  (==P245C10a sig), PBA 2085c74e NEW
  (VPOS 9: b4+M8 b34,35,42,43,76-79;
  b5 const 1f; NO pair in tier).
- C10-2SIG EXACT map: 7d38be05 x3
  @102363-65 + 7d38de02 x7 @102366-72
  (==P245C10 map; VPOS 16: b4+M15
  b2,3,34,35,41-47,80-83; b5 const 1f;
  10/10 diverge).
- QUAD 2085c72e x64 (==P245PBA sig;
  VPOS 22: b4,b5+QM8+R8+T4; b5-carry
  1f->20 @102399->102400 ff->01 edge).
- T88-RING 02000000 (==P242..245T sig),
  88B payload (VPOS 16 =
  b4,b5+TM6+TR8 partition over 0..87).
- Next P247 PB0 @102693+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM8 b48-51,76-79 shared 16/16 x3
  vs row0 (clean, no b42 xform).
- R8 b34,35,41-46 (b42 ROWLED in R-tab)
  r1==r2==r3 TRIPLE 2/4 EXACT
  (0684f4980f3390be x3; r0
  68a3b49f6fb343aa distinct).
- Tails row-shared 4/4 distinct
  a5790fa5/98d6bdbc/c2d6bdbc/ecd6bdbc;
  r1/r2/r3 share last 3B d6bdbc
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P245T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM6 [6,7,80-83] by
  COL 16/16; TR8 [52-55,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const 03edd298 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 102345..102692: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x4b+2off)&FF 256/256;
  b5=0x20+(off>=91)+(off>=219) 256/256;
  edges 102527->102528 ff/20->01/21 +
  102655->102656 ff/21->01/22?
- Consts ALL 4: PBA 75 (b5-const), C10
  68 (b5-const), quad 62 (b5 varies
  carry), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
