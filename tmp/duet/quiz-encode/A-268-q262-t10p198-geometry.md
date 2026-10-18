# A-268 (Q-262): T10P198 P-head geometry — DERIVED

Bed: census N=85641..85988 own bed (.rav[12:-4]). First-hand; P197-T tails from own
P197 census (M-by-col tails 85385..85400, this seat).

## 1. shape: CONFIRM
- 85641..85988 = 348/348 100B/84B exact: PB0 85641 sig 72030000 (REPEAT of
  P197 PB0 PREDICTED-exact); PB1 85642 sig 63160500 (== own PBB2
  PREDICTED-exact; also == P197-PBB2 sig).
- PBA 85643..85658 sig 63166100 NEW (VPOS [4,34,42,43,76,77,78,79] = b4+M7
  EXACT, b5 const).
- PBB2 85659..85660 sig 63160500 (== PB1; VPOS b4+M11 b34,41-46,80-83 EXACT,
  b5 const).
- PBC8 85661..85668 sig 7f800300 NEW (VPOS b4+M12 b34,35,41-46,80-83 EXACT,
  b5 const).
- QUAD 85669..85732 single sig 63163500 (== P197-QUAD sig 63163500, own bed
  ref — REPEAT! VPOS 21 EXACT = b4+R8+M8+tails, b5 const 0x9d).
- T-RING 85733..85988 256x single sig 37665103 NEW (VPOS 16 EXACT).
- Next @85989: PB0 sig 72030000 (REPEAT own!), PB1 85990 c7e90600 NEW, PBA
  85991..85992 sig 749c6e00 NEW (probed 2 cells).

## 2. quad + T-ring: CONFIRM
- Quad M8 b48-51,76-79: row-indep 16/16 x4, shared 16/16 (heads b48,49 FULL
  16/16 pairs).
- R8 b34,35,41-46: all 4 distinct, no pairing (72251fc81bf2c8da /
  8a25dfc94f52a1ce / da203fcd27d293d6 / 432f5fc3435287d2).
- Tails 4/4 distinct (6136affe/21303214/3cf6c5c8/ba6d6c91), 16/16 bytes
  (true no-sharing CONFIRM).
- M-tails ALL NEW vs P197T (0/16).
- T-ring TRANSPOSED (8th) CLASSIC layout CONFIRM: M6 b6,7,76-79 by COL off&15
  16/16 (m-tails IN PLACE); Q8 b48-51,72-75 by ROW off>>4 16/16 (q-tails
  RELOCATED).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 85641..85732: 92/92 exact.
- T-ring b4=(0xcb+2off)&FF 256/256; b5=0x9d+(off>=27)+(off>=155) 256/256;
  edges 85759->85760 ff/9d->01/9e + 85887->85888 ff/9e->01/9f.
- Consts (84-VPOS) ALL 5 EXACT: PBA 76, PBB 72, PBC 71, quad 63 (b5-in), T 68.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
