# A-187 (Q-181): T10P155 P-head geometry — DERIVED

Bed: census N=70677..70768 own bed (.rav[12:-4]).
First-hand; P154-M tails from own P154 census
row0 70357..70372 (this seat).

## 1. shape: CONFIRM
- 70677 100B/84B sig 03000000 (PB0); 70678
  100B/84B fat sig 51070000 NEW; PBA
  70679..70694 sig e47e0000 NEW; SINGLETON
  70695 sig 54070000 NEW; PBB9 70696..70704
  sig aa030000 NEW; QUAD 70705..70768 single
  sig f1360000 NEW.
- 92x100B exact. PBA VPOS [4,32,33,38,39,
  76-79] exact (b5 const 0x28); PBB VPOS
  [4,29,30,31,37-42,80-83] exact (13B M).

## 2. quad rows: CONFIRM
- M 7B pos[44,45,46,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 each row), shared all 4 rows 16/16
  positional (no M3 split).
- R-band 8B b32,33,37-42 row-only: rows0==1
  exact ca3f866cf36eeeed (2nd 0==1 pairing);
  row2 ca62427ba5ee1fee; row3 6a75d278bb2ebeed,
  64/64.
- Tails b80..83 row-const ALL distinct
  b4ad7daa/fdad7daa/99302423/312d6a23.
- M-novelty vs P154M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x28 WHOLE tier (no step anywhere).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 20 = b4+R8+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @70769 sig acaf0300.

## geometry agrees on all 3 legs
