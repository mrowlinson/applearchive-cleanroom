# A-286 (viewer r3): Q-280 T10P216 P-head @91905 — CONFIRM + CORRECTION

First-hand bed 91905..92268 (q280.py new;
census 91921..92268 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 9f100000
  NEW, PB1 4ab22600 NEW, PBA 4ab21602
  (==QUAD; VPOS 9 exact b4+M8 b32-35,
  76-79, b5 const ce).
- PBB10 4ab22600 (==PB1) single-sig
  (VPOS 12 exact b4+M11 b22,23,30,31,
  36-38,80-83, b5 const ce, 10/10
  diverge; NO pair/C8).
- QUAD 4ab21602 (==PBA; VPOS 17 exact
  b4+M6+R10, b5 const ce).
- T-RING 60850f3e NEW (VPOS 18 exact =
  b4,b5+M10+R6 partition).
- Next @92253 9e100000 NEW (1B off P216
  PB0: 9f->9e) + 92254 4ab22600
  (==P216PB1) + 92255/56 4ab21602
  (==P216PBA).

## 2. quad + T-ring: CONFIRM + R-pair fix
- Quad M6 b36,37,76-79 shared 16/16 x3 vs
  row0.
- CORRECTION: R6 b22,23,30,32-34 is
  DOUBLE-PAIRED r0==r1 (ec45d5d41e56) +
  r2==r3 (3b53dcb4d862) — 2/4 distinct,
  NOT unpaired 4/4. (4th consecutive
  R-pairing miss: P212 r0==r3, P214
  r1==r3, P215 r2==r3, P216 double-pair
  — analyzer R-equality check needed.)
- B10M/QR share 7/11 EXACT
  (22,23,30,80-83; B-only 31,36-38;
  Q-only 32-34).
- Tails row-shared 4/4 distinct
  48b6c491/78b6c491/97bdf3e8/c6bdf3e8
  EXACT; r0/r1 share last 3B b6c491 ✓,
  r2/r3 share last 3B bdf3e8 ✓.
- M-tails 16/16 ALL NEW vs P215T (row-0
  reference, true novelty).
- T-ring STANDARD: M10 b14,15,23,35,42,
  43,76-79 by COL 16/16; R6 b36,37,72-75
  by ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 91905..92252: 348/348
  exact (whole tier).
- T-ring b4=(0xbb+2off)&FF 256/256;
  b5=0xce+(off>=35)+(off>=163) 256/256;
  edges 92031->92032 ff/ce->01/cf +
  92159->92160 ff/cf->01/d0.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), PBB 72 (b5-const ✓), quad 67
  (b5-const ✓), T 66.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; R6 double-paired r0==r1+r2==r3
