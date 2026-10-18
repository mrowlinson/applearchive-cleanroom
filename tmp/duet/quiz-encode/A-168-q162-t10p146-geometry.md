# A-168 (Q-162): T10P146 P-head geometry — DERIVED

Bed: census N=67545..67636 own bed (.rav[12:-4]).
First-hand; P145-M tails from own P145 census
row0 67225..67240 (this seat).

## 1. shape: CONFIRM (all-100B 6th)
- 67545 100B/84B sig 03000000; 67546 100B/84B
  fat sig 33030000 NEW; PBA 67547..67562 sig
  3d330000 NEW; SINGLETON 67563 sig 33030000
  (=PB1, per-N exact); PBB9 67564..67572 sig
  99010000 NEW; QUAD 67573..67636 single sig
  7d190000 NEW.
- 92x100B exact. PBA VPOS [4,20,21,76-79]
  exact (b5 const 0x0f); PBB VPOS [4,20,21,
  22,23,24,25,26,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 8B pos[18,19,26,27,76,77,78,79] row-indep
  16/16 x4, full 16/16 distinct each row
  (heads b18,19,26,27 15/16 distinct quads
  each row).
- R-band 6B b20,21,22,23,24,25 row-only, ALL
  4 distinct: 455c4bc38f82/3fdb4f788f2a/
  305b0405efdc/485c4bc38f82, 64/64.
- Tails b80..83 row-const ALL distinct
  c9340269/0c2dd430/782d0aa8/93baa138.
- M-novelty vs P145M: ALL NEW (0/16 tails;
  8B vs 6B layout). PBA M 6B 16/16; PBB M
  11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x0f PBA/PBB; quad 0x0f->0x10
  step exactly at 67584 (67583=0f, 67584=10;
  row0 spans the step).
- Varpos partitioned exact (PBA 7 = b4+6tab;
  PBB 12 = b4+11tab; quad 20 = b4+b5+R6+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 67637 (sig 04050100).

## geometry agrees on all 3 legs
