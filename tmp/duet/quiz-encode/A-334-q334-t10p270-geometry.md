# A-334 (viewer r8): Q-334 T10P270 P-head @110697 — CONFIRM all 3

First-hand bed 110697..111044 (qr8bed own
oracle runs; census RC=0 missing=0) +
P269T ref 110441..56 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 a6930300 NEW, PB1 a5322507
  SAME-as-P269C10sig ✓ (byte-equal to
  n110367 first-hand), PBA16-PLAIN
  208c277e x16 @110699-714 (VPOS 8
  exact b4+M7 b34,42,43,76-79; b0
  const 20, b5 const 60; 16/16
  distinct, NO pair in tier).
- C10-CARRY a532450e x10 @110715-24
  (VPOS 14 exact b4,b5+M12
  b34,35,41-46,80-83; b5 60+step5;
  10/10 diverge).
- QUAD1s 1-sig 208c27fe x64 (VPOS 20
  exact b4+QM9+R6+T4; b5 const 61).
- T88-ROWTAIL 0f000000, 88B payload all
  256 ✓ (VPOS 18 exact
  b4,b5+TM7+TR5+TT4 partition over
  0..87; tails ROW-led not col-split).
- Next P271 PB0 @111045 76270700 NEW
  (new 7627 family) + 111046 fcec550e
  NEW + PBA split 34cc5ee5 x10 +
  20cc5ee5 x6 @111047-62 + C10 c3ec550e
  @111063+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM9 b47-51,76-79 shared 16/16 x3
  vs row0; NO frags (0 MIXED ✓ —
  vpos partitions exactly into b4 +
  QM9 + R6 + T4).
- R6 b34,35,42,43,45,46 (b44-skipped
  const 54 ✓) r1==r2==r3 LAST3-PAIRED
  2/4 EXACT (r123 7b9e0c9f6478 x3; r0
  3b8d37cfc067 distinct).
- Tails row-shared 4/4 distinct
  ea14f78d/4e664444/73664444/98664444
  EXACT; r1/r2/r3 share last 3B 664444
  (tails echo the R last3-pairing ✓).
- M-tails 16/16 ALL NEW vs P269T (row-0
  reference, true novelty).
- T88-ring ROWTAIL: TM7 [6,7,12,76-79]
  by COL 16/16; TR5 [51-55] by ROW
  16/16 UNPAIRED (16 distinct); tails
  b80-83 ROW-led 16/16 (staged
  _T10P270TT by q, 2nd rowtail T88 ✓);
  b84-87 const bd664444 EXACT
  (1 ring-wide; shares 664444 with
  quad r123 tails ✓).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 110697..111044: 348/348
  exact (whole tier incl 88B cells).
- C10 b4=(0xf7+2off)&FF 10/10;
  b5=0x60+(off>=5) 10/10; edge
  110719->110720 ff/60->01/61 ✓.
- T88-ring b4=(0x8b+2off)&FF 256/256;
  b5=0x61+(off>=59)+(off>=187) 256/256;
  edges 110847->110848 ff/61->01/62 +
  110975->110976 ff/62->01/63.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  C10 70 (b5-step), quad 64 (b5-const),
  T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
