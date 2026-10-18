# Q-308 (writer2 s20): T10P244 P-head @101649 — geometry?

Own first-hand bed 101649..101996 (census RC=0
missing=0), staged p244-patch.txt, sweep
348/348 err 0 (try-p244; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 44620100 NEW, PB1 3d319602
  NEW, PBA de136329 NEW (VPOS 7:
  b4+M6 b6,7,76-79; b5 const 1a;
  NO pair in tier).
- C10-2SIG EXACT map: b8a9df02 x4
  @101667-70 + dcd46f01 x2 @101671-72 +
  b8a9df02 x4 @101673-76 (VPOS 18:
  b4+M17 b0-3,6-8,10,11,48-51,80-83;
  b9 SKIPPED; b5 const 1a; 10/10
  diverge).
- QUAD-FRAG d04d/c24d/a09b/859b NEW
  (VPOS 24: b4+QM5+b0+b9+b10+b11+R10+
  T4; b5 const 1a).
- T88-RING 02000000 (==P242/243T sig),
  88B payload (VPOS 19 =
  b4,b5+TM8+b8+TR8 partition over 0..87).
- Next P245 PB0 @101997+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM5 b12,76-79 shared 16/16 x3
  vs row0 (M12 2-valued {76,96};
  M-tails carry 16/16).
- b0 2x2-FRAG: (r0,r123) x (c<11,c>=11)
  = d0/c2/a0/85 EXACT (11+5 col split;
  row-led sigs d04d/c24d row0,
  a09b/859b rows1-3).
- b9/b10/b11 DUAL-COLTABS: r0-tab vs
  r123-tab (r1==r2==r3 identical all 3;
  r0 distinct; no uniform xor/add —
  staged 2x16 tabs each).
- R10 b1-3,6-8,48-51 r1==r2==r3 TRIPLE
  2/4 EXACT (9bfa2d110601fedbf5b9 x3;
  r0 4dfd1685ee000c5f8a75 distinct;
  sig-led b1-3).
- Tails row-shared 4/4 distinct
  a3d62dc6/7e8e0fb4/a88e0fb4/d28e0fb4;
  r1/r2/r3 share last 3B 8e0fb4
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P243T (row-0
  reference, true novelty).
- T88-ring b8 COL-TAB + ROW-XOR
  X=00x11+20x5 (11+5 row split; ADD-e0
  tie flagged, staged XOR by family
  precedent); M8 [9-11,19,76-79] by COL
  16/16; R8 [13-16,80-83] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b76-79 col / b80-83 row; b84-87 const
  3e1eb3cc (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 101649..101996: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xdb+2off)&FF 256/256;
  b5=0x1a+(off>=19)+(off>=147) 256/256;
  edges 101759->101760 ff/1a->01/1b +
  101887->101888 ff/1b->01/1c?
- Consts ALL 4: PBA 77 (b5-const), C10
  66 (b5-const), quad 60 (b5-const),
  T88 69 (88-19)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
