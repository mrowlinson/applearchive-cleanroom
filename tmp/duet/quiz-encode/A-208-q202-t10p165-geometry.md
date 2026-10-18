# A-208 (Q-202): T10P165 P-head geometry — DERIVED

Bed: census N=74157..74248 own bed (.rav[12:-4]).
First-hand; P164-M tails from own P164 census
row0 73837..73852 (this seat).

## 1. shape: CONFIRM (new PB0 sig)
- 74157 100B/84B sig 11000000 (PB0; NEW PB0
  sig); 74158 100B/84B fat sig c3230000 NEW;
  PBA 74159..74174 sig 353c0200 NEW;
  SINGLETON 74175 sig b9230000 NEW; PBB9
  74176..74184 sig dc110000 NEW; QUAD
  74185..74248 single sig ce1d0100 NEW.
- 92x100B exact. PBA VPOS [4,20,21,26,27,
  76-79] exact (b5 const 0x43); PBB VPOS
  [4,11,18,19,25-30,80-83] exact (13B M).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  16/16 triples each row, full-heads),
  shared all 4 rows 16/16 positional.
- R-band 9B b11,18,19,25-30 row-only:
  rows0==3 exact 90185b93849772885a (1st
  0==3 pairing); row1 9018b8b384ffb22761;
  row2 b05853739d7f52cb5d, 64/64.
- Tails b80..83 row-const 31b77f99/b4ebd7bd/
  30f6f48a/fab77f99 (rows0,3 differ b0 only).
- M-novelty vs P164M tails: ALL NEW (0/16).
  PBA M 8B 16/16; PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 92 cells.
- b5 const 0x43 PBA/PBB; quad 0x43->0x44
  step exactly at 74240 (74239=43, 74240=44;
  row3 spans).
- Varpos partitioned exact (PBA 9 = b4+8tab;
  PBB 14 = b4+13tab; quad 22 = b4+b5+R9+M7+
  tails), 0 stragglers. NO D-class dips.
- Next tier @74249 sig 41571100.

## geometry agrees on all 3 legs
