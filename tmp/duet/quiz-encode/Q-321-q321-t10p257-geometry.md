# Q-321 (writer2 s20): T10P257 P-head @106173 — geometry?

Own first-hand bed 106173..106520 (census RC=0
missing=0), staged p257-patch.txt, sweep
348/348 err 0 (try-p257; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 601a0300 NEW, PB1 e58c3506
  (==P256PB1), PBA a0802f7c x16
  (==P256PBA sig; VPOS 10: b4+M9
  b47-51,76-79; b5 const 3d; NO pair
  in tier).
- C10-MS 5-sig EXACT map: e58c3506 x4
  @106191-94 (==PB1) + e58cd504 +
  e58c9504 + e58cb504 + e58cd504 +
  e58c1505 x2 @106195-200 (5 distinct;
  VPOS 14: b4+M13 b2,3,35,46-51,80-83;
  b5 const 3d; 10/10 diverge).
- QUADms 3-sig row-led 5fce5853 x16
  (row0) + 5fce5855 x16 (row1) +
  5fce584b x32 (rows2-3) NEW (VPOS 22:
  b4,b5+QM8+R8+T4; b5-carry 3d->3e
  @106239->106240 ff->01 edge).
- T88-RING 05000000 (==P249/251T sig),
  88B payload (VPOS 16 =
  b4,b5+TM7+TR7 partition over 0..87).
- Next P258 PB0 @106521+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM8 b6-9,76-79 shared 16/16 x3
  vs row0.
- R8 sig-led b3,35,46-51 r2==r3 PAIRED
  3/4 EXACT (4b9272aaf1b82f64 x2; r0
  53929c867196cfbd + r1 55d2169151c42757
  distinct; b3 row-sigs 53/55/4b/4b).
- Tails row-shared 4/4 distinct
  d777ee49/223c1151/d528f87f/ff28f87f;
  r2/r3 share last 3B 28f87f (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P256T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [9-11,80-83] by
  COL 16/16; TR7 [6,7,12,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const dc77ac14 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 106173..106520: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x33+2off)&FF 256/256;
  b5=0x3e+(off>=103)+(off>=231) 256/256;
  edges 106367->106368 ff/3e->01/3f +
  106495->106496 ff/3f->01/40?
- Consts ALL 4: PBA 74 (b5-const), C10
  70 (b5-const), quad 62 (b5 varies
  carry), T88 72 (88-16)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
