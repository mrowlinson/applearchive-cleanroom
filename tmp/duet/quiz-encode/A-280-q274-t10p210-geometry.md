# A-280 (viewer r3): Q-274 T10P210 P-head @89817 — CONFIRM all 3

First-hand bed 89817..90180 (q274.py new;
census 89129..90180 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 f0070000
  NEW, PB1 96e10f00 NEW, PBA 6819fe00 NEW
  (VPOS 7 exact b4+M6 b20,21,76-79, b5
  const bd).
- PAIR 89835..89836 43430e00 NEW (VPOS
  {b4,b80} ONLY exact).
- PBC8 MULTI-SIG 4 distinct
  (07af0500/8b980600/d1090400/e57c0600;
  VPOS 13 exact b4+M12 b0-2,11,18,19,24,
  25,80-83, b5 const bd).
- QUAD MULTI-SIG 4 row sigs
  07af7d00/4da87c00/91fa7e00/d1097c00
  EXACT (stable-in-row 4/4; VPOS 21 exact
  b4,b5+M7+R12; b5-carry bd->be
  @89855->89856 ff->01 edge; bd x11 +
  be x53).
- T-RING 4da8f007 NEW (VPOS 16).
- Next @90165 f0070000 REPEAT (==P210
  PB0) + 90166 e96d0f00 NEW + 90167/68
  e96dff00 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b20,26,27,76-79 shared 16/16 x3
  vs row0.
- R8 sig-led b0-2,11,18,19,24,25 UNPAIRED
  4/4 distinct.
- Tails row-shared 4/4 distinct
  40c5531b/815ff996/775496cd/6769578c
  EXACT.
- C8 M-positions == quad-R positions
  12/12 exact (set-equal).
- M-tails 16/16 ALL NEW vs P209T (true
  novelty polarity).
- T-ring STANDARD: M8 b32-35,76-79 by COL
  16/16; R6 b24,25,72-75 by ROW 16/16
  UNPAIRED (16 distinct); tails const
  (1 distinct ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 89817..90164: 348/348
  exact (whole tier).
- T-ring b4=(0x6b+2off)&FF 256/256;
  b5=0xbe+(off>=75)+(off>=203) 256/256;
  edges 89983->89984 ff/be->01/bf +
  90111->90112 ff/bf->01/c0.
- Consts ALL 4 EXACT: PBA 77 (b5-const
  bd ✓), PBC 71 (b5-const bd ✓), quad 63
  (b5 varies carry ✓), T 68.
- New (b5-const) tags CORRECT both.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
