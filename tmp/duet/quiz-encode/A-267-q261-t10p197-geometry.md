# A-267 (Q-261): T10P197 P-head geometry — DERIVED

Bed: census N=85293..85640 own bed (.rav[12:-4]). First-hand; P196-T tails from own
P196 census (M-by-col tails 85037..85052, this seat).

## 1. shape: CONFIRM
- 85293..85640 = 348/348 100B/84B exact: PB0 85293 sig 72030000 (BREAKS
  48030000 chain PREDICTED-exact); PB1 85294 sig fd1b0500.
- PBA 85295..85310 sig fd1b6d00 (VPOS [4,20,26,27,76,77,78,79] = b4+M7 EXACT,
  b5 const).
- PBB2 85311..85312 sig 63160500 NEW (VPOS b4+M12 b20,21,25-30,80-83 EXACT,
  b5 const).
- PBC8 85313..85320 sig 36720300 NEW (VPOS b4+M13 b11,18,19,25-30,80-83 EXACT,
  b5 const).
- QUAD 85321..85384 single sig 63163500 NEW (VPOS 22 EXACT = b4,b5+R8+M8+
  tails; b5 carry @off55: off54 ff/9a -> off55 01/9b, tiers {0x9a,0x9b}).
- T-240 85385..85624 240x single sig 6316c103 NEW (VPOS 17 EXACT); TAIL16
  85625..85640 single sig 6316c503 NEW (VPOS [4,5,37,38,39,76,77,78,79] =
  b4,b5+M7 EXACT).
- Next @85641: PB0 sig 72030000 (REPEAT of own PB0!), PB1 85642 sig 63160500
  (== own PBB2!), PBA 85643..85644 sig 63166100 NEW (probed 2 cells).

## 2. quad + split ring: CONFIRM (first split-row ring)
- Quad M8 b32-35,76-79: row-indep 16/16 x4, shared 16/16 (heads b32,33 15/16).
- R8 b20,21,25-30 r0==r2-PAIRED 891e5c798a133ec0 (3/4 distinct); r1/r3 1B
  near-miss (byte2 7e/80: c90b7ef9... vs c90b80f9...) EXACT.
- Tails 4/4 distinct (013a4765/6c746833/6b3a4765/f7b512d8), 13/16 bytes.
- M-tails ALL NEW vs P196T (0/16).
- T-240 TRANSPOSED (7th) CONFIRM: M7 b37-39,76-79 by COL off&15 16/16; Q8
  b21-23,31,72-75 by ROW 15/15 rows (15 distinct of 15!).
- TAIL16 = ring ROW-15 own-sig CONFIRM: M positional == 240M 16/16; Q15
  ceefdb7f3d7fe90b EXACT, novel vs all 15 Q-rows; ring b4/b5 formulas CONTINUE
  (b5 steps [119,247] full-ring; tail 9c x7 -> 9d x9 with ff->01 @85631->85632
  = off247 inside tail k6->k7).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 85293..85384: 92/92 exact.
- T-240 b4=(0x13+2off)&FF 240/240; b5=0x9b+(off>=119) SINGLE step (first
  single-carry ring CONFIRM); edge 85503->85504 ff/9b->01/9c; tail b5 cont
  9c x7 -> 9d x9 (ff->01 @85631->85632).
- Consts (84-VPOS) ALL 6 EXACT: PBA 76, PBB 71, PBC 70, quad 62, T-240 67,
  tail16 75.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
