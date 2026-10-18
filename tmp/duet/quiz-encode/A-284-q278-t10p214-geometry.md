# A-284 (viewer r3): Q-278 T10P214 P-head @91209 — CONFIRM + CORRECTION

First-hand bed 91209..91572 (q278.py new;
census 90877..91920 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 4b080000
  REPEAT, PB1 8f9b1100 (==P213B10sig),
  PBA 8f9b3d01 NEW (VPOS 10 exact b4+M9
  b23,34,35,42,43,76-79, b5 const c8).
- PBB10 8f9b1100 (==PB1) single-sig
  (VPOS 13 exact b4+M12 b34,35,41-46,
  80-83, b5 const c8, 10/10 diverge; NO
  pair/C8).
- QUAD 8f9b0901 (==P213Q; VPOS 21 exact
  b4,b5+M7+R12; b5-carry c8->c9 @91263->
  91264 ff->01 edge).
- T-RING f6b89910 NEW (VPOS 17 exact =
  b4,b5+M8+R7 partition).
- Next @91557 4b080000 REPEAT x3 + 91558
  f89f1000 NEW + 91559/60 64ff0901 NEW.

## 2. quad + T-ring: CONFIRM + R-pair fix
- Quad M7 b48-50,76-79 shared 16/16 x3 vs
  row0.
- CORRECTION: R8 b34,35,41-46 is r1==r3
  PAIRED (ce724597c793a218 both; 3/4
  distinct: r0 3c77e585e7d3680d, r2
  426d059977339b1e) — NOT unpaired 4/4.
- Tails row-shared 4/4 distinct
  f778fa40/7b78af92/3d6e68b8/7ab5df92
  EXACT (r1/r3 share R, differ tails).
- B10 M-positions == quad-R positions
  12/12 set-exact.
- M-tails 16/16 ALL NEW vs P213T (row-0
  reference, true novelty).
- T-ring STANDARD: M8 b6-9,76-79 by COL
  16/16; R7 b48-50,72-75 by ROW 16/16
  UNPAIRED (16 distinct; b48-50 shared
  with QM ✓); tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 91209..91556: 348/348
  exact (whole tier).
- T-ring b4=(0x4b+2off)&FF 256/256;
  b5=0xc9+(off>=91)+(off>=219) 256/256;
  edges 91391->91392 ff/c9->01/ca +
  91519->91520 ff/ca->01/cb.
- Consts ALL 4 EXACT: PBA 74 (b5-const
  ✓), PBB 71 (b5-const ✓), quad 63
  (b5 varies carry ✓), T 67.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; R8 r1==r3 paired (not 4/4)
