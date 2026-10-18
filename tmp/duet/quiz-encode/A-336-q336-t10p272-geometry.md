# A-336 (viewer r8): Q-336 T10P272 P-head @111393 — CONFIRM all 3

First-hand bed 111393..111740 (qr8bed own
oracle runs; census RC=0 missing=0) +
P271T ref 111137..52 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 f62a0700 NEW (new f62a family),
  PB1 25bd5c0e NEW, PBA16-PLAIN
  c0935ff8 x16 @111395-410 (VPOS 8
  exact b4+M7 b21,22,31,76-79; b0
  const c0, b5 const 66; 16/16
  distinct, NO pair in tier).
- C10-1SIG 25bd5c0e x10 @111411-20
  (VPOS 13 exact b4+M12
  b22,23,30-35,80-83; b5 const 66;
  10/10 diverge; head-sig == PB1
  sig ✓).
- QUAD1s 1-sig c0935ff8 x64 (VPOS 19
  exact b4+QM7+R7+T4; b5 const 66).
- T88-RING 0a000000, 88B payload all
  256 ✓ (VPOS 16 exact b4,b5+TM7+TR7
  partition over 0..87).
- Next P273 PB0 @111741 f22a0700 NEW
  (f62a-family f2 variant) + 111742
  25bd5c0e (==P272PB1) + PBA c0935ff8
  x16 @111743-58 + C10-5SIG map
  25bd5c0e x5/25bdbc0c/25bdec0a/
  25bd3c0b/25bdcc0b x2 @111759-68
  (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b36-38,76-79 (same positions
  as P264 ✓) shared 16/16 x3 vs row0;
  NO frags (0 MIXED ✓).
- R7 b22,23,30-34 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  3f8f317eb5563d x3; r0 87c77df9550a1a
  distinct).
- Tails row-shared 4/4 distinct
  d5b4b22a/44398e25/69398e25/43399225
  EXACT; r1/r2 share last 3B 398e25 ✓.
- M-tails 16/16 ALL NEW vs P271T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [39,46,47,80-83]
  by COL 16/16; TR7 [40-42,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const b874e2de EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 111393..111740: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xfb+2off)&FF 256/256;
  b5=0x66+(off>=3)+(off>=131) 256/256;
  edges 111487->111488 ff/66->01/67 +
  111615->111616 ff/67->01/68.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  C10 71 (b5-const), quad 65 (b5-const
  = 84-19 ✓ per A-328 rule), T88 72
  (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
