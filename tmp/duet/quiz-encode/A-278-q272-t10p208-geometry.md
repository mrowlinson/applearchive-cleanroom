# A-278 (viewer r3): Q-272 T10P208 P-head @89121 — CONFIRM + CORRECTION

First-hand bed 89121..89472 (q272.py new;
census 89129..90180 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 98070000
  (P207-next PREDICTED-exact), PB1
  bfab0e00, PBA bfabf200 (VPOS 8 exact
  b4+M7 b32-34,76-79, b5 const b8).
- FRAG UNEVEN 0e2/06-1/0e3/06-1/0e2/06-1
  EXACT: 0ex7 @89139,40,42,43,44,46,47
  bfab0e00 ==PB1 (VPOS 12 exact b4+M12
  b22,23,30,31,36-38,80-83, b5 const,
  7/7) + 06x3 @89141,45,48 bfab0600 NEW
  (VPOS 11 exact b4+M11 b22,23,30,36-38,
  80-83 — NO b31, b5 const, 3/3).
- TRIPLE48 bfabf200 (== PBA) + G16
  bfab7a00 NEW (VPOS 7 exact b4+M6
  b36,37,76-79, b5 const).
- T-RING bfab3e0d NEW (VPOS 15).
- Next @89469 98070000 (REPEAT own PB0) +
  89470 bfab0e00 (repeat) + 89471/72
  bfabf200 (repeat).

## 2. triple + T-ring: CONFIRM
- TRIPLE+G16 share ONE M6 b36,37,76-79 V0
  positional 16/16 x4 (3 thirds + G16).
- R7 b22,23,30-34 3/3 thirds
  (85d0b4bfb4580c/72d2ffbfb43122/
  ebc1fcfc340c17) + tails 3/3 thirds.
- M-tails 16/16 ALL NEW vs P207T (true
  novelty polarity).
- T-ring TRANSPOSED (18th): M7 b35,42,43,
  76-79 by COL 16/16; Q6 b36,37,72-75 by
  ROW 16/16.

## 3. counters + dips: CONFIRM counts, NONE
- Odd-lencode all 89121..89212: 92/92 exact.
- T-ring b4=(0xfb+2off)&FF 256/256;
  b5=0xb8+(off>=3)+(off>=131) 256/256
  (EARLY first step @off3); edges
  89215->89216 ff/b8->01/b9 + 89343->
  89344 ff/b9->01/ba (both coincide with
  b5 steps).
- Consts ALL 6 COUNTS EXACT: PBA 76, FRAG
  72/73, triple 66, G16 77, T 69.
- CORRECTION (2 tags): triple + G16 b5 is
  CONST b8 single-valued (VPOS 18/7 both
  ex-b5: triple = b4+R7+M6+tails, G16 =
  b4+M6) — NOT b5-in. Counts stand.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 2 b5-tags corrected b5-const
