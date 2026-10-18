# A-335 (viewer r8): Q-335 T10P271 P-head @111045 — CONFIRM all 3

First-hand bed 111045..111392 (qr8bed own
oracle runs; census RC=0 missing=0) +
P270T ref 110789..804 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 76270700 NEW (new 7627 family),
  PB1 fcec550e NEW, PBA16-SPLIT10/6
  34cc5ee5 x10 @111047-56 + 20cc5ee5
  x6 @111057-62 EXACT split (VPOS 10
  exact b0,b4+M8 b9-12,76-79; b5
  const 63; 16/16 distinct, NO pair in
  tier).
- C10-1SIG c3ec550e x10 @111063-72
  (VPOS 12 exact b4+M11 b13-19,80-83;
  b5 const 63; 10/10 diverge).
- QUAD2s 2-sig c09ba7f8 x16 (row0) +
  009d17f8 x48 (rows1-3) EXACT
  row-split (VPOS 20 exact
  b4,b5+QM8+R6+T4; b5 step o>=31).
- T88-RING 0e000000, 88B payload all
  256 ✓ (VPOS 15 exact b4,b5+TM6+TR7
  partition over 0..87).
- Next P272 PB0 @111393 f62a0700 NEW
  (new f62a family) + 111394 25bd5c0e
  NEW + PBA c0935ff8 x16 @111395-410
  + C10 25bd5c0e @111411+ (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b12-14,19,76-79 shared 16/16
  x3 vs row0; NO frags (0 MIXED ✓).
- R6 sig-led b0-2,16-18 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  009d17da74de x3; r0 c09ba7a8f99b
  distinct).
- Tails row-shared 4/4 distinct
  d45a1a47/81d84934/a6d84934/cbd84934
  EXACT; r1/r2/r3 share last 3B d84934
  (tails echo the R last3-pairing ✓).
- M-tails 16/16 ALL NEW vs P270T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM6 [28,29,80-83]
  by COL 16/16; TR7 [20-22,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const f761b25f EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 111045..111392: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xc3+2off)&FF 64/64;
  b5=0x63+(off>=31) 64/64; edge
  111103->111104 ff/63->01/64 (end of
  row1 o=30->31 ✓).
- T88-ring b4=(0x43+2off)&FF 256/256;
  b5=0x64+(off>=95)+(off>=223) 256/256;
  edges 111231->111232 ff/64->01/65 +
  111359->111360 ff/65->01/66.
- Consts ALL 4 EXACT: PBA 74 (b5-const),
  C10 72 (b5-const), quad 64 (b5-step),
  T88 73 (88-15).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
