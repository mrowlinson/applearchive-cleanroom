# Q-336 (writer2 s20): T10P272 P-head @111393 — geometry?

Own first-hand bed 111393..111740 (census RC=0
missing=0), staged p272-patch.txt, sweep
348/348 err 0 (try-p272; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 f62a0700 NEW (new f62a
  family), PB1 25bd5c0e NEW,
  PBA16-PLAIN c0935ff8 x16 @111395-410
  (VPOS 8: b4+M7 b21,22,31,76-79; b0
  const c0, b5 const 66; NO pair in
  tier).
- C10-1SIG single-sig EXACT map: 25bd5c0e
  x10 @111411-20 (VPOS 13: b4+M12
  b22,23,30-35,80-83; b5 const 66;
  10/10 diverge; head-sig == PB1 sig).
- QUAD1s 1-sig c0935ff8 x64 (VPOS 19:
  b4+QM7+R7+T4; b5 const 66).
- T88-RING 0a000000, 88B payload (VPOS
  16 = b4,b5+TM7+TR7 partition over
  0..87).
- Next P273 PB0 @111741+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b36-38,76-79 (same positions
  as P264) shared 16/16 x3 vs row0;
  NO frags (all positions COL-pure or
  ROW-pure, 0 MIXED).
- R7 b22,23,30-34 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  3f8f317eb5563d x3; r0 87c77df9550a1a
  distinct).
- Tails row-shared 4/4 distinct
  d5b4b22a/44398e25/69398e25/43399225;
  r1/r2 share last 3B 398e25.
- M-tails 16/16 ALL NEW vs P271T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [39,46,47,80-83]
  by COL 16/16; TR7 [40-42,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const b874e2de (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 111393..111740: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xfb+2off)&FF 256/256;
  b5=0x66+(off>=3)+(off>=131) 256/256;
  edges 111487->111488 ff/66->01/67 +
  111615->111616 ff/67->01/68?
- Consts ALL 4: PBA 76 (b5-const), C10
  71 (b5-const), quad 65 (b5-const),
  T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
