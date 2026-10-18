# A-182 (Q-176): T10P153 P-head geometry — DERIVED

Bed: census N=69981..70072 own bed (.rav[12:-4]).
First-hand; P150-M tails from own P150 census
row0 68965..68980 (this seat).

## 1. shape: CONFIRM (row2-odd multi-sig quad)
- 69981 100B/84B sig 03000000; 69982 100B/84B
  fat sig e0060000 NEW; PBA 69983..69998 sig
  29640000 NEW; SINGLETON 69999 sig fc040000
  NEW.
- PBB9 70000..70008 MIXED 2B-sig per-N exact:
  fc02 x6 (70000,70001,70003,70005,70006,70007)
  + 3c03 x3 at 70002,70004,70008 (6th
  mixed-sig PBB, 2nd 2B-sig).
- QUAD 70009..70072 per-row sigs: rows0,1,3
  c72f0000, row2 c7330000 (both NEW, 5th
  multi-sig quad, 1st row2-odd), 64/64.
- 92x100B exact. PBA VPOS [4,48,49,50,51,
  76-79] exact (b5 const 0x22); PBB VPOS
  [0,1,4,44,45,46,47,49,50,51,80-83] exact
  (14B).

## 2. quad rows: CONFIRM
- M 7B pos[6,7,9,76,77,78,79] row-indep 16/16
  x4, 16/16 distinct each row (heads b6,7,9
  13/16 distinct triples each row).
- R-band 7B row-only: rows1==3 exact
  2fe9837aaf76bf; row0 2f49f9e5d7c42f; row2
  3329d26d019c5f (b1=0x33), 64/64.
- b0,2,3 const 0xc7,0x00,0x00. Tails b80..83
  row-const ALL distinct 9fecec01/546594e9/
  144160ad/f42593f3.
- M-novelty vs P150M: ALL NEW (0/16 tails;
  7B vs 7B layout). PBA M 8B 16/16; PBB M
  13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x22 PBA/PBB; quad 0x22->0x23
  step exactly at 70016 (70015=22, 70016=23).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 20 = b4+b5+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 70073 (sig 783c0300).

## geometry agrees on all 3 legs
