# A-275 (viewer r3): Q-269 T10P205 P-head @88077 — CONFIRM + CORRECTION

First-hand bed 88077..88428 (q269.py +
H1/H2 vpos probe; regen RC=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 94070000
  (P204-next PREDICTED-exact), PB1 6b850e00,
  PBA 6b85f200 (VPOS 8 exact b4+M7
  b24-26,76-79, b5 const).
- FRAG 2-sig positions EXACT: 0dx6
  (88095,96,98,99,88102,03) 1d6a0d00 (VPOS
  14 exact b4+M13 b20,21,25-31,80-83, b5
  const) + 05x4 (88097,88100,01,04)
  1d6a0500 (VPOS 13 exact b4+M12
  b20,21,25-30,80-83, b5 const);
  discrim b2/b22/b23 = 05/1e/e5 vs 0d/3d/ca
  EXACT.
- H1 1d6af100 + H2 1d6a7900; T-240 1d6add0e
  (VPOS 16); TAIL16 1d6ae50e (VPOS 7 exact
  b4+M6 b37,38,76-79, b5 CONST b2, b4
  b3..d1).
- Next @88425 94070000 (REPEAT own PB0) +
  88426 1d6a0500 (== own FRAG-05) +
  88427/28 1d6a7d00 NEW.

## 2. halves + split ring: CONFIRM
- H1+H2 share ONE M8 b32-35,76-79 V0
  positional 16/16 x4 halves (within +
  H1==H2).
- H1 R7 b24-30 2/2 halves
  (bebc9310f4ba01/5c3c46e6b42217) + tails
  2/2; H2 R1 b25 2/2 (0x70/0x72 x16) +
  tails 2/2.
- M-tails 16/16 ALL NEW vs P204T (true
  novelty polarity).
- T-240 TRANSPOSED (15th): M6 b37,38,76-79
  by COL 16/16; Q8 b21-23,31,72-75 by ROW
  15/15. TAIL16 = ring ROW-15 own-sig: M
  positional==240M 16/16; Q15 novel; b4
  cont 0/16 bad; b5 const 0xb2. 2nd
  split-row ring CONFIRM.

## 3. counters + dips: CONFIRM counts, NONE
- Odd-lencode all 88077..88168: 92/92 exact.
- T-240 b4=(0xd3+2off)&FF 256/256... (240
  cells); b5=0xb0+(off>=23)+(off>=151)
  exact; edges 88191->88192 ff/b0->01/b1 +
  88319->88320 ff/b1->01/b2.
- Consts ALL 7 COUNTS EXACT: PBA 76, FRAG
  70/71, H1 64, H2 70, T-240 68, tail16 77.
- CORRECTION (3 tags): H1/H2/tail16 b5 is
  CONST (b0/b0/b2, single-valued), NOT
  b5-in: H1 VPOS 20 = b4+R7+M8+tails (no
  b5), H2 VPOS 14 = b4+R1+M8+tails (no
  b5), tail VPOS 7 (leg-1 "b5 CONST b2!"
  was already right; leg-3 tag contradicts
  it). Counts stand as filed.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 3 b5-tags corrected b5-const
