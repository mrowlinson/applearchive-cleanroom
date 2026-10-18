# A-148 (Q-142): T10P136 P-head geometry — DERIVED

Bed: census N=64065..64156 own bed (.rav[12:-4]).
First-hand; P135-M re-derived 63745 row0 (this
seat).

## 1. shape: CONFIRM (1st multi-sig quad)
- PB0 64065 96B/80B sig 14f352a6 NEW; PB1
  64066 100B/84B fat sig a1000000 NEW (1st a1
  fat); PBA 64067..64082 (16, 100B/84B sig
  120a0000 NEW); SINGLETON 64083 100B/84B sig
  a1000000 (=PB1); PBB9 64084..64092 (9,
  100B/84B sig 50000000 NEW, 9th 100B PBB);
  QUAD 64093..64156 (64=4x16, ALL 100B/84B)
  with PER-ROW sigs: rows0,2 e2070000, row1
  2e060000, row3 59060000 (all NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,32,33,34,76-79] exact (b5 const 0xf4);
  PBB VPOS [4,32,33,34,35,36,37,38,80-83]
  exact (12B).

## 2. quad rows: CONFIRM
- M 8B pos[32,33,38,39,76,77,78,79] (6th 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b32,33,38,39 16/16 distinct
  quads, 1st full-heads).
- R-band 7B b0,1,11,30,31,36,37 (sig b0,1 ride
  in band): rows0==2 exact e2072984fe601e
  (2nd 0==2 pairing); row1 2e06a991df7703;
  row3 5906f993df3315. b2,3 const 0x00.
- Tails b80..83 row-const ALL distinct
  66b414cc/c83a82cb/e1b48ad4/fefb9d93.
- M-novelty vs P135M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 6B layout). PBA M 7B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xf4 PBA/PBB; quad 0xf4->0xf5 step
  exactly at 64128.
- Quad varpos fully partitioned (counter+b5+
  R7(sig-in-band)+M8+tails); row-sig splits
  are R-band, not dips. NO D-class dips.

## geometry agrees on all 3 legs
