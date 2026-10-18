# Q-329 (writer2 s20): T10P265 P-head @108957 — geometry?

Own first-hand bed 108957..109304 (census RC=0
missing=0), staged p265-patch.txt, sweep
348/348 err 0 (try-p265; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 a0560300 NEW, PB1 bdcfaa06
  SAME-as-P264PB1, PBA16-PLAIN e0932f72
  x16 @108959-74 (VPOS 7: b4+M6
  b48,49,76-79; b0 const e0, b5
  const 53; NO pair in tier).
- C10-6SIG EXACT map: bdcfaa06 x4
  @108975-78 + bdcf7a06 x1 @108979 +
  bdcffa04 x1 @108980 + bdcf1a05 x1
  @108981 + bdcf3a05 x1 @108982 +
  bdcf7a05 x2 @108983-84 (VPOS 14:
  b4+M13 b2,3,35,46-51,80-83; b5 const
  53; 10/10 diverge).
- QUADms 3-sig dffbac59 x16 (row0) +
  dffbac5c x32 (rows1-2) + dffbac57 x16
  (row3) NEW (VPOS 19: b4+QM6+R8+T4;
  b5 const 53).
- T88-SPLIT 05/04, 88B payload (VPOS
  17 = b0,b4,b5+TM8+TR6 partition over
  0..87).
- Next P266 PB0 @109305+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM6 b6,7,76-79 shared 16/16 x3
  vs row0; NO frags (all positions
  COL-pure or ROW-pure, 0 MIXED).
- R8 b3,35,46-51 r1==r2 MID-PAIRED 3/4
  EXACT (5c52a392917ed792 x2; r0
  59d2ffd8b1a56722 + r3
  5792ce9eb1805f9a distinct).
- Tails row-shared 4/4 distinct
  473b6a01/c2fac80f/756b3610/652f4ee8
  (no shared suffix).
- M-tails 16/16 ALL NEW vs P264T (row-0
  reference, true novelty).
- T88-ring SPLIT-b0: TM8 [9-11,20,80-83]
  by COL 16/16; TR6 [6,7,76-79] by ROW
  16/16 UNPAIRED (16 distinct); b0 =
  05 iff col<3 else 04 (3+13 per row
  x16 rows); tails SPLIT b80-83 col /
  b76-79 row; b84-87 const 2032bed2
  (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 108957..109304: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xf3+2off)&FF 256/256;
  b5=0x53+(off>=7)+(off>=135) 256/256;
  edges 109055->109056 ff/53->01/54 +
  109183->109184 ff/54->01/55?
- Consts ALL 4: PBA 77 (b5-const), C10
  70 (b5-const), quad 65 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
