# A-266 (Q-260): T10P196 P-head geometry — DERIVED

Bed: census N=84945..85292 own bed (.rav[12:-4]). First-hand; P195-Q tails from own
P195 census quad row0 84625..84640 (this seat).

## 1. shape: CONFIRM
- 84945..85292 = 348/348 100B/84B exact: PB0 84945 sig 48030000 (REPEAT of
  P195 PB0 PREDICTED-exact); PB1 84946 sig 79ad0500.
- PBA 84947..84962 sig 97d75a00 NEW (VPOS [4,6,7,8,76,77,78,79] = b4+M7 EXACT,
  b5 const 0x97).
- PBB2 84963..84964 sig 34e50600 NEW (VPOS b4+M10 b6,7,48-51,80-83 EXACT, b5
  const 0x97).
- SING 84965 sig 9b720300 NEW; SING 84966 sig 34e50600 (== PBB2, NOT member
  CONFIRM); SING 84967 sig 9e720300 NEW; SING 84968 sig 9d720300 NEW; SING
  84969 sig 9e720300; PAIR 84970..84971 sig 9d720300 (VPOS [4,80] ONLY —
  differ b4+b80 EXACT); SING 84972 sig 9e720300.
- 4xALT16 84973..85036 alternating sigs 3e293700/3d293700/3e/3d (rows
  3e,3d,3e,3d) ALL NEW (each VPOS b4+M7 b13-15,76-79 EXACT; row1 84989
  B5-CARRY {0x97,0x98} CONFIRM — alt0 b5 0x97, alt2/alt3 b5 0x98, row1
  straddles the odd-lencode carry).
- T-RING 85037..85292 256x single sig ae937203 NEW (VPOS 16 EXACT).
- Next @85293: PB0 sig 72030000 NEW (BREAKS 48030000 repeat-chain!), PB1
  85294 fd1b0500 NEW, PBA 85295..85296 sig fd1b6d00 NEW (probed 2 cells).

## 2. sharers + rows + T-ring: CONFIRM
- Sig-sharer diffs EXACT: 9e-group 84967/69 3B [4,80,81], 84967/72 5B
  [4,80,81,82,83]; 9d-group 84968/70 6B [4,6,80,81,82,83] each, 84968/71 same
  6B set; pair 84970/71 2B [4,80].
- Rows: M7 POSITIONALLY shared all 4 16/16; between-row constdiffs 11/11/11B
  EXACT; M-tails 16/16 distinct ALL blocks, ALL NEW vs P195Q (0/16 each).
- T-ring TRANSPOSED (6th) + TAILS-SWAPPED (3rd) CONFIRM: M7 b20-22,72-75 by
  COL off&15 16/16; Q7 b13-15,76-79 by ROW off>>4 16/16.

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 84945..85036: 92/92 exact.
- T-ring b4=(0x5b+2off)&FF 256/256; b5=0x98+(off>=83)+(off>=211) 256/256;
  edges 85119->85120 ff/98->01/99 + 85247->85248 ff/99->01/9a.
- Consts (84-VPOS) ALL EXACT: PBA 76, PBB 73, rows 76/75/76/76 (row1 b5-carry),
  T 68 — writer's mechanical transcription holds on all 7 numbers.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
