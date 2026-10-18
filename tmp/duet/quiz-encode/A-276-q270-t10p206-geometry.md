# A-276 (viewer r3): Q-270 T10P206 P-head @88425 — CONFIRM + CORRECTION

First-hand bed 88425..88776 (q270.py + H
vpos probe; census 88041..88780 RC=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 94070000
  (REPEAT P205 PB0 PREDICTED-exact), PB1
  1d6a0500 (== FRAG-05 PREDICTED-exact),
  PBA 1d6a7d00 (VPOS 8 exact b4+M7
  b34,42,43,76-79, b5 const).
- FRAG pattern EXACT 0d2/05-2/0d1/05-3/
  0d1/05-1: 0d @88443,44,47,51 (1d6a0d00,
  VPOS 14, 4/4) + 05 @88445,46,48,49,50,52
  (1d6a0500, VPOS 14 same template, 6/6).
- H1-16 1d6a7900 (== P205-H2 ref) +
  H2-16 1d6af100 (== P205-H1 ref) + H32
  1d6a7900 (== H1).
- T-RING d7a1160f NEW (VPOS 16).
- Next @88773 94070000 (REPEAT own) +
  88774 e0300f00 NEW + 88775/76 5e0ff300
  NEW.

## 2. frag + H-shared + T-ring: CONFIRM
- Frag: both sub-groups M12 VPOS 14
  b4,b5+M12 b34,35,41-46,80-83; b5 =
  lencode carry b2/b3 VARIES both.
- H1/H2/H32 share ONE M8 b48-51,76-79 V0
  positional 16/16 x3 (H32 = V0x2).
- H32 = mini-quad: R8 b34,35,41-46 2/2
  halves (7c48a288ef72f370/ac43229edf32
  516c) + tails 2/2 halves.
- M-tails 16/16 ALL NEW vs P205T (true
  novelty polarity).
- T-ring TRANSPOSED (16th) CLASSIC: M6
  b6,7,76-79 by COL 16/16; Q8 b48-51,72-75
  by ROW 16/16.

## 3. counters + dips: CONFIRM counts, NONE
- Odd-lencode all 88425..88516: 92/92 exact.
- T-ring b4=(0x8b+2off)&FF 256/256;
  b5=0xb3+(off>=59)+(off>=187) 256/256;
  edges 88575->88576 ff/b3->01/b4 +
  88703->88704 ff/b4->01/b5.
- Consts ALL 7 COUNTS EXACT: PBA 76, FRAG
  70/70, H1/H2 75/75, H32 63, T 68.
- CORRECTION (4 tags, inverted set):
  H1/H2/H32 b5 is CONST b3 single-valued
  (VPOS 9/9/21 all ex-b5: H1/H2 =
  b4+M8, H32 = b4+R8+M8+tails) — NOT
  b5-in; FRAG 0d/05 b5 VARIES b2/b3
  (lencode carry, VPOS 14 in-b5) — IS
  b5-in (untagged in Q). Counts stand.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 4 b5-tags corrected (3 off, 1 on)
