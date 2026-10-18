# Q-328 (writer2 s20): T10P264 P-head @108609 — geometry?

Own first-hand bed 108609..108956 (census RC=0
missing=0), staged p264-patch.txt, sweep
348/348 err 0 (try-p264; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 a2560300 NEW, PB1 bdcfaa06
  NEW, PBA16-PLAIN e0932f72 x16
  @108611-26 (VPOS 9: b4+M8
  b21-23,31,76-79; b0 const e0, b5
  const 50; NO pair in tier).
- C10-1SIG single-sig EXACT map: bdcfaa06
  x10 @108627-36 (VPOS 13:
  b4+M12 b22,23,30-35,80-83; b5 const
  50; 10/10 diverge; head-sig == PB1
  sig).
- QUAD1s 1-sig e0932f72 x64 (VPOS 19:
  b4,b5+QM7+F6+T4; b5 step o>=35;
  R-LESS R7 const-folded out of VPOS).
- T88-NONSTD 06000000, 88B payload (VPOS
  18 = b4,b5+TM9+TR7 partition over
  0..87; NONSTD M/R layout).
- Next P265 PB0 @108957+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0.
- F6 row-frags b22/23/30/32/33/34: ADD
  A22=[0,80,80,128] A23=[0,47,47,121]
  A30=[0,112,112,4] A32=[0,160,160,160]
  A33=[0,224,224,48] A34=[0,33,33,195]
  64/64 each AND XOR X22=[00,50,50,80]
  X23=[00,d1,d1,87] X30=[00,90,90,7c]
  X32=[00,a0,a0,a0] X33=[00,60,60,30]
  X34=[00,21,21,43] 64/64 each — TIE
  x6 first-hand (all r1==r2 mid-paired;
  staged ADD by nearest-family precedent
  b31-ADD P229 / b19-ADD P231/P239/P263,
  flagged as tie).
- R7 sig-led b0-3,16-18 1/4 R-LESS EXACT
  (e0932f7204808d x4 all rows; FIRST
  R-less quad staged QRx4-identical +
  rtab check, uniform handler).
- Tails row-shared 4/4 distinct
  c37be99d/c0fadb1d/e5fadb1d/cb6a97b8;
  r1/r2 share last 3B fadb1d.
- M-tails 16/16 ALL NEW vs P263T (row-0
  reference, true novelty).
- T88-ring NONSTD: TM9 [18,19,39,46,47,
  80-83] by COL 16/16; TR7 [40-42,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const f36a97b8 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 108609..108956: 348/348
  exact (whole tier incl 88B cells)?
- Quad b4=(0xbb+2off)&FF 64/64;
  b5=0x50+(off>=35) 64/64; edge
  108671->108672 ff/50->01/51 (mid-row2
  o=34->35)?
- T88-ring b4=(0x3b+2off)&FF 256/256;
  b5=0x51+(off>=99)+(off>=227) 256/256;
  edges 108799->108800 ff/51->01/52 +
  108927->108928 ff/52->01/53?
- Consts ALL 4: PBA 75 (b5-const), C10
  71 (b5-const), quad 58 (b5-step),
  T88 70 (88-18)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
