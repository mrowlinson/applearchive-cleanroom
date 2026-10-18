# A-297 (viewer r3): Q-291 T10P227 P-head @95733 — CONFIRM + 2 prose fixes

First-hand bed 95733..96096 (q291.py new;
census 95749..96096 RC=0 missing=0).

## 1. shape: CONFIRM + 2 prose fixes
- 348 cells sizes {(100,84)}. PB0 bf250000
  (==P226PB0), PB1 8e634e00 NEW, PBA
  8e63b604 NEW (VPOS 8 exact b4,b5+M6
  b36,37,76-79; b5-carry eb->ec @95743->
  95744 ff->01 edge).
- PBB10 2-sig map EXACT: 96x3 @95751,52,53
  8e639600 + 4ex7 @95754..95760 8e634e00
  (VPOS 19 exact joint b4+M18 b2,23,
  32-43,80-83, b5 const ec, 10/10
  diverge; NO pair/C8). FIX: the x7 4e
  group (second-listed) ==PB1 — not the
  first-listed 96 ("first ==PB1" label
  wrong way round).
- QUADmotif 2 sigs 8e63ee04 + 8e63f604
  (VPOS 20 exact; b5 const ec single-
  valued). FIX: partition as written
  "b4,b5+M8+R6+b42+T4" sums 21 ≠ 20 —
  ground truth ex-b5 (b4+M8+R6+b42+T4 =
  1+8+6+1+4 = 20 ✓); "b5 const ec" + 64
  already right.
- T-RING a0990745 (==P226T sig ✓; VPOS 19
  exact = b4,b5+M8+R9 partition).
- Next @96081 794b0000 NEW (+96082
  8e638e00, 96083/84 ee38e608 observed).

## 2. quad + T-ring: CONFIRM
- Quad M8 b2,34,35,43,76-79 shared 16/16
  x3 vs row0; sig-led col b2 ee x11 /
  f6 x5 cols 0-10/11-15 EXACT.
- b42 row-xor X=[00,03,05,04] 64/64 vs
  row-0 M42; all-4-lows-distinct c/f/9/8
  holds all 16 cols (all M42 lows == c:
  9c/3c/1c/bc/7c/5c/dc set; col lows =
  c^X[r] = c,f,9,8 ✓ mechanism + col-0
  explicit 9c,9f,99,98).
- R6 b36-41 UNPAIRED 4/4 EXACT values
  (cb5bae95f046/9b5a58ebb025/dddb554c10a8/
  46de61cff06d, all distinct).
- Tails row-shared 4/4 distinct
  4b696cac/f3c5f3b1/bd589836/5c9fa7af
  EXACT.
- M-tails 16/16 ALL NEW vs P226T under
  BOTH references (row-0 set 16 + col-0
  rows set 1 — collapses for standard
  rings since R lacks 76-79; novelty 16
  either way, unambiguous).
- T-ring STANDARD: M8 [48-51,76-79] by
  COL 16/16; R9 [14,34,35,42,43,72-75]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 95733..96080: 348/348
  exact (whole tier).
- T-ring b4=(0xa3+2off)&FF 256/256;
  b5=0xec+(off>=47)+(off>=175) 256/256;
  edges 95871->95872 ff/ec->01/ed +
  95999->96000 ff/ed->01/ee.
- Consts ALL 4 EXACT: PBA 76 (b5 varies
  carry ✓), PBB 65 (b5-const ✓), quad 64
  (b5-const ✓), T 65.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 2 Q-prose labels fixed (counts stand)
