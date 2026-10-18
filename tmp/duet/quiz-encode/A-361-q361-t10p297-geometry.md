# A-361 (viewer r8): Q-361 T10P297 @120093 — CONFIRM all legs

First-hand bed 120093..120440 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n120093 66501000 NEW, PB1 n120094
  7b802f23 NEW.
- PBA88-PLAIN n120095-110 16x88B
  02000000 (M7 b52,53,54,80-83 16/16
  distinct ✓; VPOS 8 = b4+M7 over 88;
  b0 const 02, b5 const aa; 16/16
  distinct; consts 80 ✓).
- C10-3SIG ordered map first-hand:
  7b802f23 x8 @120111-18 + 7b808f1d
  @120119 + 7b80cf1c @120120 (3-sig
  8+1+1 ✓; M12 b2,3,35,46-51,80-83
  10/10 ✓; VPOS 14; b5 const aa;
  10/10 diverge; consts 70 ✓).
- QUAD88-4R n120121-184 01000000 x64
  88B-pay (VPOS 20 = b4+M7+R12 over
  88; b5 const aa = full odd lencode
  ✓; NO frags; consts 68 ✓).
- T88-RING256 n120185-440 sig 1e000000
  (VPOS 17 = b4,b5+TM8+TR7 partition
  over 0..87 ✓).
- Next P298 PB0 @120441 36721e00 NEW +
  120442 d46ce43c NEW + PBA88
  03000000 x16 @120443-58 + C10 map
  cb56e43c x8/0b2cfa3c/2b8be43c
  @120459-68 (window resolved; P298 in
  viewer2/3/4 turf — reported, not
  claimed).

## 2. quad + T-ring: CONFIRM
- Quad M7 b6,7,12,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R12 b11,39,50-55,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples: r0 d8f34ef5…/
  r1 e67394c411df/r2 e67394c411df/
  r3 e67394c451df — r1/r2 share
  6B-prefix, all 4 differ).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [9,10,11,20,80-83] by COL
  16/16; R7 [6,7,12,76-79] by ROW
  16/16 UNPAIRED; tails SPLIT b80-83
  col / b76-79 row (standard); b84-87
  const be38e65b first-hand
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 120093..120440:
  348/348 exact.
- T88 b4 = 0xf3 step2 256/256; b5 =
  0xaa+(o>=7)+(o>=135) 256/256;
  edges o6->7 (n120191->120192
  ff/aa->01/ab) + o134->135
  (n120319->120320 ff/ab->01/ac).
- Consts ALL 4 EXACT: 80/70/68/71.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs — backlog Q-332..Q-361 DRAINED
