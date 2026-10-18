# A-114 (Q-108): T10P119 P-head geometry — DERIVED

Bed: census N=58149..58240 own bed (.rav[12:-4]).
First-hand; P118-M re-derived 57829 row0 (A-112
bed, this seat).

## 1. shape: CONFIRM
- PB0 58149 96B/80B sig c0787002 NEW; PB1 58150
  100B/84B fat sig 04000000 (1st 04 fat);
  PBA 58151..58166 (16, 100B/84B sig
  74000000 NEW); SINGLETON 58167 100B/84B sig
  03000000; PBB 58168..58176 (9, 100B/84B sig
  01000000, 2nd 100B PBB); QUAD 58177..58240
  (64=4x16, ALL 100B/84B, SINGLE sig 1d000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,13,14,76-79] exact (b5 const 0xc6);
  PBB VPOS [4,8,9,10,11,15,16,17,18,19,
  80-83] exact (13B excl counter + tails).

## 2. quad rows: CONFIRM (1st alt-pairing)
- M 7B pos[20,21,22,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row.
- R-band 8B b8,9,10,11,15,16,17,18 row-only
  (1 distinct/row) with ALT pairing:
  rows0,2 d4f8ad1ba096383e, rows1,3
  3478c31af0d69f1d exact (1st 0==2/1==3).
- Tails b80..83 row-const d9f05859/e3b93020/
  a8f15859/123a4f20 exact.
- M-novelty vs P118M: ALL NEW (0/16 overlap,
  same 7B head+tail layout). PBA M 6B 16/16;
  PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 89 grouped
  cells + singleton (90/90); PB0/PB1 match
  too (92/92).
- b5 const 0xc6 PBA/PBB; quad single step
  0xc6->0xc7 at 58240 (last cell).
- varpos fully partitioned (counter+R+M+tails
  per group), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
