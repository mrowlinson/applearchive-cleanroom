# A-178 (Q-172): T10P151 P-head geometry — DERIVED

Bed: census N=69285..69376 own bed (.rav[12:-4]).
First-hand; P150-M tails from own P150 census
row0 68965..68980 (this seat).

## 1. shape: CONFIRM (all-100B 11th)
- 69285 100B/84B sig 03000000; 69286 100B/84B
  fat sig e3060000 NEW; PBA 69287..69302 sig
  436e0000 NEW; NO extra singleton; PBB10
  69303..69312 sig 72030000 NEW; QUAD
  69313..69376 single sig 23370000 NEW.
- 92x100B exact. PBA VPOS [4,13,14,15,76-79]
  exact (b5 const 0x1d); PBB VPOS [4,13,14,
  15,16,17,18,19,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 6B pos[20,21,76,77,78,79] row-indep 16/16
  x4, full 16/16 distinct each row (heads
  b20,21 16/16 distinct pairs each row, 4th
  full-heads).
- R-band 7B row-only: rows2==3 exact
  55bcd138c58404 (5th 2==3 pairing); row0
  38fcc4181a0305; row1 1fbc52d8f29103.
- Tails b80..83 row-const 4cdd86d9/3a000951/
  f263e8b3/3d64e8b3 (rows2,3 differ b0 only).
- M-novelty vs P150M: ALL NEW (0/16 tails;
  6B vs 7B layout). PBA M 7B 16/16; PBB M
  11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x1d PBA/PBB; quad 0x1d->0x1e
  step exactly at 69376 (last cell: 69375=1d,
  69376=1e; row3 spans the step).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 12 = b4+11tab; quad 19 = b4+b5+R7+M6+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 69377 (sig 256e0300).

## geometry agrees on all 3 legs
