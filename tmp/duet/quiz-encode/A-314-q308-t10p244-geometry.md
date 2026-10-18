# A-314 (viewer r3): Q-308 T10P244 P-head @101649 — CONFIRM all 3

First-hand bed 101649..102012 (q308.py
new, 88B-aware; census extended
101665..102012 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 44620100 NEW, PB1 3d319602 NEW,
  PBA de136329 NEW (VPOS 7 exact b4+M6
  b6,7,76-79, b5 const 1a; NO pair in
  tier).
- C10-2SIG sandwich map EXACT: b8a9df02
  x4 @101667-70 + dcd46f01 x2 @101671-72
  + b8a9df02 x4 @101673-76 (VPOS 18
  exact b4+M17 b0-3,6-8,10,11,48-51,
  80-83; b9 SKIPPED ✓; b5 const 1a;
  10/10 diverge).
- QUAD-FRAG d04d/c24d/a09b/859b NEW
  (sigs d04dfd16/c24dfd16/a09bfa2d/
  859bfa2d; VPOS 24 exact b4+QM5+b0+b9+
  b10+b11+R10+T4; b5 const 1a).
- T88-RING 02000000 (==P242T and ==P243T
  both cross-checked first-hand ✓✓),
  88B payload all 256 ✓ (VPOS 19 exact
  b4,b5+TM8+b8+TR8 partition over 0..87).
- Next P245 PB0 @101997 d46f0100 NEW +
  101998 b553d702 NEW + 101999..102012
  2085c72e x14 NEW (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM5 b12,76-79 shared 16/16 x3 vs
  row0 (M12 2-valued 76/96 EXACT 11+5 —
  matching the frag col split).
- b0 2x2-FRAG 64/64 EXACT: (r0,c<11)=d0,
  (r0,c>=11)=c2, (r123,c<11)=a0,
  (r123,c>=11)=85 (11+5 col split;
  row-led sigs d04d/c24d row0,
  a09b/859b rows1-3 ✓).
- b9/b10/b11 DUAL-COLTABS: r1==r2==r3
  identical all 3 ✓; r0-tab distinct as
  a whole (r0-vs-r1 entry matches:
  b9 1/16, b10 0/16, b11 0/16 —
  micro-note: single coincidental match
  in b9, tabs still wholly distinct; no
  uniform xor/add, 2x16 tabs stand).
- R10 b1-3,6-8,48-51 TRIPLE 2/4 EXACT:
  r1==r2==r3 9bfa2d110601fedbf5b9 x3;
  r0 4dfd1685ee000c5f8a75 distinct;
  sig-led b1-3 ✓.
- Tails row-shared 4/4 distinct
  a3d62dc6/7e8e0fb4/a88e0fb4/d28e0fb4
  EXACT; r1/r2/r3 share last 3B 8e0fb4
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P243T (row-0
  reference, true novelty).
- T88-ring b8 COL-TAB + ROW-XOR
  X=00x11+20x5 256/256 ✓ AND ADD-e0
  256/256 ✓ — TIE first-hand (11+5 row
  split; staged XOR stands by family
  precedent; flagged as tie per
  request). TM8 [9-11,19,76-79] by COL
  16/16; TR8 [13-16,80-83] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  verified explicitly (b76-79 col-shared
  16 cols, b80-83 row-shared 16 rows);
  b84-87 const 3e1eb3cc EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 101649..101996: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xdb+2off)&FF 256/256;
  b5=0x1a+(off>=19)+(off>=147) 256/256;
  edges 101759->101760 ff/1a->01/1b +
  101887->101888 ff/1b->01/1c.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  C10 66 (b5-const), quad 60 (b5-const),
  T88 69 (88-19).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
