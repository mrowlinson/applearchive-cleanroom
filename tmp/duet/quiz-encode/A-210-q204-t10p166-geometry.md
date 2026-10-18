# A-210 (Q-204): T10P166 P-head geometry — DERIVED

Bed: census N=74505..74596 own bed (.rav[12:-4]).
First-hand; P165-M tails from own P165 census
row0 74185..74200 (this seat).

## 1. shape: CONFIRM (mixed PBB + quad==PBA sig)
- 74505 100B/84B sig 11000000 (PB0); 74506
  100B/84B fat sig d3110000 NEW; PBA
  74507..74522 sig 99000100 NEW; SINGLETON
  74523 sig 99200000 NEW.
- PBB9 74524..74532 MIXED b0 per-N exact =
  10,13,26,f8,f8,c9,2d,c9,67 (b1..3 const
  110000; 10th mixed-sig PBB, 7 distinct b0).
- QUAD 74533..74596 single sig 99000100 NEW
  (== PBA sig, 2nd).
- 92x100B exact. PBA VPOS [4,34,42,43,76-79]
  exact (b5 const 0x46); PBB VPOS [0,4,11,31,
  41,42,43,48,49,80-83] exact (12B M incl
  sig b0).

## 2. quad rows: CONFIRM
- M 8B pos[48,49,50,51,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  14/16 quads each row), shared all 4 rows
  16/16 positional (4th 8B quad M).
- R-band 8B b34,35,41-46 row-only: rows0==2==3
  exact 4dee24c82b918b6a (3rd triple, 1st
  0,2,3); row1 c5efc4cf17d1d26d, 64/64.
- Tails b80..83 row-const 7aebe010/b1f7b08b/
  feebe010/41ece010 (rows0,2,3 share ebe010,
  differ b0).
- M-novelty vs P165M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x46 WHOLE tier (no step anywhere).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 13 = b4+12tab; quad 21 = b4+R8+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @74597 sig 95091000.

## geometry agrees on all 3 legs
