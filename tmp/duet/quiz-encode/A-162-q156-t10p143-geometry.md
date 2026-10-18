# A-162 (Q-156): T10P143 P-head geometry — DERIVED

Bed: census N=66501..66592 own bed (.rav[12:-4]).
First-hand; P142-M from own P142 census row0
66181..66196 (this seat).

## 1. shape: CONFIRM (all-100B 3rd)
- 66501 100B/84B sig 02000000; 66502 100B/84B
  fat sig d0050000 NEW; PBA 66503..66518 sig
  605d0000 NEW; SINGLETON 66519 eb020000 NEW;
  PBB9 66520..66528 sig 75010000 NEW; QUAD
  66529..66592 single sig 59170000 NEW.
- 92x100B exact. PBA VPOS [4,13,14,15,76-79]
  exact (b5 const 0x07); PBB VPOS [4,13,14,
  15,16,17,18,19,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 7B pos[20,21,22,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 distinct triples each row).
- R-band 7B row-only: rows2==3 exact
  ba3c9757350f3d (2nd 2==3 pairing); row0
  d1bcc217346c3d; row1 023c3837f55b3c.
- Tails b80..83 row-const 93cdaec2/d7929e3d/
  44d55611/95d55611 (rows2,3 differ b0 only).
- M-novelty vs P142M: ALL NEW (0/16 full,
  0/16 tails; 7B vs 7B layout). PBA M 7B
  16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x07 PBA/PBB; quad 0x07->0x08
  step exactly at 66560 (66559=07, 66560=08;
  row1 spans the step).
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 12 = b4+11tab; quad 20 = b4+b5+R7+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 66593 (sig 9a7a0100).

## geometry agrees on all 3 legs
