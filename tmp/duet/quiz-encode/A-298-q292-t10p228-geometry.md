# A-298 (viewer r3): Q-292 T10P228 P-head @96081 — CONFIRM + 4 count fixes

First-hand bed 96081..96428 (q292.py new;
census 96097..97124 RC=0 missing=0).

## 1. shape: CONFIRM + PBC/T-ring VPOS fixes
- 348 cells sizes {(100,84)}. PB0 794b0000
  NEW, PB1 8e638e00 NEW, PBA ee38e608 NEW
  (VPOS 9 exact b4+M8 b6-9,76-79, b5
  const ee).
- PAIR 96099..96100 4a329d00 NEW (VPOS
  {b4,b80} ONLY exact).
- PBC8 25994e00 NEW. CORRECTION: VPOS 11
  (not 13) = b4+M10 (not M12) — listed
  positions b6,7,48-51,80-83 are exact
  (10 + b4 = 11); "M12"/"VPOS 13" counts
  wrong. Consts 73 (not 72). b5 const ee.
- QUADhalf sigs 3093e904/2693e904 (b0
  half-split cols 0-7 = 0x30 x8 /
  cols 8-15 = 0x26 x8 EXACT; VPOS 21
  exact b4,b5+M9+R6+T4; b5-carry ee->ef
  @96127->96128 ff->01 edge).
- T-RING DUAL sigs f032994e (half0) /
  e632994e (half1); half-flips b0 f0/e6
  + b12 35/55 @off128 (96300->96301)
  EXACT, halves otherwise M/R-structured.
  CORRECTION: VPOS 19 (not 21) — Q's own
  partition b4,b5+M8+R7+2 flips sums
  2+8+7+2 = 19; ground-truth vpos list
  exactly those 19. Consts 65 stands
  (= 84-19 INCL flips — "(ex flips)" tag
  wrong way round).
- Next @96429 994e0000 NEW + 96430
  e6969900 NEW + 96431/32 e696d109 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M9 b0,9-12,76-79 shared 16/16 x3 vs
  row0 (sig-led b0 half-split ✓).
- R6 b6,7,48-51 UNPAIRED 4/4 EXACT values
  (22a57cd8a949/30b9545da42e/c69b71dfe16f/
  408a7c587091, all distinct).
- Tails row-shared 4/4 distinct
  4168ea6b/62116d6a/8bedcfaf/2a97368f
  EXACT.
- M-tails 16/16 ALL NEW vs P227T (row-0
  reference, true novelty).
- T-ring DUAL: M8 [16-19,72-75] by COL
  16/16; R7 [9-11,76-79] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  (b72-75 16 col-shared + b76-79 16
  row-shared, NOT const ✓); b80-83 const
  (1 ring-wide ✓).

## 3. counters + dips: CONFIRM + 2 const fixes
- Odd-lencode ALL 96081..96428: 348/348
  exact (whole tier).
- T-ring b4=(0x5b+2off)&FF 256/256;
  b5=0xef+(off>=83)+(off>=211) 256/256;
  edges 96255->96256 ff/ef->01/f0 +
  96383->96384 ff/f0->01/f1.
- CORRECTIONS: PBA consts 75 (not 74;
  VPOS 9 → 84-9); PBC consts 73 (not 72;
  VPOS 11 → 84-11). Quad 63 ✓ (varies).
  T 65 ✓ (= 84-19 incl flips).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; 4 count fixes (PBA 75, PBC V11/C73, T V19)
