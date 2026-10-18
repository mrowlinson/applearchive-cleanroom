# A-363 (viewer r10): Q-316 T10P252 P-head @104433 — CONFIRM all 3

First-hand bed 104433..104780 (q316
own; census RC=0 missing=0, 348/348)
+ P251T row0 104177..92 (own q315 bed
re-read) + P253 window 104781..800.

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 80fc0200 NEW, PB1 5d169d05 NEW,
  PBA dc65d159 x16 @104435..50 (VPOS 8
  exact b4,b5+M6 b6,7,76-79; b5-carry
  2f->30 @104447->104448 ff->01 edge
  exact; 16/16 distinct, NO pair).
- C10-2SIG sandwich EXACT map:
  8cc03106 x4 @104451-54 + 46e01803 x1
  @104455 + 8cc03106 x5 @104456-60
  (VPOS 18 exact b4+M17
  b0-3,6-8,10,11,48-51,80-83; b9
  SKIPPED ✓; b5 const 30; 10/10
  diverge).
- QUADms col-15-frag 7d091c63 x15 +
  69091c63 x1 PER ROW x4 rows NEW
  (frag @c15 all rows; VPOS 20 exact
  b4+QM9+R6+T4; b5 const 30).
- T88-RING 06000000 NEW x256, 88B
  payload all 256 ✓ (VPOS 18 exact
  b4,b5+TM8+TR8 over 0..87).
- Next P253 PB0 @104781 e0180300 NEW +
  104782 0d4a3706 NEW + PBA a096b766
  x16 @104783..98 + C10 6d4b3306
  @104799+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM9 sig-led b0 + b9-12,76-79
  shared 16/16 x3 vs row0 (b0 col-led:
  7d x15 + 69 @c15 exact).
- R6 b6,7,48-51 r1==r2 PAIRED 16/16
  cols, 3/4 EXACT (1f2fdb590062 x2;
  r0 f969885a06c1 distinct; r3
  1f2fdc590062 1B-off dc-vs-db; col0
  hexes exact).
- Tails row-shared 4/4 distinct
  f470a4a5/6e2ac0e5/982ac0e5/9951481b
  EXACT; r1/r2 share last 3B 2ac0e5
  (matching R-pair); r3 distinct.
- M-tails 16/16 ALL NEW vs P251T row-0
  (quad b76-79 16 distinct col-vals,
  zero overlap with P251T-row0
  e273c2dd; true novelty).
- T88-ring STANDARD: TM8 [8-10,19,76-79]
  by COL 16/16; TR8 [13-16,80-83] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b76-79 col / b80-83 row
  (swapped vs P251 ✓); b84-87 const
  e0a4c350 EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 104433..104780: 348/348
  exact (pay[4:6]==LE16((n<<1)|1),
  whole tier incl 88B cells).
- T88-ring b4=(0x9b+2off)&FF 256/256;
  b5=0x30+(off>=51)+(off>=179) 256/256;
  edges 104575->104576 ff/30->01/31 +
  104703->104704 ff/31->01/32 exact.
- Consts ALL 4 EXACT: PBA 76 (b5-carry),
  C10 66 (b5-const), quad 64 (b5-const),
  T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers (observed==staged per
  group). NO D-class dips (group
  sig/size norms uniform incl ms-frag,
  lencode clean).

## geometry agrees on all 3 legs
