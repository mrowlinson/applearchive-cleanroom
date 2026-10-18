# A-318 (viewer r3): Q-312 T10P248 P-head @103041 — CONFIRM all 3

First-hand bed 103041..103404 (q312.py
new, 88B-aware; census extended
103057..103404 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 1ce10200 NEW, PB1 c503ce05 NEW,
  PBA 809a1f4a NEW (VPOS 9 exact b4+M8
  b21-23,31,76-79, b5 const 25; NO pair
  in tier).
- C10-2SIG map EXACT x4/x6 (first 4/6
  split): c503ce05 x4 @103059-62 (==PB1
  sig ✓) + c503ee02 x6 @103063-68 (VPOS
  15 exact b4+M14 b2,3,22,23,30-35,80-83;
  b5 const 25; 10/10 diverge).
- QUAD-2T 809a1f2a x64 (PBA-adjacent
  4a->2a ✓; VPOS 10 exact b4+QM7+T2; NO
  R-block — first R-less quad ✓; b5
  const 25).
- T88-RING 02000000 (==P247T sig ✓
  direct cross-check; P242..246T same
  value per A-314/315/316/317), 88B
  payload all 256 ✓ (VPOS 17 exact
  b4,b5+TM8+TR7 partition over 0..87).
- Next P249 PB0 @103389 18e10200 NEW +
  103390 c503ce05 (==P248PB1) +
  103391..404 809a1f4a x14 (==P248PBA
  sig; window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0 (clean).
- NO R-block ✓; tails 2B b80,81 row-led
  4/4 distinct 6936/9336/30ea/5aea
  EXACT (r0/r1 share 2nd-B 36; r2/r3
  share 2nd-B ea); b82,83 const 3664
  quad-wide ✓.
- M-tails 16/16 ALL NEW vs P247T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [19,39,46,47,
  80-83] by COL 16/16; TR7 [40-42,76-79]
  by ROW 16/16 UNPAIRED (16 distinct;
  b42 in T-R ✓); tails SPLIT verified
  explicitly (b80-83 col-shared 16 cols,
  b76-79 row-shared 16 rows); b84-87
  const fd74651e EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 103041..103388: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xbb+2off)&FF 256/256;
  b5=0x25+(off>=35)+(off>=163) 256/256;
  edges 103167->103168 ff/25->01/26 +
  103295->103296 ff/26->01/27.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 69 (b5-const), quad 74 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
