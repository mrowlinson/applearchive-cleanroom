# A-354 (viewer r8): Q-354 T10P290 @117657 — CONFIRM all legs

First-hand bed 117657..118004 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n117657 5f6f1300 NEW, PB1 n117658
  ccbede26 NEW.
- PBA88-PLAIN n117659-74 16x88B
  02000000 (M9 b16-19,23,80-83 16/16
  distinct ✓; VPOS 10 = b4+M9 over
  88; b0 const 02, b5 const 97; 16/16
  distinct; consts 78 ✓).
- C10-3SIG ordered map first-hand:
  1b19db26 x7 @117675-81 + bb9cdb26
  @117682 + 8bf4d626 x2 @117683-84
  (3-sig 7+1+2 ✓; M13 b0-2,11,18-22,
  80-83 10/10 ✓; VPOS 14; b5 const
  97; 10/10 diverge; consts 70 ✓).
- QUAD88-4R n117685-748 02000000 x64
  88B-pay (VPOS 20 = b4+M7+R12 over
  88; b27-skipped const 55 ✓; b5
  const 97 = full odd lencode ✓; NO
  frags; consts 68 ✓).
- T88-RING256 n117749-118004 sig
  24000000 (VPOS 18 = b4,b5+TM9+TR7
  partition over 0..87 ✓).
- Next P291 PB0 @118005 5f6f1300
  (==P290PB0) + PB1 2b81c726 NEW +
  PBA88-STEP 02000000 x16 + C10-2SIG
  2b81c726 x8 + 2b816713 x2 (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad M7 b28,29,30,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R12 b16-18,22-26,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 f272eec6…
  distinct, r123 share prefix 328fc02e…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M9 [18,19,27,34,35,80-83] by COL
  16/16; R7 [28,29,30,76-79] by ROW
  16/16 UNPAIRED; tails SPLIT b80-83
  col / b76-79 row (standard); b84-87
  const fcaa79e0 first-hand
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 117657..118004:
  348/348 exact.
- T88 b4 = 0xeb step2 256/256; b5 =
  0x97+(o>=11)+(o>=139) 256/256;
  edges o10->11 (n117759->117760
  ff/97->01/98) + o138->139
  (n117887->117888 ff/98->01/99).
- Consts ALL 4 EXACT: 78/70/68/70.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
