# A-366 (viewer r10): Q-319 T10P255 P-head @105477 — CONFIRM all 3

First-hand bed 105477..105824 (q319
own; census RC=0 missing=0, 348/348)
+ P254T row0 105221..36 (own q318 bed
re-read) + P241T 100697/52 re-read +
P256 window 105825..44.

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 e4180300 (==P254PB0 re-read ✓),
  PB1 0dc83406 NEW, PBA 79824c63 NEW
  x16 @105479..94 (VPOS 8 exact b4+M7
  b9-11,76-79; b5 const 38; 16/16
  distinct, NO pair).
- C10-2SIG sandwich EXACT map:
  26c83406 x4 @105495-98 + 13641a03 x4
  @105499-502 + 26c83406 x2 @105503-04
  (VPOS 17 exact b4+M16
  b0-3,11,13-19,80-83; b12 SKIPPED ✓;
  b5 const 38; 10/10 diverge).
- QUADms 3-sig 009e1f76 x16 (row0) +
  608fcf66 x16 (row1) + 4089bf36 x32
  (rows2-3) NEW (VPOS 21 exact
  b4+QM4+5pair+R7+T4; b5 const 38).
- T88-RING 03000000 x256 (==P241T sig
  re-read @100697/52 ✓), 88B payload
  all 256 ✓ (VPOS 18 exact
  b4,b5+TM7+TR9 over 0..87).
- Next P256 PB0 @105825 641a0300 NEW +
  105826 e58c3506 NEW + PBA a0802f7c
  x16 @105827..42 + C10 e58c3506
  @105843+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM4 TAILS-ONLY b76-79 shared
  16/16 x3 vs row0.
- b12/b13/b14/b15/b19 PAIR-COLTABS:
  r0==r1 + r2==r3 identical 16/16 all
  5 (2x16-tab structure ✓; distinct
  16/10/8/6/26 exact).
- R7 sig-led b0-3,16-18 r2==r3 PAIRED
  16/16 cols, 3/4 EXACT (4089bf36856b85
  x2; r0 009e1f769e1850 + r1
  608fcf66d88719 distinct; full-sig
  row-led ✓; col0 hexes exact).
- Tails row-shared 4/4 distinct
  b3f8e313/492cce3a/feb89ebb/28b99ebb
  EXACT; r2/r3 share last 3B b89ebb
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P254T row-0
  (quad b76-79 16 distinct col-vals,
  zero overlap; true novelty).
- T88-ring STANDARD: TM7 [28-30,80-83]
  by COL 16/16; TR9 [16-19,23,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const a36fd765 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 105477..105824: 348/348
  exact (pay[4:6]==LE16((n<<1)|1),
  whole tier incl 88B cells).
- T88-ring b4=(0xc3+2off)&FF 256/256;
  b5=0x38+(off>=31)+(off>=159) 256/256;
  edges 105599->105600 ff/38->01/39 +
  105727->105728 ff/39->01/3a exact.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  C10 67 (b5-const), quad 63 (b5-const),
  T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers (observed==staged per
  group). NO D-class dips (group
  sig/size norms uniform incl 3-sig
  quad, lencode clean).

## geometry agrees on all 3 legs
