# A-355 (viewer r8): Q-355 T10P291 @118005 — CONFIRM all legs

First-hand bed 118005..118352 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n118005 5f6f1300 SAME-as-P290PB0
  ✓ (byte-equal first-hand), PB1
  n118006 2b81c726 NEW.
- PBA88-STEP n118007-22 16x88B
  02000000 (M8 b40-43,80-83 16/16
  distinct ✓; VPOS 10 = b4,b5+M8 over
  88; b0 const 02; b5 0x99+(o>=9),
  edge o8->9 n118015->118016
  ff/99->01/9a ✓; 16/16 distinct;
  consts 78 ✓).
- C10-2SIG ordered map first-hand:
  2b81c726 x8 @118023-30 + 2b816713 x2
  @118031-32 (2-sig 8+2 ✓; M16
  b2,3,34-43,80-83 10/10 ✓; VPOS 17;
  b5 const 9a; 10/10 diverge; consts
  67 ✓).
- QUAD88-2SIG-FRAG n118033-96 88B-pay:
  row0 01000000 x16 + rows1-3
  02000000 x48 EXACT row-split (VPOS
  21 = b4+M4+R12+F4 over 88; b5
  const 9a = full odd lencode ✓;
  consts 67 ✓).
- T88-RING256 n118097-352 sig 23000000
  (VPOS 19 = b4,b5+TM9+TR8 partition
  over 0..87; b51-skipped const dc
  ✓).
- Next P292 PB0 @118353 436f1300 NEW +
  PB1 2b81e720 NEW + PBA88 02000000
  x16 + C10-2SIG 08075220 x7 +
  84032910 x3 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M4 b80-83 by COL 16/16 (16
  distinct ✓).
- Quad R12 b0,19,40-45,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples incl sig-led b0:
  r0 01175bdd…/r1 022f0cdf…/r2
  022f0cdf…/r3 022f0ddf… — r1/r2
  share 6B-prefix, all 4 differ).
- FRAG b38,39,46,47 rowpair-tabs EXACT
  first-hand: r1==r2==r3 16/16 per
  position AND r0-tab differs from
  r123-tab 16/16 per position (clean
  r0-row vs r123-row split, all 4).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M9 [50,52-55,80-83] (b51-skipped)
  by COL 16/16; R8 [38,39,46,47,
  76-79] by ROW 16/16 UNPAIRED; tails
  SPLIT b80-83 col / b76-79 row
  (standard); b84-87 const 1537fc9a
  first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 118005..118352:
  348/348 exact.
- T88 b4 = 0xa3 step2 256/256; b5 =
  0x9a+(o>=47)+(o>=175) 256/256;
  edges o46->47 (n118143->118144
  ff/9a->01/9b) + o174->175
  (n118271->118272 ff/9b->01/9c).
- Consts ALL 4 EXACT: 78/67/67/69.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
