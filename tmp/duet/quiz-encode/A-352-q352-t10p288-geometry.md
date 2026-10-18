# A-352 (viewer r8): Q-352 T10P288 @116961 — CONFIRM all legs

First-hand bed 116961..117308 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n116961 0ac51600 NEW, PB1 n116962
  3bf3942d NEW.
- PBA88-PLAIN n116963-78 16x88B
  02000000 (M8 b25,26,27,35,80-83
  16/16 distinct ✓; VPOS 9 = b4+M8
  over 88; b0 const 02, b5 const 91;
  16/16 distinct; consts 79 ✓).
- C10-1SIG n116979-88 3bf3942d x10
  SAME-as-PB1 ✓ (M12 b22,23,30-35,
  80-83 10/10 ✓; VPOS 13; b5 const
  91; 10/10 diverge; consts 71 ✓).
- QUAD88-4R n116989-117052 02000000
  x64 88B-pay (VPOS 20 = b4,b5+M6+R12
  over 88; b5 0x91+(o>=3), edge o2->3
  n116991->116992 ff/91->01/92 ✓; NO
  frags; consts 68 ✓).
- T88-RING256 n117053-308 sig 2f000000
  (VPOS 15 = b4,b5+TM7+TR6 partition
  over 0..87 ✓).
- Next P289 PB0 @117309 0fc51600 NEW +
  PB1 3bf3f420 NEW + PBA88 02000000
  x16 + C10-2SIG 3bf3f420 x7 +
  3bf3f41a x3 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M6 b40,41,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R12 b26,27,34-39,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 2b022ff9…
  distinct, r123 share prefix abe8237f…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M7 [39,46,47,80-83] by COL 16/16;
  R6 [40,41,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row (standard); b84-87 const
  de75775e first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 116961..117308:
  348/348 exact.
- Quad b4 base fb step2 64/64; b5 =
  0x91+(o>=3) 64/64 (edge above ✓).
- T88 b4 = 0x7b step2 256/256; b5 =
  0x92+(o>=67)+(o>=195) 256/256;
  edges o66->67 (n117119->117120
  ff/92->01/93) + o194->195
  (n117247->117248 ff/93->01/94).
- Consts ALL 4 EXACT: 79/71/68/73.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
