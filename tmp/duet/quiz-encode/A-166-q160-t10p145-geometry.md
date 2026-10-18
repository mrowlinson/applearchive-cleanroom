# A-166 (Q-160): T10P145 P-head geometry — DERIVED

Bed: census N=67197..67288 own bed (.rav[12:-4]).
First-hand; P144-M tails from own P144 census
row0 66877..66892 (this seat).

## 1. shape: CONFIRM (double-singleton + intra-PBA step)
- 67197 100B/84B sig 02000000; 67198 100B/84B
  fat sig e3020000 NEW; PBA 67199..67214 sig
  882b0000 NEW.
- SINGLETON 67215 sig b7030000 NEW +
  SINGLETON 67216 sig b7020000 NEW (3rd
  P115-style double, per-N exact).
- PBB8 67217..67224 sig 77020000 NEW; QUAD
  67225..67288 single sig 7d270000 NEW.
- 92x100B exact. PBA VPOS [4,5,48,49,50,
  76-79] exact (b5 0x0c->0x0d @67200, per-N:
  67199=0c, 67200..67214=0d); PBB VPOS
  [4,44,45,46,47,49,50,51,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 6B pos[6,7,76,77,78,79] row-indep 16/16
  x4, 16/16 distinct each row (heads b6,7
  13/16 distinct pairs each row).
- R-band 7B row-only: rows2==3 exact
  a900c68fa244af (3rd 2==3 pairing); row0
  09612d7162f14f; row1 a9ba555362822f.
- Tails b80..83 row-const aa30b00c/6ab131dd/
  5b3555ec/aa3555ec (rows2,3 differ b0 only).
- M-novelty vs P144M: ALL NEW (0/16 tails;
  6B vs 8B layout). PBA M 7B 16/16; PBB M
  11B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 0x0c->0x0d step @67200 (PBA), const
  0x0d PBB/quad.
- Varpos partitioned exact (PBA 9 = b4+b5+
  7tab; PBB 12 = b4+11tab; quad 18 = b4+R7+
  M6+tails), 0 stragglers. NO D-class dips.
- Next tier starts 67289 (sig d3770200).

## geometry agrees on all 3 legs
