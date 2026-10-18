# A-212 (Q-206): T10P167 P-head geometry — DERIVED

Bed: census N=74853..74944 own bed (.rav[12:-4]).
First-hand; P166-M tails from own P166 census
row0 74533..74548 (this seat).

## 1. shape: CONFIRM (PBB-internal step)
- 74853 100B/84B sig 11000000 (PB0); 74854
  100B/84B fat sig db110000 NEW; PBA
  74855..74870 sig 3b1d0100 NEW; SINGLETON
  74871 sig a6230000 NEW; PBB9 74872..74880
  sig d3110000 NEW; QUAD 74881..74944 single
  sig 301d0100 NEW.
- 92x100B exact. PBA VPOS [4,13,14,15,76-79]
  exact (b5 const 0x48); PBB VPOS [4,5,13-19,
  80-83] exact (11B M; b5 step INSIDE PBB
  @74880 per-N: 74872..74879=48, 74880=49;
  1st PBB-internal).

## 2. quad rows: CONFIRM
- M 8B pos[20,21,22,23,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 quads each row), shared all 4 rows
  16/16 positional (5th 8B quad M).
- R-band 7B b13-19 row-only: rows0==2 exact
  e6fc43186363f6 (2nd 0==2 pairing); row1
  863c06b89639f7; row3 c6bc41189293f5, 64/64.
- Tails b80..83 row-const ALL distinct
  906b50c7/74eb217b/204379c8/e656d185.
- M-novelty vs P166M tails: ALL NEW (0/16).
  PBA M 7B 16/16; PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5: 0x48 const PBA; 0x48->0x49 step @74880
  (PBB); const 0x49 whole quad.
- Varpos partitioned exact (PBA 8 = b4+7tab;
  PBB 13 = b4+b5+11tab; quad 20 = b4+R7+M8+
  tails), 0 stragglers. NO D-class dips.
- Next tier @74945 sig c9da1100.

## geometry agrees on all 3 legs
