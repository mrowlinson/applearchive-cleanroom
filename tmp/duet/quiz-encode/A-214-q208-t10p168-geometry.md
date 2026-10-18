# A-214 (Q-208): T10P168 P-head geometry — DERIVED

Bed: census N=75201..75292 own bed (.rav[12:-4]).
First-hand; P167-M tails from own P167 census
row0 74881..74896 (this seat).

## 1. shape: CONFIRM (PBB-echoes-PB1 + quad==PBA)
- 75201 100B/84B sig 11000000 (PB0); 75202
  100B/84B fat sig b5230000 NEW; PBA
  75203..75218 sig 0be40200 NEW; SINGLETON
  75219 sig 24630000 NEW.
- PBB9 75220..75228 sig b5230000 (== PB1
  sig, 1st PBB-echoes-PB1, 9/9).
- QUAD 75229..75292 single sig 0be40200 NEW
  (== PBA sig, 3rd).
- 92x100B exact. PBA VPOS [4,32-35,76-79]
  exact (b5 const 0x4b); PBB VPOS [4,32-38,
  80-83] exact (11B M).

## 2. quad rows: CONFIRM
- M 8B pos[32,33,38,39,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  13/16 quads each row), shared all 4 rows
  16/16 positional (6th 8B quad M).
- R-band 6B b22,23,30,31,36,37 row-only:
  rows0==1==2 exact 041107fd7e61 (4th
  triple, 2nd 0,1,2); row3 5419e9bf1629,
  64/64.
- Tails b80..83 row-const 7ae897e7/bbe897e7/
  14ea97e7/2ee2ad25 (rows0,1 share e897e7,
  differ b0).
- M-novelty vs P167M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x4b PBA/PBB; quad 0x4b->0x4c
  step exactly at 75264 (75263=4b, 75264=4c;
  row2 spans).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 12 = b4+11tab; quad 20 = b4+b5+R6+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @75293 sig 0be43600.

## geometry agrees on all 3 legs
