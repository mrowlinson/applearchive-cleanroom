# Q-297 (writer2 s20): T10P233 P-head @97821 — geometry?

Own first-hand bed 97821..98168 (census RC=0
missing=0), staged p233-patch.txt, sweep
348/348 err 0 (try-p233; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 043b0100 NEW, PB1 dd1a3f01
  (==P232PB1), PBA dd1abf13 (==P232Q sig)
  NEW (VPOS 9: b4+M8 b48-51,76-79; b5
  const fc).
- PAIR 97839..97840 dd1a7f02 (==P232PAIR;
  diff b4+b80 only).
- FRAG8 6-sig EXACT map: 97841 6f02 +
  97842 9f01 + 97843 bf01 + 97844 df01 +
  97845,46 ef01 x2 + 97847 cf01 + 97848
  bf01 (all dd1a....; VPOS 21: b4+M20
  b2,3,20,21,23-27,35,46-51,80-83; b5
  const fc; 8/8 diverge).
- QUADms row-pair-sig daadf11c (rows
  0,3) / daadf11e (rows 1,2) NEW (VPOS
  20: b4+M6+R9+T4; b5 const fc).
- T88-RING 01000000 (==P231/232T sig),
  88B payload (VPOS 15 = b4,b5+M7+R6
  partition over 0..87).
- Next @98169 8c470100 NEW + 98170
  ee8c4701 NEW + 98171.. multi-sig head
  (aaf5/abf5/acf5/aef5/aeed x2/b6ed/
  dc3d/e43d x3/e63d/eb3d/ec3d...).

## 2. quad + T-ring?
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0.
- R9 b3,23,35,46-51 r1==r2 PAIRED 3/4
  EXACT (1e2517d802718a4752 x2; r0/r3
  distinct; sig-led b3 row-pairs
  1c/1e/1e/1c).
- Tails row-shared 4/4 distinct
  e72e30b8/196917a6/436917a6/20377b54;
  r1/r2 share last 3B 6917a6 (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P232T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [17-19,80-83] by
  COL 16/16; R6 [6,7,76-79] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b80-83 col / b76-79 row; b84-87
  const (1 ring-wide)?

## 3. counters + dips?
- Odd-lencode ALL 97821..98168: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xf3+2off)&FF 256/256;
  b5=0xfc+(off>=7)+(off>=135) 256/256;
  edges 97919->97920 ff/fc->01/fd +
  98047->98048 ff/fd->01/fe?
- Consts ALL 4: PBA 75 (b5-const), FRAG
  63 (b5-const), quad 64 (b5-const),
  T88 73 (88-15)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
