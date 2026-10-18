# A-160 (Q-154): T10P142 P-head geometry — DERIVED

Bed: census N=66153..66244 own bed (.rav[12:-4]).
First-hand; P141-M from own P141 census row0
65833..65848 (this seat).

## 1. shape: CONFIRM (mixed-sig PBB + intra-PBB step)
- 66153 100B/84B sig 02000000; 66154 100B/84B
  fat sig e3050000 NEW; PBA 66155..66170 sig
  d3540000 NEW; SINGLETON 66171 f4020000 NEW.
- PBB9 66172..66180 MIXED b0 = 59,58,74,42,
  5e,66,66,58,5e per-N exact (b1..3 const
  010000; 2nd mixed-sig PBB after P140).
- QUAD 66181..66244 single sig d3140000 NEW.
- 92x100B exact. PBA VPOS [4,44,45,46,47,
  76-79] exact (b5 const 0x04); PBB VPOS
  [0,4,5,11,31,41,42,43,48,49,80-83] exact
  (14B, b5 steps 0x04->0x05 @66176).

## 2. quad rows: CONFIRM
- M 7B pos[48,49,50,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  13/16 distinct triples each row).
- R-band 8B row-only: rows2==3 exact
  667a7de62970da38 (1st 2==3 pairing); row0
  247845e641308e39; row1 4a7ba5e125102b38.
- Tails b80..83 row-const 15c2c6fa/53990683/
  7d98294f/cf98294f (rows2,3 differ b0 only).
- M-novelty vs P141M: ALL NEW (0/16 full,
  0/16 tails; 7B vs 7B layout). PBA M 8B
  16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 0x04 PBA/PBB-head, 0x04->0x05 step
  @66176 (PBB), const 0x05 quad.
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+b5+12tab; quad 20 = b4+R8+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier starts 66245 (sig 324d0100).

## geometry agrees on all 3 legs
