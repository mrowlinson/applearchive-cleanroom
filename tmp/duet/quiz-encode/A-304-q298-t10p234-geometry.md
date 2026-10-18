# A-304 (viewer r3): Q-298 T10P234 P-head @98169 — CONFIRM all 3

First-hand bed 98169..98532 (q298.py new,
88B-aware; census 98191..99576 RC=0
missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 8c470100 NEW, PB1 ee8c4701 NEW,
  PBA16-MS 13-sig (aaf5/abf5/acf5/aef5/
  aeed/b6ed/dc3d/e43d/e63d/eb3d/ec3d/
  ee3d/f43d families; VPOS 11 exact
  b4,b5+M9 b0-2,11,19,76-79; b5-carry
  fe->ff @98175->98176 ff->01 edge;
  16/16 diverge; NO pair in tier).
- FRAG10 7-sig map EXACT: cd898b02 x3
  @98187-89 + ddfc8f02 + 958d8c02 +
  65358202 + 25b38502 + 3dd58902 +
  85768302 + 958d8c02 (positions+values
  all match; VPOS 14 exact b4+M13
  b0-2,11,18-22,80-83, b5 const ff,
  10/10 diverge).
- QUAD 40806734 NEW (VPOS 19 exact
  b4+M7+R7+T4, b5 const ff).
- T88-STEP-RING 02000000 NEW, 88B payload
  all 256 ✓ (VPOS 17 exact =
  b4,b5+M7+R7+b6step partition over
  0..87).
- Next @98517 8c470100 (==P234PB0 REPEAT)
  + 98518 45f44701 NEW + 98519..32
  45f47714 x14 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b24-26,76-79 shared 16/16 x3 vs
  row0.
- R7 b13,14,18-22 r0==r3 OUTER-PAIRED 3/4
  EXACT (b49bc46f3243a3 x2; r1/r2
  distinct, differ exactly 1B: byte-2
  e8/f8 ✓).
- Tails row-shared 4/4 distinct
  2e189304/f98d105d/311be64a/55426037
  EXACT.
- M-tails 16/16 ALL NEW vs P233T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [27,34,35,80-83]
  by COL 16/16; R7 [28-30,76-79] by ROW
  16/16 UNPAIRED (16 distinct); b6
  step-coupled 0x66+(off>=43) 256/256
  (flip rides first b5 step ✓); tails
  SPLIT b80-83 col (16) / b76-79 row
  (16); b84-87 const a0a46037 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 98169..98516: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xab+2off)&FF 256/256;
  b5=(0xff+(off>=43)+(off>=171))&FF
  256/256 (WRAP ff->00->01 — first b5
  wrap); edges 98303->98304 ff/ff->01/00
  + 98431->98432 ff/00->01/01.
- Consts ALL 4 EXACT: PBA 73 (b5 varies
  carry ✓), FRAG 70 (b5-const ✓), quad 65
  (b5-const ✓), T88 71 (88-17 ✓).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
