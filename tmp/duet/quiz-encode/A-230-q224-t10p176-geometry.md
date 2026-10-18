# A-230 (Q-224): T10P176 P-head geometry — DERIVED

Bed: census N=77985..78076 own bed (.rav[12:-4]). First-hand; P175-M from own P175 census
row0 77665..77680 (this seat).

## 1. shape: CONFIRM
- 92/92 100B/84B exact. PB0 41010000; PB1 fat 97410100; PBA 77987..78002 single sig df9a1700.
- MID10 78003..78012 per-N exact: 65f60200,ed6c0100,6f120100,a9290100,550c0100,
  550c0100,a9290100,c1130100,a9290100,bd080100 (no singleton/PBB split).
- QUAD 78013..78076 single sig df9a1700 (== PBA sig).
- PBA VPOS [4,32,33,34,35,76,77,78,79] (8B M, b5 const 0x61); MID VPOS
  [0,1,2,4,30-39,80-83] (17B M incl sig b0,1,2; b5 const 0x61).

## 2. quad rows: CONFIRM
- M 6B pos[36,37,76,77,78,79] row-indep 16/16 x4, 16/16 distinct each row
  (heads 14/16 pairs each row), shared all 4 rows 16/16.
- R-band 7B row-only: rows0==2==3 exact 6a0a06fdb34f17 (triple); row1 150304fc339f20, 64/64.
- tails b80..83 row-const b0ad1f5e/32d94512/6c1f0281/aa1f0281 (rows2,3 share b1..3, differ b0).
- M-novelty vs P175M tails: ALL NEW (0/16). PBA M 8B 16/16; MID M 17B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x61 whole tier (no step anywhere).
- varpos partitioned exact (PBA 9=b4+8tab; MID 18=b4+17tab; quad 18=b4+R7+M6+tails), 0 stragglers.
- NO D-class dips. Next tier @78077 sig df9a0b01.

## geometry agrees on all 3 legs
