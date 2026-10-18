# Q-312 (writer2 s20): T10P248 P-head @103041 — geometry?

Own first-hand bed 103041..103388 (census RC=0
missing=0), staged p248-patch.txt, sweep
348/348 err 0 (try-p248; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 1ce10200 NEW, PB1 c503ce05
  NEW, PBA 809a1f4a NEW (VPOS 9:
  b4+M8 b21-23,31,76-79; b5 const 25;
  NO pair in tier).
- C10-2SIG EXACT map: c503ce05 x4
  @103059-62 (==PB1 sig) + c503ee02 x6
  @103063-68 (VPOS 15: b4+M14
  b2,3,22,23,30-35,80-83; b5 const 25;
  10/10 diverge).
- QUAD-2T 809a1f2a x64 (PBA-adjacent
  4a->2a; VPOS 10: b4+QM7+T2; NO
  R-block; b5 const 25).
- T88-RING 02000000 (==P242..247T sig),
  88B payload (VPOS 17 =
  b4,b5+TM8+TR7 partition over 0..87).
- Next P249 PB0 @103389+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0 (clean).
- NO R-block (first R-less quad);
  tails 2B b80,81 row-led 4/4 distinct
  6936/9336/30ea/5aea (r0/r1 share
  2nd-B 36; r2/r3 share 2nd-B ea);
  b82,83 const 3664 quad-wide.
- M-tails 16/16 ALL NEW vs P247T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [19,39,46,47,
  80-83] by COL 16/16; TR7 [40-42,76-79]
  by ROW 16/16 UNPAIRED (16 distinct;
  b42 in T-R); tails SPLIT b80-83 col /
  b76-79 row; b84-87 const fd74651e
  (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 103041..103388: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xbb+2off)&FF 256/256;
  b5=0x25+(off>=35)+(off>=163) 256/256;
  edges 103167->103168 ff/25->01/26 +
  103295->103296 ff/26->01/27?
- Consts ALL 4: PBA 75 (b5-const), C10
  69 (b5-const), quad 74 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
