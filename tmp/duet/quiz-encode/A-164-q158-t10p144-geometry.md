# A-164 (Q-158): T10P144 P-head geometry — DERIVED

Bed: census N=66849..66940 own bed (.rav[12:-4]).
First-hand; P143-M from own P143 census row0
66529..66544 (this seat).

## 1. shape: CONFIRM (alternating PBB10 + multi-sig quad)
- 66849 100B/84B sig 02000000; 66850 100B/84B
  fat sig f5020000 NEW; PBA 66851..66866 sig
  542f0000 NEW; NO extra singleton.
- PBB10 66867..66876 ALTERNATING per-N exact:
  f5020000 x2 (66867,66868) + 7a010000 x3
  (66869..66871) + f5020000 x1 (66872) +
  7a010000 x3 (66873..66875) + f5020000 x1
  (66876). 3rd mixed-sig PBB, 1st alternating.
- QUAD 66877..66940 per-row sigs: rows0,2,3
  fc110000, row1 251f0000 (both NEW, 2nd
  multi-sig quad), 64/64.
- 92x100B exact. PBA VPOS [4,32,33,34,76-79]
  exact (b5 const 0x0a); PBB VPOS [0,1,4,11,
  29,30,31,32,33,34,35,36,37,38,39,80-83]
  exact (19B).

## 2. quad rows: CONFIRM
- M 8B pos[32,33,38,39,76,77,78,79] row-indep
  16/16 x4, full 16/16 distinct each row
  (heads 16/16 distinct quads each row, 2nd
  full-heads).
- R-band 6B b0,1,11,30,36,37 row-only:
  rows0==2==3 exact fc11b4b0a4f2; row1
  251f34ddfdd9, 64/64. b2,3 const 0x00.
- Tails b80..83 row-const 7ae2f433/bac458d3/
  1ce3f433/6ce3f433 (rows0,2,3 differ b0 only).
- M-novelty vs P143M: ALL NEW (0/16 full,
  0/16 tails; 8B vs 7B layout). PBA M 7B
  16/16; PBB M 18B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x0a whole tier (no step).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 19 = b4+18tab; quad 19 = b4+R6+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 66941 (sig aaa90100).

## geometry agrees on all 3 legs
