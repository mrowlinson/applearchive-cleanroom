# A-339 (viewer r8): Q-339 T10P275 P-head @112437 — CONFIRM all 3

First-hand bed 112437..112784 (qr8bed own
oracle runs; census RC=0 missing=0) +
P274T ref 112181..96 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b2690700 SAME-as-P274PB0 ✓
  (byte-equal to n112089 first-hand),
  PB1 0d2bd60e NEW, PBA16-PLAIN
  809907fc x16 @112439-54 (VPOS 8
  exact b4+M7 b36-38,76-79; b0 const
  80, b5 const 6e; 16/16 distinct, NO
  pair in tier).
- C10-2SIG EXACT map first-hand:
  0d2bd60e x5 @112455-59 + 0d2b6607 x5
  @112460-64 (VPOS 17 exact b4+M16
  b2,3,34-43,80-83; b5 const 6e;
  10/10 diverge; FIRST 5+5 C10 map
  shape ✓).
- QUAD1s 1-sig 8099077c x64 (VPOS 20
  exact b4,b5+QM7+b42+R6+T4; b5 step
  o>=47).
- T88-RING 07000000, 88B payload all
  256 ✓ (VPOS 18 exact b4,b5+TM8+TR8
  partition over 0..87).
- Next P276 PB0 @112785 b6690700 NEW +
  112786 0d2b660e NEW + PBA ddb062e6
  x16 @112787-802 + C10 386c550f
  @112803+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b34,35,43,76-79 (same positions
  as P267 ✓) shared 16/16 x3 vs row0.
- b42: row-XOR X=[00,1f,1f,1f] 64/64
  AND row-ADD A=[0,3,3,3] 64/64 — TIE
  CONFIRMED first-hand (r1==r2==r3 tab
  shape = X42-family ✓; staged XOR by
  b42-family precedent P211-P267 9th
  stands flagged as tie).
- R6 b36-41 r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 3cddeeb89103 x3; r0
  38daeca3310a distinct).
- Tails row-shared 4/4 distinct
  74fac331/bcfaf065/e1faf065/06fbf065
  EXACT; r1/r2 share last 3B faf065 ✓.
- M-tails 16/16 ALL NEW vs P274T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [52-55,80-83]
  by COL 16/16; TR8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const f9b5ac58 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 112437..112784: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xa3+2off)&FF 64/64;
  b5=0x6e+(off>=47) 64/64; edge
  112511->112512 ff/6e->01/6f (end of
  row2 o=46->47 ✓).
- T88-ring b4=(0x23+2off)&FF 256/256;
  b5=0x6f+(off>=111)+(off>=239) 256/256;
  edges 112639->112640 ff/6f->01/70 +
  112767->112768 ff/70->01/71.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  C10 67 (b5-const), quad 64 (b5-step),
  T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
