# A-324 (viewer r7): Q-324 T10P260 P-head @107217 — CONFIRM all 3

First-hand bed 107217..107610 (qr7bed
extended; census RC=0 missing=0) +
P259T ref 106961..76 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 2f370300 NEW, PB1 05010206 NEW,
  PBA 5d102060 x16 NEW (VPOS 7 exact
  b4+M6 b6,7,76-79; b5 const 45; NO
  pair in tier).
- B10 single-sig b41eaa06 x10 (VPOS 12
  exact b4+M11 b6-8,48-51,80-83; b5
  const 45; 10/10 diverge).
- QUADms col-frag 1ceba16a x9 +
  1deba16a x7 PER ROW x4 rows NEW
  (VPOS 20 exact b4,b5+QM8+R6+T4;
  b5-carry 45->46 @107263->107264
  ff->01 edge).
- T88-RING 07000000 NEW, 88B payload
  all 256 ✓ (VPOS 18 exact b4,b5+TM9+
  TR7 partition over 0..87).
- Next P261 PB0 @107565 0f550300 NEW +
  107566 adecad06 + PBA e08ad76e x16
  @107567-82 + C10 35fda506 @107583+
  (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 sig-led b0 (col-led 1c x9 +
  1d @c9-15 ✓) + b9-11,76-79 shared
  16/16 x3 vs row0.
- R6 b6,7,48-51 UNPAIRED 4/4 EXACT
  (9799fc5e4be7/95ab7e5f6f86/
  8788afdc3471/355a93dbb204).
- Tails row-shared 4/4 distinct
  fdc59ac8/f4840360/70affd40/12ee7121
  EXACT (no shared suffix).
- M-tails 16/16 ALL NEW vs P259T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM9 [8-11,19,76-79]
  by COL 16/16; TR7 [13-15,80-83] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b76-79 col / b80-83 row
  (swapped orientation ✓); b84-87
  const 5212c88a EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 107217..107564: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x5b+2off)&FF 256/256;
  b5=0x46+(off>=83)+(off>=211) 256/256;
  edges 107391->107392 ff/46->01/47 +
  107519->107520 ff/47->01/48.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  B10 72 (b5-const), quad 64 (b5 varies
  carry), T88 70 (88-18).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
