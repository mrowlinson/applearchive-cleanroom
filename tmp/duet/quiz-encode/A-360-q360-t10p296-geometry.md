# A-360 (viewer r8): Q-360 T10P296 @119745 — CONFIRM all legs

First-hand bed 119745..120092 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n119745 63501000 SAME-as-P295PB0
  ✓ (byte-equal first-hand), PB1
  n119746 7b80af20 NEW.
- PBA88-PLAIN n119747-62 16x88B
  02000000 (M10 b18,19,25,26,27,35,
  80-83 16/16 distinct ✓; VPOS 11 =
  b4+M10 over 88; b0 const 02, b5
  const a7; 16/16 distinct; consts
  77 ✓).
- C10-1SIG n119763-72 7b80af20 x10
  SAME-as-PB1 ✓ (M12 b22,23,30-35,
  80-83 10/10 ✓; VPOS 13; b5 const
  a7; 10/10 diverge; consts 71 ✓).
- QUAD88-4R n119773-836 02000000 x64
  88B-pay (VPOS 21 = b4,b5+M8+R11
  over 88; b39-skipped const 6e ✓;
  b5 0xa7+(o>=35), edge o34->35
  n119807->119808 ff/a7->01/a8 ✓; NO
  frags; consts 67 ✓).
- T88-RING256 n119837-120092 sig
  26000000 (VPOS 18 = b4,b5+TM8+TR8
  partition over 0..87 ✓).
- Next P297 PB0 @120093 66501000 NEW +
  PB1 7b802f23 NEW + PBA88 02000000
  x16 + C10-3SIG 7b802f23 x8 +
  7b808f1d + 7b80cf1c (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M8 b40-43,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R11 b26,27,34-38,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 bfbd937e…
  distinct, r123 share prefix 6757b37f…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [30,39,46,47,80-83] by COL
  16/16; R8 [40-43,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row (standard); b84-87 const
  2f7cf316 first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 119745..120092:
  348/348 exact.
- Quad b4 base bb step2 64/64; b5 =
  0xa7+(o>=35) 64/64 (edge above ✓).
- T88 b4 = 0x3b step2 256/256; b5 =
  0xa8+(o>=99)+(o>=227) 256/256;
  edges o98->99 (n119935->119936
  ff/a8->01/a9) + o226->227
  (n120063->120064 ff/a9->01/aa).
- Consts ALL 4 EXACT: 77/71/67/70.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
