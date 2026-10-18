# A-170 (Q-164): T10P147 P-head geometry — DERIVED

Bed: census N=67893..67984 own bed (.rav[12:-4]).
First-hand; P146-M tails from own P146 census
row0 67573..67588 (this seat).

## 1. shape: CONFIRM (all-100B 7th)
- 67893 100B/84B sig 03000000; 67894 100B/84B
  fat sig 2f030000 NEW; PBA 67895..67910 sig
  e73c0000 NEW; SINGLETON 67911 sig 5a060000
  NEW; PBB9 67912..67920 sig 2d030000 NEW;
  QUAD 67921..67984 single sig 3b310000 NEW.
- 92x100B exact. PBA VPOS [4,32,33,38,39,
  76-79] exact (b5 const 0x12); PBB VPOS
  [4,29,30,31,37,38,39,40,41,42,80-83]
  exact (14B).

## 2. quad rows: CONFIRM
- M 8B pos[44,45,46,47,76,77,78,79] row-indep
  16/16 x4, full 16/16 distinct each row
  (heads b44-47 15/16 distinct quads each row).
- R-band 7B row-only: rows1==3 exact
  ca8a7175dfae20 (1st 1==3 pairing); row0
  2aa01d7eef2e45; row2 0afeb56be58e6a.
- Tails b80..83 row-const ALL distinct
  b3b791e6/a839983c/d6b16781/443a983c.
- M-novelty vs P146M: ALL NEW (0/16 tails;
  8B vs 8B layout). PBA M 8B 16/16; PBB M
  13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x12 PBA/PBB; quad 0x12->0x13
  step exactly at 67968 (67967=12, 67968=13;
  row2 spans the step).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 21 = b4+b5+R7+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 67985 (sig 89300300).

## geometry agrees on all 3 legs
