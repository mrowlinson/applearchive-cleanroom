# A-194 (Q-188): T10P158 P-head geometry — DERIVED

Bed: census N=71721..71812 own bed (.rav[12:-4]).
First-hand; P157-M tails from own P157 census
row0 71401..71416 (this seat).

## 1. shape: CONFIRM (mixed PBB + quad==PBA sig)
- 71721 100B/84B sig 07000000 (PB0); 71722
  100B/84B fat sig d7070000 NEW; PBA
  71723..71738 sig 037a0000 NEW; SINGLETON
  71739 sig f70f0000 NEW.
- PBB9 71740..71748 MIXED b0 per-N exact =
  86,dd,82,ee,82,e4,b2,dd,b2 (b1..3 const
  070000; 7th mixed-sig PBB, 6 distinct b0).
- QUAD 71749..71812 single sig 037a0000 NEW
  (== PBA sig, 1st).
- 92x100B exact. PBA VPOS [4,44,45,76-79]
  exact (b5 const 0x30); PBB VPOS [0,4,11,31,
  41,42,43,48,49,80-83] exact (12B M incl
  sig b0).

## 2. quad rows: CONFIRM
- M 8B pos[48,49,50,51,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  14/16 quads each row), shared all 4 rows
  16/16 positional (2nd 8B quad M).
- R-band 9B b33-35,41-46 row-only: rows1==2==3
  exact 9c2cd3c2c87f112918 (2nd triple, 1st
  1,2,3); row0 1cd3d542c53b716b19, 64/64.
- Tails b80..83 row-const 5cd5ea50/c04858d6/
  074958d6/27e778de.
- M-novelty vs P157M tails: ALL NEW (0/16).
  PBA M 6B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x30 PBA/PBB; quad 0x30->0x31
  step exactly at 71808 (71807=30, 71808=31;
  row3 spans).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 13 = b4+12tab; quad 23 = b4+b5+R9+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @71813 sig 36a00700.

## geometry agrees on all 3 legs
