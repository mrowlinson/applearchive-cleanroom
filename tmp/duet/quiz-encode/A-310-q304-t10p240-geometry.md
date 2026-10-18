# A-310 (viewer r3): Q-304 T10P240 P-head @100257 — CONFIRM all 3

First-hand bed 100257..100620 (q304.py
new, 88B-aware; census extended
100273..100620 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 3f550100 NEW, PB1 4dc2a402 NEW,
  PBA a0955736 NEW (VPOS 11 exact
  b4+M10 b14,15,21-23,31,76-79, b5
  const 0f; NO pair in tier).
- C10-2SIG map EXACT: 4dc2a402 x3
  @100275-77 (==PB1 ✓) + 4dc25401 x7
  @100278-84 (VPOS 21 exact b4+M20
  b2,3,20-27,30-35,80-83; b5 const 0f;
  10/10 diverge).
- QUAD 4dc25415 NEW (VPOS 17 exact
  b4+M6+R6+T4; b5 const 0f).
- T88-RING 01000000 (==P231/232/236/237/
  238/239T sig ✓), 88B payload all 256 ✓
  (VPOS 17 exact b4,b5+M9+R6 partition
  over 0..87).
- Next @100605 3f550100 (==P240PB0
  REPEAT ✓) + 100606 4dc2a402 (==P240PB1
  ✓) + 100607..20 a0955736 (==P240PBA
  sig, x14 ✓).

## 2. quad + T-ring: CONFIRM
- Quad M6 b36,37,76-79 shared 16/16 x3
  vs row0.
- NO b42 coupling (b42 const 0x9f all
  64) — no XOR/ADD leg, as staged.
- R6 b22,23,30,32-34 TRIPLE-PAIRED 2/4
  EXACT: r1==r2==r3 f14c2234156e x3;
  r0 2540eeb42b46 distinct.
- Tails row-shared 4/4 distinct
  58bdc6b0/ce29d41d/f829d41d/f9b1c924
  EXACT; r1/r2 share last 3B 29d41d.
- M-tails 16/16 ALL NEW vs P239T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [19,27,39,46,47,
  80-83] by COL 16/16; R6 [40,41,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT verified explicitly
  (b80-83 col-shared 16 cols, b76-79
  row-shared 16 rows); b84-87 const
  0237bbef EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 100257..100604: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xfb+2off)&FF 256/256;
  b5=0x0f+(off>=3)+(off>=131) 256/256;
  edges 100351->100352 ff/0f->01/10 +
  100479->100480 ff/10->01/11.
- Consts ALL 4 EXACT: PBA 73 (b5-const),
  C10 63 (b5-const), quad 67 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
